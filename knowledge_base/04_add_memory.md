[Skip to main content](https://docs.mem0.ai/core-concepts/memory-operations/add#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Add Memory

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

- [How Mem0 Adds Memory](https://docs.mem0.ai/core-concepts/memory-operations/add#how-mem0-adds-memory)
- [Key terms](https://docs.mem0.ai/core-concepts/memory-operations/add#key-terms)
- [How does it work?](https://docs.mem0.ai/core-concepts/memory-operations/add#how-does-it-work)
- [Add with Mem0 Platform](https://docs.mem0.ai/core-concepts/memory-operations/add#add-with-mem0-platform)
- [Add with Mem0 Open Source](https://docs.mem0.ai/core-concepts/memory-operations/add#add-with-mem0-open-source)
- [When Should You Add Memory?](https://docs.mem0.ai/core-concepts/memory-operations/add#when-should-you-add-memory)
- [More Details](https://docs.mem0.ai/core-concepts/memory-operations/add#more-details)
- [Managed vs OSS differences](https://docs.mem0.ai/core-concepts/memory-operations/add#managed-vs-oss-differences)
- [Put it into practice](https://docs.mem0.ai/core-concepts/memory-operations/add#put-it-into-practice)
- [See it live](https://docs.mem0.ai/core-concepts/memory-operations/add#see-it-live)

# [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#how-mem0-adds-memory)  How Mem0 Adds Memory

Adding memory is how Mem0 captures useful details from a conversation so your agents can reuse them later. Think of it as saving the important sentences from a chat transcript into a structured notebook your agent can search.

**Why it matters**

- Preserves user preferences, goals, and feedback across sessions.
- Powers personalization and decision-making in downstream conversations.
- Keeps context consistent between managed Platform and OSS deployments.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#key-terms)  Key terms

- **Messages** – The ordered list of user/assistant turns you send to `add`.
- **Infer** – Controls whether Mem0 extracts structured memories (`infer=True`, default) or stores raw messages.
- **Metadata** – Optional filters (e.g., `{"category": "movie_recommendations"}`) that improve retrieval later.
- **User / Session identifiers** – `user_id`, `session_id`, or `run_id` that scope the memory for future searches.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#how-does-it-work)  How does it work?

Mem0 offers two flows:

- **Mem0 Platform** – Fully managed API with dashboard, scaling, and graph features.
- **Mem0 Open Source** – Local SDK that you run in your own environment.

Both flows take the same payload and pass it through the same pipeline.

![](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/images/add_architecture.png?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=c9a5ae97b634120b1235fe1d756d5355)

Architecture diagram illustrating the process of adding memories.

1

[Navigate to header](https://docs.mem0.ai/core-concepts/memory-operations/add#)

Information extraction

Mem0 sends the messages through an LLM that pulls out key facts, decisions, or preferences to remember.

2

[Navigate to header](https://docs.mem0.ai/core-concepts/memory-operations/add#)

Conflict resolution

Existing memories are checked for duplicates or contradictions so the latest truth wins.

3

[Navigate to header](https://docs.mem0.ai/core-concepts/memory-operations/add#)

Storage

The resulting memories land in managed vector storage (and optional graph storage) so future searches return them quickly.

Duplicate protection only runs during that conflict-resolution step when you let Mem0 infer memories (`infer=True`, the default). If you switch to `infer=False`, Mem0 stores your payload exactly as provided, so duplicates will land. Mixing both modes for the same fact will save it twice.

You trigger this pipeline with a single `add` call—no manual orchestration needed.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#add-with-mem0-platform)  Add with Mem0 Platform

Python

JavaScript

Copy

Ask AI

```
from mem0 import MemoryClient

client = MemoryClient(api_key="your-api-key")

messages = [\
    {"role": "user", "content": "I'm planning a trip to Tokyo next month."},\
    {"role": "assistant", "content": "Great! I’ll remember that for future suggestions."}\
]

client.add(
    messages=messages,
    user_id="alice",
)
```

Expect a `memory_id` (or list of IDs) in the response. Check the Mem0 dashboard to confirm the new entry under the correct user.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#add-with-mem0-open-source)  Add with Mem0 Open Source

Python

JavaScript

Copy

Ask AI

```
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key"

m = Memory()

messages = [\
    {"role": "user", "content": "I'm planning to watch a movie tonight. Any recommendations?"},\
    {"role": "assistant", "content": "How about thriller movies? They can be quite engaging."},\
    {"role": "user", "content": "I'm not a big fan of thriller movies but I love sci-fi movies."},\
    {"role": "assistant", "content": "Got it! I'll avoid thriller recommendations and suggest sci-fi movies in the future."}\
]

# Store inferred memories (default behavior)
result = m.add(messages, user_id="alice", metadata={"category": "movie_recommendations"})

# Optionally store raw messages without inference
result = m.add(messages, user_id="alice", metadata={"category": "movie_recommendations"}, infer=False)
```

Use `infer=False` only when you need to store raw transcripts. Most workflows benefit from Mem0 extracting structured memories automatically.

If you do choose `infer=False`, keep it consistent. Raw inserts skip conflict resolution, so a later `infer=True` call with the same content will create a second memory instead of updating the first.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#when-should-you-add-memory)  When Should You Add Memory?

Add memory whenever your agent learns something useful:

- A new user preference is shared
- A decision or suggestion is made
- A goal or task is completed
- A new entity is introduced
- A user gives feedback or clarification

**MCP Alternative**: With [Mem0 MCP](https://docs.mem0.ai/platform/mem0-mcp), AI agents can add memories automatically based on context.

Storing this context allows the agent to reason better in future interactions.

### [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#more-details)  More Details

For full list of supported fields, required formats, and advanced options, see the
[Add Memory API Reference](https://docs.mem0.ai/api-reference/memory/add-memories).

## [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#managed-vs-oss-differences)  Managed vs OSS differences

| Capability | Mem0 Platform | Mem0 OSS |
| --- | --- | --- |
| Conflict resolution | Automatic with dashboard visibility | SDK handles merges locally; you control storage |
| Graph writes | Toggle per request (`enable_graph=True`) | Requires configuring a graph provider |
| Rate limits | Managed quotas per workspace | Limited by your hardware and provider APIs |
| Dashboard visibility | Yes — inspect memories visually | Inspect via CLI, logs, or custom UI |

## [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#put-it-into-practice)  Put it into practice

- Review the [Advanced Memory Operations](https://docs.mem0.ai/platform/advanced-memory-operations) guide to layer metadata, rerankers, and graph toggles.
- Explore the [Add Memories API reference](https://docs.mem0.ai/api-reference/memory/add-memories) for every request/response field.

## [​](https://docs.mem0.ai/core-concepts/memory-operations/add\#see-it-live)  See it live

- [Support Inbox with Mem0](https://docs.mem0.ai/cookbooks/operations/support-inbox) shows add + search powering a support flow.
- [AI Tutor with Mem0](https://docs.mem0.ai/cookbooks/companions/ai-tutor) uses add to personalize lesson plans.

[**Explore Search Concepts**](https://docs.mem0.ai/core-concepts/memory-operations/search) [**Build a Support Agent**](https://docs.mem0.ai/cookbooks/operations/support-inbox)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/core-concepts/memory-operations/add.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/core-concepts/memory-operations/add)

[Memory Types\\
\\
Previous](https://docs.mem0.ai/core-concepts/memory-types) [Search Memory\\
\\
Next](https://docs.mem0.ai/core-concepts/memory-operations/search)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/images/add_architecture.png?w=840&fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=d099b83f91fdf36bfab4566d16295e92)

![](https://downloads.intercomcdn.com/i/o/jjv2r0tt/659404/9e903493dd0a115e31b620e84189/9a987d2bf694d15c37d85f66f2be4813.png)
