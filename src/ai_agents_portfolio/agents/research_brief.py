from __future__ import annotations

from ai_agents_portfolio.agents.base import BaseAgent
from ai_agents_portfolio.schemas import ResearchBriefInput


class ResearchBriefAgent(BaseAgent):
    name = "research-brief"
    description = "Turns rough notes into an executive-style brief."
    input_model = ResearchBriefInput

    def system_prompt(self) -> str:
        return (
            "You are a research synthesis agent. "
            "Return only valid JSON with keys: executive_summary, key_findings, risks, "
            "recommendations, next_steps."
        )

    def build_user_prompt(self, payload: ResearchBriefInput) -> str:
        return self.json_block(payload.model_dump())
