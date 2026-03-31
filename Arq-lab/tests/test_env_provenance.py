from __future__ import annotations

from pathlib import Path

from tooling.env import _normalize_env_value, collect_env_provenance, load_config


def test_normalize_env_value_strips_quotes_and_inline_comments() -> None:
    normalized, diagnostics = _normalize_env_value('  "abc123"   # comment here')

    assert normalized == "abc123"
    assert diagnostics["quotesDetected"] is True
    assert diagnostics["inlineCommentDetected"] is True
    assert diagnostics["whitespaceChanged"] is True


def test_load_config_provenance_prefers_non_empty_root_env_over_empty_example(tmp_path: Path) -> None:
    (tmp_path / ".env").write_text("GIT_TOKEN=ghp_live_token_value\n", encoding="utf-8")
    (tmp_path / ".env.example").write_text("GIT_TOKEN=\n", encoding="utf-8")

    config = load_config(tmp_path)
    provenance = collect_env_provenance(tmp_path)

    assert config.git_token == "ghp_live_token_value"
    assert provenance["keys"]["GIT_TOKEN"]["winningSource"] == str(tmp_path / ".env")
    assert provenance["keys"]["GIT_TOKEN"]["finalLength"] == len("ghp_live_token_value")
    assert provenance["keys"]["GIT_TOKEN"]["maskedPreview"].startswith("ghp_")
