from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import Any

from ai_agents_portfolio.config import settings


class LLMClient(ABC):
    mode = "unknown"

    @abstractmethod
    def generate_json(self, *, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        raise NotImplementedError


class MockLLMClient(LLMClient):
    mode = "mock"

    def generate_json(self, *, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        prompt = f"{system_prompt}\n\n{user_prompt}".lower()
        if "interview" in prompt:
            return {
                "summary": "Candidate appears strongest in applied backend and ML workflow delivery.",
                "tailored_pitch": "You build practical AI-enabled products by combining APIs, data workflows, and user-facing tooling.",
                "likely_questions": [
                    "How would you evaluate an internal copilot before rollout?",
                    "How do you separate prompt logic from application logic?",
                    "What tradeoffs matter when moving from prototype to production?"
                ],
                "star_stories": [
                    "Built a FastAPI and React workflow to move from raw CSVs to trained models.",
                    "Integrated mobile and IoT data flows to support real-time product scenarios."
                ],
                "gap_risks": [
                    "Need crisp examples of monitoring, evaluation, and rollback strategy for AI features."
                ],
            }
        if "dataset" in prompt or "csv" in prompt:
            return {
                "data_quality_checks": [
                    "Check label balance for the target variable.",
                    "Inspect missing values and duplicated customer identifiers.",
                    "Validate numeric ranges for tenure and monthly spend."
                ],
                "hypotheses": [
                    "High support ticket volume may correlate with churn.",
                    "Lower tenure may increase churn probability."
                ],
                "feature_ideas": [
                    "Support tickets per month of tenure.",
                    "Spend bucket and plan tier interaction."
                ],
                "recommended_charts": [
                    "Target balance bar chart",
                    "Spend vs tenure scatter plot",
                    "Boxplot of support tickets by churn"
                ],
                "analysis_plan": [
                    "Profile columns",
                    "Audit target leakage",
                    "Build a simple baseline classifier"
                ],
            }
        return {
            "executive_summary": "The notes indicate recurring friction in onboarding and demo readiness.",
            "key_findings": [
                "Data import is a recurring pain point.",
                "Teams need safer demo environments."
            ],
            "risks": [
                "Poor onboarding may affect activation and retention."
            ],
            "recommendations": [
                "Add CSV validation before upload.",
                "Create a sandbox demo mode."
            ],
            "next_steps": [
                "Define validation rules.",
                "Measure onboarding drop-off."
            ],
        }


class OpenAIResponsesClient(LLMClient):
    mode = "openai"

    def __init__(self):
        from openai import OpenAI

        kwargs: dict[str, Any] = {"api_key": settings.openai_api_key}
        if settings.openai_base_url:
            kwargs["base_url"] = settings.openai_base_url
        self._client = OpenAI(**kwargs)

    def generate_json(self, *, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        response = self._client.responses.create(
            model=settings.openai_model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        text = getattr(response, "output_text", "") or ""
        if not text:
            raise ValueError("Model returned empty output")
        return json.loads(text)


def build_llm_client() -> LLMClient:
    if settings.use_openai:
        return OpenAIResponsesClient()
    return MockLLMClient()
