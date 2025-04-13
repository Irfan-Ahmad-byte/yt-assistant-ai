# 🎥 YouTube Assistant AI

**AI-powered assistant for YouTube videos** — Summarize content, ask questions, and interact with videos using natural language.

---

## 🚀 Overview

**YouTube Assistant AI** is a full-stack application that enables users to:

- 🔍 **Summarize** lengthy YouTube videos.
- 💬 **Ask questions** about video content.
- 🧠 **Interact** with videos through natural language queries.

Built with a microservices architecture, the project integrates:

- **Frontend**: React.js
- **Backend**: FastAPI
- **AI Capabilities**: LangChain, OpenAI
- **Data Storage**: Qdrant Vector DB
- **Orchestration**: Docker Compose

---

## 🧠 Features

- **Transcript Extraction**: Utilizes LangChain's `YoutubeLoader` to fetch video transcripts.
- **Text Chunking**: Splits transcripts into manageable chunks using `RecursiveCharacterTextSplitter`.
- **Vector Storage**: Stores chunks in Qdrant for efficient retrieval.
- **Summarization**: Generates concise summaries with LangChain's `load_summarize_chain`.
- **Question Answering**: Retrieves relevant transcript sections to answer user queries using `RetrievalQA`.

---

## 🛠️ Tech Stack

- **Frontend**: React.js
- **Backend**: FastAPI
- **AI Libraries**: LangChain, OpenAI API
- **Vector Database**: Qdrant
- **Containerization**: Docker, Docker Compose
- **Environment Management**: `.env` files

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Irfan-Ahmad-byte/yt-assistant-ai.git
cd yt-assistant-ai
```

### 2. Set Up Environment Variables

Set environment variables as defined in `.env.example` file.

### 3. Build and Run

`docker-compose up --build`

## 🔍 Usage

- Access the Application

Visit http://localhost:3000 in your browser.

- Input YouTube URL

Enter the URL of the YouTube video you wish to analyze.

- Generate Summary

Click on the "Summarize" button to fetch and display the video summary.

- Ask Questions

Use the chat interface to ask questions about the video content.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author
Built with ❤️ by [Irfan Ahmad](!https://github.com/irfan-ahmad-byte)