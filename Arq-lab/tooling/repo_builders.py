from __future__ import annotations

import textwrap
from pathlib import Path
from typing import Any

from .git_factory import GitFactory
from .models import LabConfig, ScenarioSpec
from .utils import count_lines, ensure_dir, run_command, safe_rmtree, write_json, write_text, write_yaml_like

JAVA_MODULES = ["settlement", "payout", "partner", "ledger", "balance", "refund", "invoice", "dispute"]
PY_MODULES = ["dispatch", "delivery", "preferences", "templates", "routing", "audit", "metrics", "retry"]
NODE_MODULES = ["partners", "profiles", "invites", "tokens", "audit", "events", "compliance", "sessions"]
CSHARP_MODULES = ["Partners", "Tokens", "Invoices", "Balances", "Audit", "Callbacks"]
GO_MODULES = ["claims", "devices", "policies", "enrollment", "manifests", "bootstrap"]

GENERIC_SECRET_ALPHA = "A3-ABC123-ABCDEFGHIJK-ABCDE-ABCDE-ABCDE"
GENERIC_SECRET_BRAVO = "Ab9K2mQ7pL4xR8nT5vW1Yz7Ck3Hs6Fq2"
GENERIC_SECRET_CHARLIE = "J8nP3vT6xZ1mR4qW7cF2hK9sL5dY8b"
GENERIC_SECRET_DELTA = "N4xC7vB2mQ9rT5yK1pL8dF3hS6wZ0j"
GENERIC_SECRET_ECHO = "R6mV2qL9xC4tY8nP1kD5hF7sW3zB0j"
GENERIC_SECRET_FOXTROT = "V9pT4mQ1xZ7cR2nL8kD5hF3sW6yB0j"
GENERIC_SECRET_GOLF = "0123456789ABCDEFA31a"

PRIVATE_KEY_BLOCK_A = textwrap.dedent(
    """\
    -----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAtmJvYV7t6Vg4l0xJ5HfZK3aV6D5r5YQf5x4mG8c+K2h0mK8L
    2s9mDkLQb2j7C1Kp8v8n2qgQOa0fB7x8Y6c7E6dOe8hQz3b7x1l9kCkWc7oZr0eP
    v8pQZlQm8oC0JjTj3cV0tYd9y3nQ8Zk5hQm2nV7t7gqQz7vG7k0Zy+9oQIDAQAB
    AoIBAB9H0r2fJpO6m9l8qPp6q2G9u6x1m2q0u2R8v2e8Z1k4FQb0vKj7zq9dXxVw
    Vh2h4fY5Z+0wG9lT3xU1nQd9pQbK2uG2cQv5b3bJt0WmQy7mJm0Y8Rr0nQ+vPj2A
    tYw9nV2uRz0qY0o8dPj8Pq7o1Z0aX9pQ3o0x5G8QKBgQDhY0f+JrQm8oC0JjTj3c
    V0tYd9y3nQ8Zk5hQm2nV7t7gqQz7vG7k0Zy+9oQKBgQClpS1mYg7uQx3cJ8o9l0
    xJ5HfZK3aV6D5r5YQf5x4mG8c+K2h0mK8L2s9mDkLQ==
    -----END RSA PRIVATE KEY-----
    """
)

PRIVATE_KEY_BLOCK_B = textwrap.dedent(
    """\
    -----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEAzQm5vL9t2Xg7k1rP4hFd8sW2mY6nQ1tV5cR9pK3xJ7bN0dL2
    w8qFh3mT6vY1pD4kR7sC2nB5xJ8qL0tV3mY6pR9wF2cH5kN8dQ1tV4yB7mL0pS3x
    c6nQ9rT2vW5yK8mP1dF4hJ7sL0xC3vB6nM9qR2tY5wK8pD1fG4hJ7sL0xC3vB6nM
    AoIBAB4hT7nQ1vR8mK5pD2xC9sL6wF3yH0tV7bN4qJ1mP8rD5cK2xZ9nL6hT3vW0
    yB7mL4pS1xC8vN5qR2tY9dF6hJ3kL0wQ7pD4mT1xV8cR5nK2sH9yB6vL3qP0dF7h
    tN4xC1vB8mL5qR2pY9dF6hJ3kL0wQ7pD4mT1xV8cR5nK2sQKBgQDY3nP6tR9vW2y
    K5mL8qD1fH4sJ7xC0vB3nM6pR9tY2wF5hK8dL1qS4vN7xC0bP3mT6yR9wK2nL5hF
    zJ6pQ3tV0xC7mB4nL1sR8yD5hK2qW9vF6pT3xN0cB7mL4qR1yD8hK5pQ==
    -----END RSA PRIVATE KEY-----
    """
)

PRIVATE_KEY_BLOCK_A_REWRAPPED = textwrap.dedent(
    """\
    -----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAtmJvYV7t6Vg4l0xJ5HfZK3aV6D5r5YQf5x4mG8c+K2h0mK8L2s9mDkLQ
    b2j7C1Kp8v8n2qgQOa0fB7x8Y6c7E6dOe8hQz3b7x1l9kCkWc7oZr0ePv8pQZlQm8oC0JjTj
    3cV0tYd9y3nQ8Zk5hQm2nV7t7gqQz7vG7k0Zy+9oQIDAQABAoIBAB9H0r2fJpO6m9l8qPp6
    q2G9u6x1m2q0u2R8v2e8Z1k4FQb0vKj7zq9dXxVwVh2h4fY5Z+0wG9lT3xU1nQd9pQbK2uG2
    cQv5b3bJt0WmQy7mJm0Y8Rr0nQ+vPj2AtYw9nV2uRz0qY0o8dPj8Pq7o1Z0aX9pQ3o0x5G8Q
    KBgQDhY0f+JrQm8oC0JjTj3cV0tYd9y3nQ8Zk5hQm2nV7t7gqQz7vG7k0Zy+9oQKBgQClpS1
    mYg7uQx3cJ8o9l0xJ5HfZK3aV6D5r5YQf5x4mG8c+K2h0mK8L2s9mDkLQ==
    -----END RSA PRIVATE KEY-----
    """
)

PUBLIC_CERT_CHAIN = textwrap.dedent(
    """\
    -----BEGIN CERTIFICATE-----
    MIIDdzCCAl+gAwIBAgIUXYPublicChainOnly000000000000000000MA0GCSqGSIb3
    DQEBCwUAMFoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMx
    FTATBgNVBAsMDEFycSBTYWZlIFBLSTEUMBIGA1UEAwwLZXhhbXBsZS5sb2NhbDAe
    Fw0yNjAzMzEwMDAwMDBaFw0zNjAzMjkwMDAwMDBaMFoxCzAJBgNVBAYTAlVTMRYw
    FAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMxFTATBgNVBAsMDEFycSBTYWZlIFBLSTEUMBIGA1UE
    AwwLZXhhbXBsZS5sb2NhbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
    ALD3u7xS3afe4Lacertchainonlyblock7rJb3Bv7H4qXyD9Xv6m3L7m0s2V7D5P8
    2C0tD8yM1mL0vN2fQ3sJ8hK6pR4wT7yN3fV5qB2dL9cT1vH6mP0xZ4nQ3sF8kM2pR
    7tV1yQ9dM6cJ2pN5wR8hV3mL6qT0yC9fK2sN5bR8xW1vQ4dP7kL0mN3sH6tY9pQ2
    0C0fA6pL9vQ5nT2rW8mK4dS1yF6qP3xV0bL7cN2hR5mJ8wK6tQ1xZ4nM7vP0sC3f
    K6mR9tV2yW5pL8nQ1dH4sJ7xC0vB3mN6pR9tY2wF5hK8dL1qS4vN7xC0bP3mT6yR
    9w0CAwEAAaNTMFEwHQYDVR0OBBYEFO9PublicChainOnly000000000000000000
    MB8GA1UdIwQYMBaAFO9PublicChainOnly000000000000000000MA8GA1UdEwEB
    /wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAG1chainonlysample4Lh8fQ2mV7
    dP0xN5rK8sT1yW4pL7mQ0dF3hJ6kL9vC2xZ5nM8qR1tY4wF7hK0dL3qS6vN9xC2bP
    4mT7yR0wQ3pD6fG9hJ2kL5nQ8tV1yC4mR7pL0xN3qS6vW9zC2bF5hJ8kL1nQ4tY7
    -----END CERTIFICATE-----
    """
)

CSR_SAMPLE = textwrap.dedent(
    """\
    -----BEGIN CERTIFICATE REQUEST-----
    MIICjDCCAXQCAQAwVzELMAkGA1UEBhMCVVMxFjAUBgNVBAoMDUFSUS1MQUIgU2Ft
    cGxlMRUwEwYDVQQLDAxBcnEgU2FmZSBQS0kxETAPBgNVBAMMCGNhLmxvY2FsMIIB
    IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxSafeCSRExample000000000
    0QmL7vS4pT1yR6mN9qW2fD5hJ8kL0nQ3tV6yC9mR2pL5xN8qS1vW4zB7cF0hJ3kL6
    pQ9tY2wF5hK8dL1qS4vN7xC0bP3mT6yR9wQ2dF5hJ8kL1nQ4tY7wC0vB3mN6pR9tY
    2wF5hK8dL1qS4vN7xC0bP3mT6yR9wQIDAQABoAAwDQYJKoZIhvcNAQELBQADggEB
    AD5safeCSRexample0000000000000000mR7tV0yQ3dF6hJ9kL2nQ5tY8wC1vB4mN
    7pR0tY3wF6hK9dL2qS5vN8xC1bP4mT7yR0wQ3pD6fG9hJ2kL5nQ8tV1yC4mR7pL0x
    -----END CERTIFICATE REQUEST-----
    """
)


def _to_dict(item: Any) -> dict[str, Any]:
    return {name: getattr(item, name) for name in getattr(item, "__slots__", [])}


def _scenario_clone(scenario: ScenarioSpec, repo_name: str) -> ScenarioSpec:
    return ScenarioSpec(
        id=scenario.id,
        milestone=scenario.milestone,
        repo_name=repo_name,
        module=scenario.module,
        family=scenario.family,
        stack=scenario.stack,
        domain=scenario.domain,
        summary=scenario.summary,
        line_target=scenario.line_target,
        scan_plans=scenario.scan_plans,
        build_plan=scenario.build_plan,
        expected_findings=scenario.expected_findings,
        expected_absent=scenario.expected_absent,
        explainability_expectations=scenario.explainability_expectations,
        metadata=scenario.metadata,
    )


def _package_name(repo_name: str) -> str:
    return "com.arq." + repo_name.replace("-", "").replace("_", "")


def _package_dir(repo_root: Path, package_name: str) -> Path:
    return repo_root / "src" / "main" / "java" / Path(*package_name.split("."))


def _test_package_dir(repo_root: Path, package_name: str) -> Path:
    return repo_root / "src" / "test" / "java" / Path(*package_name.split("."))


def _min_lines(line_target: str) -> int:
    first = line_target.split("-", 1)[0]
    return int(first)


def _inflate_repository(repo_root: Path, scenario: ScenarioSpec) -> None:
    target = _min_lines(scenario.line_target)
    current = count_lines(repo_root)
    if current >= target:
        return
    docs_root = ensure_dir(repo_root / "docs" / "architecture")
    ops_root = ensure_dir(repo_root / "ops" / "playbooks")
    sql_root = ensure_dir(repo_root / "sql" / "reference")
    index = 1
    while current < target:
        write_text(
            docs_root / f"section-{index:02d}.md",
            "\n".join(
                [
                    f"# {scenario.repo_name} architecture section {index}",
                    "",
                    *[
                        f"- {scenario.domain} control note {index}.{line}: service boundaries, failover, tenancy isolation, deployment sequencing, and audit evidence retention."
                        for line in range(1, 41)
                    ],
                    "",
                ]
            ),
        )
        write_text(
            ops_root / f"runbook-{index:02d}.md",
            "\n".join(
                [
                    f"# {scenario.repo_name} operational runbook {index}",
                    "",
                    *[
                        f"{line}. Review deployment health gates, workflow approvals, retry budgets, throughput saturation alarms, and partner communication paths for iteration {index}."
                        for line in range(1, 41)
                    ],
                    "",
                ]
            ),
        )
        write_text(
            sql_root / f"reference-{index:02d}.sql",
            "\n".join(
                [
                    "-- Synthetic reference DDL used to pad realistic repository shape.",
                    *[
                        f"create table if not exists ref_{index}_{line:02d} (id varchar(36) primary key, detail varchar(255) not null, state varchar(32) not null);"
                        for line in range(1, 26)
                    ],
                    "",
                ]
            ),
        )
        current = count_lines(repo_root)
        index += 1


def _write_validation_files(repo_root: Path, scenario: ScenarioSpec, repo_metadata: dict[str, Any]) -> None:
    validation_root = ensure_dir(repo_root / "validation")
    write_yaml_like(
        validation_root / "scenario.yaml",
        [
            f"id: {scenario.id}",
            f"milestone: {scenario.milestone}",
            f"repo: {scenario.repo_name}",
            f"module: {scenario.module}",
            f"stack: {scenario.stack}",
            f"domain: {scenario.domain}",
            f"lineTarget: {scenario.line_target}",
        ],
    )
    write_json(validation_root / "expected-findings.json", [_to_dict(item) for item in scenario.expected_findings])
    write_json(validation_root / "expected-absent.json", [_to_dict(item) for item in scenario.expected_absent])
    write_yaml_like(
        validation_root / "smoke.yaml",
        ["commands:", *[f"  - {' '.join(command)}" for command in scenario.build_plan.smoke]],
    )
    branch_plan_lines = ["branches:"]
    for branch, sha in repo_metadata.get("git", {}).get("branches", {}).items():
        branch_plan_lines.append(f"  - name: {branch}")
        branch_plan_lines.append(f"    sha: {sha}")
    write_yaml_like(validation_root / "branch-plan.yaml", branch_plan_lines)
    write_text(
        validation_root / "expected-report.md",
        textwrap.dedent(
            f"""\
            # {scenario.id}

            Expected validation focus for `{scenario.repo_name}`:

            - Module: `{scenario.module}`
            - Summary: {scenario.summary}
            - Expected positives: {len(scenario.expected_findings)}
            - Expected clean surfaces: {len(scenario.expected_absent)}
            """
        ),
    )
    if scenario.explainability_expectations:
        write_json(validation_root / "explainability-contract.json", [_to_dict(item) for item in scenario.explainability_expectations])


