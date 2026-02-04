[Skip to main content](https://docs.mem0.ai/core-concepts/memory-operations/update#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Update Memory

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

- [Keep Memories Accurate with Update](https://docs.mem0.ai/core-concepts/memory-operations/update#keep-memories-accurate-with-update)
- [Key terms](https://docs.mem0.ai/core-concepts/memory-operations/update#key-terms)
- [How the update flow works](https://docs.mem0.ai/core-concepts/memory-operations/update#how-the-update-flow-works)
- [Single memory update (Platform)](https://docs.mem0.ai/core-concepts/memory-operations/update#single-memory-update-platform)
- [Batch update (Platform)](https://docs.mem0.ai/core-concepts/memory-operations/update#batch-update-platform)
- [Update with Mem0 OSS](https://docs.mem0.ai/core-concepts/memory-operations/update#update-with-mem0-oss)
- [Tips](https://docs.mem0.ai/core-concepts/memory-operations/update#tips)
- [Managed vs OSS differences](https://docs.mem0.ai/core-concepts/memory-operations/update#managed-vs-oss-differences)
- [Put it into practice](https://docs.mem0.ai/core-concepts/memory-operations/update#put-it-into-practice)
- [See it live](https://docs.mem0.ai/core-concepts/memory-operations/update#see-it-live)

# [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#keep-memories-accurate-with-update)  Keep Memories Accurate with Update

Mem0’s update operation lets you fix or enrich an existing memory without deleting it. When a user changes their preference or clarifies a fact, use update to keep the knowledge base fresh.

**Why it matters**

- Corrects outdated or incorrect memories immediately.
- Adds new metadata so filters and rerankers stay sharp.
- Works for both one-off edits and large batches (up to 1000 memories).

## [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#key-terms)  Key terms

- **memory\_id** – Unique identifier returned by `add` or `search` results.
- **text** / **data** – New content that replaces the stored memory value.
- **metadata** – Optional key-value pairs you update alongside the text.
- **batch\_update** – Platform API that edits multiple memories in a single request.
- **immutable** – Flagged memories that must be deleted and re-added instead of updated.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#how-the-update-flow-works)  How the update flow works

1

[Navigate to header](https://docs.mem0.ai/core-concepts/memory-operations/update#)

Locate the memory

Use `search` or dashboard inspection to capture the `memory_id` you want to change.

2

[Navigate to header](https://docs.mem0.ai/core-concepts/memory-operations/update#)

Submit the update

Call `update` (or `batch_update`) with new text and optional metadata. Mem0 overwrites the stored value and adjusts indexes.

3

[Navigate to header](https://docs.mem0.ai/core-concepts/memory-operations/update#)

Verify

Check the response or re-run `search` to ensure the revised memory appears with the new content.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#single-memory-update-platform)  Single memory update (Platform)

Python

JavaScript

Copy

Ask AI

```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

memory_id = "your_memory_id"
client.update(
    memory_id=memory_id,
    text="Updated memory content about the user",
    metadata={"category": "profile-update"}
)
```

Expect a confirmation message and the updated memory to appear in the dashboard almost instantly.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#batch-update-platform)  Batch update (Platform)

Update up to 1000 memories in one call.

Python

JavaScript

Copy

Ask AI

```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

update_memories = [\
    {"memory_id": "id1", "text": "Watches football"},\
    {"memory_id": "id2", "text": "Likes to travel"}\
]

response = client.batch_update(update_memories)
print(response)
```

## [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#update-with-mem0-oss)  Update with Mem0 OSS

Python

Copy

Ask AI

```
from mem0 import Memory

memory = Memory()

memory.update(
    memory_id="mem_123",
    data="Alex now prefers decaf coffee",
)
```

OSS JavaScript SDK does not expose `update` yet—use the REST API or Python SDK when self-hosting.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#tips)  Tips

- Update both `text` **and**`metadata` together to keep filters accurate.
- Batch updates are ideal after large imports or when syncing CRM corrections.
- Immutable memories must be deleted and re-added instead of updated.
- Pair updates with feedback signals (thumbs up/down) to self-heal memories automatically.

**MCP Alternative**: With [Mem0 MCP](https://docs.mem0.ai/platform/mem0-mcp), AI agents can update their own memories when users correct information.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#managed-vs-oss-differences)  Managed vs OSS differences

| Capability | Mem0 Platform | Mem0 OSS |
| --- | --- | --- |
| Update call | `client.update(memory_id, {...})` | `memory.update(memory_id, data=...)` |
| Batch updates | `client.batch_update` (up to 1000 memories) | Script your own loop or bulk job |
| Dashboard visibility | Inspect updates in the UI | Inspect via logs or custom tooling |
| Immutable handling | Returns descriptive error | Raises exception—delete and re-add |

## [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#put-it-into-practice)  Put it into practice

- Review the [Update Memory API reference](https://docs.mem0.ai/api-reference/memory/update-memory) for request/response details.
- Combine updates with [Feedback Mechanism](https://docs.mem0.ai/platform/features/feedback-mechanism) to automate corrections.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/update\#see-it-live)  See it live

- [Support Inbox with Mem0](https://docs.mem0.ai/cookbooks/operations/support-inbox) uses updates to refine customer profiles.
- [AI Tutor with Mem0](https://docs.mem0.ai/cookbooks/companions/ai-tutor) demonstrates user preference corrections mid-course.

[**Learn Delete Concepts**](https://docs.mem0.ai/core-concepts/memory-operations/delete) [**Automate Corrections**](https://docs.mem0.ai/platform/features/feedback-mechanism)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/core-concepts/memory-operations/update.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/core-concepts/memory-operations/update)

[Search Memory\\
\\
Previous](https://docs.mem0.ai/core-concepts/memory-operations/search) [Delete Memory\\
\\
Next](https://docs.mem0.ai/core-concepts/memory-operations/delete)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.
