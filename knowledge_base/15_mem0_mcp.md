[Skip to main content](https://docs.mem0.ai/platform/mem0-mcp#content-area)

[Mem0 home page![light logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/light.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=556577ecf0728aa6702b33acbd810826)![dark logo](https://mintcdn.com/mem0/k4LG2Flv5533NbwL/logo/dark.svg?fit=max&auto=format&n=k4LG2Flv5533NbwL&q=85&s=6389a5a15cdc185b704af49279dff5d6)](https://app.mem0.ai/)

v1.0.1

Search...

Ctrl KAsk AI

Search...

Navigation

Getting Started

Mem0 MCP

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

- [What is Mem0 MCP?](https://docs.mem0.ai/platform/mem0-mcp#what-is-mem0-mcp)
- [Deployment Options](https://docs.mem0.ai/platform/mem0-mcp#deployment-options)
- [Available Tools](https://docs.mem0.ai/platform/mem0-mcp#available-tools)
- [Quickstart with Python (UVX)](https://docs.mem0.ai/platform/mem0-mcp#quickstart-with-python-uvx)
- [Quickstart with Docker](https://docs.mem0.ai/platform/mem0-mcp#quickstart-with-docker)
- [Quickstart with Smithery (Hosted)](https://docs.mem0.ai/platform/mem0-mcp#quickstart-with-smithery-hosted)
- [Quick Recovery](https://docs.mem0.ai/platform/mem0-mcp#quick-recovery)
- [Next Steps](https://docs.mem0.ai/platform/mem0-mcp#next-steps)
- [Additional Resources](https://docs.mem0.ai/platform/mem0-mcp#additional-resources)

**Prerequisites**

- Mem0 Platform account ( [Sign up here](https://app.mem0.ai/))
- API key ( [Get one from dashboard](https://app.mem0.ai/settings/api-keys))
- Python 3.10+, Docker, or Node.js 14+
- An MCP-compatible client (Claude Desktop, Cursor, or custom agent)

## [​](https://docs.mem0.ai/platform/mem0-mcp\#what-is-mem0-mcp)  What is Mem0 MCP?

Mem0 MCP Server exposes Mem0’s memory capabilities as MCP tools, letting AI agents decide when to save, search, or update information.

## [​](https://docs.mem0.ai/platform/mem0-mcp\#deployment-options)  Deployment Options

Choose from three deployment methods:

1. **Python Package (Recommended)** \- Install locally with `uvx` for instant setup
2. **Docker Container** \- Isolated deployment with HTTP endpoint
3. **Smithery** \- Remote hosted service for managed deployments

## [​](https://docs.mem0.ai/platform/mem0-mcp\#available-tools)  Available Tools

The MCP server exposes these memory tools to your AI client:

| Tool | Description |
| --- | --- |
| `add_memory` | Save text or conversation history for a user/agent |
| `search_memories` | Semantic search across existing memories with filters |
| `get_memories` | List memories with structured filters and pagination |
| `get_memory` | Retrieve one memory by its `memory_id` |
| `update_memory` | Overwrite a memory’s text after confirming the ID |
| `delete_memory` | Delete a single memory by `memory_id` |
| `delete_all_memories` | Bulk delete all memories in scope |
| `delete_entities` | Delete a user/agent/app/run entity and its memories |
| `list_entities` | Enumerate users/agents/apps/runs stored in Mem0 |

* * *

## [​](https://docs.mem0.ai/platform/mem0-mcp\#quickstart-with-python-uvx)  Quickstart with Python (UVX)

1

[Navigate to header](https://docs.mem0.ai/platform/mem0-mcp#)

Install the MCP Server

Copy

Ask AI

```
uv pip install mem0-mcp-server
```

2

[Navigate to header](https://docs.mem0.ai/platform/mem0-mcp#)

Configure your MCP client

Add this to your MCP client (e.g., Claude Desktop):

Copy

Ask AI

```
{
  "mcpServers": {
    "mem0": {
      "command": "uvx",
      "args": ["mem0-mcp-server"],
      "env": {
        "MEM0_API_KEY": "m0-...",
        "MEM0_DEFAULT_USER_ID": "your-handle"
      }
    }
  }
}
```

Set your environment variables:

Copy

Ask AI

```
export MEM0_API_KEY="m0-..."
export MEM0_DEFAULT_USER_ID="your-handle"
```

3

[Navigate to header](https://docs.mem0.ai/platform/mem0-mcp#)

Test with the Python agent

Copy

Ask AI

```
# Clone the mem0-mcp repository
git clone https://github.com/mem0ai/mem0-mcp.git
cd mem0-mcp

# Set your API keys
export MEM0_API_KEY="m0-..."
export OPENAI_API_KEY="sk-openai-..."

# Run the interactive agent
python example/pydantic_ai_repl.py
```

**Sample Interactions:**

Copy

Ask AI

```
User: Remember that I love tiramisu
Agent: Got it! I've saved that you love tiramisu.

User: What do you know about my food preferences?
Agent: Based on your memories, you love tiramisu.

User: Update my project: the mobile app is now 80% complete
Agent: Updated your project status successfully.
```

4

[Navigate to header](https://docs.mem0.ai/platform/mem0-mcp#)

Verify the setup

Your AI client can now:

- Automatically save information with `add_memory`
- Search memories with `search_memories`
- Update memories with `update_memory`
- Delete memories with `delete_memory`

If you get “Connection failed”, ensure your API key is valid and the server is running.

* * *

## [​](https://docs.mem0.ai/platform/mem0-mcp\#quickstart-with-docker)  Quickstart with Docker

1

[Navigate to header](https://docs.mem0.ai/platform/mem0-mcp#)

Build the Docker image

Copy

Ask AI

```
docker build -t mem0-mcp-server https://github.com/mem0ai/mem0-mcp.git
```

2

[Navigate to header](https://docs.mem0.ai/platform/mem0-mcp#)

Run the container

Copy

Ask AI

```
docker run --rm -d \
  --name mem0-mcp \
  -e MEM0_API_KEY="m0-..." \
  -p 8080:8081 \
  mem0-mcp-server
```

3

[Navigate to header](https://docs.mem0.ai/platform/mem0-mcp#)

Configure your client for HTTP

For clients that connect via HTTP (instead of stdio):

Copy

Ask AI

```
{
  "mcpServers": {
    "mem0-docker": {
      "command": "curl",
      "args": ["-X", "POST", "http://localhost:8080/mcp", "--data-binary", "@-"],
      "env": {
        "MEM0_API_KEY": "m0-..."
      }
    }
  }
}
```

4

[Navigate to header](https://docs.mem0.ai/platform/mem0-mcp#)

Verify the setup

Copy

Ask AI

```
# Check container logs
docker logs mem0-mcp

# Test HTTP endpoint
curl http://localhost:8080/health
```

The container should start successfully and respond to HTTP requests. If port 8080 is occupied, change it with `-p 8081:8081`.

* * *

## [​](https://docs.mem0.ai/platform/mem0-mcp\#quickstart-with-smithery-hosted)  Quickstart with Smithery (Hosted)

For the simplest integration, use Smithery’s hosted Mem0 MCP server - no installation required.**Example: One-click setup in Cursor**

1. Visit [smithery.ai/server/@mem0ai/mem0-memory-mcp](https://smithery.ai/server/@mem0ai/mem0-memory-mcp) and select Cursor as your client

![Smithery Mem0 MCP Configuration](https://mintcdn.com/mem0/c6tDVF6JIyyYQWAP/images/smithery-mem0-mcp.png?fit=max&auto=format&n=c6tDVF6JIyyYQWAP&q=85&s=d51ecbcf80d4ddc5b0ac44d7f5fdea6d)

2. Open Cursor → Settings → MCP
3. Click `mem0-mcp` → Initiate authorization
4. Configure Smithery with your environment:
   - `MEM0_API_KEY`: Your Mem0 API key
   - `MEM0_DEFAULT_USER_ID`: Your user ID
   - `MEM0_ENABLE_GRAPH_DEFAULT`: Optional, set to `true` for graph memories
5. Return to Cursor settings and wait for tools to load
6. Start chatting with Cursor and begin storing preferences

**For other clients:**
Visit [smithery.ai/server/@mem0ai/mem0-memory-mcp](https://smithery.ai/server/@mem0ai/mem0-memory-mcp) to connect any MCP-compatible client with your Mem0 credentials.

* * *

## [​](https://docs.mem0.ai/platform/mem0-mcp\#quick-recovery)  Quick Recovery

- **“uvx command not found”** → Install with `pip install uv` or use `pip install mem0-mcp-server` instead. Make sure your Python environment has `uv` installed (or system-wide).
- **“Connection refused”** → Check that the server is running and the correct port is configured
- **“Invalid API key”** → Get a new key from [Mem0 Dashboard](https://app.mem0.ai/settings/api-keys)
- **“Permission denied”** → Ensure Docker has access to bind ports (try with `sudo` on Linux)

* * *

## [​](https://docs.mem0.ai/platform/mem0-mcp\#next-steps)  Next Steps

[**MCP Integration Feature**](https://docs.mem0.ai/platform/features/mcp-integration) [**Gemini 3 with Mem0 MCP**](https://docs.mem0.ai/cookbooks/frameworks/gemini-3-with-mem0-mcp)

## [​](https://docs.mem0.ai/platform/mem0-mcp\#additional-resources)  Additional Resources

- **[Mem0 MCP Repository](https://github.com/mem0ai/mem0-mcp)** \- Source code and examples
- **[Platform Quickstart](https://docs.mem0.ai/platform/quickstart)** \- Direct API integration guide
- **[MCP Specification](https://modelcontextprotocol.io/)** \- Learn about MCP protocol

Was this page helpful?

YesNo

[Suggest edits](https://github.com/mem0ai/mem0/edit/main/docs/platform/mem0-mcp.mdx) [Raise issue](https://github.com/mem0ai/mem0/issues/new?title=Issue%20on%20docs&body=Path:%20/platform/mem0-mcp)

[Overview\\
\\
Previous](https://docs.mem0.ai/platform/overview) [Platform vs Open Source\\
\\
Next](https://docs.mem0.ai/platform/platform-vs-oss)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Smithery Mem0 MCP Configuration](https://mintcdn.com/mem0/c6tDVF6JIyyYQWAP/images/smithery-mem0-mcp.png?w=840&fit=max&auto=format&n=c6tDVF6JIyyYQWAP&q=85&s=257df2c5e8bb480baa9072c7632d1c4a)

![](https://downloads.intercomcdn.com/i/o/jjv2r0tt/659404/9e903493dd0a115e31b620e84189/9a987d2bf694d15c37d85f66f2be4813.png)