def _write_common_root_files(repo_root: Path, scenario: ScenarioSpec) -> None:
    write_text(
        repo_root / "README.md",
        textwrap.dedent(
            f"""\
            # {scenario.repo_name}

            {scenario.domain}

            This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.

            ## Local development

            - Review `scripts/` for smoke and validation commands.
            - Review `validation/` for machine-readable expectations.
            - Review `docs/` for architecture and operational material.
            """
        ),
    )
    write_text(repo_root / ".gitignore", "target/\ndist/\nnode_modules/\n__pycache__/\ncoverage/\n.venv/\nbin/\nobj/\n")


def _java_request_class(package_name: str, module_name: str) -> str:
    title = module_name.title()
    return textwrap.dedent(
        f"""\
        package {package_name}.dto;

        public class {title}Request {{
            private String id;
            private String partnerCode;
            private String region;

            public {title}Request() {{
            }}

            public {title}Request(String id, String partnerCode, String region) {{
                this.id = id;
                this.partnerCode = partnerCode;
                this.region = region;
            }}

            public String getId() {{
                return id;
            }}

            public String getPartnerCode() {{
                return partnerCode;
            }}

            public String getRegion() {{
                return region;
            }}
        }}
        """
    )


def _java_response_class(package_name: str, module_name: str) -> str:
    title = module_name.title()
    return textwrap.dedent(
        f"""\
        package {package_name}.dto;

        public class {title}Response {{
            private final String id;
            private final String status;
            private final String owner;

            public {title}Response(String id, String status, String owner) {{
                this.id = id;
                this.status = status;
                this.owner = owner;
            }}

            public String getId() {{
                return id;
            }}

            public String getStatus() {{
                return status;
            }}

            public String getOwner() {{
                return owner;
            }}
        }}
        """
    )


def _java_record_class(package_name: str, module_name: str) -> str:
    title = module_name.title()
    return textwrap.dedent(
        f"""\
        package {package_name}.domain;

        import java.time.Instant;

        public class {title}Record {{
            private final String id;
            private final String owner;
            private final String region;
            private final Instant updatedAt;

            public {title}Record(String id, String owner, String region, Instant updatedAt) {{
                this.id = id;
                this.owner = owner;
                this.region = region;
                this.updatedAt = updatedAt;
            }}

            public String getId() {{
                return id;
            }}

            public String getOwner() {{
                return owner;
            }}

            public String getRegion() {{
                return region;
            }}

            public Instant getUpdatedAt() {{
                return updatedAt;
            }}
        }}
        """
    )


def _populate_java_common(repo_root: Path, scenario: ScenarioSpec) -> dict[str, Any]:
    package_name = _package_name(scenario.repo_name)
    package_root = ensure_dir(_package_dir(repo_root, package_name))
    test_root = ensure_dir(_test_package_dir(repo_root, package_name))
    _write_common_root_files(repo_root, scenario)
    app_name = scenario.repo_name.replace("-", "").title()
    write_text(
        repo_root / "pom.xml",
        textwrap.dedent(
            f"""\
            <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                     xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
              <modelVersion>4.0.0</modelVersion>
              <parent>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-parent</artifactId>
                <version>3.3.5</version>
                <relativePath/>
              </parent>
              <groupId>com.arq.lab</groupId>
              <artifactId>{scenario.repo_name}</artifactId>
              <version>1.0.0</version>
              <properties><java.version>21</java.version></properties>
              <dependencies>
                <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-web</artifactId></dependency>
                <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-validation</artifactId></dependency>
                <dependency><groupId>org.springframework.boot</groupId><artifactId>spring-boot-starter-test</artifactId><scope>test</scope></dependency>
              </dependencies>
            </project>
            """
        ),
    )
    write_text(repo_root / "mvnw", "#!/usr/bin/env sh\nmvn \"$@\"\n")
    write_text(repo_root / "mvnw.cmd", "@echo off\r\nmvn %*\r\n")
    write_text(repo_root / "scripts" / "smoke.ps1", "Write-Host 'java smoke ok'\n")
    write_text(
        package_root / f"{app_name}Application.java",
        textwrap.dedent(
            f"""\
            package {package_name};

            import org.springframework.boot.SpringApplication;
            import org.springframework.boot.autoconfigure.SpringBootApplication;

            @SpringBootApplication
            public class {app_name}Application {{
                public static void main(String[] args) {{
                    SpringApplication.run({app_name}Application.class, args);
                }}
            }}
            """
        ),
    )
    for module_name in JAVA_MODULES:
        title = module_name.title()
        write_text(package_root / "dto" / f"{title}Request.java", _java_request_class(package_name, module_name))
        write_text(package_root / "dto" / f"{title}Response.java", _java_response_class(package_name, module_name))
        write_text(package_root / "domain" / f"{title}Record.java", _java_record_class(package_name, module_name))
        write_text(
            package_root / "repository" / f"{title}Repository.java",
            textwrap.dedent(
                f"""\
                package {package_name}.repository;

                import {package_name}.domain.{title}Record;
                import java.time.Instant;
                import java.util.Collection;
                import java.util.Map;
                import java.util.concurrent.ConcurrentHashMap;
                import org.springframework.stereotype.Repository;

                @Repository
                public class {title}Repository {{
                    private final Map<String, {title}Record> storage = new ConcurrentHashMap<>();

                    public {title}Repository() {{
                        storage.put("{module_name}-seed", new {title}Record("{module_name}-seed", "{module_name}-owner", "eu-central", Instant.now()));
                    }}

                    public Collection<{title}Record> findAll() {{
                        return storage.values();
                    }}
                }}
                """
            ),
        )
        write_text(
            package_root / "service" / f"{title}Service.java",
            textwrap.dedent(
                f"""\
                package {package_name}.service;

                import {package_name}.dto.{title}Response;
                import {package_name}.repository.{title}Repository;
                import java.util.List;
                import org.springframework.stereotype.Service;

                @Service
                public class {title}Service {{
                    private final {title}Repository repository;

                    public {title}Service({title}Repository repository) {{
                        this.repository = repository;
                    }}

                    public List<{title}Response> summarize() {{
                        return repository.findAll().stream().map(record -> new {title}Response(record.getId(), "ACTIVE", record.getOwner())).toList();
                    }}
                }}
                """
            ),
        )
        write_text(
            package_root / "web" / f"{title}Controller.java",
            textwrap.dedent(
                f"""\
                package {package_name}.web;

                import {package_name}.dto.{title}Response;
                import {package_name}.service.{title}Service;
                import java.util.List;
                import org.springframework.web.bind.annotation.GetMapping;
                import org.springframework.web.bind.annotation.RequestMapping;
                import org.springframework.web.bind.annotation.RestController;

                @RestController
                @RequestMapping("/api/{module_name}")
                public class {title}Controller {{
                    private final {title}Service service;

                    public {title}Controller({title}Service service) {{
                        this.service = service;
                    }}

                    @GetMapping
                    public List<{title}Response> list() {{
                        return service.summarize();
                    }}
                }}
                """
            ),
        )
        write_text(
            test_root / "service" / f"{title}ServiceTest.java",
            textwrap.dedent(
                f"""\
                package {package_name}.service;

                import {package_name}.repository.{title}Repository;
                import org.junit.jupiter.api.Test;
                import static org.junit.jupiter.api.Assertions.assertFalse;

                class {title}ServiceTest {{
                    @Test
                    void returnsSeedData() {{
                        {title}Service service = new {title}Service(new {title}Repository());
                        assertFalse(service.summarize().isEmpty());
                    }}
                }}
                """
            ),
        )
    write_text(repo_root / "src" / "main" / "resources" / "application.yml", "spring:\n  application:\n    name: arq-lab-service\n")
    return {"packageName": package_name}


def _populate_python_common(repo_root: Path, scenario: ScenarioSpec) -> None:
    _write_common_root_files(repo_root, scenario)
    write_text(repo_root / "pyproject.toml", "[project]\nname='arq-lab-python'\nversion='1.0.0'\nrequires-python='>=3.11'\n\n[tool.pytest.ini_options]\naddopts='-q'\n")
    write_text(repo_root / "scripts" / "smoke.py", "print('python smoke ok')\n")
    write_text(repo_root / "app" / "__init__.py", "")
    write_text(repo_root / "app" / "main.py", "from fastapi import FastAPI\napp = FastAPI()\n@app.get('/health')\ndef health() -> dict[str, str]:\n    return {'status': 'ok'}\n")
    for module_name in PY_MODULES:
        write_text(repo_root / "app" / "models" / f"{module_name}.py", f"from dataclasses import dataclass\n@dataclass(slots=True)\nclass {module_name.title()}Model:\n    identifier: str\n    owner: str\n    state: str\n")
        write_text(repo_root / "app" / "services" / f"{module_name}_service.py", f"from app.models.{module_name} import {module_name.title()}Model\n\ndef load_{module_name}_records() -> list[{module_name.title()}Model]:\n    return [{module_name.title()}Model(identifier='{module_name}-seed', owner='{module_name}-owner', state='ACTIVE')]\n")
        write_text(repo_root / "tests" / f"test_{module_name}_service.py", f"from app.services.{module_name}_service import load_{module_name}_records\n\ndef test_{module_name}_records_present() -> None:\n    assert load_{module_name}_records()\n")


def _populate_node_common(repo_root: Path, scenario: ScenarioSpec) -> None:
    _write_common_root_files(repo_root, scenario)
    write_text(
        repo_root / "package.json",
        textwrap.dedent(
            f"""\
            {{
              "name": "{scenario.repo_name}",
              "version": "1.0.0",
              "private": true,
              "scripts": {{"build": "tsc -p tsconfig.json", "test": "jest"}},
              "dependencies": {{"express": "^4.21.2"}},
              "devDependencies": {{"@types/express": "^5.0.0", "@types/jest": "^29.5.14", "@types/node": "^22.13.5", "jest": "^29.7.0", "ts-jest": "^29.2.5", "typescript": "^5.8.2"}}
            }}
            """
        ),
    )
    write_text(repo_root / "tsconfig.json", '{\n  "compilerOptions": {"target": "ES2022", "module": "commonjs", "rootDir": ".", "outDir": "dist", "esModuleInterop": true, "strict": true},\n  "include": ["src/**/*.ts", "scripts/**/*.ts", "__tests__/**/*.ts"]\n}\n')
    write_text(repo_root / "jest.config.cjs", "module.exports = { preset: 'ts-jest', testEnvironment: 'node' };\n")
    write_text(repo_root / "scripts" / "smoke.ts", "console.log('node smoke ok');\n")
    write_text(repo_root / "src" / "server.ts", "import express from 'express';\nconst app = express();\napp.get('/health', (_req, res) => res.json({status: 'ok'}));\nexport default app;\n")
    for module_name in NODE_MODULES:
        title = module_name.title()
        write_text(repo_root / "src" / "modules" / module_name / f"{module_name}.service.ts", f"export type {title}Record = {{ id: string; owner: string; state: string }};\nexport function load{title}Records(): {title}Record[] {{ return [{{ id: '{module_name}-seed', owner: '{module_name}-owner', state: 'ACTIVE' }}]; }}\n")
        write_text(repo_root / "__tests__" / f"{module_name}.service.test.ts", f"import {{ load{title}Records }} from '../src/modules/{module_name}/{module_name}.service';\ntest('loads {module_name} records', () => {{ expect(load{title}Records().length).toBeGreaterThan(0); }});\n")


def _populate_config_common(repo_root: Path, scenario: ScenarioSpec) -> None:
    _write_common_root_files(repo_root, scenario)
    write_text(repo_root / "scripts" / "validate_repo.py", "print('config repo validated')\n")
    write_text(repo_root / "scripts" / "smoke.ps1", "Write-Host 'config smoke ok'\n")
    write_text(repo_root / "tests" / "test_validation.py", "def test_validation_placeholder() -> None:\n    assert True\n")
    write_text(repo_root / "config" / "runtime" / "baseline.yaml", "service:\n  enabled: true\n  retries: 3\n")
    write_text(repo_root / "deploy" / "prod" / "service.properties", "service.mode=prod\n")


def _populate_go_common(repo_root: Path, scenario: ScenarioSpec) -> None:
    _write_common_root_files(repo_root, scenario)
    write_text(repo_root / "go.mod", "module arq.lab/go\n\ngo 1.22\n")
    write_text(repo_root / "cmd" / "service" / "main.go", 'package main\nimport "fmt"\nfunc main(){fmt.Println("go smoke ok")}\n')
    for module_name in GO_MODULES:
        write_text(repo_root / "internal" / module_name / f"{module_name}.go", f"package {module_name}\n\ntype Record struct {{ ID string; Owner string; State string }}\n\nfunc Load() []Record {{ return []Record{{{{ID: \"{module_name}-seed\", Owner: \"{module_name}-owner\", State: \"ACTIVE\"}}}} }}\n")
        write_text(repo_root / "internal" / module_name / f"{module_name}_test.go", f"package {module_name}\nimport \"testing\"\nfunc TestBuildSmoke(t *testing.T) {{ if len(Load()) == 0 {{ t.Fatal(\"expected seed\") }} }}\n")


