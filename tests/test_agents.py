from ai_agents_portfolio.registry import build_registry


def test_registry_exposes_expected_agents():
    registry = build_registry()
    assert {"interview-coach", "research-brief", "csv-insight"} <= set(registry.keys())


def test_interview_coach_returns_structured_result():
    registry = build_registry()
    result = registry["interview-coach"].run(
        {
            "candidate_profile": "Engineer with FastAPI, React, and ML project delivery experience across portfolio apps.",
            "job_description": "We need someone to ship AI copilots and internal automation workflows.",
            "goals": ["tailor pitch"],
        }
    )
    assert "tailored_pitch" in result
    assert isinstance(result["likely_questions"], list)


def test_research_brief_returns_key_sections():
    registry = build_registry()
    result = registry["research-brief"].run(
        {
            "objective": "Summarize notes into a short PM brief",
            "audience": "Product manager",
            "source_notes": "Users struggle with onboarding and need safer demo environments.",
        }
    )
    assert "executive_summary" in result
    assert "recommendations" in result


def test_csv_insight_returns_analysis_plan():
    registry = build_registry()
    result = registry["csv-insight"].run(
        {
            "question": "How should we inspect the dataset before building a churn model?",
            "columns": ["tenure", "spend", "tickets", "churn"],
            "sample_rows": [{"tenure": 2, "spend": 10.5, "tickets": 1, "churn": 1}],
        }
    )
    assert "analysis_plan" in result
    assert "data_quality_checks" in result
