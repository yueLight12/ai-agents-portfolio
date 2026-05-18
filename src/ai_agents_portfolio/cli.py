from __future__ import annotations

import argparse
import json
from pathlib import Path

from ai_agents_portfolio.registry import build_registry


def main() -> None:
    parser = argparse.ArgumentParser(description="Run portfolio AI agents from the command line.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List available agents")

    run_parser = subparsers.add_parser("run", help="Run one agent from a JSON file")
    run_parser.add_argument("agent_name")
    run_parser.add_argument("--input", required=True, dest="input_path")

    args = parser.parse_args()
    registry = build_registry()

    if args.command == "list":
        for agent in registry.values():
            print(f"{agent.name}: {agent.description} [{agent.llm.mode}]")
        return

    payload = json.loads(Path(args.input_path).read_text(encoding="utf-8"))
    agent = registry.get(args.agent_name)
    if not agent:
        raise SystemExit(f"Unknown agent: {args.agent_name}")
    result = agent.run(payload)
    print(json.dumps({"agent": agent.name, "mode": agent.llm.mode, "result": result}, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