def _populate_csharp_common(repo_root: Path, scenario: ScenarioSpec) -> None:
    _write_common_root_files(repo_root, scenario)
    write_text(repo_root / "src" / "AppHost" / "AppHost.csproj", '<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><OutputType>Exe</OutputType><TargetFramework>net8.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable></PropertyGroup><ItemGroup><ProjectReference Include="..\\Library\\Library.csproj" /></ItemGroup></Project>\n')
    write_text(repo_root / "src" / "Library" / "Library.csproj", '<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><TargetFramework>net8.0</TargetFramework><ImplicitUsings>enable</ImplicitUsings><Nullable>enable</Nullable></PropertyGroup></Project>\n')
    write_text(repo_root / "tests" / "AppHost.Tests" / "AppHost.Tests.csproj", '<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><TargetFramework>net8.0</TargetFramework><IsPackable>false</IsPackable></PropertyGroup><ItemGroup><PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.11.1" /><PackageReference Include="xunit" Version="2.9.2" /><PackageReference Include="xunit.runner.visualstudio" Version="2.8.2" /></ItemGroup><ItemGroup><ProjectReference Include="..\\..\\src\\Library\\Library.csproj" /></ItemGroup></Project>\n')
    write_text(repo_root / "src" / "AppHost" / "Program.cs", 'using System; if (args.Length > 0 && args[0] == "--smoke") { Console.WriteLine("csharp smoke ok"); return; } Console.WriteLine("app host");\n')
    for module_name in CSHARP_MODULES:
        write_text(repo_root / "src" / "Library" / module_name / f"{module_name}Registry.cs", f"namespace Arq.Lab.Library.{module_name}; public static class {module_name}Registry {{ public static string[] Load() => new[] {{ \"{module_name}-seed\" }}; }}\n")
    write_text(repo_root / "tests" / "AppHost.Tests" / "RegistryTests.cs", "using Arq.Lab.Library.Partners; using Xunit; public class RegistryTests { [Fact] public void LoadsSeed() { Assert.NotEmpty(PartnersRegistry.Load()); } }\n")


def _apply_java_variant(repo_root: Path, scenario: ScenarioSpec, package_name: str) -> None:
    package_root = ensure_dir(_package_dir(repo_root, package_name))
    if scenario.family == "guardian_live_java":
        write_text(repo_root / "src" / "main" / "resources" / "application-prod.yml", "oauth:\n  client-secret: LiveSecretX9aK4mP1cQ7zR2vW\n")
        write_text(repo_root / "src" / "main" / "resources" / "keys" / "partner_rsa.pem", PRIVATE_KEY_BLOCK_A)
        write_text(package_root / "bootstrap" / "PartnerCredentialBootstrap.java", f"package {package_name}.bootstrap;\npublic class PartnerCredentialBootstrap {{ private static final String PARTNER_ACCESS_KEY = \"{GENERIC_SECRET_GOLF}\"; public String key() {{ return PARTNER_ACCESS_KEY; }} }}\n")
        write_text(repo_root / "src" / "main" / "resources" / "db" / "seed" / "live-connector.properties", f"connector.token={GENERIC_SECRET_BRAVO}\n")
        write_text(repo_root / "docs" / "operational-runbook.md", "masked_token=****-masked-token\n")
        write_text(repo_root / "src" / "test" / "resources" / "example.env", "TOKEN=example-token\n")
        write_text(repo_root / "docs" / "examples" / "pem-example.txt", "-----BEGIN PRIVATE KEY-----\nexample\n")
    elif scenario.id == "Q-V3-JAVA-001":
        write_text(package_root / "security" / "SecureDigestService.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class SecureDigestService {{ public byte[] digest(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"SHA-256\").digest(value); }} }}\n")
        write_text(package_root / "security" / "LegacyDigestService.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class LegacyDigestService {{ public byte[] md5(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"MD5\").digest(value); }} public byte[] sha1(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"SHA-1\").digest(value); }} }}\n")
        write_text(package_root / "security" / "TokenCipherService.java", f"package {package_name}.security;\nimport javax.crypto.Cipher;\npublic class TokenCipherService {{ public Cipher cipher() throws Exception {{ return Cipher.getInstance(\"AES/ECB/PKCS5Padding\"); }} }}\n")
        write_text(package_root / "security" / "ResetTokenService.java", f"package {package_name}.security;\nimport java.util.Random;\npublic class ResetTokenService {{ public int issueCode() {{ return new Random().nextInt(100000); }} }}\n")
        write_text(package_root / "security" / "PasswordKeyFactory.java", f"package {package_name}.security;\nimport javax.crypto.SecretKeyFactory;\npublic class PasswordKeyFactory {{ public SecretKeyFactory factory() throws Exception {{ return SecretKeyFactory.getInstance(\"PBEWithMD5AndDES\"); }} }}\n")
    elif scenario.id == "Q-V3-JAVA-002":
        write_text(package_root / "security" / "LegacyEnvelopeCipher.java", f"package {package_name}.security;\nimport javax.crypto.Cipher;\npublic class LegacyEnvelopeCipher {{ public Cipher cipher() throws Exception {{ return Cipher.getInstance(\"DESede/ECB/PKCS5Padding\"); }} }}\n")
        write_text(package_root / "security" / "LegacyPasswordFactory.java", f"package {package_name}.security;\nimport javax.crypto.SecretKeyFactory;\npublic class LegacyPasswordFactory {{ public SecretKeyFactory factory() throws Exception {{ return SecretKeyFactory.getInstance(\"PBEWithMD5AndDES\"); }} }}\n")
        write_text(package_root / "security" / "BatchReconciliationCipher.java", f"package {package_name}.security;\nimport javax.crypto.Cipher;\npublic class BatchReconciliationCipher {{ public Cipher cipher() throws Exception {{ return Cipher.getInstance(\"AES/ECB\"); }} }}\n")
        write_text(package_root / "security" / "SecureEnvelopeCipher.java", f"package {package_name}.security;\nimport javax.crypto.Cipher;\npublic class SecureEnvelopeCipher {{ public Cipher cipher() throws Exception {{ return Cipher.getInstance(\"AES/GCM/NoPadding\"); }} }}\n")
    elif scenario.id == "Q-V3-JAVA-004":
        write_text(package_root / "security" / "LegacyRequestSigner.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class LegacyRequestSigner {{ public byte[] sign(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"MD5\").digest(value); }} }}\n")
        write_text(package_root / "security" / "DigestInventoryRegistry.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class DigestInventoryRegistry {{ public String supported() throws Exception {{ return MessageDigest.getInstance(\"SHA-256\").getAlgorithm(); }} }}\n")
        write_text(package_root / "security" / "ScaryButSafeDigestFacade.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class ScaryButSafeDigestFacade {{ public byte[] secure(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"SHA-256\").digest(value); }} }}\n")
    elif scenario.id == "Q-V3-JAVA-005":
        write_text(package_root / "security" / "LegacyDigestService.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class LegacyDigestService {{ public byte[] digest(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"MD5\").digest(value); }} }}\n")
        write_text(package_root / "security" / "DigestInventoryOnly.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class DigestInventoryOnly {{ public String supported() throws Exception {{ return MessageDigest.getInstance(\"SHA-256\").getAlgorithm(); }} }}\n")
        write_text(package_root / "security" / "SecureDigestFacade.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class SecureDigestFacade {{ public byte[] digest(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"SHA-256\").digest(value); }} }}\n")
        write_text(repo_root / "docs" / "crypto-inventory.md", "MessageDigest inventory notes reference SHA-256 only and keep examples masked.\n")
    elif scenario.id == "Q-V3-JAVA-006":
        write_text(package_root / "security" / "LegacyEnvelopeCipher.java", f"package {package_name}.security;\nimport javax.crypto.Cipher;\npublic class LegacyEnvelopeCipher {{ public Cipher cipher() throws Exception {{ return Cipher.getInstance(\"AES/ECB/PKCS5Padding\"); }} }}\n")
        write_text(package_root / "security" / "SecureButScaryHasher.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class SecureButScaryHasher {{ public byte[] digest(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"SHA-256\").digest(value); }} }}\n")
        write_text(package_root / "security" / "SecureBuilderAdapter.java", f"package {package_name}.security;\npublic class SecureBuilderAdapter {{ public boolean enabled() {{ return true; }} }}\n")
        write_text(repo_root / "docs" / "crypto-facade.md", "Secure wrapper inventory only; no live weak crypto in docs.\n")
    elif scenario.id == "Q-V3-JAVA-007":
        write_text(
            package_root / "security" / "LegacyDigestFactory.java",
            textwrap.dedent(
                f"""\
                package {package_name}.security;

                import java.security.MessageDigest;

                public class LegacyDigestFactory {{
                    public MessageDigest build() throws Exception {{
                        return DigestFactoryAlias.legacy();
                    }}
                }}

                final class DigestFactoryAlias {{
                    static MessageDigest legacy() throws Exception {{
                        return MessageDigest.getInstance("MD5");
                    }}
                }}
                """
            ),
        )
        write_text(package_root / "security" / "SecureDigestFactory.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class SecureDigestFactory {{ public MessageDigest build() throws Exception {{ return MessageDigest.getInstance(\"SHA-256\"); }} }}\n")
        write_text(repo_root / "docs" / "helper-digest.md", "Helper factories remain safe unless they return a live weak digest.\n")
    elif scenario.id == "Q-V3-JAVA-008":
        write_text(package_root / "security" / "LegacySidePathHasher.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class LegacySidePathHasher {{ public byte[] digest(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"SHA-1\").digest(value); }} }}\n")
        write_text(package_root / "security" / "TrustAllStyleButSafeHasher.java", f"package {package_name}.security;\nimport java.security.MessageDigest;\npublic class TrustAllStyleButSafeHasher {{ public byte[] digest(byte[] value) throws Exception {{ return MessageDigest.getInstance(\"SHA-256\").digest(value); }} }}\n")
        write_text(package_root / "security" / "SecureDigestDelegate.java", f"package {package_name}.security;\npublic class SecureDigestDelegate {{ public boolean enabled() {{ return true; }} }}\n")
    elif scenario.id == "Q-V5-JAVA-001":
        write_text(package_root / "http" / "InsecureTrustManager.java", f"package {package_name}.http;\nimport java.security.cert.X509Certificate; import javax.net.ssl.X509TrustManager; public class InsecureTrustManager implements X509TrustManager {{ public void checkClientTrusted(X509Certificate[] c, String a) {{ }} public void checkServerTrusted(X509Certificate[] c, String a) {{ }} public X509Certificate[] getAcceptedIssuers() {{ return new X509Certificate[0]; }} }}\n")
        write_text(package_root / "http" / "InsecureHostnameVerifier.java", f"package {package_name}.http;\nimport javax.net.ssl.HostnameVerifier; import javax.net.ssl.SSLSession; public class InsecureHostnameVerifier implements HostnameVerifier {{ public boolean verify(String host, SSLSession session) {{ return true; }} }}\n")
        write_text(package_root / "http" / "SecurePartnerClientFactory.java", f"package {package_name}.http;\npublic class SecurePartnerClientFactory {{ public boolean enabled() {{ return true; }} }}\n")
    elif scenario.id == "Q-V5-JAVA-004":
        write_text(
            package_root / "http" / "PartnerTlsBuilder.java",
            textwrap.dedent(
                f"""\n                package {package_name}.http;\n\n                import javax.net.ssl.HostnameVerifier;\n                import javax.net.ssl.SSLSession;\n\n                public class PartnerTlsBuilder {{\n                    public HostnameVerifier buildHostnameVerifier() {{\n                        return new HostnameVerifier() {{\n                            @Override\n                            public boolean verify(String hostname, SSLSession session) {{\n                                return true;\n                            }}\n                        }};\n                    }}\n                }}\n                """
            ),
        )
        write_text(
            package_root / "http" / "BuilderTrustManager.java",
            textwrap.dedent(
                f"""\n                package {package_name}.http;\n\n                import java.security.cert.X509Certificate;\n                import javax.net.ssl.X509TrustManager;\n\n                public class BuilderTrustManager implements X509TrustManager {{\n                    @Override\n                    public void checkClientTrusted(X509Certificate[] chain, String authType) {{\n                    }}\n\n                    @Override\n                    public void checkServerTrusted(X509Certificate[] chain, String authType) {{\n                    }}\n\n                    @Override\n                    public X509Certificate[] getAcceptedIssuers() {{\n                        return new X509Certificate[0];\n                    }}\n                }}\n                """
            ),
        )
        write_text(package_root / "http" / "SafePartnerTlsBuilder.java", f"package {package_name}.http;\nimport javax.net.ssl.HostnameVerifier; import javax.net.ssl.SSLSession; public class SafePartnerTlsBuilder {{ public HostnameVerifier build() {{ return new HostnameVerifier() {{ @Override public boolean verify(String hostname, SSLSession session) {{ return hostname != null && !hostname.isBlank(); }} }}; }} }}\n")
    elif scenario.id == "Q-V5-JAVA-005":
        write_text(
            package_root / "http" / "PartnerHttpBuilder.java",
            textwrap.dedent(
                f"""\n                package {package_name}.http;\n\n                import javax.net.ssl.HostnameVerifier;\n                import javax.net.ssl.SSLSession;\n\n                public class PartnerHttpBuilder {{\n                    public HostnameVerifier verifier() {{\n                        return HostnameVerifierAlias.insecure();\n                    }}\n                }}\n\n                final class HostnameVerifierAlias {{\n                    static HostnameVerifier insecure() {{\n                        return new HostnameVerifier() {{\n                            @Override\n                            public boolean verify(String hostname, SSLSession session) {{\n                                return true;\n                            }}\n                        }};\n                    }}\n                }}\n                """
            ),
        )
        write_text(
            package_root / "http" / "TrustManagerAlias.java",
            textwrap.dedent(
                f"""\n                package {package_name}.http;\n\n                import java.security.cert.X509Certificate;\n                import javax.net.ssl.X509TrustManager;\n\n                public class TrustManagerAlias implements X509TrustManager {{\n                    @Override\n                    public void checkClientTrusted(X509Certificate[] chain, String authType) {{\n                    }}\n\n                    @Override\n                    public void checkServerTrusted(X509Certificate[] chain, String authType) {{\n                    }}\n\n                    @Override\n                    public X509Certificate[] getAcceptedIssuers() {{\n                        return new X509Certificate[0];\n                    }}\n                }}\n                """
            ),
        )
        write_text(package_root / "http" / "SecurePartnerBuilder.java", f"package {package_name}.http;\nimport javax.net.ssl.HostnameVerifier; import javax.net.ssl.SSLSession; public class SecurePartnerBuilder {{ public HostnameVerifier verifier() {{ return new HostnameVerifier() {{ @Override public boolean verify(String hostname, SSLSession session) {{ return hostname != null && !hostname.isBlank(); }} }}; }} }}\n")
        write_text(repo_root / "docs" / "tls-helper-chain.md", "TLS helper notes stay descriptive and non-executable.\n")
    elif scenario.id == "Q-V5-JAVA-006":
        write_text(
            package_root / "http" / "LiveInsecureTlsClient.java",
            textwrap.dedent(
                f"""\n                package {package_name}.http;\n\n                import javax.net.ssl.HostnameVerifier;\n                import javax.net.ssl.SSLSession;\n\n                public class LiveInsecureTlsClient {{\n                    public HostnameVerifier verifier() {{\n                        return new HostnameVerifier() {{\n                            @Override\n                            public boolean verify(String hostname, SSLSession session) {{\n                                return true;\n                            }}\n                        }};\n                    }}\n                }}\n                """
            ),
        )
        write_text(package_root / "http" / "ScaryButSafeTlsFacade.java", f"package {package_name}.http;\nimport javax.net.ssl.HostnameVerifier; import javax.net.ssl.SSLSession; public class ScaryButSafeTlsFacade {{ public HostnameVerifier verifier() {{ return new HostnameVerifier() {{ @Override public boolean verify(String hostname, SSLSession session) {{ return hostname != null && hostname.endsWith(\".corp\"); }} }}; }} }}\n")
        write_text(package_root / "http" / "SecureTlsDefaults.java", f"package {package_name}.http;\npublic class SecureTlsDefaults {{ public boolean enabled() {{ return true; }} }}\n")
        write_text(repo_root / "docs" / "safe-wrapper.md", "Scary naming alone should not create a live TLS finding.\n")
    elif scenario.id == "Q-V5-JAVA-007":
        write_text(
            package_root / "http" / "NestedHostnameBuilder.java",
            textwrap.dedent(
                f"""\
                package {package_name}.http;

                import javax.net.ssl.HostnameVerifier;
                import javax.net.ssl.SSLSession;

                public class NestedHostnameBuilder {{
                    public HostnameVerifier build() {{
                        return NestedTlsHelpers.hostnameVerifier();
                    }}
                }}

                final class NestedTlsHelpers {{
                    static HostnameVerifier hostnameVerifier() {{
                        return new HostnameVerifier() {{
                            @Override
                            public boolean verify(String hostname, SSLSession session) {{
                                return true;
                            }}
                        }};
                    }}
                }}
                """
            ),
        )
        write_text(
            package_root / "http" / "NestedTrustManagerBuilder.java",
            textwrap.dedent(
                f"""\
                package {package_name}.http;

                import java.security.cert.X509Certificate;
                import javax.net.ssl.X509TrustManager;

                public class NestedTrustManagerBuilder {{
                    public X509TrustManager build() {{
                        return NestedTrustManagerFactory.insecure();
                    }}
                }}

                final class NestedTrustManagerFactory {{
                    static X509TrustManager insecure() {{
                        return new X509TrustManager() {{
                            @Override
                            public void checkClientTrusted(X509Certificate[] chain, String authType) {{
                            }}

                            @Override
                            public void checkServerTrusted(X509Certificate[] chain, String authType) {{
                            }}

                            @Override
                            public X509Certificate[] getAcceptedIssuers() {{
                                return new X509Certificate[0];
                            }}
                        }};
                    }}
                }}
                """
            ),
        )
        write_text(package_root / "http" / "SecureTlsFactory.java", f"package {package_name}.http;\npublic class SecureTlsFactory {{ public boolean enabled() {{ return true; }} }}\n")
    elif scenario.id == "Q-V5-JAVA-008":
        write_text(package_root / "http" / "TrustAllStyleSafeClient.java", f"package {package_name}.http;\nimport javax.net.ssl.HostnameVerifier; import javax.net.ssl.SSLSession; public class TrustAllStyleSafeClient {{ public HostnameVerifier verifier() {{ return new HostnameVerifier() {{ @Override public boolean verify(String hostname, SSLSession session) {{ return hostname != null && hostname.endsWith(\".corp\"); }} }}; }} }}\n")
        write_text(package_root / "http" / "TrustAllStyleHostnameFacade.java", f"package {package_name}.http;\npublic class TrustAllStyleHostnameFacade {{ public boolean strict() {{ return true; }} }}\n")
        write_text(repo_root / "docs" / "safe-trustall.md", "TrustAll-style naming remains descriptive; runtime behavior stays strict.\n")
    elif scenario.id == "Q-V5-JAVA-003":
        write_text(
            package_root / "config" / "PartnerTlsProperties.java",
            textwrap.dedent(
                f"""\
                package {package_name}.config;

                import javax.net.ssl.HostnameVerifier;
                import javax.net.ssl.SSLSession;

                public class PartnerTlsProperties {{
                    public HostnameVerifier hostnameVerifier() {{
                        return new HostnameVerifier() {{
                            @Override
                            public boolean verify(String hostname, SSLSession session) {{
                                return true;
                            }}
                        }};
                    }}
                }}
                """
            ),
        )
        write_text(
            package_root / "config" / "PartnerTrustManager.java",
            textwrap.dedent(
                f"""\
                package {package_name}.config;

                import java.security.cert.X509Certificate;
                import javax.net.ssl.X509TrustManager;

                public class PartnerTrustManager implements X509TrustManager {{
                    @Override
                    public void checkClientTrusted(X509Certificate[] chain, String authType) {{
                    }}

                    @Override
                    public void checkServerTrusted(X509Certificate[] chain, String authType) {{
                    }}

                    @Override
                    public X509Certificate[] getAcceptedIssuers() {{
                        return new X509Certificate[0];
                    }}
                }}
                """
            ),
        )
        write_text(repo_root / "src" / "main" / "resources" / "application-prod.yml", "partner:\n  tls:\n    profile: prod\n")
        write_text(repo_root / "src" / "main" / "resources" / "application-dev.yml", "partner:\n  tls:\n    verify: true\n")


