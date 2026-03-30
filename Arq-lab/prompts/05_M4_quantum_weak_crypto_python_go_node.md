# M4 — Quantum weak crypto — Python, Go, Node

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Quantum için Python, Go ve Node/TypeScript ekosistemlerinde gerçekçi security ve platform servislerinde weak crypto, weak RNG, unsafe hash ve near-real negative ayrımını test etmek.

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


## Amaç

Java dışındaki yaygın müşteri stack'lerinde Quantum'un saha doğruluğunu zorlamak.

## Repo 1 — Q-V4-PY-001 — notification-signer-python

### Stack
- Python 3.11
- FastAPI + worker
- pytest
- pyproject
- app/services/clients/tests/docs/deploy

### Domain
Webhook signing ve outbound notification auth helper.

### Must include risky patterns
- `hashlib.md5(...)`
- weak token generation in security path
- insecure signature helper using legacy hash
- live usage route through service/client code

### Safe controls
- `hashlib.sha256`
- `secrets.token_urlsafe`
- modern signing helper

### Negative traps
- docs snippets
- string constants mentioning `md5`
- dead helper not wired to runtime
- test fixtures

## Repo 2 — Q-V4-GO-002 — device-provisioning-go

### Stack
- Go 1.22
- cmd/, internal/, pkg/, tests/, deploy/, docs/
- makefile

### Domain
Device provisioning and bootstrap credential service.

### Must include risky patterns
- md5 / sha1 in live security-related path
- weak PBKDF2 or low-iteration derivation
- insecure helper for auth or device claim signing
- live config wiring

### Safe controls
- secure hash or HMAC path
- secure RNG
- proper TLS helper

### Negative traps
- comments
- examples
- mock service
- unsupported but benign helper

## Repo 3 — Q-V4-TS-003 — customer-portal-node

### Stack
- TypeScript
- Node backend
- Jest
- src/modules/common/config/docs

### Domain
Customer portal backend with password reset, signed links, partner callback validation.

### Must include risky patterns
- md5-based hashing or fingerprint helper in live path
- `Math.random()` used for security-sensitive token or reset code
- insecure cipher algorithm string like `aes-128-ecb` in live helper
- optionally weak JWT/crypto helper

### Safe controls
- crypto-secure random path
- secure hash or HMAC path
- safe encryption utility

### Negative traps
- README snippet
- commented examples
- test-only `md5` references
- variable names that should not trigger alone

## Explainability

For all expected positives:
- fetch finding detail
- assert explainability block exists
- ensure `resolvedValue` matches live insecure primitive where available
- record `detectionSource` distribution per repo

## Realism rules

- each repo 5k+ total lines
- actual module structure
- non-trivial tests
- docs and deploy configs
- realistic package/import layout

## Output

- reports per repo
- one aggregate report `reports/M4-quantum-weak-crypto-polyglot.md`
- summary table with TP/FP/FN per language
