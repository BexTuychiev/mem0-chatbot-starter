[Skip to main content](https://docs.mem0.ai/core-concepts/memory-types#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Memory Types

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

- [How Mem0 Organizes Memory](https://docs.mem0.ai/core-concepts/memory-types#how-mem0-organizes-memory)
- [Key terms](https://docs.mem0.ai/core-concepts/memory-types#key-terms)
- [Short-term vs long-term memory](https://docs.mem0.ai/core-concepts/memory-types#short-term-vs-long-term-memory)
- [How does it work?](https://docs.mem0.ai/core-concepts/memory-types#how-does-it-work)
- [When should you use each layer?](https://docs.mem0.ai/core-concepts/memory-types#when-should-you-use-each-layer)
- [How it compares](https://docs.mem0.ai/core-concepts/memory-types#how-it-compares)
- [Put it into practice](https://docs.mem0.ai/core-concepts/memory-types#put-it-into-practice)
- [See it live](https://docs.mem0.ai/core-concepts/memory-types#see-it-live)

# [​](https://docs.mem0.ai/core-concepts/memory-types\#how-mem0-organizes-memory)  How Mem0 Organizes Memory

Mem0 separates memory into layers so agents remember the right detail at the right time. Think of it like a notebook: a sticky note for the current task, a daily journal for the session, and an archive for everything a user has shared.

**Why it matters**

- Keeps conversations coherent without repeating instructions.
- Lets agents personalize responses based on long-term preferences.
- Avoids over-fetching data by scoping memory to the correct layer.

## [​](https://docs.mem0.ai/core-concepts/memory-types\#key-terms)  Key terms

- **Conversation memory** – In-flight messages inside a single turn (what was just said).
- **Session memory** – Short-lived facts that apply for the current task or channel.
- **User memory** – Long-lived knowledge tied to a person, account, or workspace.
- **Organizational memory** – Shared context available to multiple agents or teams.

Conversation turn

Session memory

User memory

Org memory

Mem0 retrieval layer

## [​](https://docs.mem0.ai/core-concepts/memory-types\#short-term-vs-long-term-memory)  Short-term vs long-term memory

Short-term memory keeps the current conversation coherent. It includes:

- **Conversation history** – recent turns in order so the agent remembers what was just said.
- **Working memory** – temporary state such as tool outputs or intermediate calculations.
- **Attention context** – the immediate focus of the assistant, similar to what a person holds in mind mid-sentence.

Long-term memory preserves knowledge across sessions. It captures:

- **Factual memory** – user preferences, account details, and domain facts.
- **Episodic memory** – summaries of past interactions or completed tasks.
- **Semantic memory** – relationships between concepts so agents can reason about them later.

Mem0 maps these classic categories onto its layered storage so you can decide what should fade quickly versus what should last for months.

## [​](https://docs.mem0.ai/core-concepts/memory-types\#how-does-it-work)  How does it work?

Mem0 stores each layer separately and merges them when you query:

1. **Capture** – Messages enter the conversation layer while the turn is active.
2. **Promote** – Relevant details persist to session or user memory based on your `user_id`, `session_id`, and metadata.
3. **Retrieve** – The search pipeline pulls from all layers, ranking user memories first, then session notes, then raw history.

Copy

Ask AI

```
import os

from mem0 import Memory

memory = Memory(api_key=os.environ["MEM0_API_KEY"])

# Sticky note: conversation memory
memory.add(
    ["I'm Alex and I prefer boutique hotels."],
    user_id="alex",
    session_id="trip-planning-2025",
)

# Later in the session, pull long-term + session context
results = memory.search(
    "Any hotel preferences?",
    user_id="alex",
    session_id="trip-planning-2025",
)
```

Use `session_id` when you want short-term context to expire automatically; rely on `user_id` for lasting personalization.

## [​](https://docs.mem0.ai/core-concepts/memory-types\#when-should-you-use-each-layer)  When should you use each layer?

- **Conversation memory** – Tool calls or chain-of-thought that only matter within the current turn.
- **Session memory** – Multi-step tasks (onboarding flows, debugging sessions) that should reset once complete.
- **User memory** – Personal preferences, account state, or compliance details that must persist across interactions.
- **Organizational memory** – Shared FAQs, product catalogs, or policies that every agent should recall.

## [​](https://docs.mem0.ai/core-concepts/memory-types\#how-it-compares)  How it compares

| Layer | Lifetime | Short or long term | Best for | Trade-offs |
| --- | --- | --- | --- | --- |
| Conversation | Single response | Short-term | Tool execution detail | Lost after the turn finishes |
| Session | Minutes to hours | Short-term | Multi-step flows | Clear it manually when done |
| User | Weeks to forever | Long-term | Personalization | Requires consent/governance |
| Org | Configured globally | Long-term | Shared knowledge | Needs owner to keep current |

Avoid storing secrets or unredacted PII in user or org memories—Mem0 is retrievable by design. Encrypt or hash sensitive values first.

## [​](https://docs.mem0.ai/core-concepts/memory-types\#put-it-into-practice)  Put it into practice

- Use the [Add Memory](https://docs.mem0.ai/core-concepts/memory-operations/add) guide to persist user preferences.
- Follow [Advanced Memory Operations](https://docs.mem0.ai/platform/advanced-memory-operations) to tune metadata and graph writes.

## [​](https://docs.mem0.ai/core-concepts/memory-types\#see-it-live)  See it live

- [AI Tutor with Mem0](https://docs.mem0.ai/cookbooks/companions/ai-tutor) shows session vs user memories in action.
- [Support Inbox with Mem0](https://docs.mem0.ai/cookbooks/operations/support-inbox) demonstrates shared org memory.

[**Explore Memory Operations**](https://docs.mem0.ai/core-concepts/memory-operations/add) [**See a Cookbook**](https://docs.mem0.ai/cookbooks/operations/support-inbox)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/core-concepts/memory-types.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/core-concepts/memory-types)

[Quickstart\\
\\
Previous](https://docs.mem0.ai/platform/quickstart) [Add Memory\\
\\
Next](https://docs.mem0.ai/core-concepts/memory-operations/add)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![](https://downloads.intercomcdn.com/i/o/jjv2r0tt/659404/9e903493dd0a115e31b620e84189/9a987d2bf694d15c37d85f66f2be4813.png)
