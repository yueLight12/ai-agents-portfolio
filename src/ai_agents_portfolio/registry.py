from __future__ import annotations

from ai_agents_portfolio.agents import CsvInsightAgent, InterviewCoachAgent, ResearchBriefAgent
from ai_agents_portfolio.llm import build_llm_client


def build_registry():
    llm = build_llm_client()
    agents = [
        InterviewCoachAgent(llm),
        ResearchBriefAgent(llm),
        CsvInsightAgent(llm),
    ]
    return {agent.name: agent for agent in agents}
