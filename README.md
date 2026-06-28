# 🤖 Kollie's AI Engineer Journey

A documented progression from complete beginner to AI engineer,
built in public on GitHub.

## 🌐 Live Demo
- **Frontend App:** https://kollie-ai-frontend.onrender.com
- **Backend API:** https://ai-engineer-journey-w5ru.onrender.com
- **API Docs:** https://ai-engineer-journey-w5ru.onrender.com/docs

## 🚀 What I Built
A full-stack AI-powered Document Assistant that can read PDFs and
text files, answer questions about them, and maintain conversation
memory — built with a FastAPI backend and Streamlit frontend,
deployed on Render.

## 📅 Progress Log

| Day | What I Built |
|-----|-------------|
| 1-3 | Python fundamentals — variables, loops, functions, file I/O |
| 4 | GitHub setup + live weather API integration |
| 5 | First Anthropic API integration — AI chat in the terminal |
| 6 | Prompt engineering + conversation memory in terminal |
| 7 | Single-document AI Q&A assistant |
| 8 | Multi-document AI assistant in the terminal |
| 9 | Streamlit web app — document assistant in the browser |
| 10 | Multi-file upload + chat history in the browser |
| 11 | Production error handling |
| 12 | Sidebar with document stats + clear history button |
| 13 | PDF file support |
| 14 | Full conversation memory |
| 15 | Professional README and portfolio polish |
| 16 | FastAPI backend with AI endpoints |
| 17 | Connected FastAPI backend to Streamlit frontend |
| 18 | Environment variables and config system |
| 19 | Deployment configuration |
| 20 | Deployed backend API to Render (live on internet) |
| 21 | Deployed full stack — frontend + backend live on internet |

## 🛠️ Tech Stack
- Python 3.14
- Anthropic Claude API
- Streamlit
- FastAPI
- Uvicorn
- PyPDF2
- python-dotenv
- Git & GitHub
- Render (cloud deployment)

## ▶️ How to Run Locally
```bash
pip install streamlit fastapi uvicorn anthropic python-dotenv pypdf2
uvicorn day16:app --reload
streamlit run day17.py
