from pathlib import Path
import re


ROOT = Path(__file__).parents[2]

SKILLS = {
    "office-hours": (
        "clarified problem frame",
        (
            "one high-leverage question",
            "facts",
            "assumptions",
            "success condition",
            "writing-plans",
        ),
    ),
    "plan-ceo-review": (
        "user value",
        ("scope", "differentiation", "sequencing", "should this work exist", "writing-plans"),
    ),
    "plan-eng-review": (
        "architecture",
        (
            "data flow",
            "failure modes",
            "testing",
            "security",
            "observability",
            "operational cost",
            "fail-open",
            "null",
            "error handling",
            "coverage",
            "writing-plans",
        ),
    ),
    "plan-design-review": (
        "design",
        (
            "information hierarchy",
            "states",
            "responsive",
            "accessibility",
            "content honesty",
            "route preservation",
            "visual consistency",
            "vibetest",
            "writing-plans",
        ),
    ),
    "plan-devex-review": (
        "developer experience",
        (
            "setup",
            "feedback loops",
            "test commands",
            "debugging",
            "contributor documentation",
            "dependency burden",
            "failure recovery",
            "writing-plans",
        ),
    ),
}

PROMPTS = tuple(f"tests/explicit-skill-requests/prompts/{name}-please.txt" for name in SKILLS)
FORBIDDEN_RUNTIME_MARKERS = (
    "gstack",
    "preamble",
    "telemetry",
    "update-check",
    "~/.gstack",
    "~/.claude/skills/gstack",
)

SAFETY_ACTIONS = (
    ("commit", r"\bcommit\b"),
    ("push", r"\bpush\b"),
    ("deploy", r"\bdeploy\b"),
    ("open pull request", r"\bopen (?:a )?pull requests?\b"),
    ("install runtime", r"\binstall (?:a )?runtimes?\b"),
    ("mutate production", r"\bmutate production\b"),
)
SAFETY_PROHIBITION = re.compile(r"\b(?:do not|does not|must not|never)\b")


def frontmatter(text: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert match, "skill must have YAML frontmatter"
    return match.group(1)


def safety_boundary(text: str) -> str:
    match = re.search(r"^## Safety Boundary\s*\n(?P<section>.*?)(?=^## |\Z)", text, re.S | re.M)
    assert match, "skill must have a Safety Boundary section"
    return match.group("section").lower()


def assert_safety_actions_are_prohibited(safety: str, skill_name: str) -> None:
    sentences = re.split(r"(?<=[.!?])\s+", safety)
    for label, pattern in SAFETY_ACTIONS:
        assert any(
            re.search(pattern, sentence) and SAFETY_PROHIBITION.search(sentence)
            for sentence in sentences
        ), f"{skill_name} Safety Boundary must prohibit: {label}"


def test_planning_skill_contracts_are_satisfied():
    for name, (required_term, required_terms) in SKILLS.items():
        path = ROOT / "skills" / name / "SKILL.md"
        assert path.is_file(), f"missing {path}"
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        fm = frontmatter(text)
        assert re.search(rf"^name:\s*{re.escape(name)}\s*$", fm, re.M)
        assert re.search(r"^description:\s*Use when\b", fm, re.M)
        assert required_term in lowered
        for term in required_terms:
            assert term.lower() in lowered, f"{name} missing required lens term: {term}"
        assert "do not commit" in lowered
        assert "writing-plans" in text
        safety = safety_boundary(text)
        assert SAFETY_PROHIBITION.search(safety), f"{name} Safety Boundary missing prohibition wording"
        assert_safety_actions_are_prohibited(safety, name)
        for marker in FORBIDDEN_RUNTIME_MARKERS:
            assert marker not in lowered, f"{name} contains removed runtime marker: {marker}"

        if name != "office-hours":
            for section in (
                "context reviewed",
                "strengths",
                "critical findings",
                "warnings",
                "open decisions",
                "required plan changes",
                "approve",
                "approve-with-nits",
                "request-changes",
            ):
                assert section in lowered, f"{name} missing output contract: {section}"


def test_explicit_trigger_prompts_are_pressure_scenarios():
    for prompt_path in PROMPTS:
        path = ROOT / prompt_path
        assert path.is_file(), f"missing {path}"
        text = path.read_text(encoding="utf-8").lower()
        assert text.strip(), f"empty prompt: {path}"
        assert any(
            term in text
            for term in ("ambiguous", "unclear", "not sure", "details", "rough", "incomplete", "vague")
        )
        assert any(term in text for term in ("today", "deadline", "minutes", "urgent", "time pressure"))
        assert any(term in text for term in ("implement", "implementation", "code", "edit", "start building"))
