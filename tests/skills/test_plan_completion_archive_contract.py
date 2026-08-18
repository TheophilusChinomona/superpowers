from pathlib import Path


ROOT = Path(__file__).parents[2]
SDD = ROOT / "skills" / "subagent-driven-development" / "SKILL.md"
TDD = ROOT / "skills" / "test-driven-development" / "SKILL.md"
PLANS = ROOT / "skills" / "writing-plans" / "SKILL.md"
ARCHIVE = ROOT / "docs" / "superpowers" / "archive" / "README.md"

ARCHIVE_PATHS = (
    "docs/superpowers/archive/plans/",
    "docs/superpowers/archive/specs/",
)


def assert_completion_gate(text: str, name: str) -> None:
    lowered = text.lower()
    assert "plan/spec completion gate" in lowered, f"{name} missing completion gate"
    assert "re-read the plan" in lowered, f"{name} must re-read the plan"
    assert "linked spec" in lowered, f"{name} must verify the linked spec"
    assert "verification record" in lowered, f"{name} must record verification"
    assert "git mv" in lowered, f"{name} must archive with git mv"
    for archive_path in ARCHIVE_PATHS:
        assert archive_path in lowered, f"{name} missing archive path: {archive_path}"
    assert "unresolved critical" in lowered
    assert "unresolved important" in lowered
    assert "do not archive" in lowered


def test_sdd_and_tdd_end_with_plan_spec_verification_and_archive_gate():
    assert_completion_gate(SDD.read_text(encoding="utf-8"), "SDD")
    assert_completion_gate(TDD.read_text(encoding="utf-8"), "TDD")


def test_plan_writing_and_archive_policy_define_the_same_destinations():
    plans_text = PLANS.read_text(encoding="utf-8").lower()
    archive_text = ARCHIVE.read_text(encoding="utf-8").lower()
    for text, name in ((plans_text, "writing-plans"), (archive_text, "archive policy")):
        for archive_path in ARCHIVE_PATHS:
            assert archive_path in text, f"{name} missing archive path: {archive_path}"
    assert "archive only after" in plans_text
    assert "verified completion" in archive_text
    assert "source of truth" in archive_text
