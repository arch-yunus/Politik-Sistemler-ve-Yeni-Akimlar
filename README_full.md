> Politik Sistemler ve Yeni Akımlar (Political Systems & Emerging Currents)

Bu depo, siyaset teorisi, politik sistemler ve yeni akımlar üzerine derlenmiş notlar,
makaleler ve çeviriler içerir. İçeriğin daha iyi düzenlenmesi, sunulması ve yayımlanması
için bir proje iskeleti ve küçük araçlar sağlanır.

Hedef ve Kapsam

- Akademik ve popüler metinlerin toplanması ve kategorize edilmesi.
- Markdown formatındaki içeriğin temiz HTML'e çevrilmesi ve basit bir arama/gezinti
  altyapısının sağlanması.

Özellikler (ilk sürüm)

- Markdown → HTML dönüştürücü CLI (`src/convert.py`).
- İçerik meta verisi (başlık, yazar, tarih, etiketler) için başlangıç desteği.
- Basit birim testleri (`tests/`) ve CI için GitHub Actions workflow'u.

Hızlı Kurulum

1. Python 3.8+ kurulu olmalı.
2. Sanal ortam oluşturun ve bağımlılıkları yükleyin:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Örnek dönüşüm:

```powershell
python -m src.convert README_full.md -o docs/index.html
```

Geliştirme Notları

- İçerik yapılandırması için `src/` altına yeni modüller ekleyebilirsiniz.
- `tests/` altında pytest ile unit testler ekleyin.

Katkıda Bulunma

1. Fork & clone edin.
2. Yeni branch üzerinde çalışın.
3. Testleri çalıştırın ve PR açın.

Changelog

- 2026-05-22: `README_full.md` eklendi; proje iskeleti oluşturuluyor.

---
Not: Orijinal `README.md` dosyası UTF-16 formatında bulunuyor; isteğe bağlı olarak
ben bunu UTF-8 olarak değiştirebilirim veya mevcut dosyayı referans alarak ilerleyebilirim.

Research & Sources

Bu repoda toplanan temel kavramların (ideoloji, politik sistemler, yeni akımlar)
özeti ve başlangıç kaynakları için [docs/research_notes.md](docs/research_notes.md) dosyasına bakın.

Kısa kaynak listesi:

- Wikipedia — Ideology: https://en.wikipedia.org/wiki/Ideology
- Encyclopaedia Britannica — Political system: https://www.britannica.com/topic/political-system
- Encyclopaedia Britannica — Populism: https://www.britannica.com/topic/populism
- Freedom House — Freedom on the Net: https://freedomhouse.org/report/freedom-net
