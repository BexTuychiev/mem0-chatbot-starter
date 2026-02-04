[Skip to main content](https://docs.mem0.ai/integrations/langgraph#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Agent Frameworks

LangGraph

[Welcome](https://docs.mem0.ai/introduction) [Mem0 Platform](https://docs.mem0.ai/platform/overview) [Open Source](https://docs.mem0.ai/open-source/overview) [OpenMemory](https://docs.mem0.ai/openmemory/overview) [Cookbooks](https://docs.mem0.ai/cookbooks/overview) [Integrations](https://docs.mem0.ai/integrations) [API Reference](https://docs.mem0.ai/api-reference) [Release Notes](https://docs.mem0.ai/changelog)

- [Documentation](https://docs.mem0.ai/introduction)

##### Overview

- [Overview](https://docs.mem0.ai/integrations)

##### Agent Frameworks

- [Langchain](https://docs.mem0.ai/integrations/langchain)
- [LangGraph](https://docs.mem0.ai/integrations/langgraph)
- [LlamaIndex](https://docs.mem0.ai/integrations/llama-index)
- [CrewAI](https://docs.mem0.ai/integrations/crewai)
- [AutoGen](https://docs.mem0.ai/integrations/autogen)
- [Agno](https://docs.mem0.ai/integrations/agno)
- [Camel AI](https://docs.mem0.ai/integrations/camel-ai)
- [OpenClaw](https://docs.mem0.ai/integrations/openclaw)
- [OpenAI Agents SDK](https://docs.mem0.ai/integrations/openai-agents-sdk)
- [Google ADK](https://docs.mem0.ai/integrations/google-ai-adk)
- [Mastra](https://docs.mem0.ai/integrations/mastra)
- [Vercel AI SDK](https://docs.mem0.ai/integrations/vercel-ai-sdk)

##### Voice & Real-time

- [Livekit](https://docs.mem0.ai/integrations/livekit)
- [Pipecat](https://docs.mem0.ai/integrations/pipecat)
- [ElevenLabs](https://docs.mem0.ai/integrations/elevenlabs)

##### Cloud & Infrastructure

- [AWS Bedrock](https://docs.mem0.ai/integrations/aws-bedrock)

##### Developer Tools

- [Dify](https://docs.mem0.ai/integrations/dify)
- [Flowise](https://docs.mem0.ai/integrations/flowise)
- [Langchain Tools](https://docs.mem0.ai/integrations/langchain-tools)
- [AgentOps](https://docs.mem0.ai/integrations/agentops)
- [Keywords AI](https://docs.mem0.ai/integrations/keywords)
- [Raycast Extension](https://docs.mem0.ai/integrations/raycast)

On this page

- [Overview](https://docs.mem0.ai/integrations/langgraph#overview)
- [Setup and Configuration](https://docs.mem0.ai/integrations/langgraph#setup-and-configuration)
- [Define State and Graph](https://docs.mem0.ai/integrations/langgraph#define-state-and-graph)
- [Create Chatbot Function](https://docs.mem0.ai/integrations/langgraph#create-chatbot-function)
- [Set Up Graph Structure](https://docs.mem0.ai/integrations/langgraph#set-up-graph-structure)
- [Create Conversation Runner](https://docs.mem0.ai/integrations/langgraph#create-conversation-runner)
- [Main Interaction Loop](https://docs.mem0.ai/integrations/langgraph#main-interaction-loop)
- [Key Features](https://docs.mem0.ai/integrations/langgraph#key-features)
- [Conclusion](https://docs.mem0.ai/integrations/langgraph#conclusion)

Build a personalized Customer Support AI Agent using LangGraph for conversation flow and Mem0 for memory retention. This integration enables context-aware and efficient support experiences.

## [​](https://docs.mem0.ai/integrations/langgraph\#overview)  Overview

In this guide, we’ll create a Customer Support AI Agent that:

1. Uses LangGraph to manage conversation flow
2. Leverages Mem0 to store and retrieve relevant information from past interactions
3. Provides personalized responses based on user history

## [​](https://docs.mem0.ai/integrations/langgraph\#setup-and-configuration)  Setup and Configuration

Install necessary libraries:

Copy

Ask AI

```
pip install langgraph langchain-openai mem0ai python-dotenv
```

Import required modules and set up configurations:

Remember to get the Mem0 API key from [Mem0 Platform](https://app.mem0.ai/).

Copy

Ask AI

```
from typing import Annotated, TypedDict, List
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from mem0 import MemoryClient
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# Configuration
# OPENAI_API_KEY = 'sk-xxx'  # Replace with your actual OpenAI API key
# MEM0_API_KEY = 'your-mem0-key'  # Replace with your actual Mem0 API key

# Initialize LangChain and Mem0
llm = ChatOpenAI(model="gpt-4")
mem0 = MemoryClient()
```

## [​](https://docs.mem0.ai/integrations/langgraph\#define-state-and-graph)  Define State and Graph

Set up the conversation state and LangGraph structure:

Copy

Ask AI

```
class State(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], add_messages]
    mem0_user_id: str

graph = StateGraph(State)
```

## [​](https://docs.mem0.ai/integrations/langgraph\#create-chatbot-function)  Create Chatbot Function

Define the core logic for the Customer Support AI Agent:

Copy

Ask AI

```
def chatbot(state: State):
    messages = state["messages"]
    user_id = state["mem0_user_id"]

    try:
        # Retrieve relevant memories
        memories = mem0.search(messages[-1].content, user_id=user_id)

        # Handle dict response format
        memory_list = memories['results']

        context = "Relevant information from previous conversations:\n"
        for memory in memory_list:
            context += f"- {memory['memory']}\n"

        system_message = SystemMessage(content=f"""You are a helpful customer support assistant. Use the provided context to personalize your responses and remember user preferences and past interactions.
{context}""")

        full_messages = [system_message] + messages
        response = llm.invoke(full_messages)

        # Store the interaction in Mem0
        try:
            interaction = [\
                {\
                    "role": "user",\
                    "content": messages[-1].content\
                },\
                {\
                    "role": "assistant",\
                    "content": response.content\
                }\
            ]
            result = mem0.add(interaction, user_id=user_id)
            print(f"Memory saved: {len(result.get('results', []))} memories added")
        except Exception as e:
            print(f"Error saving memory: {e}")

        return {"messages": [response]}

    except Exception as e:
        print(f"Error in chatbot: {e}")
        # Fallback response without memory context
        response = llm.invoke(messages)
        return {"messages": [response]}
```

## [​](https://docs.mem0.ai/integrations/langgraph\#set-up-graph-structure)  Set Up Graph Structure

Configure the LangGraph with appropriate nodes and edges:

Copy

Ask AI

```
graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", "chatbot")

compiled_graph = graph.compile()
```

## [​](https://docs.mem0.ai/integrations/langgraph\#create-conversation-runner)  Create Conversation Runner

Implement a function to manage the conversation flow:

Copy

Ask AI

```
def run_conversation(user_input: str, mem0_user_id: str):
    config = {"configurable": {"thread_id": mem0_user_id}}
    state = {"messages": [HumanMessage(content=user_input)], "mem0_user_id": mem0_user_id}

    for event in compiled_graph.stream(state, config):
        for value in event.values():
            if value.get("messages"):
                print("Customer Support:", value["messages"][-1].content)
                return
```

## [​](https://docs.mem0.ai/integrations/langgraph\#main-interaction-loop)  Main Interaction Loop

Set up the main program loop for user interaction:

Copy

Ask AI

```
if __name__ == "__main__":
    print("Welcome to Customer Support! How can I assist you today?")
    mem0_user_id = "alice"  # You can generate or retrieve this based on your user management system
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Customer Support: Thank you for contacting us. Have a great day!")
            break
        run_conversation(user_input, mem0_user_id)
```

## [​](https://docs.mem0.ai/integrations/langgraph\#key-features)  Key Features

1. **Memory Integration**: Uses Mem0 to store and retrieve relevant information from past interactions.
2. **Personalization**: Provides context-aware responses based on user history.
3. **Flexible Architecture**: LangGraph structure allows for easy expansion of the conversation flow.
4. **Continuous Learning**: Each interaction is stored, improving future responses.

## [​](https://docs.mem0.ai/integrations/langgraph\#conclusion)  Conclusion

By integrating LangGraph with Mem0, you can build a personalized Customer Support AI Agent that can maintain context across interactions and provide personalized assistance.

[**LangChain Integration** \\
\\
Build conversational agents with LangChain and Mem0](https://docs.mem0.ai/integrations/langchain) [**CrewAI Integration** \\
\\
Create multi-agent systems with CrewAI](https://docs.mem0.ai/integrations/crewai)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/integrations/langgraph.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/integrations/langgraph)

[Langchain\\
\\
Previous](https://docs.mem0.ai/integrations/langchain) [LlamaIndex\\
\\
Next](https://docs.mem0.ai/integrations/llama-index)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![](https://downloads.intercomcdn.com/i/o/jjv2r0tt/659404/9e903493dd0a115e31b620e84189/9a987d2bf694d15c37d85f66f2be4813.png)
