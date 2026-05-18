from __future__ import annotations

from fastapi import FastAPI, HTTPException

from ai_agents_portfolio.registry import build_registry
from ai_agents_portfolio.schemas import AgentRunResponse

app = FastAPI(title="AI Agents Portfolio", version="0.1.0")
registry = build_registry()


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/agents")
def list_agents():
    return [
        {"name": agent.name, "description": agent.description, "mode": agent.llm.mode}
        for agent in registry.values()
    ]


@app.post("/agents/{agent_name}/run", response_model=AgentRunResponse)
def run_agent(agent_name: str, payload: dict):
    agent = registry.get(agent_name)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    try:
        result = agent.run(payload)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return AgentRunResponse(agent=agent.name, mode=agent.llm.mode, result=result)
