from __future__ import annotations

import hashlib
import random
import re
import textwrap
import warnings
from functools import lru_cache
from pathlib import Path
from typing import Any

import rstr
import yaml


_RULES_ROOT = Path(__file__).resolve().parents[3] / "ARQV2" / "ARQBackend" / "arq-engine-lib" / "src" / "main" / "resources" / "rules"

_GUARDIAN_BASELINE_COVERED = {"guardian.generic-api-key", "guardian.private-key"}
_QUANTUM_BASELINE_COVERED = {
    "quantum.arq-q-0012-java",
    "quantum.arq-q-0013-java",
    "quantum.arq-q-0026-java",
    "quantum.arq-q-0072-java",
    "quantum.arq-q-0082-java",
    "quantum.arq-q-0085-java",
    "quantum.arq-q-0131-java",
    "quantum.arq-q-0178-java",
    "quantum.arq-q-0247-python",
    "quantum.arq-q-0248-python",
    "quantum.arq-q-0260-python",
    "quantum.arq-q-0305-python",
    "quantum.arq-q-0418-csharp",
    "quantum.arq-q-0449-csharp",
    "quantum.arq-q-0453-csharp",
    "quantum.arq-q-0468-csharp",
    "quantum.arq-q-0488-csharp",
    "quantum.arq-q-0572-go",
    "quantum.arq-q-0573-go",
    "quantum.arq-q-0611-typescript",
    "quantum.arq-q-0613-typescript",
    "quantum.arq-q-0614-typescript",
    "quantum.arq-q-0930-config",
    "quantum.arq-q-0931-config",
    "quantum.arq-q-0949-config",
}

_NATIVE_LANGS = {
    "abap",
    "c",
    "cpp",
    "elixir",
    "erlang",
    "groovy",
    "jcl",
    "kotlin",
    "lua",
    "objectivec",
    "perl",
    "php",
    "plsql",
    "powershell",
    "ruby",
    "rust",
    "scala",
    "shell",
    "swift",
    "tsql",
    "zig",
}

_LANGUAGE_EXTENSIONS = {
    "abap": "abap",
    "c": "c",
    "config": "conf",
    "cpp": "cpp",
    "csharp": "cs",
    "elixir": "ex",
    "erlang": "erl",
    "go": "go",
    "groovy": "groovy",
    "java": "java",
    "javascript": "js",
    "jcl": "jcl",
    "kotlin": "kt",
    "lua": "lua",
    "objectivec": "m",
    "perl": "pl",
    "php": "php",
    "plsql": "sql",
    "powershell": "ps1",
    "python": "py",
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala",
    "shell": "sh",
    "swift": "swift",
    "tsql": "sql",
    "typescript": "ts",
    "zig": "zig",
}

_PEM_BLOB = "\n".join(
    [
        "-----BEGIN PRIVATE KEY-----",
        "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX",
        "g+3t4xO4X8xX2m8nQd0kY3Y8uQmP5sJY3fSxD8kM1rVx3fB6c7yQ8mJk2mN7pQ2Z",
        "zM8Y0fG4oM4uVnD3dZqN4y0oA1oZ9xL3mXhN7dV4tR1pX7sQ2mK9wW8pF6kJ4mQ3",
        "cH9xT2pR8mJ7sL0qW6nV5zP4yR3kM8uN1pX6tQ2mB9cD8fG7hJ6kL5nM4pQ3rS2t",
        "Q2dGmP4sN9vW1xY5zA8bC7dE6fG5hJ4kL3mN2pQ1rS0tU9vW8xY7zQ6rT5uV4wX3",
        "Y2zA1bC0dE9fG8hJ7kL6mN5pQ4rS3tU2vW1xY0zA9bC8dE7fG6hJ5kL4mN3pQ2rS",
        "AgMBAAECggEAJx5u8s0Qm2kL4vN6xP8rT1yW3zA5cE7gH9jK2mN4pQ6rS8tV0xY2z",
        "Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU",
        "-----END PRIVATE KEY-----",
    ]
)

_CERT_BLOB = "\n".join(
    [
        "-----BEGIN CERTIFICATE-----",
        "MIIDdzCCAl+gAwIBAgIUXYPublicChainOnly000000000000000000MA0GCSqGSIb3",
        "DQEBCwUAMFoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMx",
        "FTATBgNVBAsMDEFycSBTYWZlIFBLSTEUMBIGA1UEAwwLZXhhbXBsZS5sb2NhbDAe",
        "Fw0yNjAzMzEwMDAwMDBaFw0zNjAzMjkwMDAwMDBaMFoxCzAJBgNVBAYTAlVTMRYw",
        "FAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMxFTATBgNVBAsMDEFycSBTYWZlIFBLSTEU",
        "MBIGA1UEAwwLZXhhbXBsZS5sb2NhbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC",
        "AQoCggEBALD3u7xS3afe4Lacertchainonlyblock7rJb3Bv7H4qXyD9Xv6m3L7m0s",
        "2V7D5P82C0tD8yM1mL0vN2fQ3sJ8hK6pR4wT7yN3fV5qB2dL9cT1vH6mP0xZ4nQ3sF",
        "8kM2pR7tV1yQ9dM6cJ2pN5wR8hV3mL6qT0yC9fK2sN5bR8xW1vQ4dP7kL0mN3sH6tY",
        "9pQ20C0fA6pL9vQ5nT2rW8mK4dS1yF6qP3xV0bL7cN2hR5mJ8wK6tQ1xZ4nM7vP0s",
        "C3fK6mR9tV2yW5pL8nQ1dH4sJ7xC0vB3mN6pR9tY2wF5hK8dL1qS4vN7xC0bP3mT6",
        "yR9w0CAwEAAaNTMFEwHQYDVR0OBBYEFO9PublicChainOnly000000000000000000",
        "MB8GA1UdIwQYMBaAFO9PublicChainOnly000000000000000000MA8GA1UdEwEB",
        "/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAG1chainonlysample4Lh8fQ2mV7",
        "dP0xN5rK8sT1yW4pL7mQ0dF3hJ6kL9vC2xZ5nM8qR1tY4wF7hK0dL3qS6vN9xC2bP",
        "4mT7yR0wQ3pD6fG9hJ2kL5nQ8tV1yC4mR7pL0x",
        "-----END CERTIFICATE-----",
    ]
)

_RSA_PRIVATE_BLOB = "\n".join(
    [
        "-----BEGIN RSA PRIVATE KEY-----",
        "MIIEpAIBAAKCAQEA1c0fCoverageCampaignOnly000000000000000000000000000",
        "f2x8mY2xB5zP4gH9kL2mN5pQ8rS1tU4vW7xY0zA3bC6dE9fG2hJ5kL8mN1pQ4rS7t",
        "U0vW3xY6zA9bC2dE5fG8hJ1kL4mN7pQ0rS3tU6vW9xY2zA5bC8dE1fG4hJ7kL0mN3",
        "-----END RSA PRIVATE KEY-----",
    ]
)

_EC_PRIVATE_BLOB = "\n".join(
    [
        "-----BEGIN EC PRIVATE KEY-----",
        "MHcCAQEEICoverageCampaignOnlyECKey00000000000000000000000000000000",
        "oAoGCCqGSM49AwEHoUQDQgAEz7Q4nN8mL2pR6tV0xY4zC8fG1jK5mN9qR3tW7xA1b",
        "C5dE9hJ2kL6nP0rS4tV8xY2zA6bC0dE4fG8hJ1kL5mN9pQ3rS7tU1vW5xY9zA3bC7",
        "-----END EC PRIVATE KEY-----",
    ]
)

_OPENSSH_PRIVATE_BLOB = "\n".join(
    [
        "-----BEGIN OPENSSH PRIVATE KEY-----",
        "b3BlbnNzaC1rZXktdjEAAAAAcoveragecampaignonlyopensshprivatekeyAAAAAA",
        "AAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcnNhAAAAAwEAAQAAAIEA0Coverage",
        "campaignOnlyOpenSshKey0000000000000000000000000000000000000000000",
        "-----END OPENSSH PRIVATE KEY-----",
    ]
)

_ENCRYPTED_PRIVATE_BLOB = "\n".join(
    [
        "-----BEGIN ENCRYPTED PRIVATE KEY-----",
        "MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQICoveragecampaignonly",
        "MBAgMBgqhiQIBAzANBgkqhkiG9w0BAQEFAASCBMBCoverageCampaignEncryptedKey",
        "-----END ENCRYPTED PRIVATE KEY-----",
    ]
)

_PUBLIC_KEY_BLOB = "\n".join(
    [
        "-----BEGIN PUBLIC KEY-----",
        "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtCoverageCampaignPublic",
        "KeyOnly0000000000000000000000000000000000000000000000000000000000",
        "-----END PUBLIC KEY-----",
    ]
)

_HEX_LOWER = "0123456789abcdef"
_ALNUM_LOWER = "abcdefghijklmnopqrstuvwxyz0123456789"
_ALNUM_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
_ALNUM_MIXED = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
_BASE64ISH = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
_WORD_SAFE = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
_WORD_SAFE_EXT = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_=.-"
_PERCENT_SAFE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%"
_FLUTTERWAVE_SAFE = "abcdefgh0123456789"


def _seeded_chars(seed: str, length: int, alphabet: str) -> str:
    chars: list[str] = []
    counter = 0
    while len(chars) < length:
        digest = hashlib.sha256(f"{seed}:{counter}".encode("utf-8")).digest()
        counter += 1
        for byte in digest:
            chars.append(alphabet[byte % len(alphabet)])
            if len(chars) == length:
                break
    return "".join(chars)


