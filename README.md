# Mem0 RAG Chatbot Starter

A Streamlit chatbot that combines document retrieval (Chroma) with persistent user memory (Mem0). The chatbot autonomously decides when to search docs, search memory, or store new information about the user.

## Prerequisites

- Python 3.11+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))
- Mem0 API key ([sign up here](https://app.mem0.ai/))

## Quick Start

1. Clone this repo:
```bash
git clone https://github.com/YOUR_USERNAME/mem0-chatbot-starter.git
cd mem0-chatbot-starter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment:
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. Run the chatbot:
```bash
streamlit run app.py
```

5. Enter a User ID in the sidebar and start chatting.

## Project Structure

```
mem0-chatbot-starter/
├── app.py              # Main application (all code in one file)
├── knowledge_base/     # Markdown docs for RAG retrieval
├── requirements.txt    # Python dependencies
├── .env.example        # Template for environment variables
└── .gitignore
```

## How It Works

The chatbot has three tools:
- **search_docs**: Searches the knowledge base for technical answers
- **search_memory**: Retrieves stored context about the user
- **add_memory**: Stores new information the user shares

The LLM decides which tool to use based on each question.

## Full Tutorial

For a detailed walkthrough of how this code works, see the full tutorial article (link coming soon).
