# M3 — Quantum weak crypto — Java and C#

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Quantum için Java ve C# ekosistemlerinde gerçek uygulama hissi veren repo'larda weak algorithm, insecure mode, weak KDF, weak RNG ve explainability kalitesini zorlayıcı biçimde test etmek.

## Bu milestone için hedef repo sayısı

3 repo

## Çalışma kökü

Tüm çıktılar `Arq-lab/` altında olacak. `ARQ-SEC` repo klasörüne dokunma.

## Ortak zorunlu kurallar

- `00_master_agent_brief.md` içindeki kurallara uy.
- `.env` üzerinden Gitea ve ARQ ayarlarını oku.
- Gitea varsayılan username/password: `arq` / `arq`.
- Gitea base URL varsayılanı: `http://localhost:3000`.
- Repo'ları Gitea'da **public** oluştur.
- ARQ application create için `providerType = GENERIC_GIT` kullan.
- `repositoryLocator` olarak Gitea clone URL kullan.
- Mevcut `Arq-lab/` içeriğini bozma; idempotent genişlet.
- Başarısız network/execution varsa uydurma sonuç yazma; hata kaydı bırak.


## Bu milestone'da özellikle zorlayacağın şeyler

- weak / deprecated algorithms
- insecure mode / padding
- crypto misuse in live execution path
- near-real ama safe alternatifler
- comments/docs/dead code FP tuzakları
- explainability alanlarının kalitesi

## Global scan plan

Her repo için:
- `modules = ["quantum"]`
- `scanMode = "HEAD_SNAPSHOT"`
- `branchScope = "SINGLE_BRANCH"`
- `refName = "main"`

## Quantum explainability contract

Her quantum repo için `validation/explainability-contract.json` üret.
Assertion alanları:
- `detectionSource`
- `semanticKey`
- `resolvedValue`
- `resolutionScope`
- `queryFamily`
- `rawEvidenceJson`

## Repo 1 — Q-V3-JAVA-001 — identity-gateway-java

### Stack
- Java 21
- Spring Boot
- Maven wrapper
- JWT/auth/session modules
- test coverage
- docs + deploy

### Realistic domain
Identity gateway serving token issuance, session bridging, partner auth callbacks.

### Must include real risky patterns
- `MessageDigest.getInstance("MD5")` in a live auth/session helper
- `MessageDigest.getInstance("SHA-1")` in a signature/fingerprint path
- `Cipher.getInstance("AES/ECB/PKCS5Padding")` in live token encryption/helper code
- weak RNG pattern in security-sensitive path
- ideally one KDF / password helper using weak or legacy parameters

### Must include safe controls
- SHA-256 or SHA-512 safe helper
- AES-GCM or CBC-with-integrity wrapper
- `SecureRandom` safe path
- secure auth module that should stay clean

### Must include negative traps
- comments mentioning `AES/ECB`
- docs snippet
- disabled old helper not wired into runtime
- tests with example algorithm names

### Explainability expectation
- queryFamily Java JCA/TLS appropriate olmalı
- resolvedValue gerçek çağrıyla uyumlu olmalı
- semanticKey grouping mantıklı olmalı

## Repo 2 — Q-V3-JAVA-002 — legacy-payment-crypto-java

### Stack
Java / Spring Boot + internal crypto utilities.

### Realistic domain
Legacy payment encryption and key management helpers.

### Must include real risky patterns
- DES or 3DES live helper
- `PBEWithMD5AndDES`
- weak key spec or legacy secret key material pattern
- insecure padding/mode combo
- live usage path, not just dormant utility

### Must include safe controls
- replacement helper using modern primitives
- secure configuration class
- tests proving modern path

### Must include negative traps
- migration docs
- deprecated package retained but not wired
- sample code under docs/examples

## Repo 3 — Q-V3-CS-003 — billing-sdk-csharp

### Stack
- .NET 8
- solution with 2-3 projects
- test project
- appsettings / docs / scripts

### Realistic domain
Billing partner SDK and token signing library.

### Must include real risky patterns
- `MD5.Create()`
- `SHA1.Create()`
- `Aes.Mode = CipherMode.ECB`
- `new Random()` for OTP or reset token in security path
- optionally weak password hashing helper

### Must include safe controls
- `RandomNumberGenerator`
- `SHA256`
- modern HMAC or AEAD path

### Must include negative traps
- docs snippets
- tests-only legacy samples
- variable names like `legacySha1Disabled` that should not trigger by itself

## Repo size and realism

Her repo:
- 5k–10k total lines
- layered code
- multiple modules/projects
- real build files
- real tests
- configs and docs
- not one-file demos

## Gitea tasks

- create repos as public
- push main
- record repo URLs and commit SHAs

## ARQ tasks

- create/reuse apps
- run quantum scans
- export findings json
- fetch finding details for all expected positives
- evaluate explainability contract

## Comparison requirements

`comparison.json` içinde ayrıca:
- `explainabilityFailures`
- `unexpectedRegexOnlyFindings`
- `safeControlViolations`
alanları olsun.

## Fail criteria

- must-find crypto misuse missing
- safe controls finding alıyorsa
- docs/comments-only surface finding alıyorsa
- explainability contract kritik alanları boşsa