def _apply_python_variant(repo_root: Path, scenario: ScenarioSpec) -> None:
    if scenario.family == "guardian_live_python":
        write_text(repo_root / "app" / "config" / "runtime_settings.py", f'PROVIDER_TOKEN = "{GENERIC_SECRET_ALPHA}"\n')
        write_text(repo_root / "deploy" / "k8s" / "notification-prod.env", f"NOTIFICATION_SECRET={GENERIC_SECRET_BRAVO}\n")
        write_text(repo_root / "app" / "clients" / "webhook_client.py", f'WEBHOOK_TOKEN = "{GENERIC_SECRET_CHARLIE}"\n')
        write_text(repo_root / "app" / "security" / "jwt_bootstrap.py", f'JWT_SECRET = "{GENERIC_SECRET_GOLF}"\n')
        write_text(repo_root / ".env.example", "JWT_SECRET=example-value\n")
    elif scenario.id == "Q-V4-PY-001":
        write_text(repo_root / "app" / "security" / "secure_signature.py", "import hashlib\n\ndef sign(payload: bytes) -> str:\n    return hashlib.sha256(payload).hexdigest()\n")
        write_text(repo_root / "app" / "security" / "legacy_signature.py", "import hashlib\n\ndef sign(payload: bytes) -> str:\n    return hashlib.md5(payload).hexdigest()\n")
        write_text(repo_root / "app" / "security" / "token_factory.py", "import random\n\ndef issue_code() -> str:\n    generator = random.Random()\n    return f\"{generator.randint(100000, 999999)}\"\n")
    elif scenario.id == "Q-V4-PY-004":
        write_text(repo_root / "app" / "security" / "legacy_nonce.py", "import random\n\ndef issue_nonce() -> str:\n    generator = random.Random()\n    return f\"nonce-{generator.randint(100000, 999999)}\"\n")
        write_text(repo_root / "app" / "security" / "scary_random_wrapper.py", "import secrets\n\ndef random_or_not(value: bytes) -> str:\n    return secrets.token_hex(16)\n")
        write_text(repo_root / "app" / "security" / "hash_inventory.py", "import hashlib\n\ndef supported_algorithms() -> tuple[str, ...]:\n    return ('sha256', 'sha512')\n")
    elif scenario.id == "Q-V4-PY-005":
        write_text(repo_root / "app" / "security" / "legacy_signature.py", "import hashlib\n\ndef sign(payload: bytes) -> str:\n    return hashlib.md5(payload).hexdigest()\n")
        write_text(repo_root / "app" / "security" / "hash_inventory.py", "import hashlib\n\ndef supported_algorithms() -> tuple[str, ...]:\n    return ('sha256', 'sha512')\n")
        write_text(repo_root / "app" / "security" / "secure_hash.py", "import hashlib\n\ndef sign(payload: bytes) -> str:\n    return hashlib.sha256(payload).hexdigest()\n")
        write_text(repo_root / "docs" / "hash-guidance.md", "Use hashlib.sha256 in runtime code; examples remain descriptive only.\n")
    elif scenario.id == "Q-V4-PY-006":
        write_text(repo_root / "app" / "security" / "live_md5.py", "import hashlib as digest_lib\n\ndef sign(payload: bytes) -> str:\n    return digest_lib.md5(payload).hexdigest()\n")
        write_text(repo_root / "app" / "security" / "hash_alias_inventory.py", "import hashlib as digest_lib\n\ndef supported_algorithms() -> tuple[str, ...]:\n    return ('sha256', digest_lib.sha512().name)\n")
        write_text(repo_root / "app" / "security" / "safe_hash_wrapper.py", "import hashlib\n\ndef sign(payload: bytes) -> str:\n    return hashlib.sha256(payload).hexdigest()\n")
    elif scenario.id == "Q-V5-PY-002":
        write_text(repo_root / "app" / "clients" / "partner_pull_client.py", "import requests\n\ndef fetch_payload(url: str) -> str:\n    return requests.get(url, verify=False, timeout=5).text\n")
        write_text(repo_root / "app" / "security" / "unverified_ssl_context.py", "import ssl\n\ndef build_context():\n    return ssl._create_unverified_context()\n")
        write_text(repo_root / "app" / "clients" / "secure_partner_pull_client.py", "def fetch_payload(url: str) -> str:\n    return url\n")
    elif scenario.id == "Q-V5-PY-003":
        write_text(repo_root / "app" / "clients" / "partner_sync_client.py", "import requests\n\ndef fetch_payload(url: str) -> str:\n    return requests.get(url, verify=False, timeout=5).text\n")
        write_text(repo_root / "examples" / "tls_example.py", "import requests\n\nresponse = requests.get('https://example.invalid', verify=False)\n")
        write_text(repo_root / "tests" / "test_tls_example.py", "def test_example_placeholder() -> None:\n    assert True\n")
        write_text(repo_root / "docs" / "tls-usage.md", "Example snippets may mention verify=False but remain non-live.\n")
    elif scenario.id == "Q-V5-PY-004":
        write_text(
            repo_root / "app" / "clients" / "session_wrapper.py",
            "import requests\n\n\ndef _transport(url: str, **kwargs) -> str:\n    return requests.get(url, timeout=5, **kwargs).text\n\n\ndef fetch_payload(url: str) -> str:\n    options = {'verify': False}\n    return _transport(url, **options)\n",
        )
        write_text(repo_root / "app" / "clients" / "safe_session_wrapper.py", "import requests\n\ndef fetch_payload(url: str) -> str:\n    return requests.get(url, verify=True, timeout=5).text\n")
        write_text(repo_root / "examples" / "session_example.py", "def example() -> dict[str, bool]:\n    return {'verify': False}\n")


def _apply_node_variant(repo_root: Path, scenario: ScenarioSpec) -> None:
    if scenario.family == "guardian_live_node":
        write_text(repo_root / "src" / "config" / "secrets.ts", f'export const ACTIVE_SECRET = "{GENERIC_SECRET_GOLF}";\n')
        write_text(repo_root / "config" / "production.json", f'{{ "clientSecret": "{GENERIC_SECRET_BRAVO}" }}\n')
        write_text(repo_root / "src" / "modules" / "partners" / "bootstrap" / "partnerKeyLoader.ts", f"export const PARTNER_KEY = `{PRIVATE_KEY_BLOCK_A.rstrip()}`;\n")
        write_text(repo_root / "scripts" / "bootstrap-partner.ts", f'export const bootstrapToken = "{GENERIC_SECRET_DELTA}";\n')
    elif scenario.family == "guardian_history_node":
        write_text(repo_root / "src" / "modules" / "partner" / "bootstrap" / "mainSafe.ts", "export const mainBranchStatus = 'clean';\n")
        write_text(repo_root / "src" / "modules" / "partner" / "bootstrap" / "branchLeak.ts", "export const featureBranchToken = 'placeholder-clean-value';\n")
    elif scenario.id == "Q-V4-TS-003":
        write_text(repo_root / "src" / "modules" / "security" / "legacyDigest.ts", "import { createHash } from 'crypto';\nexport function digest(value: string): string { return createHash('md5').update(value).digest('hex'); }\n")
        write_text(repo_root / "src" / "modules" / "security" / "legacySha1Digest.ts", "import { createHash } from 'crypto';\nexport function digestSha1(value: string): string { return createHash('sha1').update(value).digest('hex'); }\n")
        write_text(repo_root / "src" / "modules" / "security" / "secureDigest.ts", "import { createHash } from 'crypto';\nexport function digestSecure(value: string): string { return createHash('sha256').update(value).digest('hex'); }\n")
    elif scenario.id == "Q-V4-TS-005":
        write_text(repo_root / "src" / "modules" / "security" / "hashFactory.ts", "import { createHash, Hash } from 'crypto';\nfunction buildLegacy(): Hash { return createHash('md5'); }\nexport function digest(value: string): string { return buildLegacy().update(value).digest('hex'); }\n")
        write_text(repo_root / "src" / "modules" / "security" / "secureHashFactory.ts", "import { createHash, Hash } from 'crypto';\nfunction buildSecure(): Hash { return createHash('sha256'); }\nexport function digest(value: string): string { return buildSecure().update(value).digest('hex'); }\n")
        write_text(repo_root / "src" / "modules" / "security" / "hashCatalog.ts", "export const supportedHashes = ['sha256', 'sha512'];\n")
    elif scenario.id == "Q-V4-TS-006":
        write_text(
            repo_root / "src" / "modules" / "security" / "hashComposer.ts",
            "import * as crypto from 'crypto';\nconst { createHash: createLegacyHash } = crypto;\nfunction legacyFactory() { return { build: () => createLegacyHash('md5') }; }\nexport function digest(value: string): string { return legacyFactory().build().update(value).digest('hex'); }\n",
        )
        write_text(repo_root / "src" / "modules" / "security" / "safeHashComposer.ts", "import * as crypto from 'crypto';\nconst { createHash } = crypto;\nexport function digest(value: string): string { return createHash('sha256').update(value).digest('hex'); }\n")
        write_text(repo_root / "src" / "modules" / "security" / "hashCatalog.ts", "export const supportedHashes = ['sha256', 'sha512'];\n")
    elif scenario.id == "Q-V6-TS-001":
        write_text(repo_root / "src" / "modules" / "http" / "insecureAgentFactory.ts", "import https from 'https';\nexport function buildAgent() { return new https.Agent({ rejectUnauthorized: false }); }\n")
        write_text(repo_root / "src" / "modules" / "http" / "insecureBillingClient.ts", "import https from 'https';\nexport function billingAgent() { return new https.Agent({ rejectUnauthorized: false }); }\n")
        write_text(repo_root / "src" / "modules" / "http" / "secureAgentFactory.ts", "import https from 'https';\nexport function buildSecureAgent() { return new https.Agent({ rejectUnauthorized: true }); }\n")
    elif scenario.id == "Q-V6-TS-002":
        write_text(repo_root / "src" / "modules" / "http" / "insecureSpreadAgent.ts", "import https from 'https';\nconst sharedTls = { rejectUnauthorized: false };\nfunction buildTlsOptions() { return { ...sharedTls }; }\nexport function buildAgent() { return new https.Agent(buildTlsOptions()); }\n")
        write_text(repo_root / "src" / "modules" / "http" / "secureSpreadAgent.ts", "import https from 'https';\nconst sharedTls = { rejectUnauthorized: true };\nfunction buildTlsOptions() { return { ...sharedTls }; }\nexport function buildAgent() { return new https.Agent(buildTlsOptions()); }\n")
        write_text(repo_root / "docs" / "tls-wrapper.md", "Wrapper and spread examples remain descriptive; only live runtime files should be flagged.\n")
    elif scenario.id == "Q-V6-TS-004":
        write_text(
            repo_root / "src" / "modules" / "http" / "composeTls.ts",
            "import https from 'https';\nconst partial = { rejectUnauthorized: false };\nfunction merged() { return Object.assign({}, { keepAlive: true }, partial); }\nfunction runtimeOptions() { return { ...merged() }; }\nexport function buildAgent() { return new https.Agent(runtimeOptions()); }\n",
        )
        write_text(repo_root / "src" / "modules" / "http" / "safeComposeTls.ts", "import https from 'https';\nconst partial = { rejectUnauthorized: true };\nexport function buildAgent() { return new https.Agent({ ...partial, keepAlive: true }); }\n")
        write_text(repo_root / "docs" / "tls-compose.md", "Object composition examples stay non-live unless wired into runtime agents.\n")


