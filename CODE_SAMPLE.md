# AI Agents Portfolio - Technical Work Sample

## Overview

This project is a compact AI agent platform built in Python. It demonstrates how to design reusable AI workflows with a clean application boundary, structured outputs, API access, command-line demos, and deterministic tests.

The goal was to build something small enough to review quickly, but realistic enough to show engineering judgment around AI-assisted products: separating prompt logic from transport logic, keeping model providers swappable, and making local testing possible without depending on a live API call.

## What It Includes

- Three reusable agents:
  - `interview-coach`: creates a tailored interview pitch, likely technical questions, STAR story ideas, and gap risks.
  - `research-brief`: converts raw notes into an executive brief with findings, risks, recommendations, and next steps.
  - `csv-insight`: inspects tabular dataset metadata and suggests quality checks, hypotheses, features, charts, and an analysis plan.
- A FastAPI service with health, registry, and agent execution endpoints.
- A CLI for fast local demos from JSON input files.
- A pluggable LLM layer with:
  - mock mode for deterministic local development and tests.
  - OpenAI mode when `OPENAI_API_KEY` is configured.
- Pytest coverage for registry behavior and structured agent outputs.

## Technical Highlights

- **Language:** Python 3.10+
- **API:** FastAPI
- **Schemas / validation:** Pydantic
- **LLM integration:** OpenAI SDK with a provider abstraction
- **Testing:** Pytest
- **Packaging:** `pyproject.toml` with editable install support

## Why This Is Relevant

This sample is relevant for AI training and software engineering work because it shows practical prompt-based application design, not just a one-off script. The agents return structured data that can be evaluated, tested, and integrated into a larger workflow.

It also shows how I think about AI systems:

- keep prompts and agent responsibilities focused.
- make output contracts explicit.
- avoid hard-coding one provider into business logic.
- support repeatable tests with deterministic mock behavior.
- expose the same core logic through both API and CLI surfaces.

## How To Run

```bash
cd ai-agents-portfolio
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
pytest
```

Run the API:

```bash
uvicorn ai_agents_portfolio.app:app --reload --port 8010
```

Run the CLI:

```bash
python -m ai_agents_portfolio.cli list
python -m ai_agents_portfolio.cli run interview-coach --input examples/interview_input.json
```

## Example Summary

The system can run locally in mock mode without an API key, which makes the project easy to review. If an `OPENAI_API_KEY` is added, the same agents can use a live model provider through the LLM abstraction.

