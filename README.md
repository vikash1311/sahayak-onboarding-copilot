# Sahayak — Agentic Onboarding Co-Pilot for First-Time Digital Banking Users

Built for SBI Hackathon @ HackCulture — Theme: Agentic AI & Emerging Tech — Problem Statement: Digital Adoption

## What it does

Sahayak is a multi-agent system that guides first-time digital banking users through
tasks step-by-step, in plain language, while completing routine actions on their
behalf — with explicit confirmation required before any money movement.

## Architecture

```
User request -> Intent Agent -> Simplification Agent -> Task-Execution Agent
              -> Trust & Safety Agent -> [confirmation gate] -> Action executes
```

- **Intent agent** — classifies what the user wants to do
- **Simplification agent** — explains it in plain, vernacular-friendly language
- **Task-execution agent** — pre-fills the workflow steps
- **Trust & safety agent** — independently flags risky actions (transfers, FDs) and
  forces explicit user confirmation before execution

## Stack

LangGraph · FastAPI · Groq (LLaMA 3.3 70B) · designed to integrate with React/React Native
frontend and IndicTrans/Bhashini for vernacular + voice support.

## Run locally

```bash
pip install -r requirements.txt --break-system-packages
cp .env.example .env   # add your GROQ_API_KEY
python -m agents.graph              # quick CLI test
uvicorn app.main:app --reload       # API server
```

Then:
```bash
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{"user_input": "I want to send money to my son", "language": "Hindi-English mix"}'
```

## Roadmap (next phase)

- [ ] Vernacular voice input via Bhashini API
- [ ] React co-pilot widget embedded in banking app demo
- [ ] Persistent session audit log (PostgreSQL)
- [ ] Real banking sandbox API integration for FD/transfer simulation
