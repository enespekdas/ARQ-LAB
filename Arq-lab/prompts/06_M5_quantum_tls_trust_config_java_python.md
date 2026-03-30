# M5 — Quantum TLS / trust / config — Java and Python

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Quantum'un trust bypass, certificate validation disable, insecure SSL context ve config-wired TLS misuse yakalama kabiliyetini Java ve Python repo'larında test etmek.

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


## Bu milestone'un farkı

Burada sadece API adı görmek yetmez. Senaryolar, **runtime'a gerçekten bağlanan** trust/TLS misuse içermeli.

## Repo 1 — Q-V5-JAVA-001 — partner-client-java

### Stack
Java / Spring Boot / Maven.

### Domain
External partner API client and settlement sync service.

### Must include real risky patterns
- custom trust-all `X509TrustManager`
- hostname verification disable
- insecure HTTP client builder (OkHttp, Apache HttpClient, RestTemplate/SSL context)
- live usage path from config/service into actual client

### Safe controls
- secure HTTP client builder
- production-safe certificate pinning or proper trust store path
- test-only insecure helper separated clearly

### Negative traps
- docs snippets
- disabled code path
- tests-only bypass
- commented legacy workaround

## Repo 2 — Q-V5-PY-002 — data-sync-python

### Stack
Python 3.11 / worker service.

### Domain
Data sync worker pulling from partner APIs and webhooks.

### Must include real risky patterns
- `requests(..., verify=False)` in live path
- insecure `httpx` or `urllib3` verification disable
- ssl context with `check_hostname = False` / cert validation off
- warnings suppression tied to insecure path

### Safe controls
- secure session wrapper
- trusted CA path config
- test-only mock clients

### Negative traps
- sample scripts
- docs
- dead helper
- comment-only code fences

## Repo 3 — Q-V5-JAVA-003 — gateway-config-java

### Stack
Java + YAML/properties config heavy.

### Domain
Gateway or edge integration service with environment-driven HTTP client settings.

### Must include real risky patterns
- insecure YAML/properties flag wired into runtime
- environment profile enabling trust bypass in prod-like active config
- config bean consumes value and actually applies it

### Must include safe controls
- safe default profile
- dev-only profile separated and clearly inactive
- secure config sample

### Negative traps
- dormant sample config
- commented alternative config
- docs table with `verify=false` as example text

## Validation focus

Expected assertions include:
- finding exists on live wired misuse
- inventory-only dormant values do not create same-level risk finding
- explainability `resolutionScope` and `queryFamily` are meaningful

## Output

Aggregate report:
- `reports/M5-quantum-tls-java-python.md`
- include per-scenario "runtime wired?" explanation
