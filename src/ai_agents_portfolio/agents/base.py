from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel

from ai_agents_portfolio.llm import LLMClient


class BaseAgent(ABC):
    name: str
    description: str
    input_model: type[BaseModel]

    def __init__(self, llm: LLMClient):
        self.llm = llm

    @abstractmethod
    def system_prompt(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def build_user_prompt(self, payload: BaseModel) -> str:
        raise NotImplementedError

    def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        validated = self.input_model.model_validate(payload)
        return self.llm.generate_json(
            system_prompt=self.system_prompt(),
            user_prompt=self.build_user_prompt(validated),
        )

    @staticmethod
    def json_block(value: dict[str, Any]) -> str:
        return json.dumps(value, indent=2, ensure_ascii=True)
