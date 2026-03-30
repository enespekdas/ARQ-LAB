# M6 — Quantum TLS / trust / config — Node, C#, config-heavy repos

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Node, C# ve config-ağırlıklı repo yüzeylerinde TLS verification disable, trust bypass ve inventory-only vs gerçek risk ayrımını test etmek.

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


## Repo 1 — Q-V6-TS-001 — customer-portal-node-tls

### Stack
TypeScript / Node backend.

### Domain
Customer portal backend calling external billing and profile APIs.

### Must include real risky patterns
- `rejectUnauthorized: false`
- custom `https.Agent` insecure setup
- axios/fetch wrapper that passes insecure agent into live client path

### Safe controls
- secure client wrapper
- dev-only mock transport that is not active
- safe config default

### Negative traps
- README examples
- non-executable config samples
- test-only mock transport

## Repo 2 — Q-V6-CS-002 — admin-integrations-csharp

### Stack
.NET 8 solution.

### Domain
Admin integration service consuming partner APIs.

### Must include real risky patterns
- `ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator`
  veya eşdeğer bypass
- callback returning `true`
- live service registration path

### Safe controls
- secure `HttpClientFactory` registration
- proper cert validation path
- test project mock client

### Negative traps
- docs
- dead example code
- configuration names that look insecure but are disabled

## Repo 3 — Q-V6-CONFIG-003 — edge-gateway-config

### Stack
Config-heavy repo with YAML/properties/appsettings/helm/env.

### Domain
Edge gateway deployment and application config.

### Must include real risky patterns
- prod-like active config with verify disable or weak protocol setting
- runtime-consumed flags
- helm values or appsettings entries that are actually mapped in code or documented as active runtime

### Must include inventory-only negatives
- dormant sample values
- alternate environment example files
- safe active config with unsafe commented examples

## Validation focus

Bu milestone'da ayrıca aşağıdaki ayrımı raporla:
- live exploit-relevant misuse
- config capability only
- dormant sample config
- documentation-only text

## Output

- scenario reports
- one matrix-style aggregate report comparing Node vs C# vs config-only surfaces
