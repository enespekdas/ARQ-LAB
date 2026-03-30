# ARQ Lab Prompt Pack

Bu paket, `ARQ-SEC` kod tabanından bağımsız bir `LAB/` workspace içinde çalışan AI agent için hazırlanmış **milestone bazlı prompt seti** içerir.

Amaç:
- gerçekçi repository senaryoları üretmek
- bu repoları local Gitea'ya yüklemek
- ARQ API ile application oluşturmak
- scan tetiklemek
- findings export almak
- expected vs actual karşılaştırması yapmak
- scenario bazlı rapor üretmek

## Varsayımlar

- Gitea localde çalışıyor
- Gitea kullanıcı adı / şifre: `arq` / `arq`
- Gitea base URL varsayılanı: `http://localhost:3001`
- ARQ API base URL için `.env` kullanılacak; varsayılan öneri: `http://localhost:8080`
- Repositories mümkünse **public** oluşturulacak; böylece `GENERIC_GIT` ile ARQ clone tarafında auth karmaşası azaltılacak
- Workspace key varsayılanı `default`
- ARQ login için kullanıcı bilgisi `.env` ile verilecek

## Repo davranışı ile uyumlu önemli notlar

Bu prompt paketi, mevcut backend contract'ına uyacak şekilde tasarlanmıştır:

- application create: `POST /api/v2/applications`
- application scan: `POST /api/v2/scans/application`
- findings export: `GET /api/v2/reports/findings`
- finding detail: `GET /api/v2/findings/{id}`
- `GENERIC_GIT` provider type kullanılacak
- `HEAD_SNAPSHOT` ve `REF_HISTORY` scan mode'ları dikkate alınacak
- `REF_HISTORY` yalnızca Guardian için kullanılacak
- `SINGLE_BRANCH` ve `ALL_BRANCHES` branch scope senaryoları ayrıştırılacak

## Kullanım sırası

1. `prompts/00_master_agent_brief.md`
2. `prompts/01_M0_foundation_automation.md`
3. Sonra sırasıyla milestone prompt'ları:
   - `02_M1_guardian_live_surfaces.md`
   - `03_M2_guardian_history_refstate.md`
   - `04_M3_quantum_weak_crypto_java_csharp.md`
   - `05_M4_quantum_weak_crypto_python_go_node.md`
   - `06_M5_quantum_tls_trust_config_java_python.md`
   - `07_M6_quantum_tls_trust_config_node_csharp_config.md`
   - `08_M7_adversarial_negatives.md`
   - `09_M8_mixed_enterprise_repos.md`
   - `10_M9_reporting_aggregation_regression.md`

## Beklenen çalışma şekli

AI agent:
- `Arq-lab/` klasörünü oluşturur
- gerekli tooling kodunu yazar
- scenario repo'larını üretir
- branch/commit graph'ını oluşturur
- local Gitea'ya push eder
- ARQ API ile application create eder
- scan tetikler
- findings export alır
- comparison ve rapor üretir

## Bu pakette neler var

- Milestone bazlı detaylı prompt'lar
- Scenario catalog
- Validation artifact template'leri
- API/automation notları
- `.env` örneği

## Önemli kalite koşulları

Her üretilen repo:
- gerçek uygulama hissi vermeli
- en az 5k satır toplam koda yaklaşmalı veya aşmalı
- sadece boilerplate/filler olmamalı
- build/test/smoke çalıştırılabilir olmalı
- hem gerçek finding hem near-real negative surface içermeli
- `validation/` altında machine-readable beklenti dosyaları barındırmalı

## Tavsiye edilen çalışma modu

Her milestone'u ayrı agent oturumunda çalıştırmak yerine:
- önce M0 ile temel automation kodunu üret
- sonra her milestone prompt'unu aynı workspace üzerinde, idempotent biçimde uygulat
- agent'a "mevcut Arq-lab içeriğini bozma, genişlet" talimatını koru
