from __future__ import annotations

from ai_agents_portfolio.agents.base import BaseAgent
from ai_agents_portfolio.schemas import InterviewCoachInput


class InterviewCoachAgent(BaseAgent):
    name = "interview-coach"
    description = "Tailors interview preparation to a candidate profile and target role."
    input_model = InterviewCoachInput

    def system_prompt(self) -> str:
        return (
            "You are an interview preparation agent. "
            "Return only valid JSON with keys: summary, tailored_pitch, likely_questions, "
            "star_stories, gap_risks."
        )

    def build_user_prompt(self, payload: InterviewCoachInput) -> str:
        return self.json_block(payload.model_dump())
