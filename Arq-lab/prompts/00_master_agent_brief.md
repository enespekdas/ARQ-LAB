# Master Agent Brief — ARQ Lab

Bu belge, diğer tüm milestone prompt'larının önüne referans olarak konulmalıdır. Milestone prompt'ları zaten büyük ölçüde self-contained tasarlanmıştır; ama aynı session içinde ilerleyeceksen önce bunu ver.

## Mission

`Arq-lab/` altında, ARQ-SEC'in Guardian ve Quantum modüllerini **gerçek müşteri repository'lerine olabildiğince benzeyen** repolarla doğrulayan tam otomatik bir lab kur.

Senin görevin sadece kod üretmek değil:
- repo üretmek
- repo'yu branch'leriyle ve commit geçmişiyle modellemek
- local Gitea'ya push etmek
- ARQ API ile application oluşturmak
- scan tetiklemek
- findings export almak
- expected vs actual kıyaslamak
- rapor üretmek

## Core principles

1. **Validation-first**
   - Yeni product feature düşünme.
   - Repo'lar test amacıyla üretilecek.
   - Ama test repo'ları gerçek uygulama gibi görünmeli.

2. **No toy repos**
   - Her service/config repo toplamda hedef olarak 5k–12k satır aralığında olsun.
   - Sadece aynı dosyayı kopyalayarak şişirme yapma.
   - Katmanlı yapı kur: controller, service, repository, config, test, deploy, docs, scripts.

3. **Runnable**
   - Her repo için build/test/smoke komutları tanımla.
   - Çalışmayan veya tamamen broken repo üretme.
   - "derlenebilir/başlatılabilir" hissi net olmalı.

4. **Positive + negative together**
   - Her repo'da hem gerçek finding yüzeyleri hem finding'e çok benzeyen ama bulunmaması gereken yüzeyler olsun.

5. **Machine-readable validation**
   - Her repo `validation/` altında şu dosyaları içersin:
     - `scenario.yaml`
     - `expected-findings.json`
     - `expected-absent.json`
     - `smoke.yaml`
     - `branch-plan.yaml`
     - `expected-report.md`
   - Quantum repo'larında ayrıca:
     - `explainability-contract.json`

6. **Git realism**
   - Snapshot repo'lar için bile gerçek git repo oluştur.
   - History/ref-state milestone'larında gerçek commit graph ve branch lineage kur.
   - Sadece `branches/main/` gibi folder snapshot'ı bırakma; gerçek git branch oluştur.

7. **Gitea workflow**
   - Local Gitea kullan.
   - Varsayılan kimlik bilgileri:
     - username: `arq`
     - password: `arq`
   - Repositories `public` olsun; ARQ tarafında `GENERIC_GIT` clone path basit kalsın.
   - Repo owner varsayılanı `arq`.

8. **ARQ workflow**
   - ARQ API ile login ol.
   - Project create / reuse et.
   - Application create et.
   - Scan tetikle.
   - Findings export al.
   - Finding detail ve occurrences ile explainability assert et.
   - Sonuçları `runs/` altında sakla.

9. **Never fake execution**
   - Gitea/ARQ erişimi yoksa veya komut çalışmıyorsa bunu logla.
   - "başarılı oldu" diye uydurma.
   - Üretilen repo ve tooling yine de bırak.

10. **Idempotent**
    - Script'ler tekrar çalıştırıldığında mevcut repo/application varsa reuse veya controlled update yap.
    - Aynı milestone iki kez koşulunca environment bozulmasın.

## Root layout to create

`Arq-lab/` altında en az şu yapıyı oluştur:

```text
Arq-lab/
  catalog/
  generated/
  tooling/
  runs/
  reports/
  templates/
  docs/
  manifests/
```

## Required automation code

`Arq-lab/tooling/` içinde Python tabanlı bir otomasyon yaz:

- `env.py`
- `gitea_client.py`
- `git_factory.py`
- `arq_client.py`
- `scan_runner.py`
- `exporter.py`
- `comparator.py`
- `report_renderer.py`
- `orchestrate.py`

İsteğe bağlı:
- `models.py`
- `utils/`
- `schemas/`

## Required capabilities

### Gitea
- repo var mı kontrol et
- yoksa create et
- visibility public ayarla
- git remote push yap
- branch ve tag'leri push et

### Git factory
- repo init
- default branch ayarla
- commit plan uygula
- branch divergence kur
- commit SHA manifest'i üret

### ARQ client
- login
- project create/reuse
- application create/reuse
- scan request
- scan status poll
- findings export
- finding detail fetch
- occurrences fetch

## Required ARQ contract assumptions

- providerType: `GENERIC_GIT`
- application create payload'ında `repositorySource.defaultBranch = "main"`
- scan endpoint:
  - `POST /api/v2/scans/application`
- Guardian history koşuları:
  - `scanMode = REF_HISTORY`
  - module sadece `guardian`
- Quantum koşuları:
  - `scanMode = HEAD_SNAPSHOT`
  - module `quantum`

## Output contract per scenario run

`runs/<run-id>/<scenario-id>/` altında en az:

- `scenario-metadata.json`
- `gitea-repository.json`
- `application.json`
- `scan-request.json`
- `scan-response.json`
- `findings-export.json`
- `findings-normalized.json`
- `finding-details/`
- `comparison.json`
- `report.md`

## Comparison buckets

Her scenario sonucu şu bucket'lara ayrılmalı:

- `mustFindMatched`
- `mustFindMissing`
- `mustNotFindViolations`
- `extraFindings`
- `mayFindReview`
- `explainabilityFailures`
- `refStateFailures`

## Repo realism rules

### Must include
- gerçek package/module naming
- production benzeri config
- testler
- docs
- CI/dev scripts
- deployment/config artifacts
- realistic framework usage

### Must not include
- anlamsız filler yorumlar
- tek dosyada 5000 satır
- sadece boş DTO/POJO yığını ile satır doldurma
- compile olmayan kırık skeleton
- generated binary junk

## Delivery mode

Her milestone sonunda:
1. oluşturulan repo listesi
2. build/test/smoke sonucu
3. Gitea repo URL'leri
4. ARQ application anahtarları
5. tetiklenen scan'ler
6. comparison summary
7. açık kalan hata/engel listesi

## Language of artifacts

- Repo kodu, dosya adları, README'ler: çoğunlukla İngilizce
- Agent log ve summary: Türkçe veya İngilizce olabilir
- Validation machine files: English field names
