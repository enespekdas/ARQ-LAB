# M9 — Reporting aggregation and regression harness

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Önceki milestone'ların çıktılarından aggregate accuracy görünümü üretmek, regression koşularını tekrarlanabilir hale getirmek ve fail bucket'larını sistematik backlog'a dönüştürmek.

## Bu milestone için hedef repo sayısı

0 new repos required; use existing outputs

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

Artık repo üretmekten çok:
- tüm milestone sonuçlarını toplamak
- aggregate accuracy görünümü üretmek
- tekrar koşulabilir regression harness kurmak
- tuning backlog çıkarmak

## Yapılacaklar

### 1) Aggregate summary üret
Aşağıdaki kırılımlarda özet çıkar:
- milestone bazında
- module bazında
- language bazında
- scenario family bazında
- TP / FP / FN
- explainability failures
- ref-state failures
- noise hot spots

### 2) Regression entrypoints
Aşağıdaki komutları destekle:
- `python -m tooling.orchestrate --milestone M1`
- `python -m tooling.orchestrate --milestone M3`
- `python -m tooling.orchestrate --all`
- `python -m tooling.orchestrate --resume-last-failed`
- `python -m tooling.orchestrate --report-only`

### 3) Stable machine outputs
Aşağıdaki dosyaları üret:
- `reports/aggregate-summary.json`
- `reports/aggregate-summary.md`
- `reports/aggregate-summary.csv`
- `reports/fail-buckets.json`
- `reports/tuning-backlog-seed.md`
- `reports/explainability-scorecard.md`

### 4) Score model
Her scenario için verdict:
- `PASS`
- `PASS_WITH_NOISE`
- `FAIL_FN`
- `FAIL_FP`
- `FAIL_EXPLAINABILITY`
- `FAIL_REF_STATE`
- `INVALID_SCENARIO`

### 5) Risk lens
Özet rapor ayrıca şu lenslerle bakmalı:
- Guardian: head/history/ref-state/dedup
- Quantum: weak crypto, TLS/trust, config misuse, explainability
- Path class: live vs docs/tests/vendor/generated
- Operational usefulness: high / medium / low

### 6) Tuning backlog
Her fail bucket için:
- likely root cause
- module
- scenario ids
- severity of validation issue
- suggested next action
- owner placeholder

## İstenen final çıktı

Agent bu milestone sonunda, insanın açıp okuyabileceği düzgün bir top-level `reports/FINAL_VALIDATION_STATUS.md` dosyası üretmeli.
Bu dosya şu soruya cevap vermeli:

**ARQ-SEC gerçekçi repository senaryolarında nerede güçlü, nerede gürültülü, nerede eksik?**