_GUARDIAN_SAMPLE_OVERRIDES = {
    "guardian.1password-service-account-token": "ops_eyJ" + _seeded_chars("guardian.1password-service-account-token", 250, _BASE64ISH),
    "guardian.adobe-client-secret": "p8e-" + _seeded_chars("guardian.adobe-client-secret", 32, _HEX_LOWER),
    "guardian.airtable-personnal-access-token": "patalmunalmunalmu" + "." + _seeded_chars("guardian.airtable-personnal-access-token.hex", 64, _HEX_LOWER),
    "guardian.alibaba-access-key-id": "LTAI" + _seeded_chars("guardian.alibaba-access-key-id", 20, _ALNUM_UPPER),
    "guardian.atlassian-api-token": "atlassian = ATATT3" + _seeded_chars("guardian.atlassian-api-token", 186, _ALNUM_UPPER),
    "guardian.authress-service-client-access-key": "sc_alpha12.beta1.acc-tenant-prod01." + ("a" * 40),
    "guardian.aws-access-key": "AKIA" + ("A" * 16),
    "guardian.aws-amazon-bedrock-api-key-long-lived": "ABSK" + _seeded_chars("guardian.aws-amazon-bedrock-api-key-long-lived", 109, _BASE64ISH),
    "guardian.aws-secret-key": 'aws_secret="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcd"',
    "guardian.cloudflare-origin-ca-key": "v1.0-" + _seeded_chars("guardian.cloudflare-origin-ca-key.a", 24, _HEX_LOWER) + "-" + _seeded_chars("guardian.cloudflare-origin-ca-key.b", 146, _HEX_LOWER),
    "guardian.curl-auth-header": 'curl -H "Authorization: Bearer testtoken12345678" https://example.internal',
    "guardian.curl-auth-user": 'curl -u "svcuser:supersecret42" https://example.internal',
    "guardian.doppler-api-token": "dp.pt." + _seeded_chars("guardian.doppler-api-token", 43, _ALNUM_LOWER),
    "guardian.dropbox-short-lived-api-token": "dropbox_token = sl." + ("a" * 135),
    "guardian.duffel-api-token": "duffel_test_" + _seeded_chars("guardian.duffel-api-token", 43, "abcdefghijklmnopqrstuvwxyz0123456789_-="),
    "guardian.dynatrace-api-token": "dt0c01." + _seeded_chars("guardian.dynatrace-api-token.a", 24, _ALNUM_LOWER) + "." + _seeded_chars("guardian.dynatrace-api-token.b", 64, _ALNUM_LOWER),
    "guardian.easypost-api-token": "EZAK" + _seeded_chars("guardian.easypost-api-token", 54, _ALNUM_LOWER),
    "guardian.easypost-test-api-token": "EZTK" + _seeded_chars("guardian.easypost-test-api-token", 54, _ALNUM_LOWER),
    "guardian.facebook-page-access-token": "EAAM" + _seeded_chars("guardian.facebook-page-access-token", 100, _ALNUM_MIXED),
    "guardian.flutterwave-encryption-key": "FLWSECK_TEST-abcdef12a0bc",
    "guardian.flutterwave-public-key": "FLWPUBK_TEST-" + ("a" * 32) + "-X",
    "guardian.flutterwave-secret-key": "FLWSECK_TEST-" + _seeded_chars("guardian.flutterwave-secret-key", 32, _FLUTTERWAVE_SAFE) + "-X",
    "guardian.frameio-api-token": "fio-u-" + ("a" * 64),
    "guardian.freemius-secret-key": '"secret_key" => "sk_' + _seeded_chars("guardian.freemius-secret-key", 29, _WORD_SAFE) + '"',
    "guardian.generic-secret": 'secret_key = "abcdefghijklmnop"',
    "guardian.gocardless-api-token": "gocardless = live_" + ("a" * 40),
    "guardian.hashicorp-tf-password": 'administrator_login_password = "' + _seeded_chars("guardian.hashicorp-tf-password", 18, "abcdefghijklmnopqrstuvwxyz0123456789_-=") + '"',
    "guardian.intra42-client-secret": "s-s4t2ud-" + _seeded_chars("guardian.intra42-client-secret", 64, _HEX_LOWER),
    "guardian.kubernetes-secret-yaml": "\n".join(
        [
            "apiVersion: v1",
            "kind: Secret",
            "metadata:",
            "  name: runtime-secrets",
            "type: Opaque",
            "data:",
            '  token: "' + _seeded_chars("guardian.kubernetes-secret-yaml", 32, _BASE64ISH) + '"',
        ]
    ),
    "guardian.linear-api-key": "lin_api_" + _seeded_chars("guardian.linear-api-key", 40, _ALNUM_LOWER),
    "guardian.nuget-config-password": '<add key="ClearTextPassword" value="NugetPass' + _seeded_chars("guardian.nuget-config-password", 10, _ALNUM_MIXED) + '!" />',
    "guardian.openshift-user-token": "sha256~" + _seeded_chars("guardian.openshift-user-token", 43, _WORD_SAFE),
    "guardian.pkcs12-file": "FAKE-PKCS12-COVERAGE-BLOB",
    "guardian.planetscale-api-token": "pscale_tkn_" + _seeded_chars("guardian.planetscale-api-token", 32, _WORD_SAFE_EXT),
    "guardian.planetscale-password": "pscale_pw_" + _seeded_chars("guardian.planetscale-password", 32, _WORD_SAFE_EXT),
    "guardian.postman-api-token": "PMAK-" + _seeded_chars("guardian.postman-api-token.a", 24, _HEX_LOWER) + "-" + _seeded_chars("guardian.postman-api-token.b", 34, _HEX_LOWER),
    "guardian.sendgrid-api-token": "SG." + _seeded_chars("guardian.sendgrid-api-token", 66, _WORD_SAFE_EXT),
    "guardian.sendinblue-api-token": "xkeysib-" + _seeded_chars("guardian.sendinblue-api-token.a", 64, _HEX_LOWER) + "-" + _seeded_chars("guardian.sendinblue-api-token.b", 16, _ALNUM_LOWER),
    "guardian.sentry-org-token": "sntrys_eyJpYXQiO" + _seeded_chars("guardian.sentry-org-token.a", 24, _BASE64ISH) + "InJlZ2lvbl91cmwi" + _seeded_chars("guardian.sentry-org-token.b", 24, _BASE64ISH) + "_" + _seeded_chars("guardian.sentry-org-token.c", 43, _BASE64ISH),
    "guardian.sidekiq-sensitive-url": "https://deadbeef:cafebabe@gems.contribsys.com",
    "guardian.slack-config-access-token": "xoxe.xoxb-1-" + _seeded_chars("guardian.slack-config-access-token", 163, _ALNUM_UPPER),
    "guardian.slack-config-refresh-token": "xoxe-1-" + _seeded_chars("guardian.slack-config-refresh-token", 146, _ALNUM_UPPER),
    "guardian.slack-webhook-url": "https://hooks.slack.com/services/" + ("A" * 43),
    "guardian.squarespace-access-token": "squarespace = 12345678-1234-1234-1234-123456789abc",
    "guardian.stripe-access-token": "stripe = sk_test_" + _seeded_chars("guardian.stripe-access-token", 24, _ALNUM_MIXED),
    "guardian.stripe-live-secret-key": "sk_live_" + ("A" * 24),
    "guardian.sumologic-access-id": "sumo = suABCDEFGHIJKL",
    "guardian.sumologic-access-token": "sumo = " + _seeded_chars("guardian.sumologic-access-token", 64, _ALNUM_LOWER),
    "guardian.telegram-bot-api-token": "telegr = 123456:A" + _seeded_chars("guardian.telegram-bot-api-token", 34, "abcdefghijklmnopqrstuvwxyz0123456789_-"),
    "guardian.travisci-access-token": "travis = " + _seeded_chars("guardian.travisci-access-token", 22, _ALNUM_LOWER),
    "guardian.twilio-api-key": "SK" + _seeded_chars("guardian.twilio-api-key", 32, "0123456789abcdefABCDEF"),
    "guardian.twitch-api-token": "twitch = " + _seeded_chars("guardian.twitch-api-token", 30, _ALNUM_LOWER),
    "guardian.twitter-access-secret": "twitter = " + _seeded_chars("guardian.twitter-access-secret", 45, _ALNUM_LOWER),
    "guardian.twitter-access-token": "twitter = 123456789012345-" + _seeded_chars("guardian.twitter-access-token", 20, _ALNUM_MIXED),
    "guardian.twitter-api-key": "twitter = " + _seeded_chars("guardian.twitter-api-key", 25, _ALNUM_LOWER),
    "guardian.twitter-api-secret": "twitter = " + _seeded_chars("guardian.twitter-api-secret", 50, _ALNUM_LOWER),
    "guardian.twitter-bearer-token": "twitter = " + ("A" * 22) + ("B" * 80),
    "guardian.typeform-api-token": "typeform = tfp_" + _seeded_chars("guardian.typeform-api-token", 59, "abcdefghijklmnopqrstuvwxyz0123456789-_.="),
    "guardian.vault-batch-token": "hvb." + _seeded_chars("guardian.vault-batch-token", 138, _WORD_SAFE),
    "guardian.vault-service-token": "hvs." + _seeded_chars("guardian.vault-service-token", 90, _WORD_SAFE),
    "guardian.yandex-access-token": "yandex = t1." + _seeded_chars("guardian.yandex-access-token.a", 12, _WORD_SAFE) + "." + _seeded_chars("guardian.yandex-access-token.b", 86, _WORD_SAFE),
    "guardian.yandex-api-key": "yandex = AQVN" + _seeded_chars("guardian.yandex-api-key", 36, _WORD_SAFE),
    "guardian.yandex-aws-access-token": "yandex = YC" + _seeded_chars("guardian.yandex-aws-access-token", 38, _WORD_SAFE),
    "guardian.zendesk-secret-key": "zendesk = " + _seeded_chars("guardian.zendesk-secret-key", 40, _ALNUM_LOWER),
}


def _read_rules(name: str) -> list[dict[str, Any]]:
    path = _RULES_ROOT / f"{name}.yml"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    return payload if isinstance(payload, list) else []


def _normalized_seeded_sample(regex: str, seed: str, *, guardian: bool) -> str:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", FutureWarning)
        sample = rstr.Xeger(random.Random(seed)).xeger(regex)
    if not isinstance(sample, str):
        raise ValueError(f"Unable to generate sample for {seed}")
    sample = sample.replace("\x00", "")
    if guardian:
        return sample.strip()
    return re.sub(r"[\r\n\t\f\v]+", " ", sample).strip()


def _quantum_language(rule: dict[str, Any]) -> str:
    language = str(rule.get("language") or rule.get("metadataTags", {}).get("language") or "").strip()
    if language:
        return language
    return str(rule.get("id") or "").rsplit("-", 1)[-1]


def _guardian_path(pack_slug: str, index: int, rule_key: str = "") -> str:
    if rule_key == "guardian.pkcs12-file":
        return f"secrets/{pack_slug}/keystore/provider_{index:03d}.p12"
    if rule_key == "guardian.freemius-secret-key":
        return f"ops/{pack_slug}/secrets/provider_{index:03d}.php"
    if rule_key == "guardian.hashicorp-tf-password":
        return f"terraform/{pack_slug}/provider_{index:03d}.tf"
    if rule_key == "guardian.kubernetes-secret-yaml":
        return f"deploy/{pack_slug}/provider_{index:03d}.yaml"
    if rule_key == "guardian.nuget-config-password":
        return f"deploy/{pack_slug}/provider_{index:03d}/nuget.config"
    variants = [
        f"integrations/{pack_slug}/runtime/provider_{index:03d}.env",
        f"integrations/{pack_slug}/config/provider_{index:03d}.yaml",
        f"deploy/{pack_slug}/provider_{index:03d}.properties",
        f"terraform/{pack_slug}/provider_{index:03d}.tfvars",
        f"ops/{pack_slug}/secrets/provider_{index:03d}.txt",
    ]
    return variants[(index - 1) % len(variants)]


def _config_path(rule: dict[str, Any], pack_slug: str, index: int) -> str:
    title = str(rule.get("name") or "").lower()
    if "spring boot tls weak protocols" in title:
        return f"deploy/live/{pack_slug}/service-{index:03d}/application.properties"
    if "tomcat/jetty tls weak protocols" in title:
        return f"deploy/live/{pack_slug}/service-{index:03d}/server.xml"
    if "kubeconfig insecure skip tls verify" in title:
        return f"deploy/live/{pack_slug}/cluster-{index:03d}/kubeconfig"
    if "ios ats insecure transport exceptions" in title:
        return f"mobile/{pack_slug}/ios-{index:03d}/Info.plist"
    if "sshd weak" in title:
        return f"deploy/live/{pack_slug}/ssh-{index:03d}/sshd_config"
    if "nginx" in title:
        return f"deploy/live/{pack_slug}/nginx-{index:03d}/nginx.conf"
    if "apache" in title:
        return f"deploy/live/{pack_slug}/apache-{index:03d}/apache.conf"
    if "haproxy" in title:
        return f"deploy/live/{pack_slug}/haproxy-{index:03d}/haproxy.cfg"
    if "ingress" in title or "kube" in title or "k8s" in title:
        return f"deploy/live/{pack_slug}/k8s-{index:03d}/ingress.yaml"
    if "envoy" in title:
        return f"deploy/live/{pack_slug}/envoy-{index:03d}/envoy.yaml"
    if "spring" in title or "jvm" in title:
        return f"deploy/live/{pack_slug}/spring-{index:03d}/application.properties"
    if "ssh" in title:
        return f"deploy/live/{pack_slug}/ssh-{index:03d}/sshd_config"
    if "openssl" in title:
        return f"deploy/live/{pack_slug}/openssl-{index:03d}/openssl.cnf"
    return f"deploy/live/{pack_slug}/runtime-{index:03d}/runtime.conf"


def _manifest_like_path(language: str, pack_slug: str, index: int, rule: dict[str, Any]) -> str:
    variant = _rule_variant(rule).lower()
    ecosystem = _rule_ecosystem(rule).lower()
    title = str(rule.get("title") or "").lower()
    if language == "java" or variant.startswith("java_") or ecosystem.startswith("java") or ecosystem.startswith("jvm"):
        return f"services/{pack_slug}/module-{index:03d}/pom.xml"
    if language == "kotlin":
        return f"services/{pack_slug}/module-{index:03d}/build.gradle.kts"
    if language == "groovy":
        return f"services/{pack_slug}/module-{index:03d}/build.gradle"
    if language == "scala":
        return f"services/{pack_slug}/module-{index:03d}/build.sbt"
    if language == "csharp" or ecosystem == "nuget":
        return f"services/{pack_slug}/module-{index:03d}/Coverage.csproj"
    if language == "python" or ecosystem == "pip":
        return f"workers/{pack_slug}/module-{index:03d}/requirements.txt"
    if language in {"typescript", "javascript"} or ecosystem == "npm":
        return f"apps/{pack_slug}/module-{index:03d}/package.json"
    if language == "go" or ecosystem == "go_modules":
        return f"services/{pack_slug}/module-{index:03d}/go.mod"
    if language == "ruby" or ecosystem == "gems":
        return f"native/{pack_slug}/module-{index:03d}/Gemfile"
    if language == "php" or ecosystem == "composer":
        return f"native/{pack_slug}/module-{index:03d}/composer.json"
    if language == "rust" or ecosystem == "crates":
        return f"native/{pack_slug}/module-{index:03d}/Cargo.toml"
    if language == "erlang" or ecosystem == "hex":
        return f"native/{pack_slug}/module-{index:03d}/rebar.config"
    if language in {"c", "cpp"} or ecosystem == "liboqs":
        return f"native/{pack_slug}/module-{index:03d}/CMakeLists.txt"
    if "xml" in title or "jwt" in title or "dependency" in title:
        return f"manifests/{pack_slug}/module-{index:03d}/dependencies.txt"
    return f"manifests/{pack_slug}/module-{index:03d}/inventory.txt"


def _key_material_extension(entry: dict[str, Any]) -> str:
    values = [*_rule_keywords(entry), str(entry.get("parameter") or ""), str(entry.get("sample") or ""), str(entry.get("title") or "")]
    for value in values:
        lowered = value.lower()
        for extension in ("cer", "crt", "der", "jks", "key", "p12", "pem", "pfx"):
            if f".{extension}" in lowered or lowered.strip() == extension:
                return extension
    return "pem"


def _quantum_path(language: str, pack_slug: str, index: int, rule: dict[str, Any]) -> str:
    title = str(rule.get("title") or "").lower()
    detector_type = str(rule.get("detector_type") or "").lower()
    variant = _rule_variant(rule).lower()
    ecosystem = _rule_ecosystem(rule).lower()
    manifest_variant = variant in {
        "java_dependency_manifest",
        "java_dependency",
        "jvm_jwt_libs",
        "jvm_xmldsig_saml",
        "bc_pqc",
        "node_xmlsig",
        "thirdparty_jose",
        "go_jose_thirdparty",
        "go_pqc",
        "ruby_saml_xmldsig",
        "php_xmldsig_saml",
        "rust_pqc",
        "erlang_jose",
        "liboqs",
    }
    manifest_ecosystem = ecosystem in {
        "java_dependency_manifest",
        "java_dependency",
        "jvm",
        "npm",
        "pip",
        "nuget",
        "go_modules",
        "gems",
        "composer",
        "crates",
        "hex",
        "liboqs",
    }
    manifestish_title = (
        "dependency inventory" in title
        or "library inventory" in title
        or "pqc library inventory" in title
        or ("inventory" in title and any(token in title for token in ("jwt", "xmldsig", "saml", "ws-security", "bouncycastle", "jose", "liboqs", "openquantumsafe")))
    )
    if detector_type == "manifest" or ((manifest_variant or manifest_ecosystem) and manifestish_title):
        return _manifest_like_path(language, pack_slug, index, rule)
    if _is_quantum_key_material(rule):
        return f"secrets/{pack_slug}/keys/rule_{index:03d}.{_key_material_extension(rule)}"
    if language == "config":
        return _config_path(rule, pack_slug, index)
    extension = _LANGUAGE_EXTENSIONS.get(language, "txt")
    if language == "java":
        return f"services/{pack_slug}/src/legacy/Rule{index:03d}.java"
    if language == "csharp":
        return f"services/{pack_slug}/src/legacy/Rule{index:03d}.cs"
    if language == "python":
        return f"workers/{pack_slug}/app/legacy/rule_{index:03d}.py"
    if language == "typescript":
        return f"apps/{pack_slug}/src/legacy/rule_{index:03d}.ts"
    if language == "javascript":
        return f"apps/{pack_slug}/src/legacy/rule_{index:03d}.js"
    if language == "go":
        return f"services/{pack_slug}/internal/legacy/rule_{index:03d}.go"
    return f"native/{pack_slug}/{language}/rule_{index:03d}.{extension}"


def _comment_prefix(language: str, path: str) -> str:
    lowered = path.lower()
    if lowered.endswith((".yaml", ".yml", ".env", ".properties", ".conf", ".cfg", ".cnf", ".tfvars", ".txt", ".ps1", ".rb", ".py", ".pl", ".lua", ".abap", ".sh", ".jcl")):
        return "#"
    if lowered.endswith(".sql"):
        return "--"
    return "//"


