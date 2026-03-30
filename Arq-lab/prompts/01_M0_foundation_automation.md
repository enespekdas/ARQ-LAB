# M0 — Foundation automation and lab scaffold

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Arq-lab temel klasör yapısını, Python automation kodunu, Gitea/ARQ client'larını ve milestone orchestration omurgasını kurmak.

## Bu milestone için hedef repo sayısı

0 application repo, but full automation foundation

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


## Yapılacaklar

### 1) Arq-lab iskeletini kur
Şu klasörleri oluştur:

```text
Arq-lab/
  catalog/
  docs/
  generated/
  manifests/
  prompts/
  reports/
  runs/
  templates/
  tooling/
```

### 2) `.env.example` ve env loader yaz
En az şu değişkenleri destekle:
- `ARQ_API_BASE_URL`
- `ARQ_WORKSPACE_KEY`
- `ARQ_EMAIL`
- `ARQ_PASSWORD`
- `GITEA_BASE_URL`
- `GITEA_USERNAME`
- `GITEA_PASSWORD`
- `GITEA_OWNER`
- `GITEA_REPO_VISIBILITY`
- `ARQ_LAB_ROOT`
- `ARQ_LAB_PROJECT_KEY`
- `ARQ_LAB_PROJECT_NAME`

### 3) Python tooling yaz
`Arq-lab/tooling/` içinde aşağıdaki modülleri üret:

- `env.py`
- `models.py`
- `gitea_client.py`
- `git_factory.py`
- `arq_client.py`
- `scan_runner.py`
- `exporter.py`
- `comparator.py`
- `report_renderer.py`
- `orchestrate.py`

İsteğe bağlı:
- `logging_utils.py`
- `schemas.py`
- `manifests.py`

### 4) Gitea client contract
Desteklenecek işlemler:
- repo exists check
- repo create
- repo metadata read
- optional delete safeguard (default disable)
- push helper için clone/push URL üretimi

### 5) Git factory contract
Desteklenecek işlemler:
- repo init
- git config set
- default branch set main
- commit sequence apply
- branch create / checkout
- merge or divergence support
- tags (optional)
- final manifest üretimi

### 6) ARQ client contract
Desteklenecek işlemler:
- auth login
- project create or get
- application create or get
- application list/read helper
- scan create
- scan poll
- findings export json/csv
- finding detail
- finding occurrences

### 7) Comparison and reporting
Aşağıdaki formatları üret:
- `comparison.json`
- scenario `report.md`
- aggregate summary `reports/summary.md`
- machine summary `reports/summary.json`

### 8) Catalog bootstrap
Şu dosyaları oluştur veya güncelle:
- `catalog/scenario-index.yaml` veya `.json`
- `catalog/milestone-status.json`
- `catalog/report-contract.md`

### 9) Execution entrypoint
Tek komutla milestone koşabilen bir entrypoint yaz:
- örn. `python -m tooling.orchestrate --milestone M1`
veya eşdeğeri.

### 10) Dry-run mode
Gerçek çevreye dokunmadan manifest üretebilen bir `--dry-run` desteği ekle.

## Kod kalitesi beklentisi

- Python 3.11+ uyumlu
- tip ipuçları ekle
- açıklayıcı exception handling
- structured logs
- retry/backoff
- idempotent resource create

## Çıktılar

Bu milestone sonunda en az şunları bırak:
- çalışan tooling kodu
- `.env.example`
- `README.md`
- örnek empty run
- basic smoke command listesi

## Rapor

Milestone sonunda `reports/M0-foundation.md` üret:
- ne kuruldu
- hangi komutlar var
- neler gerçek çalıştırıldı
- neler sadece hazırlandı
- eksik env veya servis var mı
