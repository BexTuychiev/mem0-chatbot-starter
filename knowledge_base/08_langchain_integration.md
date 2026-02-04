[Skip to main content](https://docs.mem0.ai/integrations/langchain#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Agent Frameworks

Langchain

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

- [Overview](https://docs.mem0.ai/integrations/langchain#overview)
- [Setup and Configuration](https://docs.mem0.ai/integrations/langchain#setup-and-configuration)
- [Create Prompt Template](https://docs.mem0.ai/integrations/langchain#create-prompt-template)
- [Define Helper Functions](https://docs.mem0.ai/integrations/langchain#define-helper-functions)
- [Create Chat Turn Function](https://docs.mem0.ai/integrations/langchain#create-chat-turn-function)
- [Main Interaction Loop](https://docs.mem0.ai/integrations/langchain#main-interaction-loop)
- [Key Features](https://docs.mem0.ai/integrations/langchain#key-features)
- [Conclusion](https://docs.mem0.ai/integrations/langchain#conclusion)

Build a personalized Travel Agent AI using LangChain for conversation flow and Mem0 for memory retention. This integration enables context-aware and efficient travel planning experiences.

## [​](https://docs.mem0.ai/integrations/langchain\#overview)  Overview

In this guide, we’ll create a Travel Agent AI that:

1. Uses LangChain to manage conversation flow
2. Leverages Mem0 to store and retrieve relevant information from past interactions
3. Provides personalized travel recommendations based on user history

## [​](https://docs.mem0.ai/integrations/langchain\#setup-and-configuration)  Setup and Configuration

Install necessary libraries:

Copy

Ask AI

```
pip install langchain langchain_openai mem0ai python-dotenv
```

Import required modules and set up configurations:

Remember to get the Mem0 API key from [Mem0 Platform](https://app.mem0.ai/).

Copy

Ask AI

```
import os
from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from mem0 import MemoryClient
from dotenv import load_dotenv

load_dotenv()

# Configuration
# os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
# os.environ["MEM0_API_KEY"] = "your-mem0-api-key"

# Initialize LangChain and Mem0
llm = ChatOpenAI(model="gpt-4.1-nano-2025-04-14")
mem0 = MemoryClient()
```

## [​](https://docs.mem0.ai/integrations/langchain\#create-prompt-template)  Create Prompt Template

Set up the conversation prompt template:

Copy

Ask AI

```
prompt = ChatPromptTemplate.from_messages([\
    SystemMessage(content="""You are a helpful travel agent AI. Use the provided context to personalize your responses and remember user preferences and past interactions.\
    Provide travel recommendations, itinerary suggestions, and answer questions about destinations.\
    If you don't have specific information, you can make general suggestions based on common travel knowledge."""),\
    MessagesPlaceholder(variable_name="context"),\
    HumanMessage(content="{input}")\
])
```

## [​](https://docs.mem0.ai/integrations/langchain\#define-helper-functions)  Define Helper Functions

Create functions to handle context retrieval, response generation, and addition to Mem0:

Copy

Ask AI

```
def retrieve_context(query: str, user_id: str) -> List[Dict]:
    """Retrieve relevant context from Mem0"""
    try:
        memories = mem0.search(query, user_id=user_id)
        memory_list = memories['results']

        serialized_memories = ' '.join([mem["memory"] for mem in memory_list])
        context = [\
            {\
                "role": "system",\
                "content": f"Relevant information: {serialized_memories}"\
            },\
            {\
                "role": "user",\
                "content": query\
            }\
        ]
        return context
    except Exception as e:
        print(f"Error retrieving memories: {e}")
        # Return empty context if there's an error
        return [{"role": "user", "content": query}]

def generate_response(input: str, context: List[Dict]) -> str:
    """Generate a response using the language model"""
    chain = prompt | llm
    response = chain.invoke({
        "context": context,
        "input": input
    })
    return response.content

def save_interaction(user_id: str, user_input: str, assistant_response: str):
    """Save the interaction to Mem0"""
    try:
        interaction = [\
            {\
              "role": "user",\
              "content": user_input\
            },\
            {\
                "role": "assistant",\
                "content": assistant_response\
            }\
        ]
        result = mem0.add(interaction, user_id=user_id)
        print(f"Memory saved successfully: {len(result.get('results', []))} memories added")
    except Exception as e:
        print(f"Error saving interaction: {e}")
```

## [​](https://docs.mem0.ai/integrations/langchain\#create-chat-turn-function)  Create Chat Turn Function

Implement the main function to manage a single turn of conversation:

Copy

Ask AI

```
def chat_turn(user_input: str, user_id: str) -> str:
    # Retrieve context
    context = retrieve_context(user_input, user_id)

    # Generate response
    response = generate_response(user_input, context)

    # Save interaction
    save_interaction(user_id, user_input, response)

    return response
```

## [​](https://docs.mem0.ai/integrations/langchain\#main-interaction-loop)  Main Interaction Loop

Set up the main program loop for user interaction:

Copy

Ask AI

```
if __name__ == "__main__":
    print("Welcome to your personal Travel Agent Planner! How can I assist you with your travel plans today?")
    user_id = "alice"

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Travel Agent: Thank you for using our travel planning service. Have a great trip!")
            break

        response = chat_turn(user_input, user_id)
        print(f"Travel Agent: {response}")
```

## [​](https://docs.mem0.ai/integrations/langchain\#key-features)  Key Features

1. **Memory Integration**: Uses Mem0 to store and retrieve relevant information from past interactions.
2. **Personalization**: Provides context-aware responses based on user history and preferences.
3. **Flexible Architecture**: LangChain structure allows for easy expansion of the conversation flow.
4. **Continuous Learning**: Each interaction is stored, improving future responses.

## [​](https://docs.mem0.ai/integrations/langchain\#conclusion)  Conclusion

By integrating LangChain with Mem0, you can build a personalized Travel Agent AI that can maintain context across interactions and provide tailored travel recommendations and assistance.

[**LangGraph Integration** \\
\\
Build stateful agents with LangGraph and Mem0](https://docs.mem0.ai/integrations/langgraph) [**LangChain Tools** \\
\\
Use Mem0 as LangChain tools for agent workflows](https://docs.mem0.ai/integrations/langchain-tools)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/integrations/langchain.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/integrations/langchain)

[Overview\\
\\
Previous](https://docs.mem0.ai/integrations) [LangGraph\\
\\
Next](https://docs.mem0.ai/integrations/langgraph)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.