def _rule_title(entry: dict[str, Any]) -> str:
    return str(entry.get("title") or entry.get("family") or "").strip().lower()


def _rule_family(entry: dict[str, Any]) -> str:
    return str(entry.get("family") or "").strip().lower()


def _rule_variant(entry: dict[str, Any]) -> str:
    return str(entry.get("variant") or "").strip()


def _rule_ecosystem(entry: dict[str, Any]) -> str:
    return str(entry.get("ecosystem") or "").strip()


def _rule_keywords(entry: dict[str, Any]) -> list[str]:
    keywords = entry.get("keywords")
    if not isinstance(keywords, list):
        return []
    return [str(keyword).strip() for keyword in keywords if str(keyword).strip()]


def _first_keyword(entry: dict[str, Any], default: str = "") -> str:
    keywords = _rule_keywords(entry)
    return keywords[0] if keywords else default


def _first_int(*values: Any) -> int | None:
    for value in values:
        match = re.search(r"\b(512|768|1024|2048|3072|4096|[1-9]\d{0,4})\b", str(value))
        if match:
            return int(match.group(1))
    return None


def _looks_placeholder_sample(sample: str) -> bool:
    stripped = sample.strip()
    lowered = stripped.lower()
    return not stripped or lowered in {"other", "tls", "des", "rc4", "blowfish"}


def _usable_anchor(anchor: str) -> str:
    stripped = anchor.strip()
    if not stripped:
        return ""
    if any(token in stripped for token in ("(?", "\\s", "\\S", "{0,", "[", "]", "|", "...")):
        return ""
    return stripped


def _keyword_fallback(entry: dict[str, Any], *, joiner: str = "\n", limit: int = 4) -> str:
    keywords = _rule_keywords(entry)
    if not keywords:
        return ""
    return joiner.join(keywords[:limit])


def _first_non_empty(*values: Any) -> str:
    for value in values:
        text = str(value or "").strip()
        if text and text.lower() != "other":
            return text
    return ""


def _entry_blob(entry: dict[str, Any]) -> str:
    return " ".join(
        [
            _rule_title(entry),
            _rule_family(entry),
            _rule_variant(entry),
            _rule_ecosystem(entry),
            str(entry.get("algorithm") or ""),
            str(entry.get("parameter") or ""),
            str(entry.get("evidence_anchor") or ""),
            str(entry.get("sample") or ""),
            " ".join(_rule_keywords(entry)),
        ]
    ).lower()


def _append_statement(snippet: str) -> str:
    stripped = snippet.strip()
    if not stripped:
        return stripped
    if stripped.endswith((";", "}", "]")):
        return stripped
    return stripped + ";"


def _quantum_key_material_payload(entry: dict[str, Any], extension: str = "") -> str:
    signals = " ".join(
        [
            _entry_blob(entry),
            extension,
        ]
    ).lower()
    parameter = str(entry.get("parameter") or "").strip().lower()
    anchor = str(entry.get("evidence_anchor") or "").strip().lower()
    if "begin ec private key" in parameter or "begin ec private key" in anchor:
        return _EC_PRIVATE_BLOB
    if "begin rsa private key" in parameter or "begin rsa private key" in anchor:
        return _RSA_PRIVATE_BLOB
    if "begin openssh private key" in parameter or "begin openssh private key" in anchor:
        return _OPENSSH_PRIVATE_BLOB
    if "begin encrypted private key" in parameter or "begin encrypted private key" in anchor:
        return _ENCRYPTED_PRIVATE_BLOB
    if "begin private key" in parameter or "begin private key" in anchor:
        return _PEM_BLOB
    if any(token in signals for token in ("certificate", "begin certificate", ".cer", ".crt", ".der")):
        return _CERT_BLOB
    if "public key" in signals:
        return _PUBLIC_KEY_BLOB
    if "openssh private key" in signals:
        return _OPENSSH_PRIVATE_BLOB
    if "encrypted private key" in signals:
        return _ENCRYPTED_PRIVATE_BLOB
    if "rsa private key" in signals:
        return _RSA_PRIVATE_BLOB
    if "ec private key" in signals:
        return _EC_PRIVATE_BLOB
    return _PEM_BLOB


def _is_quantum_key_material(entry: dict[str, Any]) -> bool:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "")
    return (
        "key material artifact" in title
        or "key material in repo" in title
        or "pem private key" in title
        or "private key" in title
        or "begin private key" in sample.lower()
        or "begin rsa private key" in sample.lower()
        or "begin ec private key" in sample.lower()
        or "begin openssh private key" in sample.lower()
    )


