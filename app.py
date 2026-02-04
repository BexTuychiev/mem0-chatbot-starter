"""
Agentic RAG Chatbot with Mem0 + LangChain

A chatbot that combines document retrieval (Chroma) with persistent user memory (Mem0).
The agent autonomously decides when to search docs, search memory, or store new memories.
"""

import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from mem0 import MemoryClient

load_dotenv()

KNOWLEDGE_BASE_DIR = Path(__file__).parent / "knowledge_base"

SYSTEM_PROMPT = """You are a Mem0 documentation assistant with access to docs and user memory.

Tools:
- search_docs: Technical questions, how-to, features, troubleshooting
- search_memory: When user references past context or needs personalization
- add_memory: When user shares preferences, goals, experience level, or asks you to remember

You may call up to 5 tools total per response. After gathering enough context, provide your final answer. Don't keep searching indefinitely - synthesize what you have."""

# Global cache
_vectorstore = None


def get_vectorstore():
    """Load knowledge base into Chroma vectorstore."""
    global _vectorstore
    if _vectorstore is not None:
        return _vectorstore

    loader = DirectoryLoader(
        str(KNOWLEDGE_BASE_DIR),
        glob="*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    _vectorstore = Chroma.from_documents(splits, embeddings)
    return _vectorstore


@tool
def search_docs(query: str) -> str:
    """Search Mem0 documentation for technical information and code examples."""
    vectorstore = get_vectorstore()
    results = vectorstore.similarity_search(query, k=3)

    if not results:
        return "No relevant documentation found."

    formatted = []
    for doc in results:
        source = Path(doc.metadata.get("source", "unknown")).stem.replace("_", " ")
        formatted.append(f"[Source: {source}]\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted)


def create_memory_tools(user_id: str):
    """Create memory tools bound to a specific user ID."""
    mem0_client = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))

    @tool
    def search_memory(query: str) -> str:
        """Search user's stored preferences and past interactions."""
        try:
            results = mem0_client.search(query, filters={"user_id": user_id}, limit=5)
            if not results.get("results"):
                return "No relevant memories found for this user."
            memories = [m["memory"] for m in results["results"]]
            return "User context:\n- " + "\n- ".join(memories)
        except Exception as e:
            return f"Error searching memory: {str(e)}"

    @tool
    def add_memory(content: str) -> str:
        """Store new information about the user for future reference."""
        try:
            mem0_client.add(
                messages=[{"role": "user", "content": content}], user_id=user_id
            )
            return "Noted. I'll remember this for future conversations."
        except Exception as e:
            return f"Error saving memory: {str(e)}"

    return search_memory, add_memory


def create_chatbot(user_id: str):
    """Create a LangChain agent configured for a specific user."""
    search_memory, add_memory = create_memory_tools(user_id)
    tools = [search_docs, search_memory, add_memory]

    return create_agent(
        model="openai:gpt-5-mini", tools=tools, system_prompt=SYSTEM_PROMPT
    )


def initialize_session_state():
    """Initialize Streamlit session state."""
    defaults = {"messages": [], "agent": None, "user_id": "", "show_tools": True}
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def render_sidebar():
    """Render the sidebar with configuration options."""
    with st.sidebar:
        st.title("Configuration")
        user_id = st.text_input(
            "User ID",
            value=st.session_state.user_id,
            placeholder="Enter your user ID...",
        )

        if user_id and user_id != st.session_state.user_id:
            st.session_state.user_id = user_id
            st.session_state.agent = create_chatbot(user_id)
            st.session_state.messages = []
            st.rerun()

        if st.session_state.user_id:
            st.success(f"Active user: {st.session_state.user_id}")

        st.session_state.show_tools = st.checkbox(
            "Show tool calls", value=st.session_state.show_tools
        )

        if st.button("Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()


def render_message(msg: dict):
    """Render a single message."""
    if msg["role"] in ("user", "assistant"):
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    elif msg["role"] == "tool" and st.session_state.show_tools:
        with st.expander(f"Tool: {msg['tool_name']}", expanded=False):
            st.code(
                msg["content"][:1000] + ("..." if len(msg["content"]) > 1000 else "")
            )


def process_user_input(prompt: str):
    """Process user input and get agent response with streaming."""
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_text = ""
        tool_results = {}

        # Stream using stream_mode="messages" for token-level streaming
        # recursion_limit caps the number of agent loop iterations (LLM + tool calls)
        for chunk, metadata in st.session_state.agent.stream(
            {"messages": [{"role": "user", "content": prompt}]},
            stream_mode="messages",
            config={"recursion_limit": 15},
        ):
            node = metadata.get("langgraph_node")

            # Model node streams LLM tokens
            if node == "model":
                if hasattr(chunk, "content") and chunk.content:
                    response_text += chunk.content
                    response_placeholder.markdown(response_text + "▌")

            # Tools node streams tool results
            elif node == "tools":
                if hasattr(chunk, "name") and hasattr(chunk, "content"):
                    tool_results[chunk.name] = chunk.content
                    st.session_state.messages.append(
                        {
                            "role": "tool",
                            "tool_name": chunk.name,
                            "content": chunk.content,
                        }
                    )

        # Final response
        if response_text:
            response_placeholder.markdown(response_text)
            st.session_state.messages.append(
                {"role": "assistant", "content": response_text}
            )

        # Show tool calls
        if st.session_state.show_tools:
            for name, content in tool_results.items():
                with st.expander(f"Tool: {name}", expanded=False):
                    st.code(content[:1000] + ("..." if len(content) > 1000 else ""))


def main():
    """Main application entry point."""
    st.set_page_config(page_title="Mem0 Docs Assistant", page_icon="🧠", layout="wide")
    initialize_session_state()
    render_sidebar()

    st.title("Mem0 Documentation Assistant")
    st.caption(
        "Ask questions about Mem0. I'll search the docs and remember your preferences."
    )

    if not os.getenv("OPENAI_API_KEY"):
        st.error("Please set OPENAI_API_KEY environment variable.")
        return
    if not os.getenv("MEM0_API_KEY"):
        st.error("Please set MEM0_API_KEY environment variable.")
        return
    if not st.session_state.user_id:
        st.info("Enter a User ID in the sidebar to start chatting.")
        return

    if st.session_state.agent is None:
        st.session_state.agent = create_chatbot(st.session_state.user_id)

    for msg in st.session_state.messages:
        render_message(msg)

    if prompt := st.chat_input("Ask about Mem0 or tell me about yourself..."):
        process_user_input(prompt)


if __name__ == "__main__":
    main()
