[Skip to main content](https://docs.mem0.ai/core-concepts/memory-operations/delete#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Delete Memory

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

- [Remove Memories Safely](https://docs.mem0.ai/core-concepts/memory-operations/delete#remove-memories-safely)
- [Key terms](https://docs.mem0.ai/core-concepts/memory-operations/delete#key-terms)
- [How the delete flow works](https://docs.mem0.ai/core-concepts/memory-operations/delete#how-the-delete-flow-works)
- [Delete a single memory (Platform)](https://docs.mem0.ai/core-concepts/memory-operations/delete#delete-a-single-memory-platform)
- [Batch delete multiple memories (Platform)](https://docs.mem0.ai/core-concepts/memory-operations/delete#batch-delete-multiple-memories-platform)
- [Delete memories by filter (Platform)](https://docs.mem0.ai/core-concepts/memory-operations/delete#delete-memories-by-filter-platform)
- [Delete with Mem0 OSS](https://docs.mem0.ai/core-concepts/memory-operations/delete#delete-with-mem0-oss)
- [Use cases recap](https://docs.mem0.ai/core-concepts/memory-operations/delete#use-cases-recap)
- [Method comparison](https://docs.mem0.ai/core-concepts/memory-operations/delete#method-comparison)
- [Put it into practice](https://docs.mem0.ai/core-concepts/memory-operations/delete#put-it-into-practice)
- [See it live](https://docs.mem0.ai/core-concepts/memory-operations/delete#see-it-live)

# [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#remove-memories-safely)  Remove Memories Safely

Deleting memories is how you honor compliance requests, undo bad data, or clean up expired sessions. Mem0 lets you delete a specific memory, a list of IDs, or everything that matches a filter.

**Why it matters**

- Satisfies user erasure (GDPR/CCPA) without touching the rest of your data.
- Keeps knowledge bases accurate by removing stale or incorrect facts.
- Works for both the managed Platform API and the OSS SDK.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#key-terms)  Key terms

- **memory\_id** – Unique ID returned by `add`/`search` identifying the record to delete.
- **batch\_delete** – API call that removes up to 1000 memories in one request.
- **delete\_all** – Filter-based deletion by user, agent, run, or metadata.
- **immutable** – Flagged memories that cannot be updated; delete + re-add instead.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#how-the-delete-flow-works)  How the delete flow works

1

[Navigate to header](https://docs.mem0.ai/core-concepts/memory-operations/delete#)

Choose the scope

Decide whether you’re removing a single memory, a list, or everything that matches a filter.

2

[Navigate to header](https://docs.mem0.ai/core-concepts/memory-operations/delete#)

Submit the delete call

Call `delete`, `batch_delete`, or `delete_all` with the required IDs or filters.

3

[Navigate to header](https://docs.mem0.ai/core-concepts/memory-operations/delete#)

Verify

Confirm the response message, then re-run `search` or check the dashboard/logs to ensure the memory is gone.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#delete-a-single-memory-platform)  Delete a single memory (Platform)

Python

JavaScript

Copy

Ask AI

```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

memory_id = "your_memory_id"
client.delete(memory_id=memory_id)
```

You’ll receive a confirmation payload. The dashboard reflects the removal within seconds.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#batch-delete-multiple-memories-platform)  Batch delete multiple memories (Platform)

Python

JavaScript

Copy

Ask AI

```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

delete_memories = [\
    {"memory_id": "id1"},\
    {"memory_id": "id2"}\
]

response = client.batch_delete(delete_memories)
print(response)
```

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#delete-memories-by-filter-platform)  Delete memories by filter (Platform)

Python

JavaScript

Copy

Ask AI

```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

# Delete all memories for a specific user
client.delete_all(user_id="alice")
```

You can also filter by other parameters such as:

- `agent_id`
- `run_id`
- `metadata` (as JSON string)

`delete_all` requires at least one filter (user, agent, run, or metadata). Calling it with no filters raises an error to prevent accidental data loss.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#delete-with-mem0-oss)  Delete with Mem0 OSS

Python

Copy

Ask AI

```
from mem0 import Memory

memory = Memory()

memory.delete(memory_id="mem_123")
memory.delete_all(user_id="alice")
```

The OSS JavaScript SDK does not yet expose deletion helpers—use the REST API or Python SDK when self-hosting.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#use-cases-recap)  Use cases recap

- Forget a user’s preferences at their request.
- Remove outdated or incorrect facts before they spread.
- Clean up memories after session expiration or retention deadlines.
- Comply with privacy legislation (GDPR, CCPA) and internal policies.

**MCP Alternative**: With [Mem0 MCP](https://docs.mem0.ai/platform/mem0-mcp), AI agents can delete their own memories when data becomes irrelevant or at user request.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#method-comparison)  Method comparison

| Method | Use when | IDs required | Filters |
| --- | --- | --- | --- |
| `delete(memory_id)` | You know the exact record | ✔️ | ✖️ |
| `batch_delete([...])` | You have a list of IDs to purge | ✔️ | ✖️ |
| `delete_all(...)` | You need to forget a user/agent/run | ✖️ | ✔️ |

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#put-it-into-practice)  Put it into practice

- Review the [Delete Memory API reference](https://docs.mem0.ai/api-reference/memory/delete-memory), plus [Batch Delete](https://docs.mem0.ai/api-reference/memory/batch-delete) and [Filtered Delete](https://docs.mem0.ai/api-reference/memory/delete-memories).
- Pair deletes with [Expiration Policies](https://docs.mem0.ai/platform/features/expiration-date) to automate retention.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/delete\#see-it-live)  See it live

- [Support Inbox with Mem0](https://docs.mem0.ai/cookbooks/operations/support-inbox) demonstrates compliance-driven deletes.
- [Data Management tooling](https://docs.mem0.ai/platform/features/direct-import) shows how deletes fit into broader lifecycle flows.

[**Review Add Concepts**](https://docs.mem0.ai/core-concepts/memory-operations/add) [**Enable Expiration Policies**](https://docs.mem0.ai/platform/features/expiration-date)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/core-concepts/memory-operations/delete.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/core-concepts/memory-operations/delete)

[Update Memory\\
\\
Previous](https://docs.mem0.ai/core-concepts/memory-operations/update) [Overview\\
\\
Next](https://docs.mem0.ai/platform/features/platform-overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.