def _java_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    parameter = str(entry.get("parameter") or "").strip()
    algorithm = str(entry.get("algorithm") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    variant = _rule_variant(entry).lower()
    keywords = _rule_keywords(entry)
    keyword_blob = " ".join(keywords).lower()
    usable_anchor = _usable_anchor(anchor)
    bits = _first_int(title, sample) or 1024
    target = _first_non_empty(parameter, algorithm)
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "dependency inventory" in title:
        return parameter or sample
    if "ec weak curve" in title:
        curve = target or "prime224v1"
        return "\n".join(
            [
                'KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC");',
                f'kpg.initialize(new ECGenParameterSpec("{curve}"));',
            ]
        )
    if variant == "java_bouncycastle":
        if usable_anchor:
            return _append_statement(usable_anchor)
        bc_target = target or _first_keyword(entry, "RSA")
        if "cipher.getinstance" in anchor.lower() or "aead inventory" in title or "aes mode" in title:
            return f'Cipher.getInstance("{bc_target or "ChaCha20-Poly1305"}");'
        if "keypairgenerator" in anchor.lower() or "asymmetric keygen inventory" in title:
            return f'KeyPairGenerator.getInstance("{bc_target or "RSA"}");'
        return _append_statement(_keyword_fallback(entry, limit=2) or 'Signature.getInstance("SHA256withRSA")')
    if "aead inventory" in title:
        return f'Cipher.getInstance("{target or "ChaCha20-Poly1305"}");'
    if "aes mode" in title:
        mode = target or "AES/GCM/NoPadding"
        return f'Cipher.getInstance("{mode}");'
    if "asymmetric keygen inventory" in title:
        return f'KeyPairGenerator.getInstance("{target or "RSA"}");'
    if "crypto usage inventory" in title:
        if "securerandom.getinstance" in usable_anchor.lower() or "securerandom.getinstance" in keyword_blob:
            return f'SecureRandom.getInstance("{target or "SHA1PRNG"}");'
        if "securerandom" in usable_anchor.lower() or "securerandom" in keyword_blob:
            return "new SecureRandom();"
        if "cipherinputstream" in usable_anchor.lower() or "cipherinputstream" in keyword_blob:
            return 'new CipherInputStream(System.in, Cipher.getInstance("AES/GCM/NoPadding"));'
        if "cipheroutputstream" in usable_anchor.lower() or "cipheroutputstream" in keyword_blob:
            return 'new CipherOutputStream(System.out, Cipher.getInstance("AES/GCM/NoPadding"));'
        if "sealedobject" in usable_anchor.lower() or "sealedobject" in keyword_blob:
            return 'new SealedObject("payload", Cipher.getInstance("AES/GCM/NoPadding"));'
        if "cipher.getinstance" in usable_anchor.lower() or "cipher.getinstance" in keyword_blob:
            return f'Cipher.getInstance("{target or "AES/GCM/NoPadding"}");'
        if "certificatefactory.getinstance" in usable_anchor.lower() or "certificatefactory.getinstance" in keyword_blob:
            return f'CertificateFactory.getInstance("{target or "X.509"}");'
        if "keyfactory.getinstance" in usable_anchor.lower() or "keyfactory.getinstance" in keyword_blob:
            return f'KeyFactory.getInstance("{target or "RSA"}");'
        if "keyagreement.getinstance" in usable_anchor.lower() or "keyagreement.getinstance" in keyword_blob:
            return f'KeyAgreement.getInstance("{target or "ECDH"}");'
        if "keymanagerfactory.getinstance" in usable_anchor.lower() or "keymanagerfactory.getinstance" in keyword_blob:
            return f'KeyManagerFactory.getInstance("{target or "SunX509"}");'
        if "keystore.getinstance" in usable_anchor.lower() or "keystore.getinstance" in keyword_blob:
            return f'KeyStore.getInstance("{target or "PKCS12"}");'
        if "mac.getinstance" in usable_anchor.lower() or "mac.getinstance" in keyword_blob:
            return f'Mac.getInstance("{target or "HmacSHA256"}");'
        if "messagedigest.getinstance" in usable_anchor.lower() or "messagedigest.getinstance" in keyword_blob:
            return f'MessageDigest.getInstance("{target or "SHA-256"}");'
        if "signature.getinstance" in usable_anchor.lower() or "signature.getinstance" in keyword_blob:
            return f'Signature.getInstance("{target or "SHA256withRSA"}");'
        if "sslcontext.getinstance" in usable_anchor.lower() or "sslcontext.getinstance" in keyword_blob:
            return f'SSLContext.getInstance("{target or "TLS"}");'
        if "trustmanagerfactory.getinstance" in usable_anchor.lower() or "trustmanagerfactory.getinstance" in keyword_blob:
            return f'TrustManagerFactory.getInstance("{target or "PKIX"}");'
        if "keypairgenerator.getinstance" in usable_anchor.lower() or "keypairgenerator.getinstance" in keyword_blob:
            return f'KeyPairGenerator.getInstance("{target or "RSA"}");'
        if "keygenerator.getinstance" in usable_anchor.lower() or "keygenerator.getinstance" in keyword_blob:
            return f'KeyGenerator.getInstance("{target or "AES"}");'
        return _append_statement(usable_anchor or f'KeyPairGenerator.getInstance("{target or "RSA"}")')
    if "shor target signature inventory" in title:
        return f'Signature.getInstance("{target or "SHA256withRSA"}");'
    if "hash inventory" in title:
        return f'MessageDigest.getInstance("{target or "SHA-256"}");'
    if "ec curve inventory" in title:
        curve = target or "secp256r1"
        return "\n".join(
            [
                'KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC");',
                f'kpg.initialize(new ECGenParameterSpec("{curve}"));',
            ]
        )
    if "hndl key exchange inventory" in title:
        return f'KeyAgreement.getInstance("{target or "ECDH"}");'
    if "kdf inventory" in title:
        return f'SecretKeyFactory.getInstance("{target or "PBKDF2WithHmacSHA256"}");'
    if "keystore type inventory" in title:
        return f'KeyStore.getInstance("{target or "JKS"}");'
    if "mac inventory" in title:
        return f'Mac.getInstance("{target or "HmacSHA256"}");'
    if "tls & store system properties" in title:
        if parameter == "https.cipherSuites":
            return 'System.setProperty("https.cipherSuites", "TLS_RSA_WITH_3DES_EDE_CBC_SHA");'
        if parameter == "https.protocols":
            return 'System.setProperty("https.protocols", "TLSv1,TLSv1.1");'
        if parameter == "jdk.tls.client.protocols":
            return 'System.setProperty("jdk.tls.client.protocols", "TLSv1,TLSv1.1");'
        if parameter == "jdk.tls.server.protocols":
            return 'System.setProperty("jdk.tls.server.protocols", "TLSv1,TLSv1.1");'
        if parameter == "javax.net.ssl.keyStorePassword":
            return 'System.setProperty("javax.net.ssl.keyStorePassword", "changeit");'
        if parameter == "javax.net.ssl.trustStorePassword":
            return 'System.setProperty("javax.net.ssl.trustStorePassword", "changeit");'
        if parameter == "javax.net.ssl.keyStore":
            return 'System.setProperty("javax.net.ssl.keyStore", "legacy.jks");'
        if parameter == "javax.net.ssl.trustStore":
            return 'System.setProperty("javax.net.ssl.trustStore", "legacy.jks");'
        return _append_statement(usable_anchor or 'System.setProperty("https.protocols", "TLSv1,TLSv1.1")')
    if "symmetric key size inventory" in title:
        size = bits if bits >= 128 else 256
        return f'KeyGenerator.getInstance("AES").init({size});'
    if "xdh parameter inventory" in title:
        return anchor or 'NamedParameterSpec.X25519'
    if "hardcoded symmetric key" in title:
        if "secretkeyspec" in usable_anchor.lower() or "secretkeyspec" in keyword_blob:
            return 'new SecretKeySpec(Base64.getDecoder().decode("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVo="), "AES");'
        return 'byte[] keyBytes = Base64.getDecoder().decode("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVo=");'
    if "rsa keysize" in title:
        return "\n".join(
            [
                'KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");',
                f'kpg.initialize({bits});',
            ]
        )
    if "rsa encryption" in title or "rsa pkcs#1 v1.5 padding" in title:
        return f'Cipher.getInstance("{target or "RSA/ECB/PKCS1Padding"}");'
    if "weak signature algorithm" in title:
        return f'Signature.getInstance("{target or ("MD5withRSA" if "md5" in keyword_blob or "md5" in sample.lower() else "SHA1withRSA")}");'
    if "weak symmetric cipher" in title:
        if target:
            return f'Cipher.getInstance("{target}");'
        if "desede" in keyword_blob or "3des" in keyword_blob or "tripledes" in keyword_blob:
            return 'Cipher.getInstance("DESede");'
        if "rc4" in keyword_blob or "arc4" in keyword_blob:
            return 'Cipher.getInstance("RC4");'
        if "blowfish" in keyword_blob:
            return 'Cipher.getInstance("Blowfish");'
        if "rc2" in keyword_blob:
            return 'Cipher.getInstance("RC2");'
        return 'Cipher.getInstance("DES");'
    if "xmlenc weak key transport" in title:
        return 'String xmlTransport = "http://www.w3.org/2001/04/xmlenc#rsa-1_5";'
    if "weak tls ciphersuite" in title:
        parameter_upper = parameter.upper()
        if "_RC4_" in parameter_upper:
            return 'SSLSocket socket = (SSLSocket) SSLSocketFactory.getDefault().createSocket(); socket.setEnabledCipherSuites(new String[]{"SSL_RSA_WITH_RC4_128_SHA"});'
        if "_ANON_" in parameter_upper:
            return 'SSLSocket socket = (SSLSocket) SSLSocketFactory.getDefault().createSocket(); socket.setEnabledCipherSuites(new String[]{"TLS_DH_anon_WITH_AES_128_CBC_SHA"});'
        if "_DES_" in parameter_upper:
            return 'SSLSocket socket = (SSLSocket) SSLSocketFactory.getDefault().createSocket(); socket.setEnabledCipherSuites(new String[]{"TLS_RSA_WITH_DES_CBC_SHA"});'
        if "_MD5" in parameter_upper:
            return 'SSLSocket socket = (SSLSocket) SSLSocketFactory.getDefault().createSocket(); socket.setEnabledCipherSuites(new String[]{"TLS_RSA_WITH_NULL_MD5"});'
        if "_NULL_" in parameter_upper:
            return 'SSLSocket socket = (SSLSocket) SSLSocketFactory.getDefault().createSocket(); socket.setEnabledCipherSuites(new String[]{"TLS_RSA_WITH_NULL_SHA"});'
        return 'SSLSocket socket = (SSLSocket) SSLSocketFactory.getDefault().createSocket(); socket.setEnabledCipherSuites(new String[]{"SSL_RSA_WITH_3DES_EDE_CBC_SHA"});'
    if "weak tls protocol" in title:
        return 'SSLSocket socket = (SSLSocket) SSLSocketFactory.getDefault().createSocket(); socket.setEnabledProtocols(new String[]{"TLSv1", "TLSv1.1", "SSLv3"});'
    if "xmldsig" in title or "saml" in title:
        return 'String xmlAlgo = "http://www.w3.org/2000/09/xmldsig#rsa-sha1";'
    if "jwt" in title and "inventory" in title:
        return '\n'.join(['String jwtAlg = "RS256";', 'String jwtDependency = "com.auth0:java-jwt";'])
    if "xmldsig" in title or "saml" in title:
        return '\n'.join(['String xmlAlgo = "http://www.w3.org/2000/09/xmldsig#rsa-sha1";', *keywords[:3]])
    if variant in {"java_dependency", "jvm_jwt_libs", "jvm_xmldsig_saml", "bc_pqc"}:
        return "\n".join(keywords[:4]) or sample
    if "md5" in title:
        return 'MessageDigest.getInstance("MD5");'
    if "sha1" in title or "sha-1" in title:
        return 'MessageDigest.getInstance("SHA-1");'
    if "rng" in title or "random" in title:
        return "new java.util.Random().nextInt();"
    if "ecb" in title:
        return 'Cipher.getInstance("AES/ECB/PKCS5Padding");'
    if "rc4" in title or "arc4" in title:
        return 'Cipher.getInstance("RC4");'
    if "blowfish" in title:
        return 'Cipher.getInstance("Blowfish");'
    if "3des" in title or "tripledes" in title:
        return 'Cipher.getInstance("DESede");'
    if "des" in title:
        return 'Cipher.getInstance("DES");'
    if "hostname verifier" in title or "trust manager" in title or "trust bypass" in title:
        return "HostnameVerifier verifier = (host, session) -> true;"
    if "existing pack" in title:
        if "keystore" in keyword_blob and "tochararray" in keyword_blob:
            return '\n'.join(
                [
                    'KeyStore store = KeyStore.getInstance("JKS");',
                    'store.load(new ByteArrayInputStream(new byte[0]), "changeit".toCharArray());',
                ]
            )
        if "keyagreement" in keyword_blob and "dh" in keyword_blob:
            return 'KeyAgreement.getInstance("DH");'
        if "signature.getinstance" in keyword_blob:
            if "md5" in sample.lower() or "md5" in keyword_blob:
                return 'Signature.getInstance("MD5withRSA");'
            if "sha1" in sample.lower() or "sha1" in keyword_blob:
                return 'Signature.getInstance("SHA1withRSA");'
        if "pbekeyspec" in sample.lower() or "pbekeyspec" in keyword_blob:
            return 'new PBEKeySpec("legacy-password".toCharArray(), "salt".getBytes(), 457, 128);'
        if "begin" in keyword_blob and "private key" in keyword_blob:
            return _quantum_key_material_payload(entry)
        if "sslcontext" in keyword_blob:
            return 'SSLContext.getInstance("TLSv1");'
        if "cipher.getinstance" in keyword_blob:
            return 'Cipher.getInstance("AES/GCM/NoPadding");'
        if "hmacmd5" in keyword_blob:
            return 'Mac.getInstance("HmacMD5");'
    return usable_anchor or _keyword_fallback(entry) or sample or f'// coverage placeholder for {entry["rule_key"]}'


def _csharp_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    parameter = str(entry.get("parameter") or "").strip()
    algorithm = str(entry.get("algorithm") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    keywords = _rule_keywords(entry)
    keyword_blob = " ".join(keywords).lower()
    usable_anchor = _usable_anchor(anchor)
    bits = _first_int(title, sample) or 1024
    target = _first_non_empty(parameter, algorithm)
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "bouncycastle: crypto library usage" in title:
        return "var bcNamespace = \"Org.BouncyCastle.Crypto\";"
    if "bouncycastle: rsa/ecdsa keygen/signing" in title:
        return "var bcAlgorithm = \"Org.BouncyCastle.Crypto.Generators.RsaKeyPairGenerator\";"
    if "bouncycastle" in title and "inventory" in title:
        return usable_anchor or "using Org.BouncyCastle.Crypto;"
    if "jwt: rs256/es256" in title:
        return 'var alg = SecurityAlgorithms.RsaSha256;\nvar alt = SecurityAlgorithms.EcdsaSha256;'
    if "jwt: hs256" in title:
        return 'var alg = SecurityAlgorithms.HmacSha256;'
    if "token validation disabled" in title:
        return "new TokenValidationParameters { ValidateIssuerSigningKey = false, ValidateAudience = false };"
    if "using: system.security.cryptography" in title:
        return "using System.Security.Cryptography;"
    if "using: system.net" in title:
        return "using System.Net;"
    if "rsa pkcs#1 v1.5" in title:
        return "var padding = RSAEncryptionPadding.Pkcs1;"
    if "rsa: all rsa usage" in title or "rsacryptoserviceprovider shor-vulnerable inventory" in title:
        return "RSA.Create();"
    if "rsacryptoserviceprovider" in title and "inventory" in title:
        return "new RSACryptoServiceProvider(2048);"
    if "rsacng" in title:
        return "new RSACng();"
    if "ecdsacng" in title:
        return "new ECDsaCng();"
    if "ecdiffiehellmancng" in title:
        return "new ECDiffieHellmanCng();"
    if "dsacryptoserviceprovider" in title:
        return "new DSACryptoServiceProvider();"
    if "bouncycastle pqc" in title:
        return "var pqc = new KyberKeyPairGenerator();\nvar pqcAlt = \"Dilithium\";"
    if "random" in title or "rng" in title:
        return "new Random().Next();"
    if "servercertificatevalidationcallback" in title:
        return "ServicePointManager.ServerCertificateValidationCallback += (_, _, _, _) => true;"
    if "sslstream: remotecertificatevalidationcallback always-true" in title:
        return "var stream = new SslStream(Stream.Null, false, (_, _, _, _) => true);"
    if "servicepointmanager" in title and "tls" in title:
        if "tls1.1" in target.lower() or "tlsv1" in sample.lower():
            return "ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls | SecurityProtocolType.Tls11;"
        return "ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3 | SecurityProtocolType.Tls;"
    if "httpclient: httpclienthandler with insecure ssl validation" in title:
        return "\n".join(
            [
                "var handler = new HttpClientHandler();",
                "handler.ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator;",
            ]
        )
    if "sslstream" in title:
        return "var stream = new SslStream(Stream.Null, false, (_, _, _, _) => true);"
    if "dangerousacceptany" in title or "trust bypass" in title:
        return "handler.ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator;"
    if "passwordderivebytes" in title or "pbkdf1" in title:
        return 'new PasswordDeriveBytes("legacy-password", new byte[] {1,2,3,4});'
    if "weak kdf" in title and "pbkdf2" in title:
        return "Rfc2898DeriveBytes.Pbkdf2(\"password\", new byte[] {1,2,3,4}, 1000, HashAlgorithmName.SHA1, 32);"
    if "rfc2898derivebytes" in title:
        return "new Rfc2898DeriveBytes(\"password\", new byte[] {1,2,3,4}, 1000);"
    if "md5cryptoserviceprovider" in title:
        return "new MD5CryptoServiceProvider();"
    if "md5" in title:
        return "MD5.Create();"
    if "sha1" in title or "sha-1" in title:
        return "SHA1.Create();"
    if "rijndaelmanaged" in title and "ecb" in title:
        return "var alg = new RijndaelManaged { Mode = CipherMode.ECB };"
    if "aescryptoserviceprovider" in title and "ecb" in title:
        return "var alg = new AesCryptoServiceProvider { Mode = CipherMode.ECB };"
    if "ecb" in title:
        return "var alg = Aes.Create(); alg.Mode = CipherMode.ECB;"
    if "rc4" in title or "arc4" in title:
        return "new RC2CryptoServiceProvider();"
    if "rc2cryptoserviceprovider" in title:
        return "new RC2CryptoServiceProvider();"
    if "3des" in title or "tripledes" in title:
        if "cryptoserviceprovider" in title:
            return "new TripleDESCryptoServiceProvider();"
        return "TripleDES.Create();"
    if "des" in title:
        if "cryptoserviceprovider" in title:
            return "new DESCryptoServiceProvider();"
        return "DES.Create();"
    if "rsa keysize" in title:
        return f"new RSACryptoServiceProvider({bits});"
    if "rsacryptoserviceprovider with keysize" in title or "rsacryptoserviceprovider weak key size" in title:
        return f"new RSACryptoServiceProvider({bits});"
    if "ecdsa" in title and "inventory" in title:
        return "ECDsa.Create();"
    if "ecdiffiehellman" in title and "inventory" in title:
        return "ECDiffieHellman.Create();"
    if "hmacmd5" in title:
        return "new HMACMD5();"
    if "hardcoded symmetric key/iv" in title:
        return "var aes = new RijndaelManaged(); aes.Key = new byte[] {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6}; aes.IV = new byte[] {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6};"
    if "jwt" in title and "inventory" in title:
        return '\n'.join(['var jwtLibrary = "System.IdentityModel.Tokens.Jwt";', 'var alg = "RS256";', *keywords[:2]])
    if "tokenvalidationparameters" in title or "token validation disabled" in title:
        return "new TokenValidationParameters { ValidateIssuerSigningKey = false, RequireSignedTokens = false, ValidateIssuer = false, ValidateAudience = false, ValidateLifetime = false };"
    if "x509certificate2" in title and "password" in title:
        return "new X509Certificate2(\"legacy.pfx\", \"password\");"
    if "aesgcm" in title:
        return "new AesGcm(new byte[16]);"
    if "chacha20poly1305" in title:
        return "new ChaCha20Poly1305(new byte[32]);"
    if "randomnumbergenerator.getbytes" in title or "randomnumbergenerator.fill" in title:
        return "var buffer = new byte[16]; RandomNumberGenerator.Fill(buffer);"
    if "xmldsig weak algorithm uri" in title:
        return "var xmlAlg = \"http://www.w3.org/2000/09/xmldsig#rsa-sha1\";"
    return usable_anchor or _keyword_fallback(entry) or sample or f"// coverage placeholder for {entry['rule_key']}"


def _python_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    parameter = str(entry.get("parameter") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    keywords = _rule_keywords(entry)
    usable_anchor = _usable_anchor(anchor)
    bits = _first_int(title, sample) or 1024
    target = _first_non_empty(parameter)
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "import: ssl module" in title:
        return "import ssl"
    if "import: hashlib" in title:
        return "import hashlib"
    if "import-only" in title:
        return usable_anchor or sample
    if "urllib3" in title and "certificate verification disabled" in title:
        return "urllib3.PoolManager(cert_reqs=ssl.CERT_NONE, assert_hostname=False)"
    if "pyopenssl" in title and "verify_none" in title:
        return "ctx.set_verify(SSL.VERIFY_NONE, lambda *args: True)"
    if "paramiko" in title and "autoaddpolicy" in title:
        return "client.set_missing_host_key_policy(paramiko.AutoAddPolicy())"
    if "sslcontext.check_hostname disabled" in title:
        return "ctx = ssl.create_default_context()\nctx.check_hostname = False"
    if "random: non-cryptographic rng" in title:
        return "random.Random().randint(1, 9)"
    if "pycrypto: rsa key generation" in title:
        return f"RSA.generate({bits})"
    if "python-rsa" in title and "weak rsa key size" in title:
        return f"rsa.newkeys({bits})"
    if "python-rsa" in title and "inventory" in title:
        return "rsa.newkeys(2048)"
    if "pem private key in python source" in title:
        return _quantum_key_material_payload(entry)
    if "os.urandom usage" in title:
        return "os.urandom(32)"
    if "jwt" in title and "inventory" in title:
        return '\n'.join(['import jwt', 'jwt.encode({"sub": "coverage"}, "secret", algorithm="RS256")', *keywords[:2]])
    if "cryptography: pkcs1v15" in title:
        return "padding.PKCS1v15()"
    if "pkcs#1 v1.5 encryption" in title:
        return "\n".join(["from Crypto.Cipher import PKCS1_v1_5", "cipher = PKCS1_v1_5.new(object())"])
    if "verify=false" in title or "trust bypass" in title:
        return 'requests.get("https://partner.example", verify=False)'
    if "cert_none" in title:
        return "ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)\nctx.verify_mode = ssl.CERT_NONE"
    if "unverified_context" in title:
        return "ssl._create_unverified_context()"
    if "protocol_tls" in title or "protocol_sslv3" in title:
        return "ssl.SSLContext(ssl.PROTOCOL_TLSv1)"
    if "pbkdf2" in title and "low iter" in title:
        return 'hashlib.pbkdf2_hmac("sha1", b"pw", b"salt", 1000)'
    if "hmac-md5" in title or "hmac with md5" in title:
        return 'hmac.new(b"legacy-key", b"payload", hashlib.md5).hexdigest()'
    if "md5" in title:
        return 'hashlib.md5(b"legacy").hexdigest()'
    if "sha1" in title or "sha-1" in title:
        return 'hashlib.sha1(b"legacy").hexdigest()'
    if "random" in title or "rng" in title:
        return "random.Random().randint(1, 9)"
    if "ecb" in title:
        return 'AES.new(b"0123456789ABCDEF", AES.MODE_ECB)'
    if "arc4" in title or "rc4" in title:
        return 'ARC4.new(b"legacy-rc4-key")'
    if "blowfish" in title:
        return 'Blowfish.new(b"legacy-blowfish")'
    if "3des" in title or "des3" in title:
        return 'DES3.new(b"Sixteen byte key", DES3.MODE_ECB)'
    if "des" in title:
        return 'DES.new(b"8bytekey", DES.MODE_ECB)'
    if "rsa keysize" in title:
        return f"rsa.generate_private_key(public_exponent=65537, key_size={bits})"
    if "rsa key generation" in title and "inventory" in title:
        return "rsa.generate_private_key(public_exponent=65537, key_size=2048)"
    if "ecdh key exchange" in title:
        return "ec.generate_private_key(ec.SECP256R1()).exchange(ec.ECDH(), peer_public_key)"
    if "jwt alg=none" in title or "verification disabled" in title:
        return 'jwt.decode(token, options={"verify_signature": False})'
    if "hardcoded secret/key in source" in title:
        return 'HARDCODED_SECRET = "coverage-static-key-0123456789ABCDEF"'
    if "jwt" in title and "inventory" in title:
        return 'jwt.encode({"sub": "coverage"}, "secret", algorithm="HS256")'
    if "xmldsig" in title or "saml" in title:
        return "\n".join(["import xmlsec", *keywords[:3]]) if keywords else "import xmlsec"
    if target == "CERT_NONE":
        return "ctx = ssl.create_default_context()\nctx.verify_mode = ssl.CERT_NONE"
    if "validate_cert" in title or "verify_mode" in title:
        return "ctx = ssl.create_default_context()\nctx.verify_mode = ssl.CERT_NONE"
    return usable_anchor or _keyword_fallback(entry) or sample or f"# coverage placeholder for {entry['rule_key']}"


def _typescript_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    keywords = _rule_keywords(entry)
    usable_anchor = _usable_anchor(anchor)
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "shor inventory" in title:
        if "ecdsa" in title or "hndl inventory" in title:
            return 'crypto.createECDH("prime256v1");'
        return 'crypto.generateKeyPairSync("rsa", { modulusLength: 2048 });'
    if "jwt" in title and "inventory" in title:
        return 'jsonwebtoken.sign({ sub: "coverage" }, "secret", { algorithm: "RS256" });'
    if "xmldsig" in title or "saml" in title:
        return usable_anchor or '\n'.join(['const xmlCryptoPackage = "xml-crypto";', 'const samlLibrary = "samlify";', *keywords[:2]])
    if "node_tls_reject_unauthorized" in title or "rejectunauthorized" in title:
        return "process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';"
    if "rsa-sha1" in title or "md5" in title and "createsign" in title:
        return 'crypto.createSign("RSA-SHA1").update("legacy");'
    if "rejectunauthorized" in title or "trust bypass" in title:
        return "const opts = { rejectUnauthorized: false }; https.request(opts);"
    if "weak cipher" in title:
        return 'crypto.createCipheriv("des-ede3-cbc", Buffer.alloc(24), Buffer.alloc(8));'
    if "hndl inventory" in title:
        return 'crypto.createECDH("prime256v1");'
    if "legacy rsa key size" in title:
        return 'crypto.generateKeyPairSync("rsa", { modulusLength: 1024 });'
    if "weak kdf" in title:
        return 'crypto.pbkdf2Sync("password", "salt", 1000, 32, "sha1");'
    if "jwt alg=none" in title or "verification disabled" in title:
        return 'jsonwebtoken.verify(token, "", { algorithms: ["none"] });'
    if "md5" in title:
        return 'crypto.createHash("md5").update("legacy").digest("hex");'
    if "sha1" in title or "sha-1" in title:
        return 'crypto.createHash("sha1").update("legacy").digest("hex");'
    if "xmldsig" in title or "saml" in title:
        return 'const xmlSignatureAlgorithm = "rsa-sha1";'
    if "jwt" in title and "inventory" in title:
        return 'const alg = "RS256";'
    return usable_anchor or _keyword_fallback(entry) or sample or f"// coverage placeholder for {entry['rule_key']}"


def _javascript_sample(entry: dict[str, Any]) -> str:
    return _typescript_sample(entry)


def _go_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    parameter = str(entry.get("parameter") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    keywords = _rule_keywords(entry)
    usable_anchor = _usable_anchor(anchor)
    bits = _first_int(title, sample) or 1024
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "jwt rs/es inventory" in title:
        return "jwt.SigningMethodRS256\njwt.SigningMethodES256"
    if "pqc library inventory" in title:
        return 'import "github.com/cloudflare/circl/sign/dilithium"\n// kyber dilithium liboqs'
    if "insecureskipverify" in title or "trust bypass" in title:
        return "tls.Config{InsecureSkipVerify: true}"
    if "hndl inventory" in title:
        return 'ecdh.P256()'
    if "shor inventory" in title and "ecdsa" in title:
        return 'ecdsa.GenerateKey(elliptic.P256(), rand.Reader)'
    if "shor inventory" in title and "rsa" in title:
        return 'rsa.GenerateKey(rand.Reader, 2048)'
    if "rsa key size" in title or "legacy rsa key size" in title:
        return f"rsa.GenerateKey(rand.Reader, {bits})"
    if "md5" in title:
        return 'md5.Sum([]byte("legacy"))'
    if "sha1" in title or "sha-1" in title:
        return 'sha1.Sum([]byte("legacy"))'
    if "random" in title or "rng" in title:
        return "rand.New(rand.NewSource(7)).Int()"
    if "weak kdf" in title:
        return 'pbkdf2.Key([]byte("pw"), []byte("salt"), 1000, 32, sha1.New)'
    if "ecb" in title:
        return "NewECBEncrypter(block, iv)"
    if "rc4" in title:
        return 'rc4.NewCipher([]byte("legacy-key"))'
    if "3des" in title:
        return 'des.NewTripleDESCipher([]byte("123456789012345678901234"))'
    if "des" in title:
        return 'des.NewCipher([]byte("12345678"))'
    if "jwt" in title and "inventory" in title:
        return 'jwt.SigningMethodRS256\njwt.SigningMethodES256'
    if "jwt verification disabled" in title or "alg=none" in title:
        return 'jwt.Parse(tokenString, nil, jwt.WithValidMethods([]string{"none"}))'
    return usable_anchor or _keyword_fallback(entry) or sample or f"// coverage placeholder for {entry['rule_key']}"


def _shell_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    usable_anchor = _usable_anchor(str(entry.get("evidence_anchor") or "").strip())
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "wget" in title:
        return "wget --no-check-certificate https://example.internal/archive.tgz"
    if "curl -k" in title or "tls trust bypass" in title:
        return "curl -k https://example.internal/health"
    if "weak cipher" in title:
        return "openssl enc -des-cbc -in input.txt -out output.bin -k legacy-pass"
    if "legacy rsa key size" in title:
        return "openssl genrsa 1024"
    if "shor inventory" in title:
        return "openssl genrsa 2048"
    if "hndl inventory" in title:
        return "openssl dhparam 2048"
    if "keystore password" in title:
        return "keytool -list -keystore legacy.jks -storepass changeit"
    return usable_anchor or _keyword_fallback(entry) or str(entry.get("sample") or "").strip() or f"# coverage placeholder for {entry['rule_key']}"


def _powershell_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    usable_anchor = _usable_anchor(str(entry.get("evidence_anchor") or "").strip())
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "servercertificatevalidationcallback" in title or "tls trust bypass" in title:
        return "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = { $true }"
    if "skipcertificatecheck" in title:
        return "Invoke-WebRequest https://example.internal -SkipCertificateCheck"
    if "shor inventory" in title and "rsa" in title:
        return "[System.Security.Cryptography.RSA]::Create()"
    if "hndl inventory" in title:
        return "[System.Security.Cryptography.ECDiffieHellman]::Create()"
    if "jwt alg=none" in title or "validation disabled" in title:
        return "$params = New-Object Microsoft.IdentityModel.Tokens.TokenValidationParameters -Property @{ ValidateIssuerSigningKey = $false }"
    return usable_anchor or _keyword_fallback(entry) or str(entry.get("sample") or "").strip() or f"# coverage placeholder for {entry['rule_key']}"


def _ruby_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    usable_anchor = _usable_anchor(str(entry.get("evidence_anchor") or "").strip())
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "tls weak protocol" in title:
        return "ctx = OpenSSL::SSL::SSLContext.new\nctx.min_version = OpenSSL::SSL::TLS1_VERSION"
    if "tls trust bypass" in title:
        return "http.verify_mode = OpenSSL::SSL::VERIFY_NONE"
    if "weak cipher" in title:
        return "OpenSSL::Cipher.new('des-ede3-cbc')"
    if "insecure mode (ecb)" in title:
        return "OpenSSL::Cipher.new('AES-128-ECB')"
    if "shor inventory" in title:
        return "OpenSSL::PKey::RSA.new(2048)"
    if "hndl inventory" in title:
        return "OpenSSL::PKey::EC.generate('prime256v1')"
    if "jwt alg=none" in title or "verification disabled" in title:
        return "JWT.decode(token, nil, false, { algorithm: 'none' })"
    if "jwt rs/es inventory" in title:
        return "JWT.encode(payload, private_key, 'RS256')"
    if "weak kdf" in title:
        return "OpenSSL::PKCS5.pbkdf2_hmac('password', 'salt', 1000, 32, 'sha1')"
    if "xmldsig" in title or "saml" in title:
        return "require 'ruby-saml'"
    return usable_anchor or _keyword_fallback(entry) or str(entry.get('sample') or '').strip() or f'# coverage placeholder for {entry["rule_key"]}'


def _php_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    usable_anchor = _usable_anchor(str(entry.get("evidence_anchor") or "").strip())
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "tls trust bypass" in title:
        return "$ctx = stream_context_create(['ssl' => ['verify_peer' => false, 'verify_peer_name' => false]]);"
    if "weak hash (md5)" in title:
        return "md5('legacy');"
    if "weak hash (sha1)" in title:
        return "sha1('legacy');"
    if "weak cipher" in title:
        return "openssl_encrypt($data, 'des-ede3-cbc', $key, 0, $iv);"
    if "legacy rsa key size" in title:
        return "openssl_pkey_new(['private_key_bits' => 1024]);"
    if "shor inventory" in title:
        return "openssl_pkey_new(['private_key_bits' => 2048]);"
    if "jwt alg=none" in title or "verification disabled" in title:
        return "JWT::decode($token, null, false);"
    if "jwt rs/es inventory" in title:
        return "JWT::encode(['sub' => 'coverage'], $privateKey, 'RS256');"
    if "weak kdf" in title:
        return "hash_pbkdf2('sha1', 'password', 'salt', 1000, 32);"
    if "xmldsig" in title or "saml" in title:
        return "use RobRichards\\XMLSecLibs\\XMLSecurityKey;"
    return usable_anchor or _keyword_fallback(entry) or str(entry.get('sample') or '').strip() or f'// coverage placeholder for {entry["rule_key"]}'


def _rust_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    usable_anchor = _usable_anchor(str(entry.get("evidence_anchor") or "").strip())
    bits = _first_int(title, entry.get("sample")) or 1024
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "tls trust bypass" in title:
        return "let cfg = rustls::ClientConfig::builder().dangerous().with_custom_certificate_verifier(verifier);"
    if "shor inventory" in title:
        return "let _key = rsa::RsaPrivateKey::new(&mut rand::thread_rng(), 2048).unwrap();"
    if "hndl inventory" in title:
        return "let _secret = p256::ecdh::EphemeralSecret::random(&mut rand_core::OsRng);"
    if "jwt rs/es inventory" in title:
        return "let _alg = jsonwebtoken::Algorithm::RS256;"
    if "legacy rsa key size" in title:
        return f"let _key = rsa::RsaPrivateKey::new(&mut rand::thread_rng(), {bits}).unwrap();"
    if "weak kdf" in title:
        return 'pbkdf2::pbkdf2_hmac::<sha1::Sha1>(b"password", b"salt", 1000, &mut [0u8; 32]);'
    if "non-crypto rng" in title:
        return "let mut rng = rand::thread_rng(); let _sample: u32 = rng.gen();"
    if "tls weak protocol" in title:
        return "let _method = openssl::ssl::SslMethod::tlsv1();"
    if "weak cipher" in title:
        return "let _cipher = openssl::symm::Cipher::des_ede3_cbc();"
    if "pqc library inventory" in title:
        return "use oqs::kem::Algorithm::Kyber512;"
    return usable_anchor or _keyword_fallback(entry) or str(entry.get('sample') or '').strip() or f'// coverage placeholder for {entry["rule_key"]}'


def _cpp_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    usable_anchor = _usable_anchor(str(entry.get("evidence_anchor") or "").strip())
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "tls trust bypass" in title:
        return "SSL_CTX_set_verify(ctx, SSL_VERIFY_NONE, NULL);"
    if "weak hash (md5)" in title:
        return "EVP_DigestInit_ex(ctx, EVP_md5(), NULL);"
    if "weak hash (sha1)" in title:
        return "EVP_DigestInit_ex(ctx, EVP_sha1(), NULL);"
    if "insecure mode (ecb)" in title:
        return "EVP_EncryptInit_ex(ctx, EVP_aes_128_ecb(), NULL, key, NULL);"
    if "legacy rsa key size" in title:
        return "RSA_generate_key_ex(rsa, 1024, e, NULL);"
    if "shor inventory" in title:
        return "RSA_generate_key_ex(rsa, 2048, e, NULL);"
    if "hndl inventory" in title:
        return "EVP_PKEY_CTX_new_id(EVP_PKEY_EC, NULL);"
    if "weak kdf" in title:
        return "PKCS5_PBKDF2_HMAC(\"password\", 8, salt, 4, 1000, EVP_sha1(), 32, out);"
    if "pqc library inventory" in title:
        return "#include <oqs/oqs.h>"
    return usable_anchor or _keyword_fallback(entry) or str(entry.get("sample") or "").strip() or f"// coverage placeholder for {entry['rule_key']}"


def _c_sample(entry: dict[str, Any]) -> str:
    return _cpp_sample(entry)


def _swift_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    usable_anchor = _usable_anchor(str(entry.get("evidence_anchor") or "").strip())
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "shor inventory" in title:
        return 'let rsaAlgorithm = "SecKeyAlgorithm.rsaEncryptionPKCS1"'
    if "hndl inventory" in title:
        return 'let ecdhCurve = "P256.KeyAgreement.PrivateKey"'
    if "jwt rs/es inventory" in title:
        return 'let jwtAlg = "RS256"'
    if "tls weak config" in title:
        return 'let ats = ["NSAllowsArbitraryLoads": true]'
    if "weak kdf" in title:
        return 'let rounds = 1000'
    return usable_anchor or _keyword_fallback(entry) or str(entry.get("sample") or "").strip() or f"// coverage placeholder for {entry['rule_key']}"


def _objectivec_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    usable_anchor = _usable_anchor(str(entry.get("evidence_anchor") or "").strip())
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    if "tls trust bypass" in title:
        return "NSDictionary *settings = @{ (id)kCFStreamSSLValidatesCertificateChain: @NO };"
    if "tls weak config" in title:
        return '@{ @"NSAllowsArbitraryLoads": @YES };'
    if "legacy rsa key size" in title:
        return '@{ (id)kSecAttrKeyType: (id)kSecAttrKeyTypeRSA, (id)kSecAttrKeySizeInBits: @1024 };'
    if "weak kdf" in title:
        return "CCKeyDerivationPBKDF(kCCPBKDF2, \"password\", 8, salt, 4, kCCPRFHmacAlgSHA1, 1000, out, 32);"
    return usable_anchor or _keyword_fallback(entry) or str(entry.get("sample") or "").strip() or f"// coverage placeholder for {entry['rule_key']}"


def _config_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    parameter = str(entry.get("parameter") or "").strip()
    keywords = _rule_keywords(entry)
    if "nginx insecure cipher" in title:
        return "ssl_ciphers RC4:3DES:MD5;"
    if "nginx tls weak protocol" in title:
        return "ssl_protocols TLSv1 TLSv1.1;"
    if "apache tls weak protocol" in title:
        return "SSLProtocol TLSv1 TLSv1.1"
    if "apache insecure cipher" in title:
        return "SSLCipherSuite RC4:3DES:MD5"
    if "haproxy tls weak min version" in title:
        return "ssl-min-ver TLSv1.0"
    if "haproxy insecure ciphers" in title:
        return "ssl-default-bind-ciphers RC4:3DES:MD5"
    if "kubeconfig insecure skip tls verify" in title:
        return textwrap.dedent(
            """\
            apiVersion: v1
            clusters:
              - cluster:
                  insecure-skip-tls-verify: true
                  server: https://cluster.internal
                name: kubeconfig
            """
        ).strip()
    if "k8s ingress weak tls" in title:
        return "nginx.ingress.kubernetes.io/ssl-protocols: TLSv1 TLSv1.1"
    if "openssl minprotocol weak" in title:
        return "MinProtocol = TLSv1.0"
    if "openssl seclevel lowered" in title:
        return "CipherString = DEFAULT@SECLEVEL=0"
    if "jvm client protocols forced legacy" in title:
        return "jdk.tls.client.protocols=TLSv1,TLSv1.1"
    if "sshd weak kexalgorithms" in title:
        return "KexAlgorithms diffie-hellman-group1-sha1"
    if "sshd weak ciphers" in title:
        return "Ciphers 3des-cbc"
    if "key material artifacts (pkcs12/jks)" in title:
        return "server.ssl.key-store=legacy.jks"
    if "ios ats insecure transport exceptions" in title:
        return "<key>NSAllowsArbitraryLoads</key><true/>"
    if "spring boot tls weak protocols" in title:
        return "server.ssl.enabled-protocols=TLSv1,TLSv1.1"
    if "tomcat/jetty tls weak protocols" in title:
        return "<Connector sslEnabledProtocols=\"TLSv1,TLSv1.1\" />"
    if keywords:
        return "\n".join(keywords[:4])
    return _usable_anchor(str(entry.get("evidence_anchor") or "").strip()) or sample or "# coverage config placeholder"


def _quantum_effective_sample(entry: dict[str, Any]) -> str:
    language = str(entry.get("language") or "").strip()
    if language == "java":
        return _java_sample(entry)
    if language == "csharp":
        return _csharp_sample(entry)
    if language == "python":
        return _python_sample(entry)
    if language == "typescript":
        return _typescript_sample(entry)
    if language == "javascript":
        return _javascript_sample(entry)
    if language == "go":
        return _go_sample(entry)
    if language == "shell":
        return _shell_sample(entry)
    if language == "powershell":
        return _powershell_sample(entry)
    if language == "ruby":
        return _ruby_sample(entry)
    if language == "php":
        return _php_sample(entry)
    if language == "rust":
        return _rust_sample(entry)
    if language == "cpp":
        return _cpp_sample(entry)
    if language == "c":
        return _c_sample(entry)
    if language == "swift":
        return _swift_sample(entry)
    if language == "objectivec":
        return _objectivec_sample(entry)
    if language in {"kotlin", "scala", "groovy"}:
        return _java_sample(entry)
    if language == "config":
        return _config_sample(entry)
    if _is_quantum_key_material(entry):
        return _quantum_key_material_payload(entry)
    sample = str(entry.get("sample") or "").strip()
    anchor = _usable_anchor(str(entry.get("evidence_anchor") or "").strip())
    return anchor or _keyword_fallback(entry) or sample or f"coverage::{entry['rule_key']}"


def _indented(snippet: str, prefix: str) -> str:
    return textwrap.indent(snippet.rstrip(), prefix)


def _manifest_content(entry: dict[str, Any], path: str) -> str:
    values = [value for value in [str(entry.get("parameter") or "").strip(), str(entry.get("sample") or "").strip(), *_rule_keywords(entry)] if value]
    title = str(entry.get("title") or entry["rule_key"])
    if path.endswith("pom.xml"):
        dependencies = []
        for value in values:
            if ":" in value:
                group, artifact, *_ = value.split(":")
                dependencies.append(
                    "\n".join(
                        [
                            "    <dependency>",
                            f"      <groupId>{group}</groupId>",
                            f"      <artifactId>{artifact}</artifactId>",
                            "      <version>1.0.0</version>",
                            "    </dependency>",
                        ]
                    )
                )
        if not dependencies:
            dependencies.append(f"    <!-- {' '.join(values[:4] or [title])} -->")
        return "\n".join(["<project>", "  <dependencies>", *dependencies[:6], "  </dependencies>", "</project>", ""])
    if path.endswith("package.json"):
        deps = [value.strip('"') for value in values if "/" in value or "-" in value or value.islower()]
        if not deps:
            deps = [title.replace(" ", "-").lower()]
        body = ",\n".join(f'    "{value}": "1.0.0"' for value in deps[:6])
        return "{\n  \"dependencies\": {\n" + body + "\n  }\n}\n"
    if path.endswith("requirements.txt"):
        return "\n".join(values[:6] or ["requests==2.32.0"]) + "\n"
    if path.endswith(".csproj"):
        refs = [f'    <PackageReference Include="{value}" Version="1.0.0" />' for value in values if "." in value or value[:1].isupper()]
        if not refs:
            refs = [f'    <!-- {" ".join(values[:4] or [title])} -->']
        return "<Project Sdk=\"Microsoft.NET.Sdk\">\n  <ItemGroup>\n" + "\n".join(refs[:6]) + "\n  </ItemGroup>\n</Project>\n"
    if path.endswith("go.mod"):
        requires = [f"\t{value} v1.0.0" for value in values if "/" in value]
        if not requires:
            requires = ["\tgithub.com/golang-jwt/jwt/v5 v5.0.0"]
        return "module arq.coverage\n\ngo 1.22\n\nrequire (\n" + "\n".join(requires[:6]) + "\n)\n"
    if path.endswith("Gemfile"):
        gems = [f"gem '{value}'" for value in values if value]
        return "source 'https://rubygems.org'\n" + "\n".join(gems[:6] or ["gem 'ruby-saml'"]) + "\n"
    if path.endswith("composer.json"):
        reqs = [f'    "{value}": "^1.0"' for value in values if "/" in value]
        if not reqs:
            reqs = ['    "robrichards/xmlseclibs": "^3.0"']
        return "{\n  \"require\": {\n" + ",\n".join(reqs[:6]) + "\n  }\n}\n"
    if path.endswith("Cargo.toml"):
        deps = [f'{value.split("/")[-1].replace("-", "_")} = "1.0.0"' for value in values if value]
        return "[package]\nname = \"coverage\"\nversion = \"0.1.0\"\n\n[dependencies]\n" + "\n".join(deps[:6] or ['oqs = "0.9.0"']) + "\n"
    if path.endswith("build.gradle.kts"):
        deps = [f'implementation(\"{value}:1.0.0\")' for value in values if ":" in value]
        return "plugins { kotlin(\"jvm\") version \"1.9.0\" }\ndependencies {\n  " + "\n  ".join(deps[:6] or [f"// {' '.join(values[:4] or [title])}"]) + "\n}\n"
    if path.endswith("build.gradle"):
        deps = [f'implementation "{value}:1.0.0"' for value in values if ":" in value]
        return "plugins { id 'groovy' }\ndependencies {\n  " + "\n  ".join(deps[:6] or [f"// {' '.join(values[:4] or [title])}"]) + "\n}\n"
    if path.endswith("build.sbt"):
        deps = [f'libraryDependencies += "{value.split(":")[0]}" % "{value.split(":")[1]}" % "1.0.0"' for value in values if ":" in value]
        return "scalaVersion := \"2.13.14\"\n" + "\n".join(deps[:6] or [f'// {" ".join(values[:4] or [title])}']) + "\n"
    if path.endswith("rebar.config"):
        return "{deps, [" + ", ".join(values[:4] or ["jose"]) + "]}.\n"
    if path.endswith("CMakeLists.txt"):
        return "cmake_minimum_required(VERSION 3.20)\nproject(coverage)\n# " + " ".join(values[:6] or [title]) + "\n"
    return "\n".join(values[:6] or [title]) + "\n"


def _coverage_evidence_lines(entry: dict[str, Any], comment: str) -> list[str]:
    lines = [f"{comment} rule_key: {entry['rule_key']}"]
    anchor = str(entry.get("evidence_anchor") or "").strip()
    sample = str(entry.get("sample") or "").strip()
    keywords = _rule_keywords(entry)
    if anchor:
        lines.append(f"{comment} evidence_anchor: {anchor}")
    if sample:
        lines.append(f"{comment} regex_sample: {sample}")
    if keywords:
        lines.append(f"{comment} keywords: {' | '.join(keywords[:6])}")
    return lines


def _java_imports(entry: dict[str, Any], snippet: str) -> list[str]:
    blob = f"{snippet}\n{_entry_blob(entry)}".lower()
    imports: list[str] = []
    if any(token in blob for token in ("messagedigest", "keypairgenerator", "signature", "keyfactory", "secureRandom".lower(), "certificatefactory", "keystore", "keygenerator")):
        imports.append("import java.security.*;")
    if any(token in blob for token in ("ecgenparameterspec", "namedparameterspec")):
        imports.append("import java.security.spec.*;")
    if any(token in blob for token in ("cipher", "secretkeyfactory", "mac", "cipherinputstream", "cipheroutputstream", "sealedobject", "secretkeyspec", "keyagreement")):
        imports.append("import javax.crypto.*;")
    if any(token in blob for token in ("sslcontext", "sslparameters", "sslsocket", "sslsocketfactory", "trustmanagerfactory", "keymanagerfactory", "hostnameverifier")):
        imports.append("import javax.net.ssl.*;")
    if "base64" in blob:
        imports.append("import java.util.Base64;")
    if "bytearrayinputstream" in blob:
        imports.append("import java.io.*;")
    return imports or ["import java.security.*;", "import javax.crypto.*;"]


def _csharp_usings(entry: dict[str, Any], snippet: str) -> list[str]:
    blob = f"{snippet}\n{_entry_blob(entry)}".lower()
    usings = ["using System;"]
    if any(token in blob for token in ("servicepointmanager", "securityprotocoltype", "x509certificate2")):
        usings.append("using System.Net;")
    if any(token in blob for token in ("httpclient", "httpclienthandler", "socketshttphandler")):
        usings.append("using System.Net.Http;")
    if any(token in blob for token in ("sslstream", "remotecertificatevalidationcallback")):
        usings.extend(["using System.IO;", "using System.Net.Security;"])
    if any(
        token in blob
        for token in (
            "md5",
            "sha1",
            "rsa",
            "ecdsa",
            "ecdiffiehellman",
            "rijndaelmanaged",
            "ciphermode",
            "hmacmd5",
            "randomnumbergenerator",
            "passwordderivebytes",
            "rfc2898derivebytes",
            "aesgcm",
            "chacha20poly1305",
            "x509certificate2",
        )
    ):
        usings.append("using System.Security.Cryptography;")
    if "tokenvalidationparameters" in blob or "securityalgorithms" in blob:
        usings.append("using Microsoft.IdentityModel.Tokens;")
    seen: set[str] = set()
    ordered: list[str] = []
    for item in usings:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


def _python_imports(entry: dict[str, Any], snippet: str) -> list[str]:
    blob = f"{snippet}\n{_entry_blob(entry)}".lower()
    imports: list[str] = []
    if "hashlib" in blob:
        imports.append("import hashlib")
    if "hmac." in snippet or "hmac " in blob:
        imports.append("import hmac")
    if "random." in snippet or " random" in blob:
        imports.append("import random")
    if "ssl." in snippet or " ssl" in blob:
        imports.append("import ssl")
    if "urllib3" in blob:
        imports.append("import urllib3")
    if "paramiko" in blob:
        imports.append("import paramiko")
    if "requests." in snippet or " requests" in blob:
        imports.append("import requests")
    if "ssl.verify_none" in blob or "from openssl import ssl" in blob or " verify_none" in blob:
        imports.append("from OpenSSL import SSL")
    crypto_members = []
    for member in ("AES", "ARC4", "DES", "DES3", "Blowfish", "PKCS1_v1_5"):
        if f"{member}." in snippet:
            crypto_members.append(member)
    if crypto_members:
        imports.append(f"from Crypto.Cipher import {', '.join(crypto_members)}")
    if "RSA." in snippet:
        imports.append("from Crypto.PublicKey import RSA")
    crypto_asymmetric = []
    if "rsa." in snippet:
        crypto_asymmetric.append("rsa")
    if "ec." in snippet:
        crypto_asymmetric.append("ec")
    if crypto_asymmetric:
        imports.append(f"from cryptography.hazmat.primitives.asymmetric import {', '.join(crypto_asymmetric)}")
    if "padding." in snippet:
        imports.append("from cryptography.hazmat.primitives.asymmetric import padding")
    if "jwt." in snippet or " jwt" in blob:
        imports.append("import jwt")
    if "os." in snippet:
        imports.append("import os")
    if "xmlsec" in blob:
        imports.append("import xmlsec")
    seen: set[str] = set()
    ordered: list[str] = []
    for item in imports:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


def _code_like_quantum_content(entry: dict[str, Any], snippet: str) -> str:
    language = str(entry.get("language") or "").strip()
    path = str(entry["path"])
    if any(
        path.endswith(suffix)
        for suffix in (
            "pom.xml",
            "package.json",
            "requirements.txt",
            ".csproj",
            "go.mod",
            "Gemfile",
            "composer.json",
            "Cargo.toml",
            "build.gradle.kts",
            "build.gradle",
            "build.sbt",
            "rebar.config",
            "CMakeLists.txt",
        )
    ):
        return _manifest_content(entry, path)
    comment = _comment_prefix(language, path)
    title = entry.get("title") or entry["rule_key"]
    if _is_quantum_key_material(entry):
        extension = Path(path).suffix.lower()
        if extension in {".cer", ".crt", ".der"}:
            return _CERT_BLOB + "\n"
        if extension in {".jks", ".p12", ".pfx"}:
            return "BINARY_KEYSTORE_PLACEHOLDER\n"
        return "\n".join([*_coverage_evidence_lines(entry, comment), _quantum_key_material_payload(entry, extension).rstrip(), ""])
    stem = Path(path).stem.replace("-", "_")
    evidence_lines = _coverage_evidence_lines(entry, comment)
    if language == "java":
        imports = _java_imports(entry, snippet)
        return "\n".join(
            [
                "package legacy.coverage;",
                *imports,
                f"public final class {stem.title().replace('_', '')} {{",
                "    public void execute() throws Exception {",
                *[f"        {line}" for line in evidence_lines],
                _indented(snippet, "        "),
                "    }",
                "}",
                "",
            ]
        )
    if language == "csharp":
        usings = _csharp_usings(entry, snippet)
        return "\n".join(
            [
                *usings,
                "namespace Arq.Lab.Coverage;",
                f"public static class {stem.title().replace('_', '')} {{",
                "    public static void Execute() {",
                *[f"        {line}" for line in evidence_lines],
                _indented(snippet, "        "),
                "    }",
                "}",
                "",
            ]
        )
    if language == "python":
        imports = _python_imports(entry, snippet)
        return "\n".join(
            [
                *imports,
                "",
                "def execute():",
                *[f"    {line}" for line in evidence_lines],
                _indented(snippet, "    "),
                "",
                "if __name__ == '__main__':",
                "    execute()",
                "",
            ]
        )
    if language == "typescript":
        return "\n".join(
            [
                "import crypto from 'crypto';",
                "import https from 'https';",
                "import jsonwebtoken from 'jsonwebtoken';",
                f"export function {stem.replace('_', '')}() {{",
                *[f"  {line}" for line in evidence_lines],
                _indented(snippet, "  "),
                "}",
                "",
            ]
        )
    if language == "javascript":
        return "\n".join(
            [
                "const crypto = require('crypto');",
                "const https = require('https');",
                "const jsonwebtoken = require('jsonwebtoken');",
                "function executeCoverageRule() {",
                *[f"  {line}" for line in evidence_lines],
                _indented(snippet, "  "),
                "}",
                "module.exports = { executeCoverageRule };",
                "",
            ]
        )
    if language == "go":
        return "\n".join(
            [
                "package legacy",
                'import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")',
                "func ExecuteCoverage() any {",
                *[f"    {line}" for line in evidence_lines],
                _indented(snippet, "    "),
                "    return nil",
                "}",
                "",
            ]
        )
    if language == "kotlin":
        return "\n".join(
            [
                "package legacy.coverage",
                "import java.security.*",
                "import java.security.spec.*",
                "import javax.crypto.*",
                "import javax.net.ssl.*",
                f"object {stem.title().replace('_', '')} {{",
                "    @JvmStatic fun execute() {",
                *[f"        {line}" for line in evidence_lines],
                _indented(snippet, "        "),
                "    }",
                "}",
                "",
            ]
        )
    if language == "scala":
        return "\n".join(
            [
                "package legacy.coverage",
                "import java.security._",
                "import java.security.spec._",
                "import javax.crypto._",
                "import javax.net.ssl._",
                f"object {stem.title().replace('_', '')} {{",
                "  def execute(): Unit = {",
                *[f"    {line}" for line in evidence_lines],
                _indented(snippet, "    "),
                "  }",
                "}",
                "",
            ]
        )
    if language == "groovy":
        return "\n".join(
            [
                "package legacy.coverage",
                "import java.security.*",
                "import java.security.spec.*",
                "import javax.crypto.*",
                "import javax.net.ssl.*",
                f"class {stem.title().replace('_', '')} {{",
                "    static void execute() {",
                *[f"        {line}" for line in evidence_lines],
                _indented(snippet, "        "),
                "    }",
                "}",
                "",
            ]
        )
    if language == "ruby":
        return "\n".join(
            [
                "require 'openssl'",
                "require 'jwt'",
                "payload = { sub: 'coverage' }",
                *evidence_lines,
                snippet.rstrip(),
                "",
            ]
        )
    if language == "php":
        return "\n".join(
            [
                "<?php",
                *[f"// {line[3:] if line.startswith('// ') else line}" for line in evidence_lines],
                _indented(snippet, ""),
                "",
            ]
        )
    if language == "rust":
        return "\n".join(
            [
                "use rand::Rng;",
                "use rsa;",
                "use openssl::ssl::SslMethod;",
                "use openssl::symm::Cipher;",
                f"fn {stem.replace('_', '').lower()}() {{",
                *[f"    {line}" for line in evidence_lines],
                _indented(snippet, "    "),
                "}",
                "",
            ]
        )
    if language == "shell":
        return "\n".join(
            [
                "#!/usr/bin/env sh",
                *evidence_lines,
                snippet.rstrip(),
                "",
            ]
        )
    if language == "powershell":
        return "\n".join(
            [
                *evidence_lines,
                "function Invoke-CoverageRule {",
                _indented(snippet, "    "),
                "}",
                "",
            ]
        )
    if language == "cpp":
        return "\n".join(
            [
                "#include <openssl/ssl.h>",
                "#include <openssl/evp.h>",
                "#include <openssl/rsa.h>",
                "#include <oqs/oqs.h>",
                *evidence_lines,
                "int execute_coverage_cpp() {",
                _indented(snippet, "    "),
                "    return 0;",
                "}",
                "",
            ]
        )
    if language == "c":
        return "\n".join(
            [
                "#include <openssl/ssl.h>",
                "#include <openssl/evp.h>",
                "#include <openssl/rsa.h>",
                *evidence_lines,
                "int execute_coverage_c(void) {",
                _indented(snippet, "    "),
                "    return 0;",
                "}",
                "",
            ]
        )
    if language == "swift":
        return "\n".join(
            [
                "import Foundation",
                *[f"// {line[3:] if line.startswith('// ') else line}" for line in evidence_lines],
                "func executeCoverageSwift() {",
                _indented(snippet, "    "),
                "}",
                "",
            ]
        )
    if language == "objectivec":
        return "\n".join(
            [
                "#import <Foundation/Foundation.h>",
                "#import <Security/Security.h>",
                *[f"// {line[3:] if line.startswith('// ') else line}" for line in evidence_lines],
                "void executeCoverageObjC(void) {",
                _indented(snippet, "    "),
                "}",
                "",
            ]
        )
    return "\n".join(
        [
            *_coverage_evidence_lines(entry, comment),
            snippet.rstrip(),
            "",
        ]
    )


def _entry_content(entry: dict[str, Any]) -> str:
    if str(entry.get("rule_key") or "").startswith("quantum."):
        snippet = _quantum_effective_sample(entry)
        return _code_like_quantum_content(entry, snippet)
    comment = _comment_prefix(str(entry.get("language") or ""), str(entry["path"]))
    return "\n".join(
        [
            f"{comment} coverage campaign entry",
            f"{comment} rule_key: {entry['rule_key']}",
            str(entry["sample"]),
            "",
        ]
    )


def _chunk(items: list[dict[str, Any]], size: int) -> list[list[dict[str, Any]]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


@lru_cache(maxsize=1)
def _guardian_rule_entries() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in _read_rules("guardian"):
        rule_key = f"guardian.{item['id']}"
        if rule_key in _GUARDIAN_BASELINE_COVERED:
            continue
        sample = _GUARDIAN_SAMPLE_OVERRIDES.get(rule_key, "")
        regex = item.get("regex")
        if not sample:
            if not isinstance(regex, str) or not regex.strip():
                path_regex = item.get("pathRegex")
                if not (isinstance(path_regex, str) and path_regex.strip()):
                    continue
            else:
                try:
                    sample = _normalized_seeded_sample(regex, rule_key, guardian=True)
                except Exception:
                    continue
        if not sample:
            continue
        rows.append(
            {
                "rule_key": rule_key,
                "title": item.get("name") or item["id"],
                "family": item["id"],
                "language": "config",
                "sample": sample,
            }
        )
    return rows


@lru_cache(maxsize=1)
def _quantum_rule_entries() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in _read_rules("quantum"):
        rule_key = f"quantum.{item['id']}"
        if rule_key in _QUANTUM_BASELINE_COVERED:
            continue
        regex = item.get("regex")
        metadata = item.get("metadataTags") if isinstance(item.get("metadataTags"), dict) else {}
        keywords = item.get("keywords") if isinstance(item.get("keywords"), list) else []
        sample = ""
        if isinstance(regex, str) and regex.strip():
            try:
                sample = _normalized_seeded_sample(regex, rule_key, guardian=False)
            except Exception:
                sample = ""
        if not sample:
            sample = str(metadata.get("evidenceAnchor") or metadata.get("parameter") or metadata.get("algorithm") or "").strip()
        if not sample and keywords:
            sample = " ".join(str(keyword).strip() for keyword in keywords[:4] if str(keyword).strip()).strip()
        if not sample:
            continue
        rows.append(
            {
                "rule_key": rule_key,
                "title": item.get("name") or item["id"],
                "family": str(metadata.get("ruleFamily") or item.get("name") or ""),
                "language": _quantum_language(item),
                "sample": sample,
                "regex": regex,
                "algorithm": str(metadata.get("algorithm") or ""),
                "parameter": str(metadata.get("parameter") or ""),
                "evidence_anchor": str(metadata.get("evidenceAnchor") or ""),
                "detector_type": str(metadata.get("detectorType") or ""),
                "variant": str(metadata.get("variant") or ""),
                "ecosystem": str(metadata.get("ecosystem") or ""),
                "applicable_min_version": str(metadata.get("applicableMinVersion") or ""),
                "applicable_max_version": str(metadata.get("applicableMaxVersion") or ""),
                "keywords": [str(keyword).strip() for keyword in keywords if str(keyword).strip()],
            }
        )
    return rows


def _build_descriptor(
    *,
    scenario_id: str,
    milestone: str,
    repo_name: str,
    module: str,
    stack: str,
    domain: str,
    summary: str,
    scan_kind: str,
    entries: list[dict[str, Any]],
    line_target: str,
) -> dict[str, Any]:
    expected_findings = [
        {
            "key": f"rule-{index:03d}",
            "path_contains": entry["path"],
            "rule": entry["rule_key"],
        }
        for index, entry in enumerate(entries, start=1)
    ]
    return {
        "id": scenario_id,
        "milestone": milestone,
        "repo_name": repo_name,
        "module": module,
        "family": "coverage_bundle_repo",
        "stack": stack,
        "domain": domain,
        "summary": summary,
        "scan_kind": scan_kind,
        "line_target": line_target,
        "expected_findings": expected_findings,
        "metadata": {
            "coverageBundle": {
                "entries": entries,
                "generatedRuleCount": len(entries),
                "module": module,
                "scanKind": scan_kind,
            }
        },
    }


def _coverage_milestone_for_language(language: str) -> str:
    lowered = language.strip().lower()
    if lowered in {"java", "csharp", "kotlin", "scala", "groovy"}:
        return "M3"
    if lowered in {"python", "typescript", "javascript", "go"}:
        return "M4"
    if lowered == "config":
        return "M6"
    return "M8"


def _coverage_id_prefix_for_milestone(milestone: str) -> str:
    return {
        "M3": "Q-V3-COV-",
        "M4": "Q-V4-COV-",
        "M6": "Q-V6-COV-",
        "M8": "M-V8-COV-",
    }[milestone]


def _coverage_stack_for_language(language: str) -> str:
    lowered = language.strip().lower()
    if lowered == "java":
        return "Java / precision coverage pack"
    if lowered == "csharp":
        return "C# / precision coverage pack"
    if lowered == "python":
        return "Python / precision coverage pack"
    if lowered in {"typescript", "javascript"}:
        return "TypeScript / JavaScript precision coverage pack"
    if lowered == "go":
        return "Go / precision coverage pack"
    if lowered == "config":
        return "Config / infra precision coverage pack"
    if lowered in {"kotlin", "scala", "groovy"}:
        return "JVM language precision coverage pack"
    return "Native / mixed precision coverage pack"


def _version_bucket_token(value: str) -> str:
    token = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    return token or "any"


def _version_bucket_label(min_version: str, max_version: str) -> str:
    minimum = min_version.strip() or "any"
    maximum = max_version.strip() or "any"
    if minimum == maximum:
        return minimum
    return f"{minimum}-to-{maximum}"


@lru_cache(maxsize=1)
def coverage_campaign_descriptors() -> list[dict[str, Any]]:
    guardian_rules = _guardian_rule_entries()
    guardian_themes = [
        ("G-V1-COV-101", "guardian-coverage-saas", "SaaS integration credential corpus covering provider-specific secrets in runtime configs, deploy files, and CI handoff notes."),
        ("G-V1-COV-102", "guardian-coverage-cloud", "Cloud and infrastructure credential corpus spanning live ops surfaces, Terraform vars, and integration runtime state."),
        ("G-V1-COV-103", "guardian-coverage-automation", "Automation and CI credential corpus covering pipeline tokens, bot credentials, and service access keys."),
        ("G-V1-COV-104", "guardian-coverage-partners", "Partner ecosystem credential corpus spanning payments, messaging, maps, and collaboration providers."),
        ("G-V1-COV-105", "guardian-coverage-enterprise", "Enterprise admin credential corpus with mixed config formats, runtime secrets, and operational packaging."),
        ("G-V1-COV-106", "guardian-coverage-support", "Support and success operations credential corpus covering CRM, ticketing, and helpdesk automation providers."),
        ("G-V1-COV-107", "guardian-coverage-marketing", "Marketing and growth credential corpus covering analytics, ads, email, and campaign providers."),
        ("G-V1-COV-108", "guardian-coverage-data", "Data platform credential corpus spanning warehouses, ETL, observability, and ingestion providers."),
        ("G-V1-COV-109", "guardian-coverage-mobile", "Mobile and edge credential corpus covering notification, device, maps, and auth providers."),
        ("G-V1-COV-110", "guardian-coverage-security", "Security and platform credential corpus covering vault handoff, secrets brokers, and admin access providers."),
        ("G-V1-COV-111", "guardian-coverage-platform", "Platform credential corpus covering cloud runtime, SSO brokers, and internal developer platform providers."),
        ("G-V1-COV-112", "guardian-coverage-long-tail", "Long-tail provider credential corpus covering the remaining active Guardian families needed for truthful coverage."),
    ]

    descriptors: list[dict[str, Any]] = []
    for (scenario_id, repo_name, domain), chunk in zip(guardian_themes, _chunk(guardian_rules, 20), strict=False):
        entries = []
        pack_slug = repo_name.replace("_", "-")
        for index, rule in enumerate(chunk, start=1):
            path = _guardian_path(pack_slug, index, rule["rule_key"])
            entries.append(
                {
                    **rule,
                    "path": path,
                    "content": _entry_content({**rule, "path": path}),
                }
            )
        descriptors.append(
            _build_descriptor(
                scenario_id=scenario_id,
                milestone="M1",
                repo_name=repo_name,
                module="guardian",
                stack="Config / IaC / CI credential coverage bundle",
                domain=domain,
                summary=f"Guardian provider coverage bundle exercising {len(entries)} distinct secret families.",
                scan_kind="guardian",
                entries=entries,
                line_target="6000-9000",
            )
        )

    quantum_rules = _quantum_rule_entries()
    by_language: dict[str, list[dict[str, Any]]] = {}
    for rule in quantum_rules:
        by_language.setdefault(rule["language"], []).append(rule)

    native_rules = [rule for rule in quantum_rules if rule["language"] in _NATIVE_LANGS]
    used_rule_keys: set[str] = set()

    quantum_pack_defs: list[tuple[str, str, str, str, str, list[dict[str, Any]], int]] = [
        ("Q-V3-COV-101", "M3", "quantum-coverage-java-a", "Java / hybrid coverage pack", "Java crypto coverage pack A spanning block ciphers, RNG, keygen, KDF, inventory, and legacy primitives.", by_language.get("java", []), 25),
        ("Q-V3-COV-102", "M3", "quantum-coverage-java-b", "Java / hybrid coverage pack", "Java crypto coverage pack B extending legacy cipher, signature, and helper-driven rule families.", by_language.get("java", [])[25:], 25),
        ("Q-V3-COV-103", "M3", "quantum-coverage-csharp-a", "C# / hybrid coverage pack", "C# crypto and TLS coverage pack A spanning RNG, hash, cipher, key, and validation callback families.", by_language.get("csharp", []), 25),
        ("Q-V3-COV-104", "M3", "quantum-coverage-csharp-b", "C# / hybrid coverage pack", "C# crypto and TLS coverage pack B extending registration, key material, and inventory rule families.", by_language.get("csharp", [])[25:], 25),
        ("Q-V3-COV-105", "M3", "quantum-coverage-java-c", "Java / hybrid coverage pack", "Java crypto coverage pack C targeting remaining weak hash, cipher, JWT, XMLDSIG, and inventory families.", by_language.get("java", [])[50:], 30),
        ("Q-V3-COV-106", "M3", "quantum-coverage-java-d", "Java / hybrid coverage pack", "Java crypto coverage pack D targeting additional RSA/ECDSA, TLS, and key-material rule families.", by_language.get("java", [])[80:], 30),
        ("Q-V3-COV-107", "M3", "quantum-coverage-csharp-c", "C# / hybrid coverage pack", "C# crypto and TLS coverage pack C targeting additional delegate, provider, inventory, and weak primitive families.", by_language.get("csharp", [])[50:], 30),
        ("Q-V3-COV-108", "M3", "quantum-coverage-java-e", "Java / hybrid coverage pack", "Java crypto coverage pack E targeting late-slice Java rule families that remained uncovered after the earlier campaign waves.", by_language.get("java", [])[110:], 30),
        ("Q-V4-COV-101", "M4", "quantum-coverage-python-a", "Python / hybrid coverage pack", "Python crypto coverage pack A spanning hashlib, HMAC, secrets, JWT, and key-material rule families.", by_language.get("python", []), 20),
        ("Q-V4-COV-102", "M4", "quantum-coverage-python-b", "Python / hybrid coverage pack", "Python crypto coverage pack B extending TLS wrappers, kwargs passthrough, and legacy inventory families.", by_language.get("python", [])[20:], 20),
        ("Q-V4-COV-103", "M4", "quantum-coverage-polyglot-web", "TypeScript / JavaScript / Go coverage pack", "Polyglot web coverage pack spanning Node, TypeScript, JavaScript, and Go crypto/TLS families.", by_language.get("typescript", []) + by_language.get("javascript", []) + by_language.get("go", []), 30),
        ("Q-V4-COV-104", "M4", "quantum-coverage-python-c", "Python / hybrid coverage pack", "Python crypto coverage pack C targeting remaining digest, TLS, JWT, and key-material families.", by_language.get("python", [])[40:], 30),
        ("Q-V6-COV-101", "M6", "quantum-coverage-config", "Config / infra coverage pack", "Config-heavy quantum coverage pack spanning Envoy, Nginx, Apache, SSH, kube, JVM, and OpenSSL families.", by_language.get("config", []), 20),
        ("M-V8-COV-101", "M8", "quantum-coverage-native-a", "Native / mixed coverage pack", "Mixed native coverage pack A spanning Kotlin, Scala, Groovy, Ruby, Swift, C, and C++ rule families.", native_rules, 30),
        ("M-V8-COV-102", "M8", "quantum-coverage-native-b", "Native / mixed coverage pack", "Mixed native coverage pack B extending shell, PowerShell, PHP, Objective-C, Rust, Erlang, SQL, and workflow-adjacent rule families.", native_rules[30:], 30),
        ("M-V8-COV-103", "M8", "quantum-coverage-native-c", "Native / mixed coverage pack", "Mixed native coverage pack C extending remaining lesser-exercised native and scripting rule families.", native_rules[60:], 30),
        ("M-V8-COV-104", "M8", "quantum-coverage-native-d", "Native / mixed coverage pack", "Mixed native coverage pack D targeting additional Kotlin, Scala, Ruby, Rust, and C-family rule families.", native_rules[90:], 30),
        ("M-V8-COV-105", "M8", "quantum-coverage-native-e", "Native / mixed coverage pack", "Mixed native coverage pack E targeting remaining native and scripting quantum families that were still uncovered after earlier waves.", native_rules[120:], 30),
        ("M-V8-COV-106", "M8", "quantum-coverage-native-f", "Native / mixed coverage pack", "Mixed native coverage pack F targeting the tail of the native and scripting rule catalog to close the remaining surfaced-coverage gap.", native_rules[150:], 30),
    ]

    for scenario_id, milestone, repo_name, stack, domain, source_rows, limit in quantum_pack_defs:
        chunk = source_rows[:limit]
        if not chunk:
            continue
        used_rule_keys.update(rule["rule_key"] for rule in chunk)
        entries = []
        pack_slug = repo_name.replace("_", "-")
        for index, rule in enumerate(chunk, start=1):
            path = _quantum_path(rule["language"], pack_slug, index, rule)
            entries.append(
                {
                    **rule,
                    "path": path,
                    "content": _entry_content({**rule, "path": path}),
                }
            )
        descriptors.append(
            _build_descriptor(
                scenario_id=scenario_id,
                milestone=milestone,
                repo_name=repo_name,
                module="quantum",
                stack=stack,
                domain=domain,
                summary=f"Quantum coverage bundle exercising {len(entries)} distinct rule candidates across {stack.lower()}.",
                scan_kind="quantum",
                entries=entries,
                line_target="1200-1800",
            )
        )

    def _remaining(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [row for row in rows if row["rule_key"] not in used_rule_keys]

    def _append_chunked_quantum_descriptors(
        *,
        milestone: str,
        id_prefix: str,
        counter_start: int,
        repo_prefix: str,
        stack: str,
        domain_prefix: str,
        rows: list[dict[str, Any]],
        chunk_size: int,
    ) -> int:
        counter = counter_start
        for chunk_index, chunk in enumerate(_chunk(rows, chunk_size), start=1):
            if not chunk:
                continue
            scenario_id = f"{id_prefix}{counter:03d}"
            counter += 1
            repo_name = f"{repo_prefix}-{chunk_index:02d}"
            pack_slug = repo_name.replace("_", "-")
            entries = []
            for index, rule in enumerate(chunk, start=1):
                path = _quantum_path(rule["language"], pack_slug, index, rule)
                entries.append(
                    {
                        **rule,
                        "path": path,
                        "content": _entry_content({**rule, "path": path}),
                    }
                )
            descriptors.append(
                _build_descriptor(
                    scenario_id=scenario_id,
                    milestone=milestone,
                    repo_name=repo_name,
                    module="quantum",
                    stack=stack,
                    domain=f"{domain_prefix} wave {chunk_index:02d}",
                    summary=f"Quantum coverage bundle exercising {len(entries)} additional rule candidates across {stack.lower()}.",
                    scan_kind="quantum",
                    entries=entries,
                    line_target="1200-1800",
                )
            )
        return counter

    qv3_counter = 109
    qv3_counter = _append_chunked_quantum_descriptors(
        milestone="M3",
        id_prefix="Q-V3-COV-",
        counter_start=qv3_counter,
        repo_prefix="quantum-coverage-java-f",
        stack="Java / hybrid coverage pack",
        domain_prefix="Java crypto late-slice coverage pack",
        rows=_remaining(by_language.get("java", [])),
        chunk_size=20,
    )
    qv3_counter = _append_chunked_quantum_descriptors(
        milestone="M3",
        id_prefix="Q-V3-COV-",
        counter_start=qv3_counter,
        repo_prefix="quantum-coverage-csharp-d",
        stack="C# / hybrid coverage pack",
        domain_prefix="C# crypto and TLS late-slice coverage pack",
        rows=_remaining(by_language.get("csharp", [])),
        chunk_size=20,
    )

    qv4_counter = 105
    qv4_counter = _append_chunked_quantum_descriptors(
        milestone="M4",
        id_prefix="Q-V4-COV-",
        counter_start=qv4_counter,
        repo_prefix="quantum-coverage-python-d",
        stack="Python / hybrid coverage pack",
        domain_prefix="Python crypto and TLS late-slice coverage pack",
        rows=_remaining(by_language.get("python", [])),
        chunk_size=20,
    )
    qv4_counter = _append_chunked_quantum_descriptors(
        milestone="M4",
        id_prefix="Q-V4-COV-",
        counter_start=qv4_counter,
        repo_prefix="quantum-coverage-go-b",
        stack="Go / hybrid coverage pack",
        domain_prefix="Go crypto and TLS late-slice coverage pack",
        rows=_remaining(by_language.get("go", [])),
        chunk_size=15,
    )

    qv6_counter = 102
    _append_chunked_quantum_descriptors(
        milestone="M6",
        id_prefix="Q-V6-COV-",
        counter_start=qv6_counter,
        repo_prefix="quantum-coverage-config-b",
        stack="Config / infra coverage pack",
        domain_prefix="Config hardening late-slice coverage pack",
        rows=_remaining(by_language.get("config", [])),
        chunk_size=10,
    )

    mv8_counter = 107
    _append_chunked_quantum_descriptors(
        milestone="M8",
        id_prefix="M-V8-COV-",
        counter_start=mv8_counter,
        repo_prefix="quantum-coverage-native-g",
        stack="Native / mixed coverage pack",
        domain_prefix="Native and scripting late-slice coverage pack",
        rows=_remaining(native_rules),
        chunk_size=20,
    )

    precision_counters = {
        "M3": 201,
        "M4": 201,
        "M6": 201,
        "M8": 201,
    }
    precision_groups: dict[tuple[str, str, str], list[dict[str, Any]]] = {}
    for rule in quantum_rules:
        min_version = str(rule.get("applicable_min_version") or "").strip()
        max_version = str(rule.get("applicable_max_version") or "").strip()
        precision_groups.setdefault((rule["language"], min_version, max_version), []).append(rule)

    for (language, min_version, max_version), rows in sorted(
        precision_groups.items(),
        key=lambda item: (
            _coverage_milestone_for_language(item[0][0]),
            item[0][0],
            item[0][1],
            item[0][2],
        ),
    ):
        milestone = _coverage_milestone_for_language(language)
        id_prefix = _coverage_id_prefix_for_milestone(milestone)
        stack = _coverage_stack_for_language(language)
        bucket_label = _version_bucket_label(min_version, max_version)
        bucket_token = _version_bucket_token(bucket_label)
        for chunk_index, chunk in enumerate(_chunk(rows, 18), start=1):
            scenario_id = f"{id_prefix}{precision_counters[milestone]:03d}"
            precision_counters[milestone] += 1
            repo_name = f"quantum-precision-{language}-{bucket_token}-{chunk_index:02d}"
            pack_slug = repo_name.replace("_", "-")
            entries = []
            for index, rule in enumerate(chunk, start=1):
                path = _quantum_path(rule["language"], pack_slug, index, rule)
                entries.append(
                    {
                        **rule,
                        "path": path,
                        "content": _entry_content({**rule, "path": path}),
                    }
                )
            descriptors.append(
                _build_descriptor(
                    scenario_id=scenario_id,
                    milestone=milestone,
                    repo_name=repo_name,
                    module="quantum",
                    stack=stack,
                    domain=f"{language} version-sliced precision coverage pack ({bucket_label}) wave {chunk_index:02d}",
                    summary=f"Quantum precision coverage bundle exercising {len(entries)} {language} rule candidates within the {bucket_label} applicability slice.",
                    scan_kind="quantum",
                    entries=entries,
                    line_target="900-1400",
                )
            )

    return descriptors
