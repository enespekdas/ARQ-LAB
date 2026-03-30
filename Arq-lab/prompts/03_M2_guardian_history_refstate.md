# M2 — Guardian history ref-state dedup

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Guardian için history-only, head-only, head+history, branch divergence ve PEM rotation/dedup davranışını gerçek git graph üzerinde doğrulamak.

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


## Bu milestone'un özü

Bu milestone snapshot değil, **git lineage validation** milestone'udur.

Ayrı folder snapshot'ı yetmez. Gerçek:
- commit sırası
- branch divergence
- secret ekleme/silme
- PEM rotation
- same lineage vs new lineage

oluşturulmalı.

## Global scan plan

Her repo için en az iki koşu planla:

1. Guardian `HEAD_SNAPSHOT`
2. Guardian `REF_HISTORY`

Gerekli olan repo'larda ayrıca:
3. Guardian `ALL_BRANCHES` + `HEAD_SNAPSHOT`

## Repo 1 — G-V2-HIST-001 — payments-history-lineage

### Stack
Java / Spring Boot, 5k+ total lines.

### Goal
Bir secret history'de kalacak ama head'de olmayacak.

### Commit plan
- `c001`: bootstrap repo
- `c002`: live partner access token ekle
- `c003`: docs noise ekle
- `c004`: token'ı kaldır ve güvenli referansla değiştir
- `c005`: unrelated refactor

### Expected behavior
- head snapshot sonucu: history-only secret görünmemeli veya presentOnHead false olacak şekilde doğru modellenmeli (ürün contract'ına göre değerlendir)
- ref history sonucu:
  - secret finding bulunmalı
  - `presentInHistory = true`
  - `presentOnHead = false`
  - exposure scope `HISTORY_ONLY`

### Near-real negatives
- README token example
- masked logs
- test fixtures

## Repo 2 — G-V2-HIST-002 — partner-branch-divergence

### Stack
Node / TypeScript, 5k+ total lines.

### Goal
main temiz, feature branch kirli; single-branch ve all-branches davranışı ayrışmalı.

### Branch plan
- `main`: clean baseline
- `feature/partner-hotfix`: temporary secret leaked
- `release/2026.04`: clean release branch
- optionally `feature/docs-refresh`: noise-only branch

### Expected behavior
- `SINGLE_BRANCH` main scan: leak görünmemeli
- `ALL_BRANCHES` scan: feature branch leak görünmeli
- duplicate explosion olmamalı
- ref-state bilgisi tutarlı olmalı

### Must include
- gerçek branch-only secret
- docs/test/example near-real negatives

## Repo 3 — G-V2-HIST-003 — pem-rotation-lineage

### Stack
Python service + ops config, 5k+ total lines.

### Goal
PEM rotation, canonicalization ve dedup continuity test etmek.

### Commit plan
- `c001`: bootstrap
- `c002`: PEM A ekle
- `c003`: formatting / line wrap değişikliği
- `c004`: PEM A kaldır, PEM B ekle
- `c005`: docs example PEM ekle
- `c006`: safe cleanup

### Expected behavior
- PEM A ve PEM B lineage'ı karıştırılmamalı
- line wrap veya whitespace değişimi gereksiz duplicate üretmemeli
- docs example finding üretmemeli
- final head durumuna göre doğru exposure modelling yapılmalı

## Required validation artifacts per repo

- `validation/branch-plan.yaml` commit-by-commit detaylı olmalı
- `validation/expected-findings.json` Guardian export alanlarını assert etmeli:
  - `presentOnHead`
  - `presentInHistory`
  - `exposureScope`
- `validation/expected-absent.json`
- `validation/expected-report.md` history anlatımı içermeli

## Git assembly requirement

Bu milestone için agent:
- overlay/commit plan mantığı kurmalı
- her repo için gerçek git commit graph üretmeli
- branch SHA manifest'i çıkarmalı
- `manifests/git-graphs-M2.json` dosyası üretmeli

## Gitea and ARQ execution

- Repos Gitea'ya push edilecek
- Applications create/reuse edilecek
- Aşağıdaki koşular senaryoya göre yapılacak:
  - head snapshot / main
  - ref history / main
  - all branches / guardian

## Raporlama zorunluluğu

Her repo raporu şu özel alanları içersin:
- branch graph summary
- commit timeline
- expected exposure model
- actual exposure model
- dedup verdict
- ref-state verdict

## Fail criteria

Aşağıdakilerden biri varsa fail:
- history-only finding head-only gibi görünüyorsa
- all-branches ile single-branch ayrımı kayboluyorsa
- PEM rotation duplicate patlaması yaratıyorsa
- docs/test/example surfaces finding alıyorsa