def _apply_config_variant(repo_root: Path, scenario: ScenarioSpec) -> None:
    if scenario.family == "guardian_live_config":
        write_text(repo_root / "config" / "runtime" / "admin-prod.yaml", f"auth:\n  secret: {GENERIC_SECRET_GOLF}\n")
        write_text(repo_root / "ops" / "runtime" / "portal.env", f"PORTAL_TOKEN={GENERIC_SECRET_ECHO}\n")
        write_text(repo_root / "config" / "keys" / "admin_portal.pem", PRIVATE_KEY_BLOCK_A)
        write_text(repo_root / "deploy" / "prod" / "admin.properties", f"admin.password={GENERIC_SECRET_BRAVO}\n")
        write_text(repo_root / "terraform" / "sample.tfvars", "admin_password = \"example\"\n")
    elif scenario.id == "Q-V6-CONFIG-003":
        write_text(repo_root / "deploy" / "envoy.yaml", "tls_minimum_protocol_version: TLSv1_0\ntrust_chain_verification: ACCEPT_UNTRUSTED\n")
        write_text(repo_root / "runtime" / ".env", "NODE_TLS_REJECT_UNAUTHORIZED=0\n")
        write_text(repo_root / "helm" / "examples" / "values.yaml", "tls:\n  verify: true\n")
    elif scenario.id == "Q-V6-CONFIG-004":
        write_text(repo_root / "deploy" / "live" / "envoy.yaml", "tls_minimum_protocol_version: TLSv1_2\ntrust_chain_verification: ACCEPT_UNTRUSTED\n")
        write_text(repo_root / "runtime" / ".env", "NODE_TLS_REJECT_UNAUTHORIZED=0\n")
        write_text(repo_root / "helm" / "examples" / "values.yaml", "tls:\n  trust_chain_verification: ACCEPT_UNTRUSTED\n")
        write_text(repo_root / "docs" / "runtime-notes.md", "# Runtime notes\n# Example override only: NODE_TLS_REJECT_UNAUTHORIZED=0\n")
        write_text(repo_root / "tests" / "fixtures" / "runtime.env", "NODE_TLS_REJECT_UNAUTHORIZED=0\n")
    elif scenario.id == "Q-V6-CONFIG-005":
        write_text(repo_root / "deploy" / "live" / "envoy.yaml", "trust_chain_verification: ACCEPT_UNTRUSTED\n")
        write_text(repo_root / "runtime" / ".env", "NODE_TLS_REJECT_UNAUTHORIZED=0\n")
        write_text(repo_root / "docs" / "runtime-overlays.md", "# Example overlay\n# trust_chain_verification: ACCEPT_UNTRUSTED\n# NODE_TLS_REJECT_UNAUTHORIZED=0\n")
        write_text(repo_root / "examples" / "envoy" / "values.yaml", "tls:\n  trust_chain_verification: ACCEPT_UNTRUSTED\n")
        write_text(repo_root / "tests" / "fixtures" / "runtime.env", "NODE_TLS_REJECT_UNAUTHORIZED=0\n")
    elif scenario.id == "Q-V6-CONFIG-006":
        write_text(repo_root / "deploy" / "live" / "envoy.yaml", "tls_minimum_protocol_version: TLSv1_0\ntrust_chain_verification: ACCEPT_UNTRUSTED\n")
        write_text(repo_root / "runtime" / "live.env", "NODE_TLS_REJECT_UNAUTHORIZED=0\n")
        write_text(repo_root / "docs" / "examples.md", "# Example values\n# trust_chain_verification: ACCEPT_UNTRUSTED\n# NODE_TLS_REJECT_UNAUTHORIZED=0\n")
        write_text(repo_root / "helm" / "examples" / "values.yaml", "envoy:\n  trustChainVerification: ACCEPT_UNTRUSTED\n")
        write_text(repo_root / "tests" / "fixtures" / "runtime.env", "NODE_TLS_REJECT_UNAUTHORIZED=0\n")


def _apply_go_variant(repo_root: Path, scenario: ScenarioSpec) -> None:
    if scenario.id == "Q-V4-GO-002":
        write_text(
            repo_root / "internal" / "security" / "legacy_hash.go",
            textwrap.dedent(
                """\
                package security

                import (
                    "crypto/md5"
                    "crypto/sha1"
                )

                func Digest(input []byte) ([]byte, []byte) {
                    left := md5.New()
                    left.Write(input)
                    right := sha1.New()
                    right.Write(input)
                    return left.Sum(nil), right.Sum(nil)
                }
                """
            ),
        )
        write_text(repo_root / "internal" / "security" / "secure_hmac.go", 'package security\nimport "crypto/sha256"\nfunc SecureDigest(input []byte) [32]byte { return sha256.Sum256(input) }\n')
    elif scenario.id == "Q-V4-GO-003":
        write_text(
            repo_root / "internal" / "security" / "legacy_hash.go",
            textwrap.dedent(
                """\
                package security

                import (
                    "crypto/md5"
                    "crypto/sha1"
                )

                func Digest(input []byte) ([]byte, []byte) {
                    left := md5.New()
                    left.Write(input)
                    right := sha1.New()
                    right.Write(input)
                    return left.Sum(nil), right.Sum(nil)
                }
                """
            ),
        )
        write_text(repo_root / "docs" / "crypto-notes.md", "md5 and sha1 examples live only in archived docs, not runtime guidance.\n")
        write_text(repo_root / "internal" / "security" / "hash_inventory_test.go", "package security\nimport \"testing\"\nfunc TestInventoryOnly(t *testing.T) { left, right := Digest([]byte(\"seed\")); if len(left) == 0 || len(right) == 0 { t.Fatal(\"expected digest output\") } }\n")
    elif scenario.id == "Q-V4-GO-004":
        write_text(
            repo_root / "internal" / "security" / "helper_hash.go",
            textwrap.dedent(
                """\
                package security

                import "crypto/md5"

                func legacyFactory() hashWrapper {
                    return hashWrapper{newFunc: md5.New}
                }

                type hashWrapper struct {
                    newFunc func() interface{ Write([]byte) (int, error); Sum([]byte) []byte }
                }

                func Digest(input []byte) []byte {
                    digest := legacyFactory().newFunc()
                    digest.Write(input)
                    return digest.Sum(nil)
                }
                """
            ),
        )
        write_text(repo_root / "docs" / "hash-guidance.md", "Go hash helper docs remain descriptive and non-runtime.\n")
        write_text(repo_root / "internal" / "security" / "helper_hash_test.go", "package security\nimport \"testing\"\nfunc TestHelperHashSmoke(t *testing.T) { if len(Digest([]byte(\"seed\"))) == 0 { t.Fatal(\"expected bytes\") } }\n")


def _apply_csharp_variant(repo_root: Path, scenario: ScenarioSpec) -> None:
    if scenario.id == "Q-V3-CS-003":
        write_text(repo_root / "src" / "Library" / "Security" / "LegacyHashService.cs", "using System.Security.Cryptography; namespace Arq.Lab.Library.Security; public static class LegacyHashService { public static byte[] Md5(byte[] value) => MD5.Create().ComputeHash(value); public static byte[] Sha1(byte[] value) => SHA1.Create().ComputeHash(value); }\n")
        write_text(repo_root / "src" / "Library" / "Security" / "LegacyCipherService.cs", "using System.Security.Cryptography; namespace Arq.Lab.Library.Security; public static class LegacyCipherService { public static Aes Cipher() { var aes = Aes.Create(); aes.Mode = CipherMode.ECB; return aes; } }\n")
        write_text(repo_root / "src" / "Library" / "Security" / "OtpTokenService.cs", "using System; namespace Arq.Lab.Library.Security; public static class OtpTokenService { public static int IssueCode() => new Random().Next(100000, 999999); }\n")
        write_text(repo_root / "src" / "Library" / "Security" / "SecureOtpTokenService.cs", "using System.Security.Cryptography; namespace Arq.Lab.Library.Security; public static class SecureOtpTokenService { public static int IssueCode() => RandomNumberGenerator.GetInt32(100000, 999999); }\n")
    elif scenario.id == "Q-V3-CS-004":
        write_text(repo_root / "src" / "Library" / "Security" / "LegacyDigestService.cs", "using System.Security.Cryptography; namespace Arq.Lab.Library.Security; public static class LegacyDigestService { public static byte[] Md5(byte[] value) => MD5.Create().ComputeHash(value); }\n")
        write_text(repo_root / "src" / "Library" / "Security" / "DigestInventoryOnly.cs", "using System.Security.Cryptography; namespace Arq.Lab.Library.Security; public static class DigestInventoryOnly { public static string Supported() => SHA256.HashData(System.Text.Encoding.UTF8.GetBytes(\"seed\")).Length.ToString(); }\n")
        write_text(repo_root / "src" / "Library" / "Security" / "SecureDigestFacade.cs", "using System.Security.Cryptography; namespace Arq.Lab.Library.Security; public static class SecureDigestFacade { public static byte[] Sha256(byte[] value) => SHA256.HashData(value); }\n")
        write_text(repo_root / "docs" / "csharp-crypto-notes.md", "Inventory-only C# notes should stay descriptive and safe.\n")
    elif scenario.id == "Q-V3-CS-005":
        write_text(repo_root / "src" / "Library" / "Security" / "LegacyDigestFactory.cs", "using System.Security.Cryptography; namespace Arq.Lab.Library.Security; public static class LegacyDigestFactory { public static byte[] Md5(byte[] value) => MD5.Create().ComputeHash(value); public static byte[] Sha1(byte[] value) => SHA1.Create().ComputeHash(value); }\n")
        write_text(repo_root / "src" / "Library" / "Security" / "DigestInventoryCatalog.cs", "using System; using System.Security.Cryptography; namespace Arq.Lab.Library.Security; public static class DigestInventoryCatalog { public static int Sample() => new Random().Next(100, 999); public static string Supported() => SHA256.HashData(System.Text.Encoding.UTF8.GetBytes(\"seed\")).Length.ToString(); }\n")
        write_text(repo_root / "src" / "Library" / "Security" / "SecureRandomFacade.cs", "using System.Security.Cryptography; namespace Arq.Lab.Library.Security; public static class SecureRandomFacade { public static int Next() => RandomNumberGenerator.GetInt32(100, 999); }\n")
    elif scenario.id == "Q-V6-CS-002":
        write_text(repo_root / "src" / "Library" / "Http" / "InsecurePartnerClientRegistration.cs", "using System.Net.Http; namespace Arq.Lab.Library.Http; public static class InsecurePartnerClientRegistration { public static HttpClientHandler Build() => new HttpClientHandler { ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator }; }\n")
        write_text(repo_root / "src" / "Library" / "Http" / "SecurePartnerClientRegistration.cs", "using System.Net.Http; namespace Arq.Lab.Library.Http; public static class SecurePartnerClientRegistration { public static HttpClientHandler Build() => new HttpClientHandler(); }\n")
    elif scenario.id == "Q-V6-CS-003":
        write_text(repo_root / "src" / "Library" / "Http" / "InsecureServiceRegistration.cs", "using System.Net.Http; namespace Arq.Lab.Library.Http; public static class InsecureServiceRegistration { public static HttpClientHandler Build() => new HttpClientHandler { ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator }; }\n")
        write_text(repo_root / "src" / "Library" / "Http" / "HttpInventoryCatalog.cs", "using System.Net.Http; namespace Arq.Lab.Library.Http; public static class HttpInventoryCatalog { public static string HandlerName() => typeof(HttpClientHandler).Name; }\n")
        write_text(repo_root / "src" / "Library" / "Http" / "SecureServiceRegistration.cs", "using System.Net.Http; namespace Arq.Lab.Library.Http; public static class SecureServiceRegistration { public static HttpClientHandler Build() => new HttpClientHandler(); }\n")
        write_text(repo_root / "docs" / "http-registration.md", "Inventory-only C# HttpClient registration notes remain non-live.\n")
    elif scenario.id == "Q-V6-CS-004":
        write_text(
            repo_root / "src" / "Library" / "Http" / "HttpClientPolicy.cs",
            "using System.Net.Http; namespace Arq.Lab.Library.Http; public static class HttpClientPolicy { private static readonly Func<HttpClientHandler, HttpClientHandler> Binder = handler => { handler.ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator; return handler; }; public static HttpClientHandler Build() => Binder(new HttpClientHandler()); }\n",
        )
        write_text(repo_root / "src" / "Library" / "Http" / "HttpPolicyInventory.cs", "using System.Net.Http; namespace Arq.Lab.Library.Http; public static class HttpPolicyInventory { public static string Name() => typeof(HttpClientHandler).Name; }\n")
        write_text(repo_root / "src" / "Library" / "Http" / "SecureHttpClientPolicy.cs", "using System.Net.Http; namespace Arq.Lab.Library.Http; public static class SecureHttpClientPolicy { public static HttpClientHandler Build() => new HttpClientHandler(); }\n")


