# 📇 Modern VCF Rehber Düzenleyici

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-success)

> **Modern VCF Rehber Düzenleyici**, `.vcf (vCard)` formatındaki rehber dosyalarını **temizlemek, düzenlemek ve optimize etmek** için geliştirilmiş modern, hızlı ve kullanıcı dostu bir **Python masaüstü uygulamasıdır**.

Bozuk karakterler, mükerrer numaralar ve karmaşık telefon formatları artık sorun değil 🚀

---

## ✨ Özellikler

- 📥 **Gelişmiş VCF İçe Aktarma**
  - UTF-8 & QUOTED-PRINTABLE desteği
  - Bozuk karakterleri otomatik düzeltme

- 🔁 **Mükerrer Numara Temizleme**
  - Aynı telefon numaralarını algılar
  - Tekilleştirir ve raporlar

- 📞 **Akıllı Numara Normalizasyonu**
  - Tüm numaraları `+90 5xx xxx xx xx` formatına çevirir
  - `0`, `90`, `+90` varyasyonlarını destekler

- 🔍 **Canlı Arama**
  - İsim veya numaraya göre anlık filtreleme

- ✏️ **Kayıt Düzenleme**
  - İsim ve numara güncelleme

- 🗑️ **Güvenli Silme**
  - Onaylı kişi silme

- 💾 **Temiz VCF Dışa Aktarma**
  - Düzenlenmiş rehberi yeni `.vcf` dosyası olarak kaydetme

- 🎨 **Modern Dark UI**
  - `ttkbootstrap` destekli karanlık tema

---

## 🖼️ Arayüz

```md
![Uygulama Görünümü](screenshot.png)
```

---

## 🛠️ Kurulum

### 1️⃣ Gereksinimler

- Python **3.9+**
- Windows işletim sistemi

### 2️⃣ Depoyu Klonla

```bash
git clone https://github.com/ebubekirbastama/modern-vcf-rehber-duzenleyici.git
cd modern-vcf-rehber-duzenleyici
```

### 3️⃣ Gerekli Paketi Yükle

```bash
pip install ttkbootstrap
```

### 4️⃣ Çalıştır

```bash
python app.py
```

---

## 📂 Desteklenen VCF Alanları

- `FN` – Full Name
- `N` – Alternatif isim
- `ORG` – Kurum adı (fallback)
- `TEL` – Çoklu numara desteği

İsim bulunamazsa otomatik olarak:
- ORG
- Telefon numarası
- veya **“İsimsiz”** atanır.

---

## 🔐 Güvenlik

- 🔒 İnternet bağlantısı gerekmez
- 🖥️ Tüm işlemler **lokal** çalışır
- ❌ Harici sunucu veya veri aktarımı yok

---

## 🗺️ Yol Haritası

- [ ] CSV içe / dışa aktarma
- [ ] Toplu kişi düzenleme
- [ ] Ülke kodu seçimi
- [ ] Otomatik yedekleme
- [ ] EXE paketleme (PyInstaller)

---

## 🤝 Katkı Sağla

Katkılar her zaman memnuniyetle karşılanır 🙌

1. Fork'la 🍴  
2. Yeni bir branch oluştur 🌱  
3. Commit at 💾  
4. Pull Request gönder 🚀  

---

## 📜 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır.  
Detaylar için `LICENSE` dosyasına göz atabilirsiniz.

---

## 👨‍💻 Geliştirici

**Ebubekir Bastama**  
📍 Türkiye  
💡 Python | Desktop Apps | Automation  

⭐ Eğer projeyi beğendiysen repo'ya star atmayı unutma!

---

> “Rehberini temizle, sadeleştir, kontrolü eline al.” 📱✨
