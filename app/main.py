"""
FastAPI wrapper around the Sahayak LangGraph agent.
Run: uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel
from agents.graph import build_graph

app = FastAPI(title="Sahayak — Agentic Onboarding Co-Pilot")
graph = build_graph()


class TaskRequest(BaseModel):
    user_input: str
    language: str = "English"
    confirmed: bool = False


@app.post("/run")
def run_task(req: TaskRequest):
    result = graph.invoke(
        {
            "user_input": req.user_input,
            "language": req.language,
            "intent": None,
            "simplified_explanation": None,
            "proposed_action": None,
            "risk_flag": None,
            "confirmed": req.confirmed,
            "final_result": None,
        }
    )
    return result


@app.get("/health")
def health():
    return {"status": "ok"}
