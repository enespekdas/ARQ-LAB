# M7 — Adversarial negatives

## Rolün

Sen `Arq-lab/` altında çalışan bir AI engineering agent'sın. Bu milestone için hem **repo üretimi** hem **automation entegrasyonu** hem **validation artifact üretimi** yapacaksın.

## Ana amaç

Guardian ve Quantum için özellikle false positive üretmemesi gereken docs, examples, tests, vendor/generated ve safe-wrapper yüzeylerini yoğun biçimde test etmek.

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


## Bu milestone'da başarı ölçütü

Burada asıl başarı **temiz kalmak**. Must-not-find ihlali bu milestone'da kritik fail sayılır.

## Repo 1 — N-V7-DOCS-001 — docs-samples-repo

### İçerik
- çok sayıda README
- docs pages
- blog-style snippets
- code fences
- example env values
- example PEM headers
- example `verify=false` and `AES/ECB` text mentions

### Beklenti
- gerçek finding **olmamalı**

## Repo 2 — N-V7-VENDOR-002 — vendor-generated-repo

### İçerik
- generated JS bundles (text-based synthetic, binary değil)
- copied vendor examples
- lockfiles
- framework boilerplate
- generated client code
- minified-like sample text

### Beklenti
- gerçek finding olmamalı
- gerekiyorsa sadece explicitly review bucket

## Repo 3 — N-V7-TESTS-003 — test-mocks-repo

### İçerik
- unit test mocks
- fake tokens
- dummy API keys
- insecure-looking helper names
- TLS bypass mocks in test-only code
- fake certificates

### Beklenti
- gerçek risk finding olmamalı

## Repo 4 — N-V7-SAFE-004 — safe-wrapper-playground

### İçerik
- modern secure wrappers
- secure hash/HMAC helpers
- secure TLS clients
- safe key loading
- scary naming traps but safe implementation

### Beklenti
- gerçek risk finding olmamalı

## Zorunlu kurallar

- Yine de repo'lar 5k+ total lines bandında olsun
- gerçek build/test/smoke barındırsın
- sadece boş docs deposu yapma
- bazı dosyalar üretim-benzeri isimler taşısın ama live risk olmasın

## Validation contract

Bu milestone için `expected-absent.json` çok katı olacak.
`mustFind` boş olabilir veya çok sınırlı `mayFindReview` kullanılabilir.

## Rapor

Aggregate rapor ayrıca:
- FP heatmap by path class
- docs/test/vendor/generated/safe-wrapper bazında noise table
içersin.
