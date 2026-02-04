[Skip to main content](https://docs.mem0.ai/open-source/overview#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Getting Started

Overview

[Welcome](https://docs.mem0.ai/introduction) [Mem0 Platform](https://docs.mem0.ai/platform/overview) [Open Source](https://docs.mem0.ai/open-source/overview) [OpenMemory](https://docs.mem0.ai/openmemory/overview) [Cookbooks](https://docs.mem0.ai/cookbooks/overview) [Integrations](https://docs.mem0.ai/integrations) [API Reference](https://docs.mem0.ai/api-reference) [Release Notes](https://docs.mem0.ai/changelog)

- [Documentation](https://docs.mem0.ai/introduction)

##### Getting Started

- [Overview](https://docs.mem0.ai/open-source/overview)
- [Python SDK Quickstart](https://docs.mem0.ai/open-source/python-quickstart)
- [Node SDK Quickstart](https://docs.mem0.ai/open-source/node-quickstart)

##### Self-Hosting Features

- [Overview](https://docs.mem0.ai/open-source/features/overview)
- [Graph Memory](https://docs.mem0.ai/open-source/features/graph-memory)
- [Enhanced Metadata Filtering](https://docs.mem0.ai/open-source/features/metadata-filtering)
- [Reranker-Enhanced Search](https://docs.mem0.ai/open-source/features/reranker-search)
- [Async Memory](https://docs.mem0.ai/open-source/features/async-memory)
- [Multimodal Support](https://docs.mem0.ai/open-source/features/multimodal-support)
- [Custom Fact Extraction Prompt](https://docs.mem0.ai/open-source/features/custom-fact-extraction-prompt)
- [Custom Update Memory Prompt](https://docs.mem0.ai/open-source/features/custom-update-memory-prompt)
- [REST API Server](https://docs.mem0.ai/open-source/features/rest-api)
- [OpenAI Compatibility](https://docs.mem0.ai/open-source/features/openai_compatibility)

##### Configuration

- [Configure the OSS Stack](https://docs.mem0.ai/open-source/configuration)
- LLMs

- Vector Databases

- Embedding Models

- Rerankers


##### Community & Support

- [Development](https://docs.mem0.ai/contributing/development)
- [Documentation](https://docs.mem0.ai/contributing/documentation)

On this page

- [Mem0 Open Source Overview](https://docs.mem0.ai/open-source/overview#mem0-open-source-overview)
- [What Mem0 OSS provides](https://docs.mem0.ai/open-source/overview#what-mem0-oss-provides)
- [Choose your path](https://docs.mem0.ai/open-source/overview#choose-your-path)
- [Default components](https://docs.mem0.ai/open-source/overview#default-components)
- [Keep going](https://docs.mem0.ai/open-source/overview#keep-going)

# [​](https://docs.mem0.ai/open-source/overview\#mem0-open-source-overview)  Mem0 Open Source Overview

Mem0 Open Source delivers the same adaptive memory engine as the platform, but packaged for teams that need to run everything on their own infrastructure. You own the stack, the data, and the customizations.

Mem0 v1.0.0 brought rerankers, async-by-default clients, and Azure OpenAI support. See the [release notes](https://docs.mem0.ai/changelog) for the full rundown before upgrading.

## [​](https://docs.mem0.ai/open-source/overview\#what-mem0-oss-provides)  What Mem0 OSS provides

- **Full control**: Tune every component, from LLMs to vector stores, inside your environment.
- **Offline ready**: Keep memory on your own network when compliance or privacy demands it.
- **Extendable codebase**: Fork the repo, add providers, and ship custom automations.

Begin with the [Python quickstart](https://docs.mem0.ai/open-source/python-quickstart) (or the Node.js variant) to clone the repo, configure dependencies, and validate memory reads/writes locally.

## [​](https://docs.mem0.ai/open-source/overview\#choose-your-path)  Choose your path

[**Python Quickstart** \\
\\
Bootstrap CLI and verify add/search loop.](https://docs.mem0.ai/open-source/python-quickstart) [**Node.js Quickstart** \\
\\
Install TypeScript SDK and run starter script.](https://docs.mem0.ai/open-source/node-quickstart)

[**Configure Components** \\
\\
LLM, embedder, vector store, reranker setup.](https://docs.mem0.ai/open-source/configuration) [**Graph Memory Capability** \\
\\
Relationship-aware recall with Neo4j, Memgraph.](https://docs.mem0.ai/open-source/features/graph-memory) [**Tune Retrieval & Rerankers** \\
\\
Hybrid retrieval and reranker controls.](https://docs.mem0.ai/open-source/features/reranker-search)

[**Deploy with Docker Compose** \\
\\
Reference deployment with REST endpoints.](https://docs.mem0.ai/cookbooks/companions/local-companion-ollama) [**Use the REST API** \\
\\
Async add/search flows and automation.](https://docs.mem0.ai/open-source/features/rest-api)

Need a managed alternative? Compare hosting models in the [Platform vs OSS guide](https://docs.mem0.ai/platform/platform-vs-oss) or switch tabs to the Platform documentation.

What you get with Mem0 OSS

| Benefit | What you get |
| --- | --- |
| Full infrastructure control | Host on your own servers with complete access to configuration and deployment. |
| Complete customization | Modify the implementation, extend functionality, and tailor it to your stack. |
| Local development | Perfect for development, testing, and offline environments. |
| No vendor lock-in | Keep ownership of your data, providers, and pipelines. |
| Community driven | Contribute improvements and tap into a growing ecosystem. |

## [​](https://docs.mem0.ai/open-source/overview\#default-components)  Default components

Mem0 OSS works out of the box with sensible defaults:

- LLM: OpenAI `gpt-4.1-nano-2025-04-14` (via `OPENAI_API_KEY`)
- Embeddings: OpenAI `text-embedding-3-small`
- Vector store: Local Qdrant instance storing data at `/tmp/qdrant`
- History store: SQLite database at `~/.mem0/history.db`
- Reranker: Disabled until you configure a provider

Override any component with [`Memory.from_config`](https://docs.mem0.ai/open-source/configuration).

## [​](https://docs.mem0.ai/open-source/overview\#keep-going)  Keep going

[**Review Platform vs OSS**](https://docs.mem0.ai/platform/platform-vs-oss) [**Run the Python Quickstart**](https://docs.mem0.ai/open-source/python-quickstart)

Need a managed alternative? Compare hosting models in the [Platform vs OSS guide](https://docs.mem0.ai/platform/platform-vs-oss) or switch tabs to the Platform documentation.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/open-source/overview.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/open-source/overview)

[Python SDK Quickstart\\
\\
Next](https://docs.mem0.ai/open-source/python-quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![](https://downloads.intercomcdn.com/i/o/jjv2r0tt/659404/9e903493dd0a115e31b620e84189/9a987d2bf694d15c37d85f66f2be4813.png)
