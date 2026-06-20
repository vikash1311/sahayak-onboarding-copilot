"""
Sahayak — Agentic Onboarding Co-Pilot
Multi-agent LangGraph skeleton: Intent -> Simplify -> Execute -> Trust&Safety -> Done

Run: python -m agents.graph
Requires: pip install langgraph langchain-groq python-dotenv --break-system-packages
Set GROQ_API_KEY in a .env file (see .env.example).
"""

import os
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)


class SahayakState(TypedDict):
    user_input: str
    language: str
    intent: Optional[str]
    simplified_explanation: Optional[str]
    proposed_action: Optional[dict]
    risk_flag: Optional[str]
    confirmed: bool
    final_result: Optional[str]


# ---------- Agent 1: Intent ----------
def intent_agent(state: SahayakState) -> SahayakState:
    prompt = f"""You are a banking intent classifier for a first-time digital banking user.
Classify the user's request into one of: UPI_SETUP, FUND_TRANSFER, FD_CREATION, BALANCE_CHECK, OTHER.
User said (in {state['language']}): "{state['user_input']}"
Respond with only the category name."""
    intent = llm.invoke(prompt).content.strip()
    return {**state, "intent": intent}


# ---------- Agent 2: Simplification ----------
def simplification_agent(state: SahayakState) -> SahayakState:
    prompt = f"""Explain in simple {state['language']}, in 2 short sentences, no jargon,
what the user is about to do for intent: {state['intent']}.
Avoid technical banking terms. Use everyday language a first-time digital banking user would understand."""
    explanation = llm.invoke(prompt).content.strip()
    return {**state, "simplified_explanation": explanation}


# ---------- Agent 3: Task Execution (pre-fill, not actually executing money movement here) ----------
def task_execution_agent(state: SahayakState) -> SahayakState:
    action = {
        "intent": state["intent"],
        "steps": [
            "Step 1: Verify account",
            "Step 2: Pre-fill required fields",
            "Step 3: Await user confirmation",
        ],
    }
    return {**state, "proposed_action": action}


# ---------- Agent 4: Trust & Safety ----------
def trust_safety_agent(state: SahayakState) -> SahayakState:
    risky_intents = {"FUND_TRANSFER", "FD_CREATION"}
    flag = "REQUIRES_EXPLICIT_CONFIRMATION" if state["intent"] in risky_intents else "LOW_RISK"
    return {**state, "risk_flag": flag}


# ---------- Confirmation gate ----------
def confirmation_gate(state: SahayakState) -> str:
    if state["risk_flag"] == "REQUIRES_EXPLICIT_CONFIRMATION" and not state["confirmed"]:
        return "await_confirmation"
    return "execute"


def await_confirmation_node(state: SahayakState) -> SahayakState:
    return {
        **state,
        "final_result": f"Waiting for your confirmation before proceeding with: {state['intent']}",
    }


def execute_node(state: SahayakState) -> SahayakState:
    return {
        **state,
        "final_result": f"Action '{state['intent']}' completed successfully (simulated).",
    }


def build_graph():
    graph = StateGraph(SahayakState)
    graph.add_node("intent", intent_agent)
    graph.add_node("simplify", simplification_agent)
    graph.add_node("execute_plan", task_execution_agent)
    graph.add_node("trust_safety", trust_safety_agent)
    graph.add_node("await_confirmation", await_confirmation_node)
    graph.add_node("execute", execute_node)

    graph.set_entry_point("intent")
    graph.add_edge("intent", "simplify")
    graph.add_edge("simplify", "execute_plan")
    graph.add_edge("execute_plan", "trust_safety")
    graph.add_conditional_edges(
        "trust_safety",
        confirmation_gate,
        {"await_confirmation": "await_confirmation", "execute": "execute"},
    )
    graph.add_edge("await_confirmation", END)
    graph.add_edge("execute", END)

    return graph.compile()


if __name__ == "__main__":
    app = build_graph()
    result = app.invoke(
        {
            "user_input": "I want to send money to my son",
            "language": "Hindi-English mix",
            "intent": None,
            "simplified_explanation": None,
            "proposed_action": None,
            "risk_flag": None,
            "confirmed": False,
            "final_result": None,
        }
    )
    print("\n--- Sahayak run ---")
    for k, v in result.items():
        print(f"{k}: {v}")
