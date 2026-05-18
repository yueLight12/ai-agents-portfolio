from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class InterviewCoachInput(BaseModel):
    candidate_profile: str = Field(..., min_length=20)
    job_description: str = Field(..., min_length=20)
    goals: list[str] = Field(default_factory=list)


class ResearchBriefInput(BaseModel):
    objective: str = Field(..., min_length=10)
    audience: str = Field(..., min_length=3)
    source_notes: str = Field(..., min_length=20)


class CsvInsightInput(BaseModel):
    question: str = Field(..., min_length=10)
    columns: list[str] = Field(default_factory=list)
    sample_rows: list[dict[str, Any]] = Field(default_factory=list)


class AgentRunResponse(BaseModel):
    agent: str
    mode: str
    result: dict[str, Any]
