[Skip to main content](https://docs.mem0.ai/platform/quickstart#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Getting Started

Quickstart

[Welcome](https://docs.mem0.ai/introduction) [Mem0 Platform](https://docs.mem0.ai/platform/overview) [Open Source](https://docs.mem0.ai/open-source/overview) [OpenMemory](https://docs.mem0.ai/openmemory/overview) [Cookbooks](https://docs.mem0.ai/cookbooks/overview) [Integrations](https://docs.mem0.ai/integrations) [API Reference](https://docs.mem0.ai/api-reference) [Release Notes](https://docs.mem0.ai/changelog)

- [Documentation](https://docs.mem0.ai/introduction)

##### Getting Started

- [Overview](https://docs.mem0.ai/platform/overview)
- [Mem0 MCP](https://docs.mem0.ai/platform/mem0-mcp)
- [Platform vs Open Source](https://docs.mem0.ai/platform/platform-vs-oss)
- [Quickstart](https://docs.mem0.ai/platform/quickstart)

##### Core Concepts

- [Memory Types](https://docs.mem0.ai/core-concepts/memory-types)
- [Add Memory](https://docs.mem0.ai/core-concepts/memory-operations/add)
- [Search Memory](https://docs.mem0.ai/core-concepts/memory-operations/search)
- [Update Memory](https://docs.mem0.ai/core-concepts/memory-operations/update)
- [Delete Memory](https://docs.mem0.ai/core-concepts/memory-operations/delete)

##### Platform Features

- [Overview](https://docs.mem0.ai/platform/features/platform-overview)
- Essential Features

- Advanced Features

- Data Management

- Integration Features


##### Support & Troubleshooting

- [FAQs](https://docs.mem0.ai/platform/faqs)

##### Migration Guide

- [Migrate from Open Source to Platform](https://docs.mem0.ai/migration/oss-to-platform)
- [Migrating from v0.x to v1.0.0](https://docs.mem0.ai/migration/v0-to-v1)
- [Breaking Changes in v1.0.0](https://docs.mem0.ai/migration/breaking-changes)
- [API Reference Changes](https://docs.mem0.ai/migration/api-changes)

##### Contribute

- [Contribution Hub](https://docs.mem0.ai/platform/contribute)

On this page

- [Prerequisites](https://docs.mem0.ai/platform/quickstart#prerequisites)
- [Installation](https://docs.mem0.ai/platform/quickstart#installation)
- [What’s Next?](https://docs.mem0.ai/platform/quickstart#what%E2%80%99s-next)
- [Additional Resources](https://docs.mem0.ai/platform/quickstart#additional-resources)

Get started with Mem0 Platform’s hosted API in under 5 minutes. This guide shows you how to authenticate and store your first memory.

## [​](https://docs.mem0.ai/platform/quickstart\#prerequisites)  Prerequisites

- Mem0 Platform account ( [Sign up here](https://app.mem0.ai/))
- API key ( [Get one from dashboard](https://app.mem0.ai/dashboard/settings?tab=api-keys&subtab=configuration))
- Python 3.10+, Node.js 14+, or cURL

## [​](https://docs.mem0.ai/platform/quickstart\#installation)  Installation

1

[Navigate to header](https://docs.mem0.ai/platform/quickstart#)

Install SDK

pip

npm

Copy

Ask AI

```
pip install mem0ai
```

2

[Navigate to header](https://docs.mem0.ai/platform/quickstart#)

Set your API key

Python

JavaScript

cURL

Copy

Ask AI

```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")
```

3

[Navigate to header](https://docs.mem0.ai/platform/quickstart#)

Add a memory

Python

JavaScript

cURL

Copy

Ask AI

```
messages = [\
    {"role": "user", "content": "I'm a vegetarian and allergic to nuts."},\
    {"role": "assistant", "content": "Got it! I'll remember your dietary preferences."}\
]
client.add(messages, user_id="user123")
```

4

[Navigate to header](https://docs.mem0.ai/platform/quickstart#)

Search memories

Python

JavaScript

cURL

Copy

Ask AI

```
results = client.search("What are my dietary restrictions?", filters={"user_id": "user123"})
print(results)
```

**Output:**

Copy

Ask AI

```
{
  "results": [\
    {\
      "id": "14e1b28a-2014-40ad-ac42-69c9ef42193d",\
      "memory": "Allergic to nuts",\
      "user_id": "user123",\
      "categories": ["health"],\
      "created_at": "2025-10-22T04:40:22.864647-07:00",\
      "score": 0.30\
    }\
  ]
}
```

**Pro Tip**: Want AI agents to manage their own memory automatically? Use [Mem0 MCP](https://docs.mem0.ai/platform/mem0-mcp) to let LLMs decide when to save, search, and update memories.

## [​](https://docs.mem0.ai/platform/quickstart\#what%E2%80%99s-next)  What’s Next?

[**Memory Operations** \\
\\
Learn how to search, update, and delete memories with complete CRUD operations](https://docs.mem0.ai/core-concepts/memory-operations/add) [**Platform Features** \\
\\
Explore advanced features like metadata filtering, graph memory, and webhooks](https://docs.mem0.ai/platform/features/platform-overview) [**API Reference** \\
\\
See complete API documentation and integration examples](https://docs.mem0.ai/api-reference/memory/add-memories)

## [​](https://docs.mem0.ai/platform/quickstart\#additional-resources)  Additional Resources

- **[Platform vs OSS](https://docs.mem0.ai/platform/platform-vs-oss)** \- Understand the differences between Platform and Open Source
- **[Troubleshooting](https://docs.mem0.ai/platform/faqs)** \- Common issues and solutions
- **[Integration Examples](https://docs.mem0.ai/cookbooks/companions/quickstart-demo)** \- See Mem0 in action

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/platform/quickstart.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/platform/quickstart)

[Platform vs Open Source\\
\\
Previous](https://docs.mem0.ai/platform/platform-vs-oss) [Memory Types\\
\\
Next](https://docs.mem0.ai/core-concepts/memory-types)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![](https://downloads.intercomcdn.com/i/o/jjv2r0tt/659404/9e903493dd0a115e31b620e84189/9a987d2bf694d15c37d85f66f2be4813.png)