def _commit_current_state(git_factory: GitFactory, repo_root: Path, message: str) -> str:
    git_factory.add_all(repo_root)
    return git_factory.commit_all(repo_root, message)


def _build_java_repo(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    metadata = _populate_java_common(repo_root, scenario)
    _apply_java_variant(repo_root, scenario, metadata["packageName"])
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, f"bootstrap {scenario.id}")
    return metadata


def _build_python_repo(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _populate_python_common(repo_root, scenario)
    _apply_python_variant(repo_root, scenario)
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, f"bootstrap {scenario.id}")
    return {}


def _build_node_repo(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _populate_node_common(repo_root, scenario)
    _apply_node_variant(repo_root, scenario)
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, f"bootstrap {scenario.id}")
    return {}


def _build_config_repo(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _populate_config_common(repo_root, scenario)
    _apply_config_variant(repo_root, scenario)
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, f"bootstrap {scenario.id}")
    return {}


def _build_go_repo(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _populate_go_common(repo_root, scenario)
    _apply_go_variant(repo_root, scenario)
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, f"bootstrap {scenario.id}")
    return {}


def _build_csharp_repo(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _populate_csharp_common(repo_root, scenario)
    _apply_csharp_variant(repo_root, scenario)
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, f"bootstrap {scenario.id}")
    return {}


