[Skip to main content](https://docs.mem0.ai/integrations/langchain-tools#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Developer Tools

Langchain Tools

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

- [Overview](https://docs.mem0.ai/integrations/langchain-tools#overview)
- [Installation](https://docs.mem0.ai/integrations/langchain-tools#installation)
- [Authentication](https://docs.mem0.ai/integrations/langchain-tools#authentication)
- [Available Tools](https://docs.mem0.ai/integrations/langchain-tools#available-tools)
- [1\. ADD Memory Tool](https://docs.mem0.ai/integrations/langchain-tools#1-add-memory-tool)
- [Schema](https://docs.mem0.ai/integrations/langchain-tools#schema)
- [Implementation](https://docs.mem0.ai/integrations/langchain-tools#implementation)
- [Example Usage](https://docs.mem0.ai/integrations/langchain-tools#example-usage)
- [2\. SEARCH Memory Tool](https://docs.mem0.ai/integrations/langchain-tools#2-search-memory-tool)
- [Schema](https://docs.mem0.ai/integrations/langchain-tools#schema-2)
- [Implementation](https://docs.mem0.ai/integrations/langchain-tools#implementation-2)
- [Example Usage](https://docs.mem0.ai/integrations/langchain-tools#example-usage-2)
- [3\. GET\_ALL Memory Tool](https://docs.mem0.ai/integrations/langchain-tools#3-get-all-memory-tool)
- [Schema](https://docs.mem0.ai/integrations/langchain-tools#schema-3)
- [Implementation](https://docs.mem0.ai/integrations/langchain-tools#implementation-3)
- [Example Usage](https://docs.mem0.ai/integrations/langchain-tools#example-usage-3)
- [Integration with AI Agents](https://docs.mem0.ai/integrations/langchain-tools#integration-with-ai-agents)

## [​](https://docs.mem0.ai/integrations/langchain-tools\#overview)  Overview

Mem0 provides a suite of tools for storing, searching, and retrieving memories, enabling agents to maintain context and learn from past interactions. The tools are built as Langchain tools, making them easily integrable with any AI agent implementation.

## [​](https://docs.mem0.ai/integrations/langchain-tools\#installation)  Installation

Install the required dependencies:

Copy

Ask AI

```
pip install langchain_core
pip install mem0ai
```

## [​](https://docs.mem0.ai/integrations/langchain-tools\#authentication)  Authentication

Import the necessary dependencies and initialize the client:

Copy

Ask AI

```
from langchain_core.tools import StructuredTool
from mem0 import MemoryClient
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import os

os.environ["MEM0_API_KEY"] = "your-api-key"

client = MemoryClient(
    org_id=your_org_id,
    project_id=your_project_id
)
```

## [​](https://docs.mem0.ai/integrations/langchain-tools\#available-tools)  Available Tools

Mem0 provides three main tools for memory management:

### [​](https://docs.mem0.ai/integrations/langchain-tools\#1-add-memory-tool)  1\. ADD Memory Tool

The ADD tool allows you to store new memories with associated metadata. It’s particularly useful for saving conversation history and user preferences.

#### [​](https://docs.mem0.ai/integrations/langchain-tools\#schema)  Schema

Copy

Ask AI

```
class Message(BaseModel):
    role: str = Field(description="Role of the message sender (user or assistant)")
    content: str = Field(description="Content of the message")

class AddMemoryInput(BaseModel):
    messages: List[Message] = Field(description="List of messages to add to memory")
    user_id: str = Field(description="ID of the user associated with these messages")
    metadata: Optional[Dict[str, Any]] = Field(description="Additional metadata for the messages", default=None)

    class Config:
        json_schema_extra = {
            "examples": [{\
                "messages": [\
                    {"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."},\
                    {"role": "assistant", "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy."}\
                ],\
                "user_id": "alex",\
                "metadata": {"food": "vegan"}\
            }]
        }
```

#### [​](https://docs.mem0.ai/integrations/langchain-tools\#implementation)  Implementation

Copy

Ask AI

```
def add_memory(messages: List[Message], user_id: str, metadata: Optional[Dict[str, Any]] = None) -> Any:
    """Add messages to memory with associated user ID and metadata."""
    message_dicts = [msg.dict() for msg in messages]
    return client.add(message_dicts, user_id=user_id, metadata=metadata)

add_tool = StructuredTool(
    name="add_memory",
    description="Add new messages to memory with associated metadata",
    func=add_memory,
    args_schema=AddMemoryInput
)
```

#### [​](https://docs.mem0.ai/integrations/langchain-tools\#example-usage)  Example Usage

Code

Output

Copy

Ask AI

```
add_input = {
    "messages": [\
        {"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."},\
        {"role": "assistant", "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy."}\
    ],
    "user_id": "alex",
    "metadata": {"food": "vegan"}
}
add_result = add_tool.invoke(add_input)
```

### [​](https://docs.mem0.ai/integrations/langchain-tools\#2-search-memory-tool)  2\. SEARCH Memory Tool

The SEARCH tool enables querying stored memories using natural language queries and advanced filtering options.

#### [​](https://docs.mem0.ai/integrations/langchain-tools\#schema-2)  Schema

Copy

Ask AI

```
class SearchMemoryInput(BaseModel):
    query: str = Field(description="The search query string")
    filters: Dict[str, Any] = Field(description="Filters to apply to the search")

    class Config:
        json_schema_extra = {
            "examples": [{\
                "query": "tell me about my allergies?",\
                "filters": {\
                    "AND": [\
                        {"user_id": "alex"},\
                        {"created_at": {"gte": "2024-01-01", "lte": "2024-12-31"}}\
                    ]\
                }\
            }]
        }
```

#### [​](https://docs.mem0.ai/integrations/langchain-tools\#implementation-2)  Implementation

Copy

Ask AI

```
def search_memory(query: str, filters: Dict[str, Any]) -> Any:
    """Search memory with the given query and filters."""
    return client.search(query=query, filters=filters)

search_tool = StructuredTool(
    name="search_memory",
    description="Search through memories with a query and filters",
    func=search_memory,
    args_schema=SearchMemoryInput
)
```

#### [​](https://docs.mem0.ai/integrations/langchain-tools\#example-usage-2)  Example Usage

Code

Output

Copy

Ask AI

```
search_input = {
    "query": "what is my name?",
    "filters": {
        "AND": [\
            {"user_id": "alex"},\
            {"created_at": {"gte": "2024-07-20", "lte": "2024-12-10"}}\
        ]
    }
}
result = search_tool.invoke(search_input)
```

### [​](https://docs.mem0.ai/integrations/langchain-tools\#3-get-all-memory-tool)  3\. GET\_ALL Memory Tool

The GET\_ALL tool retrieves all memories matching specified criteria, with support for pagination.

#### [​](https://docs.mem0.ai/integrations/langchain-tools\#schema-3)  Schema

Copy

Ask AI

```
class GetAllMemoryInput(BaseModel):
    filters: Dict[str, Any] = Field(description="Filters to apply to the retrieval")
    page: Optional[int] = Field(description="Page number for pagination", default=1)
    page_size: Optional[int] = Field(description="Number of items per page", default=50)

    class Config:
        json_schema_extra = {
            "examples": [{\
                "filters": {\
                    "AND": [\
                        {"user_id": "alex"},\
                        {"created_at": {"gte": "2024-07-01", "lte": "2024-07-31"}},\
                        {"categories": {"contains": "food_preferences"}}\
                    ]\
                },\
                "page": 1,\
                "page_size": 50\
            }]
        }
```

#### [​](https://docs.mem0.ai/integrations/langchain-tools\#implementation-3)  Implementation

Copy

Ask AI

```
def get_all_memory(filters: Dict[str, Any], page: int = 1, page_size: int = 50) -> Any:
    """Retrieve all memories matching the specified criteria."""
    return client.get_all(filters=filters, page=page, page_size=page_size)

get_all_tool = StructuredTool(
    name="get_all_memory",
    description="Retrieve all memories matching specified filters",
    func=get_all_memory,
    args_schema=GetAllMemoryInput
)
```

#### [​](https://docs.mem0.ai/integrations/langchain-tools\#example-usage-3)  Example Usage

Code

Output

Copy

Ask AI

```
get_all_input = {
    "filters": {
        "AND": [\
            {"user_id": "alex"},\
            {"created_at": {"gte": "2024-07-01", "lte": "2024-12-31"}}\
        ]
    },
    "page": 1,
    "page_size": 50
}
get_all_result = get_all_tool.invoke(get_all_input)
```

## [​](https://docs.mem0.ai/integrations/langchain-tools\#integration-with-ai-agents)  Integration with AI Agents

All tools are implemented as Langchain `StructuredTool` instances, making them compatible with any AI agent that supports the Langchain tools interface. To use these tools with your agent:

1. Initialize the tools as shown above
2. Add the tools to your agent’s toolset
3. The agent can now use these tools to manage memories through natural language interactions

Each tool provides structured input validation through Pydantic models and returns consistent responses that can be processed by your agent.

[**LangChain Integration** \\
\\
Build conversational agents with LangChain and Mem0](https://docs.mem0.ai/integrations/langchain) [**LangGraph Integration** \\
\\
Create stateful workflows with LangGraph](https://docs.mem0.ai/integrations/langgraph)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/integrations/langchain-tools.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/integrations/langchain-tools)

[Flowise\\
\\
Previous](https://docs.mem0.ai/integrations/flowise) [AgentOps\\
\\
Next](https://docs.mem0.ai/integrations/agentops)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![](https://downloads.intercomcdn.com/i/o/jjv2r0tt/659404/9e903493dd0a115e31b620e84189/9a987d2bf694d15c37d85f66f2be4813.png)
