# 🤝 Sahayak — Agentic Onboarding Co-Pilot for Digital Banking

> Built for **SBI Hackathon @ HackCulture** · Theme: Agentic AI & Emerging Tech · Problem: Digital Adoption

Sahayak ("helper" in Hindi) is a **multi-agent AI system** that guides first-time digital banking users through financial tasks step-by-step — in plain, vernacular-friendly language — while completing routine actions on their behalf. Any money movement requires **explicit user confirmation** before execution.

---

## 🎯 Problem Statement

Millions of first-time digital banking users in India abandon onboarding flows because:
- Banking UX assumes digital literacy they don't have
- Instructions are in English, not their native language
- No one to guide them through actions like sending money or opening an FD

**Sahayak fixes this with a conversational, trust-safe multi-agent co-pilot.**

---

## ✨ Features

- **Plain-language guidance** — explains banking tasks in simple, vernacular-friendly terms
- **Multi-agent orchestration** — 4 specialized agents, each with a distinct responsibility
- **Trust & safety gate** — risky actions (transfers, FDs) require explicit user confirmation before execution
- **Intent classification** — understands Hinglish / mixed-language inputs
- **REST API** — easy to embed in any banking app frontend
- **Designed for vernacular expansion** — roadmap includes Bhashini / IndicTrans voice support

---

## 🧠 Agent Architecture

```
User request
     │
     ▼
┌─────────────────┐
│  Intent Agent   │  ← classifies what the user wants to do
└────────┬────────┘
         │
         ▼
┌──────────────────────┐
│ Simplification Agent │  ← explains it in plain, vernacular-friendly language
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│ Task-Execution Agent │  ← pre-fills workflow steps on behalf of user
└────────┬─────────────┘
         │
         ▼
┌────────────────────────┐
│ Trust & Safety Agent   │  ← independently flags risky actions
└────────┬───────────────┘
         │
         ▼
  [Confirmation Gate]  ←── user must explicitly approve
         │
         ▼
    Action Executes
```

---

## 🛠️ Tech Stack

| Layer          | Technology                          |
|----------------|-------------------------------------|
| Agent Framework| LangGraph                           |
| API Server     | FastAPI (Python)                    |
| LLM            | Groq · LLaMA 3.3 70B                |
| Frontend (planned) | React / React Native            |
| Voice / I18n (planned) | IndicTrans / Bhashini API |
| Language       | Python 3.11+                        |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- [Groq API Key](https://console.groq.com)

### Setup

```bash
# Clone the repository
git clone https://github.com/vikash1311/sahayak-onboarding-copilot.git
cd sahayak-onboarding-copilot

# Install dependencies
pip install -r requirements.txt --break-system-packages

# Configure environment
cp .env.example .env
# Add your GROQ_API_KEY to .env
```

### Run

```bash
# Quick CLI test (graph mode)
python -m agents.graph

# Start the API server
uvicorn app.main:app --reload
```

### Example API Call

```bash
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{"user_input": "I want to send money to my son", "language": "Hindi-English mix"}'
```

---

## 📁 Project Structure

```
sahayak-onboarding-copilot/
├── agents/               # LangGraph agent definitions
│   ├── intent_agent.py   # Classifies user intent
│   ├── simplification_agent.py
│   ├── task_agent.py     # Pre-fills banking workflows
│   ├── safety_agent.py   # Trust & risk flagging
│   └── graph.py          # LangGraph orchestration graph
├── app/
│   └── main.py           # FastAPI entry point & /run endpoint
├── requirements.txt
└── README.md
```

---

## 🔮 Roadmap

- [ ] Vernacular voice input via **Bhashini API**
- [ ] React co-pilot widget embeddable in banking apps
- [ ] Persistent session audit log (PostgreSQL)
- [ ] Real banking sandbox API integration (FD / transfer simulation)
- [ ] Multi-language support (Hindi, Marathi, Tamil, Bengali)

---

## 🏆 Hackathon

Built at **HackCulture · SBI Hackathon**
- **Theme:** Agentic AI & Emerging Tech
- **Problem Statement:** Digital Adoption in banking for first-time users

---

## 👨‍💻 Author

**Vikash Gautam**
[GitHub](https://github.com/vikash1311) · [LinkedIn](https://linkedin.com/in/vikash2808) · [Portfolio](https://vikash-gautam.netlify.app)

---

## 📄 License

MIT
