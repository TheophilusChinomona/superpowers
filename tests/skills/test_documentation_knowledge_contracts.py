from pathlib import Path
import re


ROOT = Path(__file__).parents[2]

SKILL_CONTRACTS = {
    "document-release": (
        "release",
        (
            "verified",
            "git diff",
            "tests",
            "routes",
            "docs",
            "unverified",
            "sentio-os/01-projects",
        ),
    ),
    "document-generate": (
        "generate",
        (
            "inventory",
            "audience",
            "entry points",
            "dependencies",
            "inference",
            "verify every path",
            "source of truth",
        ),
    ),
    "learn": (
        "durable",
        (
            "reusable",
            "project",
            "date",
            "observed evidence",
            "lesson",
            "application boundary",
            "source links",
            "01-projects",
            "03-resources",
            "superseded",
        ),
    ),
    "diagram": (
        "source-first",
        (
            "mermaid",
            "excalidraw json",
            "editable source",
            "renderer",
            "svg",
            "png",
            "no renderer",
            "local or repository tooling",
        ),
    ),
}

SENTIO_OS_PATH = r"C:\Users\Givemore\Desktop\Sentio-OS"
MISSING_PATH_GATE = (
    "if it is missing, report the missing path and ask",
    "do not substitute another vault",
)

NO_SIDE_EFFECTS = (
    "do not automatically commit",
    "do not automatically push",
    "do not automatically deploy",
    "do not automatically open a pull request",
    "do not automatically install a runtime",
    "do not automatically mutate production",
)

SECRET_BOUNDARY = (
    "secret",
    "credential",
    ".env",
    "token",
    "private key",
)

SEMANTIC_SECRET_PROTECTION = (
    "never read, print, or copy credentials or equivalent sensitive material",
    ".env",
    "tokens",
    "private keys",
    "sensitive logs",
)

FORBIDDEN_UPSTREAM_RUNTIME = (
    "~/.gstack",
    "gstack/bin",
    "gstack-update",
    "gstack-config",
    "gstack-session",
    "telemetry",
    "update-check",
    "update check",
    ".jsonl",
    "bun",
    "playwright",
    "shell helper",
    "automatic file-opening",
)

PROMPTS = {
    "document-release": (
        "unverified",
        "release",
        "tests",
        "today",
        "implement",
    ),
    "document-generate": (
        ".env",
        "credential",
        "repository",
        "documentation",
        "edit",
    ),
    "learn": (
        "transient",
        "one-off",
        "durable",
        "reusable",
        "todo",
        "today",
    ),
    "diagram": (
        "incomplete",
        "relationship",
        "mermaid",
        "source",
        "renderer",
        "implement",
    ),
}


def frontmatter(text: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert match, "skill must have YAML frontmatter"
    return match.group(1)


def test_documentation_knowledge_skill_contracts_are_satisfied():
    for name, (required_term, required_terms) in SKILL_CONTRACTS.items():
        path = ROOT / "skills" / name / "SKILL.md"
        assert path.is_file(), f"missing {path}"
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        fm = frontmatter(text)

        assert re.search(rf"^name:\s*{re.escape(name)}\s*$", fm, re.M)
        assert re.search(r"^description:\s*Use when\b", fm, re.M)
        assert required_term in lowered
        for term in required_terms:
            assert term in lowered, f"{name} missing required contract term: {term}"

        if name == "diagram":
            assert "mermaid remains the default source for simple" in lowered
            assert "excalidraw json only when the user explicitly requests" in lowered
            assert "when a flowchart renderer supports that conversion" not in lowered
            assert "repository or hermes tools" not in lowered

        assert "sentio-os" in lowered
        assert SENTIO_OS_PATH in text, f"{name} must use the exact Sentio-OS path"
        for term in MISSING_PATH_GATE:
            assert term in lowered, f"{name} missing missing-path gate term: {term}"
        assert "repository" in lowered
        assert "source of truth" in lowered
        for term in SECRET_BOUNDARY:
            assert term in lowered, f"{name} missing secret boundary term: {term}"
        for term in SEMANTIC_SECRET_PROTECTION:
            assert term in lowered, f"{name} missing semantic secret protection: {term}"
        for term in NO_SIDE_EFFECTS:
            assert term in lowered, f"{name} missing no-side-effect boundary: {term}"
        for marker in FORBIDDEN_UPSTREAM_RUNTIME:
            assert marker not in lowered, f"{name} contains removed runtime marker: {marker}"


def test_documentation_knowledge_explicit_trigger_prompts_cover_risky_cases():
    for name, required_terms in PROMPTS.items():
        path = ROOT / "tests" / "explicit-skill-requests" / "prompts" / f"{name}-please.txt"
        assert path.is_file(), f"missing {path}"
        text = path.read_text(encoding="utf-8").lower()
        assert text.strip(), f"empty prompt: {path}"
        assert name in text
        for term in required_terms:
            assert term in text, f"{name} prompt missing risky-case term: {term}"
