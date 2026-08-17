from pathlib import Path
import re


ROOT = Path(__file__).parents[2]


HELPER_MAPPING = {
    "new_tab": "new_tab(url)",
    "goto_url": "goto_url(url)",
    "wait_for_load": "wait_for_load()",
    "page_info": "page_info()",
    "js": "js(expr)",
    "cdp": "cdp(",
    "capture_screenshot": "capture_screenshot()",
}

NO_RUNTIME_BOUNDARIES = (
    "bun",
    "playwright",
    "chromium",
    "gstack",
    "telemetry",
    "update check",
    "hidden session",
    "analytics",
    "automatic side effect",
)

UNAUTHORIZED_HELPER_CALLS = (
    "playwright(",
    "puppeteer(",
    "selenium(",
    "pyppeteer",
    "browser_use(",
    "browser-use",
    "requests_html",
)

UNAUTHORIZED_BROWSER_INSTRUCTIONS = (
    r"\b(?:use|run|start|launch|install|configure|persist)\s+(?:a\s+)?(?:shell browser|browser server|browser runtime)\b",
    r"\b(?:npm|pnpm|yarn|bun|pip|uv)\s+install\b",
)

REPRESENTATIVE_EXPLORATION = {
    "navigation": ("new_tab(url)", "goto_url(url)", "wait_for_load()"),
    "dom/element inspection": ("page_info()", "js(expr)", "dom", "elements"),
    "forms": ("forms", "inputs"),
    "dialogs": ("dialogs",),
    "uploads": ("uploads",),
    "responsive checks": ("responsive", "viewport"),
    "before/after state": ("before-state", "after-state"),
    "screenshots": ("capture_screenshot()", "screenshots"),
}

OUTPUT_CONTRACT = (
    "target url",
    "observed page state",
    "elements inspected",
    "actions taken",
    "failed or blocked",
    "evidence",
    "not tested",
    "blocked",
    "passed",
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


PROMPT_PATH = ROOT / "tests" / "explicit-skill-requests" / "prompts" / "browse-please.txt"


def frontmatter(text: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert match, "skill must have YAML frontmatter"
    return match.group(1)


def helper_mapping(text: str) -> str:
    match = re.search(r"\| need \| helper \|\n(?P<mapping>(?:\|.*\n)+)", text)
    assert match, "skill must include the Hermes helper mapping table"
    return match.group("mapping")


def assert_nearby_prohibition(text: str, term: str) -> None:
    matches = list(re.finditer(re.escape(term), text))
    assert matches, f"missing prohibited-boundary term: {term}"
    for match in matches:
        line_start = text.rfind("\n", 0, match.start()) + 1
        line_end = text.find("\n", match.end())
        context = text[line_start:] if line_end == -1 else text[line_start:line_end]
        assert re.search(r"\b(?:do not|must not|never|no|does not)\b", context), (
            f"{term!r} must have nearby prohibition wording"
        )


def safety_boundary(text: str) -> str:
    match = re.search(r"^## safety boundary\s*\n(?P<section>.*?)(?=^## |\Z)", text, re.S | re.M)
    assert match, "browse skill must have a Safety Boundary section"
    return match.group("section").lower()


def assert_safety_actions_are_prohibited(safety: str) -> None:
    sentences = re.split(r"(?<=[.!?])\s+", safety)
    for label, pattern in SAFETY_ACTIONS:
        assert any(
            re.search(pattern, sentence) and SAFETY_PROHIBITION.search(sentence)
            for sentence in sentences
        ), f"browse Safety Boundary must prohibit: {label}"


def test_browse_is_hermes_native_and_distinct_from_vibetest():
    path = ROOT / "skills" / "browse" / "SKILL.md"
    assert path.is_file(), f"missing {path}"
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    fm = frontmatter(text)
    mapping = helper_mapping(lowered)

    assert re.search(r"^name:\s*browse\s*$", fm, re.M)
    assert re.search(r"^description:\s*Use when\b", fm, re.M)
    assert "browser_exec" in lowered
    for helper, invocation in HELPER_MAPPING.items():
        assert helper in mapping, f"helper missing from Hermes mapping: {helper}"
        assert invocation in mapping, f"representative mapping entry missing: {invocation}"
    for term in UNAUTHORIZED_HELPER_CALLS:
        assert term not in mapping, f"unauthorized helper in Hermes mapping: {term}"
        assert term not in lowered, f"unauthorized helper instruction: {term}"
    for pattern in UNAUTHORIZED_BROWSER_INSTRUCTIONS:
        for match in re.finditer(pattern, lowered):
            line_start = lowered.rfind("\n", 0, match.start()) + 1
            line_end = lowered.find("\n", match.end())
            context = lowered[line_start:] if line_end == -1 else lowered[line_start:line_end]
            assert re.search(r"\b(?:do not|must not|never|no|does not)\b", context), (
                f"unauthorized browser instruction: {pattern}"
            )
    assert "vibetest" in lowered
    assert "direct exploration" in lowered
    assert "systematic qa" in lowered
    for term in NO_RUNTIME_BOUNDARIES:
        assert_nearby_prohibition(lowered, term)
    safety = safety_boundary(lowered)
    assert SAFETY_PROHIBITION.search(safety), "browse Safety Boundary missing prohibition wording"
    assert_safety_actions_are_prohibited(safety)
    for term in OUTPUT_CONTRACT:
        assert term in lowered, f"missing output contract term: {term}"
    for area, terms in REPRESENTATIVE_EXPLORATION.items():
        for term in terms:
            assert term in lowered, f"missing {area} coverage term: {term}"
    assert "automatically attached" in lowered
    assert "another vision tool" in lowered
    assert "guess credentials" in lowered or "guessed credentials" in lowered
    assert "copy secrets" in lowered


def test_browse_explicit_trigger_prompt_covers_direct_request():
    assert PROMPT_PATH.is_file(), f"missing {PROMPT_PATH}"
    text = PROMPT_PATH.read_text(encoding="utf-8").lower()
    assert text.strip()
    assert "browse" in text
    assert "https://example.com" in text
    assert "title" in text
    assert "visible links" in text or "links" in text
    assert "vibetest" in text
    assert "today" in text or "immediately" in text or "now" in text
    assert "implement" in text or "edit" in text or "build" in text