def _build_guardian_history_java(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    metadata = _populate_java_common(repo_root, scenario)
    package_name = metadata["packageName"]
    package_root = ensure_dir(_package_dir(repo_root, package_name))
    git_factory.init(repo_root)
    if scenario.id == "G-V2-HIST-004":
        source_target = package_root / "history" / "bootstrap" / "PartnerTokenBootstrap.java"
        moved_target = package_root / "history" / "archive" / "PartnerCredentialArchive.java"
        write_text(source_target, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenBootstrap {{ private static final String PARTNER_TOKEN = \"safe-reference\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _inflate_repository(repo_root, scenario)
        _commit_current_state(git_factory, repo_root, "c001 bootstrap repo")
        write_text(source_target, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenBootstrap {{ private static final String PARTNER_TOKEN = \"{GENERIC_SECRET_GOLF}\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c002 add transient partner token")
        ensure_dir(moved_target.parent)
        if source_target.exists():
            source_target.replace(moved_target)
        write_text(moved_target, f"package {package_name}.history.archive;\npublic class PartnerCredentialArchive {{ private static final String PARTNER_TOKEN = \"{GENERIC_SECRET_GOLF}\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c003 move token archive into history package")
        write_text(repo_root / "docs" / "rename-plan.md", "masked_token=****\n")
        _commit_current_state(git_factory, repo_root, "c004 add rename plan noise")
        write_text(moved_target, f"package {package_name}.history.archive;\npublic class PartnerCredentialArchive {{ private static final String PARTNER_TOKEN = \"safe-reference\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c005 remove token after archive migration")
        write_text(package_root / "service" / "HistoryRefactor.java", f"package {package_name}.service;\npublic class HistoryRefactor {{ public boolean enabled() {{ return true; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c006 unrelated refactor")
    elif scenario.id == "G-V2-HIST-006":
        source_target = package_root / "history" / "bootstrap" / "PartnerTokenRelocationBootstrap.java"
        moved_target = package_root / "history" / "relocation" / "PartnerTokenRelocationArchive.java"
        write_text(source_target, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenRelocationBootstrap {{ private static final String PARTNER_TOKEN = \"safe-reference\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _inflate_repository(repo_root, scenario)
        _commit_current_state(git_factory, repo_root, "c001 bootstrap repo")
        write_text(source_target, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenRelocationBootstrap {{ private static final String PARTNER_TOKEN = \"{GENERIC_SECRET_CHARLIE}\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c002 add transient relocation token")
        ensure_dir(moved_target.parent)
        if source_target.exists():
            source_target.replace(moved_target)
        write_text(moved_target, f"package {package_name}.history.relocation;\npublic class PartnerTokenRelocationArchive {{ private static final String PARTNER_TOKEN = \"{GENERIC_SECRET_CHARLIE}\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c003 move token into relocation archive")
        write_text(repo_root / "docs" / "relocation-plan.md", "masked_partner_token=****\n")
        _commit_current_state(git_factory, repo_root, "c004 add relocation plan noise")
        write_text(moved_target, f"package {package_name}.history.relocation;\npublic class PartnerTokenRelocationArchive {{ private static final String PARTNER_TOKEN = \"safe-reference\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c005 remove relocation token from head")
        write_text(package_root / "service" / "RelocationCleanup.java", f"package {package_name}.service;\npublic class RelocationCleanup {{ public boolean enabled() {{ return true; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c006 unrelated relocation cleanup")
        write_text(package_root / "service" / "RelocationMetrics.java", f"package {package_name}.service;\npublic class RelocationMetrics {{ public int backlog() {{ return 0; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c007 add safe metrics")
    elif scenario.id == "G-V2-HIST-017":
        original = package_root / "history" / "bootstrap" / "PartnerTokenArchive.java"
        duplicate = package_root / "history" / "archive" / "PartnerTokenArchive.java"
        write_text(original, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenArchive {{ private static final String PARTNER_TOKEN = \"safe-reference\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _inflate_repository(repo_root, scenario)
        _commit_current_state(git_factory, repo_root, "c001 bootstrap repo")
        write_text(original, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenArchive {{ private static final String PARTNER_TOKEN = \"{GENERIC_SECRET_FOXTROT}\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c002 add secret on main")
        ensure_dir(duplicate.parent)
        write_text(duplicate, f"package {package_name}.history.archive;\npublic class PartnerTokenArchive {{ private static final String PARTNER_TOKEN = \"{GENERIC_SECRET_FOXTROT}\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c003 duplicate secret into archive path")
        write_text(repo_root / "docs" / "cherry-pick.md", "history-only operational note\n")
        _commit_current_state(git_factory, repo_root, "c004 add docs chore")
        write_text(original, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenArchive {{ private static final String PARTNER_TOKEN = \"safe-reference\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        if duplicate.exists():
            duplicate.unlink()
        _commit_current_state(git_factory, repo_root, "c005 revert secret from head")
        git_factory.checkout(repo_root, "feature/archive-duplication", create=True)
        write_text(repo_root / "docs" / "feature-archive.md", "archive duplication branch retains only docs context\n")
        _commit_current_state(git_factory, repo_root, "c006 feature archive docs")
        git_factory.checkout(repo_root, "main")
        git_factory.checkout(repo_root, "release/2026.07", create=True)
        write_text(repo_root / "docs" / "release.md", "release branch remains clean\n")
        _commit_current_state(git_factory, repo_root, "c007 release branch clean")
        git_factory.checkout(repo_root, "main")
    else:
        target = package_root / "history" / "bootstrap" / "PartnerTokenArchive.java"
        write_text(target, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenArchive {{ private static final String PARTNER_TOKEN = \"safe-reference\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _inflate_repository(repo_root, scenario)
        _commit_current_state(git_factory, repo_root, "c001 bootstrap repo")
        write_text(target, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenArchive {{ private static final String PARTNER_TOKEN = \"{GENERIC_SECRET_GOLF}\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c002 add live partner access token")
        write_text(repo_root / "docs" / "noise.md", "masked-token=****\n")
        _commit_current_state(git_factory, repo_root, "c003 add docs noise")
        write_text(target, f"package {package_name}.history.bootstrap;\npublic class PartnerTokenArchive {{ private static final String PARTNER_TOKEN = \"safe-reference\"; public String current() {{ return PARTNER_TOKEN; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c004 remove token and replace with safe reference")
        write_text(package_root / "service" / "HistoryRefactor.java", f"package {package_name}.service;\npublic class HistoryRefactor {{ public boolean enabled() {{ return true; }} }}\n")
        _commit_current_state(git_factory, repo_root, "c005 unrelated refactor")
    return metadata


def _build_guardian_history_node(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _populate_node_common(repo_root, scenario)
    _apply_node_variant(repo_root, scenario)
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, "c001 main clean baseline")
    if scenario.id == "G-V2-HIST-007":
        git_factory.checkout(repo_root, "feature/customer-hotfix", create=True)
        write_text(repo_root / "src" / "modules" / "partner" / "bootstrap" / "featureBranchToken.ts", "export const featureBranchToken = '0123456789ABCDEFA31a';\n")
        _commit_current_state(git_factory, repo_root, "c002 temporary secret on feature branch")
        write_text(repo_root / "docs" / "branch-chore.md", "feature branch operational note only\n")
        docs_sha = _commit_current_state(git_factory, repo_root, "c003 feature docs chore")
        git_factory.checkout(repo_root, "main")
        git_factory.checkout(repo_root, "release/2026.05", create=True)
        write_text(repo_root / "docs" / "release.md", "release branch remains clean\n")
        _commit_current_state(git_factory, repo_root, "c004 release branch clean state")
        git_factory.checkout(repo_root, "main")
        git_factory.checkout(repo_root, "hotfix/cherry-picked-docs", create=True)
        run_command(["git", "cherry-pick", docs_sha], repo_root, check=True)
        git_factory.checkout(repo_root, "main")
    elif scenario.id == "G-V2-HIST-014":
        split_target = repo_root / "src" / "modules" / "partner" / "bootstrap" / "partnerSecret.ts"
        write_text(split_target, "export const partnerSecret = 'safe-reference';\n")
        _commit_current_state(git_factory, repo_root, "c002 safe baseline file")
        write_text(split_target, "export const partnerSecret = 'A3-ABC123-' + 'ABCDEFGHIJK-ABCDE-ABCDE-ABCDE';\n")
        _commit_current_state(git_factory, repo_root, "c003 split secret assembly")
        write_text(split_target, "export const partnerSecret = 'A3-ABC123-ABCDEFGHIJK-ABCDE-ABCDE-ABCDE';\n")
        _commit_current_state(git_factory, repo_root, "c004 canonical secret assembly")
        write_text(repo_root / "docs" / "split-secret.md", "Split and concat examples here remain descriptive only.\n")
        write_text(repo_root / "examples" / "concat-demo.ts", "export const concatDemo = ['example', 'only'].join('-');\n")
        _commit_current_state(git_factory, repo_root, "c005 docs and example context")
        write_text(split_target, "export const partnerSecret = 'safe-reference';\n")
        _commit_current_state(git_factory, repo_root, "c006 remove secret from head")
    else:
        git_factory.checkout(repo_root, "feature/partner-hotfix", create=True)
        write_text(repo_root / "src" / "modules" / "partner" / "bootstrap" / "branchLeak.ts", "export const featureBranchToken = '0123456789ABCDEFA31a';\n")
        _commit_current_state(git_factory, repo_root, "c002 temporary secret on feature branch")
        git_factory.checkout(repo_root, "main")
        git_factory.checkout(repo_root, "release/2026.04", create=True)
        write_text(repo_root / "docs" / "release.md", "release branch remains clean\n")
        _commit_current_state(git_factory, repo_root, "c003 release branch clean state")
        git_factory.checkout(repo_root, "main")
        git_factory.checkout(repo_root, "feature/docs-refresh", create=True)
        write_text(repo_root / "docs" / "branch-notes.md", "docs refresh branch only\n")
        _commit_current_state(git_factory, repo_root, "c004 noise-only docs branch")
        git_factory.checkout(repo_root, "main")
    return {}


def _build_guardian_history_python(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _populate_python_common(repo_root, scenario)
    write_text(repo_root / "app" / "security" / "rotation_state.py", "def state() -> str:\n    return 'safe'\n")
    git_factory.init(repo_root)
    _inflate_repository(repo_root, scenario)
    _commit_current_state(git_factory, repo_root, "c001 bootstrap")
    if scenario.id == "G-V2-HIST-005":
        write_text(repo_root / "ops" / "runtime" / "partner_runtime.env", f"PARTNER_RUNTIME_TOKEN={GENERIC_SECRET_BRAVO}\n")
        _commit_current_state(git_factory, repo_root, "c002 add runtime token")
        write_text(repo_root / "ops" / "runtime" / "partner_runtime.env", f"PARTNER_RUNTIME_TOKEN = \"{GENERIC_SECRET_BRAVO}\"\n")
        _commit_current_state(git_factory, repo_root, "c003 reformat runtime token")
        ensure_dir(repo_root / "ops" / "archive")
        if (repo_root / "ops" / "runtime" / "partner_runtime.env").exists():
            (repo_root / "ops" / "runtime" / "partner_runtime.env").replace(repo_root / "ops" / "archive" / "partner_runtime.env")
        _commit_current_state(git_factory, repo_root, "c004 move runtime token to archive")
        write_text(repo_root / "docs" / "examples" / "runtime-reference.md", "PARTNER_RUNTIME_TOKEN=example-value\n")
        _commit_current_state(git_factory, repo_root, "c005 add runtime docs example")
        write_text(repo_root / "ops" / "archive" / "partner_runtime.env", "PARTNER_RUNTIME_TOKEN=safe-reference\n")
        _commit_current_state(git_factory, repo_root, "c006 remove runtime token and keep safe placeholder")
    elif scenario.id == "G-V2-HIST-008":
        write_text(repo_root / "ops" / "keys" / "service-private.pem", PRIVATE_KEY_BLOCK_A)
        _commit_current_state(git_factory, repo_root, "c002 add private key lineage")
        write_text(repo_root / "docs" / "certs" / "public-chain.pem", PUBLIC_CERT_CHAIN)
        _commit_current_state(git_factory, repo_root, "c003 add public chain docs")
        write_text(repo_root / "ops" / "csr" / "service.csr", CSR_SAMPLE)
        _commit_current_state(git_factory, repo_root, "c004 add csr lineage")
        write_text(repo_root / "docs" / "pki-lineage.md", "Public chain and CSR remain explanatory only.\n")
        _commit_current_state(git_factory, repo_root, "c005 add pki lineage docs")
        write_text(repo_root / "ops" / "keys" / "service-private.pem", "-----BEGIN PRIVATE KEY-----\nplaceholder-only\n")
        _commit_current_state(git_factory, repo_root, "c006 remove live private key from head")
    elif scenario.id == "G-V2-HIST-009":
        write_text(repo_root / "ops" / "runtime" / "partner_token.env", f"PARTNER_RUNTIME_TOKEN={GENERIC_SECRET_DELTA}\n")
        _commit_current_state(git_factory, repo_root, "c002 add canonical token")
        write_text(repo_root / "ops" / "runtime" / "partner_token.env", f"PARTNER_RUNTIME_TOKEN = \"{GENERIC_SECRET_DELTA}\"\n")
        _commit_current_state(git_factory, repo_root, "c003 quote runtime token")
        ensure_dir(repo_root / "ops" / "archive")
        if (repo_root / "ops" / "runtime" / "partner_token.env").exists():
            (repo_root / "ops" / "runtime" / "partner_token.env").replace(repo_root / "ops" / "archive" / "partner_token.env")
        _commit_current_state(git_factory, repo_root, "c004 move token into archive")
        write_text(repo_root / "docs" / "token-wrapping.md", "PARTNER_RUNTIME_TOKEN=base64-looking-example-only\n")
        write_text(repo_root / "examples" / "base64-reference.txt", "UEFSVE5FUl9SVU5USU1FX1RPS0VOPWV4YW1wbGU=\n")
        _commit_current_state(git_factory, repo_root, "c005 add wrapping and base64 docs")
        write_text(repo_root / "ops" / "archive" / "partner_token.env", "PARTNER_RUNTIME_TOKEN=safe-reference\n")
        _commit_current_state(git_factory, repo_root, "c006 remove runtime token and keep safe placeholder")
    elif scenario.id == "G-V2-HIST-015":
        write_text(repo_root / "docs" / "certs" / "public-chain.pem", PUBLIC_CERT_CHAIN)
        write_text(repo_root / "ops" / "csr" / "service.csr", CSR_SAMPLE)
        _commit_current_state(git_factory, repo_root, "c002 keep main cert and csr only")
        git_factory.checkout(repo_root, "feature/private-key-hotfix", create=True)
        write_text(repo_root / "ops" / "keys" / "feature-private.pem", PRIVATE_KEY_BLOCK_B)
        _commit_current_state(git_factory, repo_root, "c003 feature branch private key")
        git_factory.checkout(repo_root, "main")
        git_factory.checkout(repo_root, "release/2026.06", create=True)
        write_text(repo_root / "docs" / "release.md", "release branch remains cert-only and clean.\n")
        _commit_current_state(git_factory, repo_root, "c004 release branch clean")
        git_factory.checkout(repo_root, "main")
    elif scenario.id == "G-V2-HIST-016":
        write_text(repo_root / "ops" / "runtime" / "runtime-values.yaml", f"runtime:\n  partnerToken: >-\n    {GENERIC_SECRET_ALPHA}\n")
        _commit_current_state(git_factory, repo_root, "c002 add folded yaml secret")
        write_text(repo_root / "docs" / "masked-values.yaml", "runtime:\n  partnerToken: masked-example-value\n")
        write_text(repo_root / "docs" / "tutorials" / "runtime-values.md", "Folded YAML examples in docs remain placeholder-only.\n")
        _commit_current_state(git_factory, repo_root, "c003 add masked docs example")
        write_text(repo_root / "ops" / "runtime" / "runtime-values.yaml", "runtime:\n  partnerToken: masked-reference-only\n")
        _commit_current_state(git_factory, repo_root, "c004 remove live secret from head")
    else:
        write_text(repo_root / "ops" / "keys" / "service-a.pem", PRIVATE_KEY_BLOCK_A_REWRAPPED)
        _commit_current_state(git_factory, repo_root, "c002 add PEM A")
        write_text(repo_root / "ops" / "keys" / "service-a.pem", PRIVATE_KEY_BLOCK_A)
        _commit_current_state(git_factory, repo_root, "c003 formatting change")
        if (repo_root / "ops" / "keys" / "service-a.pem").exists():
            (repo_root / "ops" / "keys" / "service-a.pem").unlink()
        write_text(repo_root / "ops" / "keys" / "service-b.pem", PRIVATE_KEY_BLOCK_B)
        _commit_current_state(git_factory, repo_root, "c004 rotate to PEM B")
        write_text(repo_root / "docs" / "examples" / "pem-reference.md", "-----BEGIN PRIVATE KEY-----\nexample\n")
        _commit_current_state(git_factory, repo_root, "c005 docs example PEM")
        write_text(repo_root / "app" / "security" / "rotation_state.py", "def state() -> str:\n    return 'rotated-b'\n")
        _commit_current_state(git_factory, repo_root, "c006 safe cleanup")
    return {}


def _build_negative_repo(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _populate_python_common(repo_root, scenario)
    if scenario.family == "negative_docs":
        if scenario.id == "N-V7-DOCS-005":
            write_text(repo_root / "docs" / "tutorials" / "quickstart.md", "export const apiToken = 'sample-token-only';\nverify=false appears in fenced docs only.\n")
            write_text(repo_root / "examples" / "quickstart" / ".env.sample", "NOTIFICATION_TOKEN=example-value\n")
            write_text(repo_root / "docs" / "snippets" / "tls.md", "client = requests.get(url, verify=False)  # tutorial snippet only\n")
        elif scenario.id == "N-V7-DOCS-006":
            write_text(repo_root / "docs" / "certs" / "public-chain.pem", PUBLIC_CERT_CHAIN)
            write_text(repo_root / "examples" / "csr" / "service.csr", CSR_SAMPLE)
            write_text(repo_root / "docs" / "pki" / "rotation.md", "Public chain and CSR examples live here; no private key material is shipped.\n")
        elif scenario.id == "N-V7-DOCS-009":
            write_text(repo_root / "docs" / "runbooks" / "masked-values.md", "ghp_xxxxMASKEDxxxx1234 and sk_live_example_only_placeholder are masked docs examples.\n")
            write_text(repo_root / "examples" / "placeholders" / "values.env", "API_TOKEN=example-only-placeholder\n")
            write_text(repo_root / "docs" / "tutorials" / "entropy.md", "High-entropy-looking strings in docs stay non-live by design.\n")
        elif scenario.id == "N-V7-DOCS-010":
            write_text(repo_root / "docs" / "jwks" / "jwks.json", '{\"keys\":[{\"kty\":\"RSA\",\"kid\":\"sample-key\",\"use\":\"sig\"}]}\n')
            write_text(repo_root / "docs" / "csr" / "service.csr", CSR_SAMPLE)
            write_text(repo_root / "docs" / "pem" / "public.pem", PUBLIC_CERT_CHAIN)
        elif scenario.id == "N-V7-DOCS-013":
            write_text(repo_root / "docs" / "tutorials" / "masked-values.md", "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example.signature\n")
            write_text(repo_root / "docs" / "jwt" / "examples.md", "Use only masked JWT examples and public claims in tutorials.\n")
            write_text(repo_root / "docs" / "pem" / "public-chain.pem", PUBLIC_CERT_CHAIN)
        else:
            write_text(repo_root / "docs" / "runbooks" / "samples.md", "Token example: token=example-value\nverify=false is a documentation string only\n")
    elif scenario.family == "negative_vendor":
        if scenario.id == "N-V7-VENDOR-007":
            write_text(repo_root / "vendor" / "bundle.min.js", "var a='md5 demo text';var b='NODE_TLS_REJECT_UNAUTHORIZED=0';var c='-----BEGIN PRIVATE KEY----- docs';\n")
            write_text(repo_root / "generated" / "openapi" / "client.ts", "export const insecureExample = 'rejectUnauthorized false';\n")
            write_text(repo_root / "package-lock.json", "{\"packages\":{\"\":{\"integrity\":\"sha512-placeholder-integrity-value-only\"}}}\n")
        elif scenario.id == "N-V7-VENDOR-011":
            write_text(repo_root / "vendor" / "bundle.min.js", "var a='md5 demo text';var b='NODE_TLS_REJECT_UNAUTHORIZED=0';var c='-----BEGIN PRIVATE KEY----- docs';\n")
            write_text(repo_root / "generated" / "openapi" / "client.ts", "export const generatedExample = 'rejectUnauthorized false';\n")
            write_text(repo_root / "generated" / "swagger" / "openapi.json", '{\"openapi\":\"3.0.0\",\"info\":{\"title\":\"Generated Client\"}}\n')
            write_text(repo_root / "pnpm-lock.yaml", "lockfileVersion: '9.0'\npackages:\n  /demo/1.0.0:\n    resolution: {integrity: sha512-placeholder-only}\n")
        elif scenario.id == "N-V7-VENDOR-014":
            write_text(repo_root / "vendor" / "app.min.js", "var a='md5 example';var b='rejectUnauthorized false';var c='-----BEGIN PRIVATE KEY----- example';\n")
            write_text(repo_root / "dist" / "app.min.js.map", "{\"version\":3,\"file\":\"app.min.js\",\"sources\":[\"generated/client.ts\"]}\n")
            write_text(repo_root / "generated" / "client" / "sdk.ts", "export const clientExample = 'NODE_TLS_REJECT_UNAUTHORIZED=0';\n")
            write_text(repo_root / "pnpm-lock.yaml", "lockfileVersion: '9.0'\npackages:\n  /client/1.0.0:\n    resolution: {integrity: sha512-placeholder-only}\n")
        else:
            write_text(repo_root / "vendor" / "bundle.js", "var sample='md5 example text'; var tls='rejectUnauthorized false text';\n")
            write_text(repo_root / "generated" / "client.ts", "export const sample = 'AES/ECB example';\n")
    elif scenario.family == "negative_tests":
        write_text(repo_root / "fixtures" / "tokens.json", '{"token":"example-value","certificate":"-----BEGIN PRIVATE KEY----- example"}\n')
        write_text(repo_root / "mocks" / "certificates" / "mock.pem", "-----BEGIN PRIVATE KEY-----\nexample\n")
        if scenario.id == "N-V7-TESTS-015":
            write_text(repo_root / "tests" / "fixtures" / "nested" / "tokens.env", "SERVICE_TOKEN=example-only-placeholder\n")
            write_text(repo_root / "tests" / "fixtures" / "nested" / "certs" / "fixture.pem", "-----BEGIN PRIVATE KEY-----\nfixture-only\n")
            write_text(repo_root / "mocks" / "nested" / "responses" / "payload.json", '{"jwt":"eyJhbGciOiJIUzI1NiJ9.example.signature"}\n')
    elif scenario.family == "negative_safe":
        if scenario.id == "N-V7-SAFE-008":
            write_text(repo_root / "app" / "security" / "masked_values.py", "MASKED_TOKEN = 'ghp_xxxxMASKEDxxxx1234'\nPUBLIC_SAMPLE = 'sk_live_example_only_placeholder'\n")
            write_text(repo_root / "app" / "security" / "placeholder_env.py", "def runtime_locator() -> str:\n    return 'vault://example/runtime-token'\n")
            write_text(repo_root / "docs" / "safe-placeholders.md", "Use ONLY masked examples like ghp_xxxxMASKEDxxxx1234 in docs and runbooks.\n")
        elif scenario.id == "N-V7-SAFE-012":
            write_text(repo_root / "app" / "security" / "vault_reference.py", "def runtime_locator() -> str:\n    return 'vault://platform/runtime-token'\n")
            write_text(repo_root / "app" / "security" / "scary_safe_tls.py", "def tls_profile() -> dict[str, bool]:\n    return {'verify': True}\n")
            write_text(repo_root / "docs" / "wrapper-safety.md", "Scary naming and vault refs remain safe when runtime values are externalized.\n")
        elif scenario.id == "N-V7-SAFE-016":
            write_text(repo_root / "app" / "security" / "vault_reference.py", "def runtime_locator() -> str:\n    return 'vault://payments/runtime-secret'\n")
            write_text(repo_root / "app" / "security" / "safe_trustall_wrapper.py", "def tls_options() -> dict[str, bool]:\n    return {'verify': True}\n")
            write_text(repo_root / "docs" / "runtime-safety.md", "Scary names, vault references, and safe wrappers are intentionally non-live here.\n")
        else:
            write_text(repo_root / "app" / "security" / "secure_hashing.py", "import hashlib\n\ndef digest(value: bytes) -> str:\n    return hashlib.sha256(value).hexdigest()\n")
            write_text(repo_root / "app" / "security" / "secure_tls.py", "def verify_enabled() -> bool:\n    return True\n")
            write_text(repo_root / "app" / "security" / "secure_key_loader.py", "def key_reference() -> str:\n    return 'vault://platform/key'\n")
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, f"bootstrap {scenario.id}")
    return {}


def _build_mixed_monorepo(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _write_common_root_files(repo_root, scenario)
    java_root = repo_root / "services" / "platform-java"
    python_root = repo_root / "workers" / "sync-worker"
    node_root = repo_root / "apps" / "admin-api"
    _populate_java_common(java_root, _scenario_clone(scenario, "platform-java"))
    _populate_python_common(python_root, _scenario_clone(scenario, "sync-worker"))
    _populate_node_common(node_root, _scenario_clone(scenario, "admin-api"))
    write_text(java_root / "src" / "main" / "resources" / "application-prod.yml", "oauth:\n  client-secret: LiveSecretX9aK4mP1cQ7zR2vW\n")
    write_text(python_root / "app" / "security" / "runtime_secret.py", f'RUNTIME_SECRET = "{GENERIC_SECRET_GOLF}"\n')
    write_text(repo_root / "shared" / "config" / "keys" / "platform_service.pem", PRIVATE_KEY_BLOCK_A)
    package_name = _package_name("platform-java")
    package_root = ensure_dir(_package_dir(java_root, package_name))
    write_text(package_root / "security" / "LegacyCipherService.java", f"package {package_name}.security;\nimport javax.crypto.Cipher;\npublic class LegacyCipherService {{ public Cipher cipher() throws Exception {{ return Cipher.getInstance(\"AES/ECB/PKCS5Padding\"); }} }}\n")
    write_text(node_root / "src" / "modules" / "security" / "legacyDigest.ts", "import { createHash } from 'crypto';\nexport function digest(value: string): string { return createHash('md5').update(value).digest('hex'); }\n")
    write_text(python_root / "app" / "clients" / "insecure_partner.py", "import requests\n\ndef fetch_payload(url: str) -> str:\n    return requests.get(url, verify=False, timeout=5).text\n")
    if scenario.id in {"M-V8-003", "M-V8-005", "M-V8-007", "M-V8-009", "M-V8-011", "M-V8-012"}:
        write_text(repo_root / "shared" / "config" / "keys" / "mesh_service.pem", PRIVATE_KEY_BLOCK_B)
        write_text(repo_root / "vendor" / "third-party-sdk.js", "var secret='example-only'; var weak='md5 example';\n")
        write_text(repo_root / "generated" / "openapi" / "mesh-client.ts", "export const generatedExample = 'verify=false';\n")
        write_text(repo_root / "packages" / "shared-fixtures" / "seed.json", '{"token":"fixture-only","tls":"rejectUnauthorized false"}\n')
        write_text(repo_root / "deploy" / "charts" / "values.yaml", "tls:\n  verify: true\n")
        write_text(repo_root / "packages" / "shared-libs" / "README.md", "# Shared libs\n\nFixtures, vendor drops, and generated clients live outside active runtime code.\n")
    if scenario.id == "M-V8-005":
        write_text(repo_root / "apps" / "portal-web" / "src" / "config" / "runtime.ts", "export const runtimeFlags = { verify: true };\n")
        write_text(repo_root / "services" / "platform-java" / "docs" / "module-boundaries.md", "Platform service keeps generated clients and vendor drops outside live request handlers.\n")
        write_text(repo_root / "generated" / "charts" / "values.yaml", "verify: false # generated example only\n")
        write_text(repo_root / "vendor" / "sdk" / "mesh-client.js", "module.exports = { note: 'vendor example only' };\n")
    elif scenario.id == "M-V8-009":
        write_text(repo_root / "services" / "platform-java" / "docs" / "payments-mesh.md", "Payments mesh docs separate live crypto paths from generated and vendor content.\n")
        write_text(repo_root / "generated" / "openapi" / "payments-client.ts", "export const generatedPaymentExample = 'md5 example only';\n")
        write_text(repo_root / "vendor" / "sdk" / "payments-sdk.js", "module.exports = { note: 'vendor example only' };\n")
    elif scenario.id == "M-V8-011":
        write_text(repo_root / "packages" / "shared-libs" / "docs" / "safe-helpers.md", "Shared helper docs remain safe while history carries one removed secret.\n")
        write_text(repo_root / "apps" / "portal-web" / "src" / "config" / "runtime.ts", "export const runtimeFlags = { verify: true };\n")
    elif scenario.id == "M-V8-012":
        write_text(node_root / "src" / "modules" / "security" / "secureTlsWrapper.ts", "export function secureTlsWrapper() { return { rejectUnauthorized: true }; }\n")
        write_text(repo_root / "generated" / "openapi" / "verify-client.ts", "export const generatedVerifyExample = 'verify=false';\n")
        write_text(repo_root / "vendor" / "sdk" / "verify-sdk.js", "module.exports = { note: 'vendor example only' };\n")
    write_text(repo_root / "scripts" / "smoke.ps1", "Write-Host 'mixed monorepo smoke ok'\n")
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, f"bootstrap {scenario.id}")
    if scenario.id == "M-V8-007":
        legacy_env = repo_root / "shared" / "config" / "legacy.env"
        write_text(legacy_env, f"LEGACY_SYNC_TOKEN={GENERIC_SECRET_CHARLIE}\n")
        _commit_current_state(git_factory, repo_root, "c002 add history-only workspace secret")
        if legacy_env.exists():
            legacy_env.unlink()
        write_text(repo_root / "docs" / "workspace-history.md", "legacy.env token was removed from head and survives only in main history.\n")
        _commit_current_state(git_factory, repo_root, "c003 remove history-only workspace secret")
        git_factory.checkout(repo_root, "feature/shared-lib-cleanup", create=True)
        write_text(repo_root / "packages" / "shared-libs" / "cleanup.md", "shared lib cleanup branch remains clean and fixture-only.\n")
        _commit_current_state(git_factory, repo_root, "c004 shared lib cleanup branch")
        git_factory.checkout(repo_root, "main")
        git_factory.checkout(repo_root, "release/2026.05", create=True)
        write_text(repo_root / "deploy" / "release-notes.md", "release branch stays clean while main retains only history truth.\n")
        _commit_current_state(git_factory, repo_root, "c005 release branch clean")
        git_factory.checkout(repo_root, "main")
    elif scenario.id == "M-V8-011":
        legacy_env = repo_root / "shared" / "config" / "legacy.env"
        write_text(legacy_env, f"LEGACY_WORKSPACE_TOKEN={GENERIC_SECRET_DELTA}\n")
        _commit_current_state(git_factory, repo_root, "c002 add workspace history secret")
        if legacy_env.exists():
            legacy_env.unlink()
        write_text(repo_root / "docs" / "workspace-history.md", "legacy.env token was removed; only history should retain it.\n")
        _commit_current_state(git_factory, repo_root, "c003 remove workspace history secret")
        git_factory.checkout(repo_root, "feature/shared-lib-cleanup", create=True)
        write_text(repo_root / "packages" / "shared-libs" / "cleanup.md", "shared lib cleanup remains safe\n")
        _commit_current_state(git_factory, repo_root, "c004 shared lib cleanup branch")
        git_factory.checkout(repo_root, "main")
        git_factory.checkout(repo_root, "release/2026.05", create=True)
        write_text(repo_root / "deploy" / "release-notes.md", "release branch remains clean and doc-only.\n")
        _commit_current_state(git_factory, repo_root, "c005 release branch clean")
        git_factory.checkout(repo_root, "main")
    return {}


def _build_mixed_infra(repo_root: Path, scenario: ScenarioSpec, git_factory: GitFactory) -> dict[str, Any]:
    _write_common_root_files(repo_root, scenario)
    _populate_python_common(repo_root, scenario)
    console_root = repo_root / "ops" / "console"
    _populate_node_common(console_root, _scenario_clone(scenario, "console"))
    write_text(repo_root / "app" / "config" / "production.env", "APP_SECRET=0123456789ABCDEFA31a\n")
    write_text(repo_root / "deploy" / "envoy.yaml", "tls_minimum_protocol_version: TLSv1_0\ntrust_chain_verification: ACCEPT_UNTRUSTED\n")
    write_text(console_root / "src" / "modules" / "security" / "legacyDigest.ts", "import { createHash } from 'crypto';\nexport function digest(value: string): string { return createHash('md5').update(value).digest('hex'); }\n")
    if scenario.id in {"M-V8-004", "M-V8-006", "M-V8-008", "M-V8-010"}:
        write_text(repo_root / "deploy" / "examples" / "envoy.yaml", "trust_chain_verification: ACCEPT_UNTRUSTED\n")
        write_text(repo_root / "kustomize" / "fixtures" / "dev.env", "NODE_TLS_REJECT_UNAUTHORIZED=0\n")
        write_text(repo_root / "terraform" / "modules" / "edge" / "variables.tf", 'variable "tls_profile" { default = "modern" }\n')
        write_text(repo_root / ".github" / "workflows" / "deploy.yml", "name: deploy\non: [push]\njobs:\n  deploy:\n    runs-on: ubuntu-latest\n    steps:\n      - run: echo deploy\n")
        write_text(repo_root / "helm" / "control-plane" / "values.yaml", "envoy:\n  trustChainVerification: STRICT\n")
    if scenario.id == "M-V8-006":
        write_text(repo_root / "kustomize" / "overlays" / "staging" / "kustomization.yaml", "resources:\n  - ../../base\n")
        write_text(repo_root / "terraform" / "environments" / "prod" / "main.tf", 'module "edge" { source = "../../modules/edge" }\n')
        write_text(repo_root / "docs" / "infra" / "overlay-matrix.md", "Examples and fixture overlays remain dormant while deploy/envoy.yaml drives runtime policy.\n")
    elif scenario.id == "M-V8-008":
        write_text(repo_root / "docs" / "examples" / "tls-hotfix.md", "Example rejectUnauthorized snippets remain dormant and non-runtime.\n")
        write_text(repo_root / "generated" / "manifests" / "envoy-example.yaml", "trust_chain_verification: ACCEPT_UNTRUSTED # generated example only\n")
        write_text(repo_root / "ops" / "runbooks" / "branch-hotfix.md", "Feature branch carries the Guardian secret while main keeps the live config misuse.\n")
    elif scenario.id == "M-V8-010":
        write_text(repo_root / "generated" / "manifests" / "envoy-example.yaml", "trust_chain_verification: ACCEPT_UNTRUSTED # generated example only\n")
        write_text(repo_root / "kustomize" / "overlays" / "prod" / "kustomization.yaml", "resources:\n  - ../../base\n")
        write_text(repo_root / "docs" / "infra" / "discovery-wave.md", "Generated manifests and dormant overlays remain non-runtime beside deploy/envoy.yaml.\n")
    write_text(repo_root / "scripts" / "smoke.ps1", "Write-Host 'infra mixed smoke ok'\n")
    _inflate_repository(repo_root, scenario)
    git_factory.init(repo_root)
    _commit_current_state(git_factory, repo_root, "c001 bootstrap mixed repo")
    git_factory.checkout(repo_root, "feature/hotfix-ssl", create=True)
    write_text(repo_root / "ops" / "hotfix" / "feature-secret.txt", "FEATURE_SECRET=Ab9K2mQ7pL4xR8nT5vW1Yz7Ck3Hs6Fq2\n")
    _commit_current_state(git_factory, repo_root, "c002 temporary hotfix secret")
    git_factory.checkout(repo_root, "main")
    git_factory.checkout(repo_root, "release/2026.04", create=True)
    write_text(repo_root / "ops" / "release-notes.md", "release branch clean\n")
    _commit_current_state(git_factory, repo_root, "c003 release branch clean")
    git_factory.checkout(repo_root, "main")
    if scenario.id in {"M-V8-004", "M-V8-006", "M-V8-008", "M-V8-010"}:
        git_factory.checkout(repo_root, "feature/charts-cleanup", create=True)
        write_text(repo_root / "ops" / "charts" / "README.md", "charts cleanup branch stays clean\n")
        _commit_current_state(git_factory, repo_root, "c004 charts cleanup branch")
        git_factory.checkout(repo_root, "main")
    return {}


def materialize_scenario(config: LabConfig, scenario: ScenarioSpec, git_factory: GitFactory) -> tuple[Path, dict[str, Any]]:
    repo_root = config.repositories_root / scenario.repo_name
    if repo_root.exists():
        safe_rmtree(repo_root, config.repositories_root)
    ensure_dir(repo_root)
    if scenario.family in {"guardian_live_java", "quantum_crypto_java", "quantum_tls_java", "quantum_tls_java_config"}:
        builder_metadata = _build_java_repo(repo_root, scenario, git_factory)
    elif scenario.family == "guardian_history_java":
        builder_metadata = _build_guardian_history_java(repo_root, scenario, git_factory)
    elif scenario.family in {"guardian_live_python", "quantum_crypto_python", "quantum_tls_python"}:
        builder_metadata = _build_python_repo(repo_root, scenario, git_factory)
    elif scenario.family == "guardian_history_python":
        builder_metadata = _build_guardian_history_python(repo_root, scenario, git_factory)
    elif scenario.family in {"guardian_live_node", "quantum_crypto_node", "quantum_tls_node"}:
        builder_metadata = _build_node_repo(repo_root, scenario, git_factory)
    elif scenario.family == "guardian_history_node":
        builder_metadata = _build_guardian_history_node(repo_root, scenario, git_factory)
    elif scenario.family in {"guardian_live_config", "quantum_tls_config"}:
        builder_metadata = _build_config_repo(repo_root, scenario, git_factory)
    elif scenario.family == "quantum_crypto_go":
        builder_metadata = _build_go_repo(repo_root, scenario, git_factory)
    elif scenario.family in {"quantum_crypto_csharp", "quantum_tls_csharp"}:
        builder_metadata = _build_csharp_repo(repo_root, scenario, git_factory)
    elif scenario.family.startswith("negative_"):
        builder_metadata = _build_negative_repo(repo_root, scenario, git_factory)
    elif scenario.family == "mixed_monorepo":
        builder_metadata = _build_mixed_monorepo(repo_root, scenario, git_factory)
    elif scenario.family == "mixed_infra_repo":
        builder_metadata = _build_mixed_infra(repo_root, scenario, git_factory)
    else:
        raise ValueError(f"Unsupported scenario family: {scenario.family}")

    repo_metadata = {
        "scenarioId": scenario.id,
        "repoName": scenario.repo_name,
        "lineCount": count_lines(repo_root),
        "git": git_factory.manifest(repo_root),
        "builderMetadata": builder_metadata,
    }
    write_json(repo_root / "validation" / "repo-metadata.json", repo_metadata)
    _write_validation_files(repo_root, scenario, repo_metadata)
    return repo_root, repo_metadata
