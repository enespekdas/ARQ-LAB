from tooling.arq_client import infer_provider_type


def test_infer_provider_type_detects_github_https_locator() -> None:
    assert infer_provider_type("https://github.com/ARQ-Sec/folded-yaml-lineage.git") == "GITHUB"


def test_infer_provider_type_detects_github_ssh_locator() -> None:
    assert infer_provider_type("git@github.com:ARQ-Sec/folded-yaml-lineage.git") == "GITHUB"


def test_infer_provider_type_falls_back_to_generic_git() -> None:
    assert infer_provider_type("https://example.internal/scm/platform/repo.git") == "GENERIC_GIT"
