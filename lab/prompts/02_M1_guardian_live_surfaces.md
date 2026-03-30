# M1 — Guardian realistic live surfaces

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Guardian için gerçek uygulama hissi veren, hem gerçek secret hem de near-real negative yüzeyleri barındıran orta büyüklükte repo paketleri üretmek; Gitea'ya push etmek; ARQ application create ve head snapshot scan tetiklemek; findings'i expected contract ile kıyaslamak.

## Bu milestone için hedef repo sayısı

4 repo

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


## Repo üretim standardı

Her repo:
- toplamda **en az 5k satır**, tercihen 5k–9k aralığında olsun
- src + tests + config + docs + scripts içersin
- build/test/smoke komutları olsun
- `validation/` altında machine-readable beklenti dosyaları olsun
- gerçek production naming kullansın
- filler code kullanmasın

## Bu milestone için scan planı

Her repo için en az:
- `modules = ["guardian"]`
- `scanMode = "HEAD_SNAPSHOT"`
- `branchScope = "SINGLE_BRANCH"`
- `refName = "main"`

## Repo 1 — G-V1-JAVA-001 — payments-service-java

### Stack
- Java 21
- Spring Boot
- Maven wrapper
- PostgreSQL config
- basic REST controllers
- service / repository / config package'ları
- unit + integration test skeleton

### Realistic domain
Partner settlement ve payout yöneten küçük/orta ölçekli payments service.

### Must include real findings
- `src/main/resources/application-prod.yml` içinde gerçek-looking OAuth client secret
- `src/main/resources/keys/partner_rsa.pem` içinde valid-looking PEM private key
- `src/main/java/.../PartnerCredentialBootstrap.java` içinde generic API key veya access key benzeri sabit
- `src/main/resources/db/seed/live-connector.properties` içinde gerçek-looking secret token

### Must include near-real negatives
- `README.md` içinde example `.env` block
- `docs/operational-runbook.md` içinde masked token
- `src/test/resources/example.env` içinde placeholder değerler
- `src/test/java/.../PaymentControllerTest.java` içinde dummy strings
- `docs/examples/pem-example.txt` içinde incomplete or example PEM markers

### Must not be only config
- uygulama kodu, controller, DTO, service, repository, config, mapper, error handling, tests olsun

### Validation files
- `validation/scenario.yaml`
- `validation/expected-findings.json`
- `validation/expected-absent.json`
- `validation/smoke.yaml`
- `validation/branch-plan.yaml`
- `validation/expected-report.md`

## Repo 2 — G-V1-PY-002 — notification-worker-python

### Stack
- Python 3.11
- FastAPI + background worker pattern
- pytest
- `pyproject.toml`
- app, worker, config, client, tests, docs, deploy klasörleri

### Realistic domain
Transactional email/SMS/push notification dispatch worker.

### Must include real findings
- active runtime settings içinde hardcoded provider token
- `deploy/k8s/notification-prod.env` içinde gerçek-looking secret
- `app/clients/webhook_client.py` veya benzeri dosyada live API key
- `app/security/jwt_bootstrap.py` içinde secret-like constant

### Must include near-real negatives
- `tests/fixtures/sample_payload.json`
- `docs/local-dev.md` example values
- comment-only sample token lines
- masked DSN / redacted webhook examples
- `.env.example`

## Repo 3 — G-V1-TS-003 — partner-api-node

### Stack
- TypeScript
- NestJS veya iyi yapılandırılmış Express
- Jest
- src/config, src/modules, src/common, test, docs, scripts

### Realistic domain
Partner onboarding ve credential provisioning API.

### Must include real findings
- `src/config/secrets.ts` içinde active secret
- `config/production.json` içinde live client credential
- `src/modules/partners/bootstrap/partnerKeyLoader.ts` veya benzeri dosyada certificate/key material
- `scripts/bootstrap-partner.ts` içinde active key/token

### Must include near-real negatives
- `README.md` quickstart
- `docs/sample-webhooks.md`
- `__tests__/fixtures/`
- `.env.example`
- variable-name traps that look scary but are harmless

## Repo 4 — G-V1-CONFIG-004 — legacy-admin-config

### Stack
Config-heavy repo; yine de toplam satır hedefi 5k+.
İçerik:
- `config/`
- `deploy/`
- `ops/`
- `scripts/`
- `docs/`
- `ansible/`
- `terraform/`
- shell helpers

### Realistic domain
Legacy admin portal ve ops provisioning konfigürasyonları.

### Must include real findings
- active `.properties` / `.yaml` secret values
- live private key material
- real-looking service account token
- ops runtime config içinde secret

### Must include near-real negatives
- `terraform/sample.tfvars`
- `docs/templates/`
- `examples/`
- masked values
- placeholders like `changeme`, `example`, `dummy`

## Gitea tasks

Bu milestone kapsamında:
1. Her repo'yu localde oluştur.
2. Build/test/smoke çalıştır.
3. `arq` kullanıcısı altında local Gitea'ya public repo olarak create et.
4. `main` branch'i push et.
5. Repo metadata manifest'ini `manifests/gitea-repos-M1.json` içinde sakla.

## ARQ tasks

1. ARQ project `arq-lab` create/reuse et.
2. Her repo için application create/reuse et:
   - key pattern: `arq-lab-<scenario-id-lower>`
   - repository locator: Gitea clone URL
   - providerType: `GENERIC_GIT`
3. Guardian-only head scan tetikle.
4. Findings export al.
5. Comparison yap.
6. Scenario raporları ve aggregate M1 raporu üret.

## Acceptance

Bu milestone sadece aşağıdaki durumda pass sayılır:
- tüm repolar build/test/smoke seviyesinde geçerli
- Gitea'ya push edilmiş
- ARQ'da application create edilmiş
- scan request gönderilmiş
- findings export alınmış
- her repo için `mustFind`, `mustNotFind` kıyası yapılmış

## Çıktılar

- `generated/M1/...`
- `runs/<timestamp>/...`
- `reports/M1-guardian-live-surfaces.md`
- `reports/M1-guardian-live-surfaces.json`

## Önemli
Secret değerleri gerçek-world görünümlü olsun ama harici canlı servislere ait gerçek credential olmasın. Sentetik fakat format olarak ikna edici değerler kullan.
