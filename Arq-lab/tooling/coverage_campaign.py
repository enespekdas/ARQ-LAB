from __future__ import annotations

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


def _guardian_path(pack_slug: str, index: int) -> str:
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
    if (
        "dependency inventory" in title
        or detector_type == "manifest"
        or variant in {"java_dependency_manifest", "java_dependency", "jvm_jwt_libs", "jvm_xmldsig_saml", "bc_pqc", "node_xmlsig", "thirdparty_jose", "go_jose_thirdparty", "go_pqc", "ruby_saml_xmldsig", "php_xmldsig_saml", "rust_pqc", "erlang_jose", "liboqs"}
        or ecosystem in {"java_dependency_manifest", "java_dependency", "jvm", "npm", "pip", "nuget", "go_modules", "gems", "composer", "crates", "hex", "liboqs"}
    ):
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


def _is_quantum_key_material(entry: dict[str, Any]) -> bool:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "")
    return "key material artifact" in title or "private key" in title or "begin private key" in sample.lower()


def _java_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    parameter = str(entry.get("parameter") or "").strip()
    algorithm = str(entry.get("algorithm") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    variant = _rule_variant(entry).lower()
    keywords = _rule_keywords(entry)
    bits = _first_int(title, sample) or 1024
    if _is_quantum_key_material(entry):
        return _PEM_BLOB
    if "dependency inventory" in title:
        return parameter or sample
    if variant == "java_bouncycastle":
        target = parameter or algorithm or _first_keyword(entry, "RSA")
        if "cipher.getinstance" in anchor.lower() or "aead inventory" in title or "aes mode" in title:
            return '\n'.join(
                [
                    "Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());",
                    f'Cipher.getInstance("{target or "ChaCha20-Poly1305"}", "BC");',
                ]
            )
        if "keypairgenerator" in anchor.lower() or "asymmetric keygen inventory" in title:
            return '\n'.join(
                [
                    "Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());",
                    f'KeyPairGenerator.getInstance("{target or "RSA"}", "BC");',
                ]
            )
        return '\n'.join(
            [
                "Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());",
                anchor or sample or "\n".join(keywords[:2]) or "Signature.getInstance(\"SHA256withRSA\", \"BC\");",
            ]
        )
    if "aead inventory" in title:
        return anchor or 'Cipher.getInstance("ChaCha20-Poly1305");'
    if "aes mode" in title:
        mode = parameter or "AES/GCM/NoPadding"
        return f'Cipher.getInstance("{mode}");'
    if "asymmetric keygen inventory" in title:
        target = parameter or algorithm or "RSA"
        return anchor or f'KeyPairGenerator.getInstance("{target}");'
    if "crypto usage inventory" in title:
        return anchor or 'KeyPairGenerator.getInstance("RSA");'
    if "shor target signature inventory" in title:
        target = parameter or algorithm or "SHA256withRSA"
        return anchor or f'Signature.getInstance("{target}");'
    if "hash inventory" in title:
        target = parameter or algorithm or "SHA-256"
        return f'MessageDigest.getInstance("{target}");'
    if "ec curve inventory" in title:
        target = parameter or "secp256r1"
        return f'new ECGenParameterSpec("{target}");'
    if "kdf inventory" in title:
        target = parameter or "PBKDF2WithHmacSHA256"
        return f'SecretKeyFactory.getInstance("{target}");'
    if "keystore type inventory" in title:
        target = parameter or "JKS"
        return f'KeyStore.getInstance("{target}");'
    if "mac inventory" in title:
        target = parameter or "HmacSHA256"
        return f'Mac.getInstance("{target}");'
    if "tls & store system properties" in title:
        return '\n'.join(
            [
                'System.setProperty("javax.net.ssl.keyStore", "legacy.jks");',
                'System.setProperty("javax.net.ssl.keyStorePassword", "changeit");',
                'System.setProperty("javax.net.ssl.trustStore", "legacy-truststore.jks");',
                'System.setProperty("javax.net.ssl.trustStorePassword", "changeit");',
            ]
        )
    if "symmetric key size inventory" in title:
        size = bits if bits >= 128 else 256
        return f'KeyGenerator.getInstance("AES").init({size});'
    if "xdh parameter inventory" in title:
        return anchor or 'NamedParameterSpec.X25519'
    if "hardcoded symmetric key" in title:
        return 'byte[] keyBytes = Base64.getDecoder().decode("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVo=");'
    if "rsa keysize" in title:
        return f'KeyPairGenerator.getInstance("RSA").initialize({bits});'
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
    return sample or f'// coverage placeholder for {entry["rule_key"]}'


def _csharp_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    parameter = str(entry.get("parameter") or "").strip()
    algorithm = str(entry.get("algorithm") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    keywords = _rule_keywords(entry)
    bits = _first_int(title, sample) or 1024
    if _is_quantum_key_material(entry):
        return _PEM_BLOB
    if "bouncycastle" in title and "inventory" in title:
        return anchor or "using Org.BouncyCastle.Crypto;"
    if "jwt: rs256/es256" in title:
        return 'var alg = SecurityAlgorithms.RsaSha256;\nvar alt = SecurityAlgorithms.EcdsaSha256;'
    if "jwt: hs256" in title:
        return 'var alg = SecurityAlgorithms.HmacSha256;'
    if "token validation disabled" in title:
        return "new TokenValidationParameters { ValidateIssuerSigningKey = false, ValidateAudience = false };"
    if "using: system.security.cryptography" in title:
        return "using System.Security.Cryptography;"
    if "rsa pkcs#1 v1.5" in title:
        return "var padding = RSAEncryptionPadding.Pkcs1;"
    if "rsa: all rsa usage" in title:
        return "RSA.Create();"
    if "bouncycastle pqc" in title:
        return "var pqc = new KyberKeyPairGenerator();\nvar pqcAlt = \"Dilithium\";"
    if "random" in title or "rng" in title:
        return "new Random().Next();"
    if "servercertificatevalidationcallback" in title:
        return "ServicePointManager.ServerCertificateValidationCallback += (_, _, _, _) => true;"
    if "servicepointmanager" in title and "tls" in title:
        return "ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3 | SecurityProtocolType.Tls;"
    if "dangerousacceptany" in title or "trust bypass" in title:
        return "handler.ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator;"
    if "passwordderivebytes" in title or "pbkdf1" in title:
        return 'new PasswordDeriveBytes("legacy-password", new byte[] {1,2,3,4});'
    if "md5" in title:
        return "MD5.Create();"
    if "sha1" in title or "sha-1" in title:
        return "SHA1.Create();"
    if "ecb" in title:
        return "new AesManaged { Mode = CipherMode.ECB };"
    if "rc4" in title or "arc4" in title:
        return 'RC4.Create();'
    if "3des" in title or "tripledes" in title:
        return "TripleDES.Create();"
    if "des" in title:
        return "DES.Create();"
    if "rsa keysize" in title:
        return f"RSA.Create({bits});"
    if "ecdsa" in title and "inventory" in title:
        return anchor or "ECDsa.Create();"
    if "ecdiffiehellman" in title and "inventory" in title:
        return anchor or "ECDiffieHellman.Create();"
    if "hmacmd5" in title:
        return "new HMACMD5();"
    if "hardcoded symmetric key/iv" in title:
        return "var aes = Aes.Create(); aes.Key = new byte[] {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6};"
    if "jwt" in title and "inventory" in title:
        return '\n'.join(['var jwtLibrary = "System.IdentityModel.Tokens.Jwt";', 'var alg = "RS256";', *keywords[:2]])
    return sample or f"// coverage placeholder for {entry['rule_key']}"


def _python_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    parameter = str(entry.get("parameter") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    keywords = _rule_keywords(entry)
    bits = _first_int(title, sample) or 1024
    if _is_quantum_key_material(entry):
        return _PEM_BLOB
    if "import: ssl module" in title:
        return "import ssl"
    if "import: hashlib" in title:
        return "import hashlib"
    if "import-only" in title:
        return anchor or sample
    if "urllib3" in title and "certificate verification disabled" in title:
        return 'urllib3.PoolManager(cert_reqs="CERT_NONE", assert_hostname=False)'
    if "pyopenssl" in title and "verify_none" in title:
        return "ctx.set_verify(SSL.VERIFY_NONE, lambda *args: True)"
    if "paramiko" in title and "autoaddpolicy" in title:
        return "client.set_missing_host_key_policy(paramiko.AutoAddPolicy())"
    if "random: non-cryptographic rng" in title:
        return "random.Random().randint(1, 9)"
    if "python-rsa" in title and "weak rsa key size" in title:
        return f"rsa.newkeys({bits})"
    if "os.urandom usage" in title:
        return "os.urandom(32)"
    if "jwt" in title and "inventory" in title:
        return '\n'.join(['import jwt', 'jwt.encode({"sub": "coverage"}, "secret", algorithm="RS256")', *keywords[:2]])
    if "cryptography: pkcs1v15" in title:
        return "padding.PKCS1v15()"
    if "verify=false" in title or "trust bypass" in title:
        return 'requests.get("https://partner.example", verify=False)'
    if "cert_none" in title:
        return "ssl_context.verify_mode = ssl.CERT_NONE"
    if "unverified_context" in title:
        return "ssl._create_unverified_context()"
    if "protocol_tls" in title or "protocol_sslv3" in title:
        return "ssl.SSLContext(ssl.PROTOCOL_TLSv1)"
    if "pbkdf2" in title and "low iter" in title:
        return 'hashlib.pbkdf2_hmac("sha1", b"pw", b"salt", 1000)'
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
    if "jwt" in title and "inventory" in title:
        return 'jwt.encode({"sub": "coverage"}, "secret", algorithm="HS256")'
    if "xmldsig" in title or "saml" in title:
        return "\n".join(["import xmlsec", *keywords[:3]]) if keywords else "import xmlsec"
    return sample or f"# coverage placeholder for {entry['rule_key']}"


def _typescript_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    keywords = _rule_keywords(entry)
    if _is_quantum_key_material(entry):
        return _PEM_BLOB
    if "jwt" in title and "inventory" in title:
        return 'const jwtLib = "jsonwebtoken";\nconst algorithm = "RS256";\nconst alternate = "ES256";'
    if "xmldsig" in title or "saml" in title:
        return anchor or '\n'.join(['const xmlCryptoPackage = "xml-crypto";', 'const samlLibrary = "samlify";', *keywords[:2]])
    if "node_tls_reject_unauthorized" in title or "rejectunauthorized" in title:
        return "process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';"
    if "rsa-sha1" in title or "md5" in title and "createsign" in title:
        return 'crypto.createSign("RSA-SHA1").update("legacy");'
    if "rejectunauthorized" in title or "trust bypass" in title:
        return "const opts = { rejectUnauthorized: false }; https.request(opts);"
    if "md5" in title:
        return 'crypto.createHash("md5").update("legacy").digest("hex");'
    if "sha1" in title or "sha-1" in title:
        return 'crypto.createHash("sha1").update("legacy").digest("hex");'
    if "xmldsig" in title or "saml" in title:
        return 'const xmlSignatureAlgorithm = "rsa-sha1";'
    if "jwt" in title and "inventory" in title:
        return 'const alg = "RS256";'
    return sample or f"// coverage placeholder for {entry['rule_key']}"


def _javascript_sample(entry: dict[str, Any]) -> str:
    return _typescript_sample(entry)


def _go_sample(entry: dict[str, Any]) -> str:
    title = _rule_title(entry)
    sample = str(entry.get("sample") or "").strip()
    parameter = str(entry.get("parameter") or "").strip()
    anchor = str(entry.get("evidence_anchor") or "").strip()
    keywords = _rule_keywords(entry)
    bits = _first_int(title, sample) or 1024
    if _is_quantum_key_material(entry):
        return _PEM_BLOB
    if "jwt rs/es inventory" in title:
        return "jwt.SigningMethodRS256\njwt.SigningMethodES256"
    if "pqc library inventory" in title:
        return 'import "github.com/cloudflare/circl/sign/dilithium"\n// kyber dilithium liboqs'
    if "insecureskipverify" in title or "trust bypass" in title:
        return "tls.Config{InsecureSkipVerify: true}"
    if "rsa key size" in title or "legacy rsa key size" in title:
        return f"rsa.GenerateKey(rand.Reader, {bits})"
    if "md5" in title:
        return 'md5.Sum([]byte("legacy"))'
    if "sha1" in title or "sha-1" in title:
        return 'sha1.Sum([]byte("legacy"))'
    if "random" in title or "rng" in title:
        return "rand.New(rand.NewSource(7)).Int()"
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
    return sample or f"// coverage placeholder for {entry['rule_key']}"


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
    return sample or "# coverage config placeholder"


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
    if language == "config":
        return _config_sample(entry)
    if _is_quantum_key_material(entry):
        return _PEM_BLOB
    sample = str(entry.get("sample") or "").strip()
    return sample or f"coverage::{entry['rule_key']}"


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
        return "\n".join([*_coverage_evidence_lines(entry, comment), snippet.rstrip(), ""])
    stem = Path(path).stem.replace("-", "_")
    evidence_lines = _coverage_evidence_lines(entry, comment)
    if language == "java":
        return "\n".join(
            [
                "package legacy.coverage;",
                "import java.security.*;",
                "import java.util.*;",
                "import javax.crypto.*;",
                "import javax.net.ssl.*;",
                "import java.util.Base64;",
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
        return "\n".join(
            [
                "using System;",
                "using System.Net;",
                "using System.Net.Http;",
                "using System.Security.Cryptography;",
                "using System.Net.Security;",
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
        return "\n".join(
            [
                "import hashlib",
                "import random",
                "import ssl",
                "import requests",
                "from Crypto.Cipher import AES, ARC4, DES, DES3, Blowfish",
                "import jwt",
                "from cryptography.hazmat.primitives.asymmetric import rsa",
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
                'import ("crypto/des"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5")',
                "func ExecuteCoverage() any {",
                *[f"    {line}" for line in evidence_lines],
                _indented(snippet, "    "),
                "    return nil",
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
        regex = item.get("regex")
        if not isinstance(regex, str) or not regex.strip():
            continue
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
    ]

    descriptors: list[dict[str, Any]] = []
    for (scenario_id, repo_name, domain), chunk in zip(guardian_themes, _chunk(guardian_rules, 20), strict=False):
        entries = []
        pack_slug = repo_name.replace("_", "-")
        for index, rule in enumerate(chunk, start=1):
            path = _guardian_path(pack_slug, index)
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
                line_target="7000-10000",
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
                    line_target="7000-10000",
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

    return descriptors
