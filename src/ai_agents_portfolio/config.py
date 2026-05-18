from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "").strip()
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()
    openai_base_url: str = os.getenv("OPENAI_BASE_URL", "").strip()

    @property
    def use_openai(self) -> bool:
        return bool(self.openai_api_key)


settings = Settings()
