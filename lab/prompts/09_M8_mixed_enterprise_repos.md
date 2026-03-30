# M8 — Mixed enterprise repositories

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Gerçek müşteri ortamını en yakından taklit eden, hem Guardian hem Quantum sinyallerini aynı repo'da barındıran orta-büyük karma repo'lar üretmek ve operasyonel usefulness seviyesini ölçmek.

## Bu milestone için hedef repo sayısı

2 repo

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


## Bu milestone neden önemli

Önceki milestone'lar kontrollü ve hedefliydi. Burada amaç:
- aynı repo içinde çoklu teknoloji
- hem secrets hem crypto/TLS/config sinyalleri
- docs/tests/vendor/infrastructure gürültüsü
- analist açısından triage edilebilirlik

## Repo 1 — M-V8-001 — internal-platform-monorepo

### Stack
- Java service
- Node/TypeScript backend or admin API
- Python worker
- shared config
- docs
- CI scripts
- deployment manifests

### Target size
Toplam 10k–20k satır.

### Must include Guardian positives
- birkaç gerçek secret in live surfaces
- en az bir key material
- en az bir generic secret
- near-real negatives across docs/tests/examples

### Must include Quantum positives
- en az iki gerçek insecure crypto/TLS/config misuse
- farklı dil/stack'lerde dağıtılmış
- explainability assert edilebilir olmalı

### Must include negatives
- docs
- vendor/generated folder
- test-only mocks
- secure alternatives

## Repo 2 — M-V8-002 — infra-app-mixed-repo

### Stack
- application code
- helm
- k8s
- YAML/properties/env
- pipeline scripts
- shell/PowerShell
- maybe small SQL or migration layer

### Target size
Toplam 8k–15k satır.

### Focus
- infra + app together
- live config secrets
- TLS/config misuse
- docs/example negatives
- branch with temporary hotfix and release branch

## Scan plan

Her repo için en az:
- Guardian head snapshot
- Quantum head snapshot

Senaryoya uygunsa ek olarak:
- Guardian ref history
- Guardian all branches

## Reporting focus

Bu milestone raporunda ayrıca şu sorular cevaplanmalı:
- Noise analyst'i boğuyor mu?
- Explainability operasyonel olarak yeterli mi?
- Mixed repo'da findings ayrışıyor mu?
- Hangi finding'ler immediate action, hangileri tuning candidate?

## Output

- repo-level reports
- one executive-style aggregate report
- one tuning backlog seed file
