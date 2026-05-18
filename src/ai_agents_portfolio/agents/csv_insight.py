from __future__ import annotations

from ai_agents_portfolio.agents.base import BaseAgent
from ai_agents_portfolio.schemas import CsvInsightInput


class CsvInsightAgent(BaseAgent):
    name = "csv-insight"
    description = "Suggests a structured analysis path for tabular datasets."
    input_model = CsvInsightInput

    def system_prompt(self) -> str:
        return (
            "You are a data analysis planning agent. "
            "Return only valid JSON with keys: data_quality_checks, hypotheses, feature_ideas, "
            "recommended_charts, analysis_plan."
        )

    def build_user_prompt(self, payload: CsvInsightInput) -> str:
        return self.json_block(payload.model_dump())
