# 📊 Excel İçe/Dışa Aktarma - Kullanım Kılavuzu

## 📥 Excel İçe Aktarma

### Nasıl Kullanılır?

1. **Excel Dosyası Hazırlayın**
   - İlk satır başlık olmalı: `Ad Soyad | Telefon Numarası`
   - Veriler 2. satırdan itibaren başlamalı
   - Desteklenen formatlar: `.xlsx`, `.xls`

2. **İçe Aktarın**
   - "📥 Excel İçe Aktar" butonuna tıklayın
   - Excel dosyanızı seçin
   - İki seçenek sunulur:
     - **Evet**: Mevcut rehberi değiştir
     - **Hayır**: Mevcut rehbere ekle

3. **Sonuç**
   - Kaç kişi içe aktarıldığı gösterilir
   - Mükerrer numaralar otomatik atlanır
   - Tüm numaralar normalize edilir

### Excel Dosya Formatı

```
| Ad Soyad       | Telefon Numarası  |
|----------------|-------------------|
| Ahmet Yılmaz   | 05321234567       |
| Mehmet Demir   | +90 533 999 88 77 |
| Ayşe Kaya      | 905341112233      |
```

### Özellikler

✅ **Otomatik Normalizasyon**
- Tüm numara formatları kabul edilir
- `0532`, `+90532`, `90532` → `+90 532 xxx xx xx`

✅ **Mükerrer Kontrolü**
- Aynı numara birden fazla kez varsa sadece biri alınır
- Kaç mükerrer atlandığı raporlanır

✅ **Esnek Format**
- İsim yoksa "İsimsiz" olarak kaydedilir
- Boş satırlar otomatik atlanır

---

## 📤 Excel Dışa Aktarma

### Nasıl Kullanılır?

1. **Dışa Aktarın**
   - "📤 Excel Dışa Aktar" butonuna tıklayın
   - Kayıt konumunu ve dosya adını seçin
   - Dosya otomatik oluşturulur

2. **Oluşturulan Dosya**
   Excel dosyası **2 sayfa** içerir:
   
   **Sayfa 1: Rehber**
   - Ad Soyad
   - Telefon Numarası
   - Durum (✓ Türk Mobil / ○ Diğer)
   
   **Sayfa 2: İstatistikler**
   - Toplam Kişi
   - Mükerrer Temizlenen
   - Orijinal Kayıt
   - Dışa Aktarma Tarihi

### Excel Çıktı Özellikleri

🎨 **Profesyonel Tasarım**
- Renkli başlık satırı (mavi)
- Otomatik sütun genişlikleri
- Düzenli hizalama

📊 **İstatistik Sayfası**
- Rehber özeti
- Tarih damgası
- Kolay analiz

💾 **Standart Format**
- `.xlsx` formatı
- Excel, LibreOffice, Google Sheets uyumlu
- Mobil cihazlarda açılabilir

---

## 🔄 Kullanım Senaryoları

### Senaryo 1: Yedekleme
```
1. Mevcut rehberi VCF olarak yükle
2. "📤 Excel Dışa Aktar" ile yedekle
3. Excel dosyasını güvenli yere kaydet
```

### Senaryo 2: Toplu Ekleme
```
1. Excel'de yeni kişileri hazırla
2. "📥 Excel İçe Aktar" ile yükle
3. "Hayır" seçerek mevcut rehbere ekle
```

### Senaryo 3: Temizleme ve Dışa Aktarma
```
1. VCF dosyasını yükle
2. Mükerrerler otomatik temizlenir
3. Excel olarak dışa aktar
4. Başka sistemlerde kullan
```

### Senaryo 4: Veri Analizi
```
1. Rehberi Excel'e aktar
2. İstatistikler sayfasını incele
3. Excel'de pivot table oluştur
4. Detaylı analiz yap
```

---

## 📋 Örnek Excel Şablonu

### Basit Şablon
```
Ad Soyad         | Telefon Numarası
-----------------|------------------
Ahmet Yılmaz     | 05321234567
Mehmet Demir     | +90 533 999 88 77
Ayşe Kaya        | 905341112233
```

### Gelişmiş Şablon
```
Ad Soyad              | Telefon Numarası   | Notlar (opsiyonel)
----------------------|--------------------|--------------------
Ahmet Yılmaz          | 05321234567        | İş
Mehmet Demir          | +90 533 999 88 77  | Arkadaş
Ayşe Kaya             | 905341112233       | Aile
ABC Şirketi           | 0 212 555 12 34    | Kurumsal
```

**Not**: "Notlar" sütunu şu an için desteklenmez, sadece ilk 2 sütun okunur.

---

## ⚠️ Önemli Notlar

### İçe Aktarma
- ✅ Sadece ilk 2 sütun okunur (Ad, Numara)
- ✅ İlk satır başlık olarak atlanır
- ✅ Boş satırlar otomatik göz ardı edilir
- ⚠️ Numara sütunu boş olan satırlar atlanır

### Dışa Aktarma
- ✅ Tüm kişiler dışa aktarılır
- ✅ Otomatik istatistik sayfası eklenir
- ✅ Mevcut dosya üzerine yazma uyarısı verilir
- ⚠️ Çok büyük rehberler (10.000+) yavaş olabilir

---

## 🐛 Sorun Giderme

**Soru**: Excel dosyası açılmıyor?
**Cevap**: Dosyanın `.xlsx` veya `.xls` uzantılı olduğundan emin olun.

**Soru**: İçe aktarma sırasında hata alıyorum?
**Cevap**: 
- Excel dosyasının açık olmadığından emin olun
- Başlık satırının doğru olduğunu kontrol edin
- En az 1 veri satırı olmalı

**Soru**: Dışa aktarma sırasında hata alıyorum?
**Cevap**:
- Hedef klasöre yazma izniniz olduğundan emin olun
- Aynı isimde açık bir Excel dosyası varsa kapatın

**Soru**: Numaralar yanlış formatta?
**Cevap**: Uygulama otomatik normalize eder, endişelenmeyin!

---

## 💡 İpuçları

1. **Yedekleme**: Düzenli olarak Excel'e aktararak yedek alın
2. **Paylaşım**: Excel formatı evrensel, kolayca paylaşılabilir
3. **Analiz**: İstatistik sayfasını kullanarak rehberinizi analiz edin
4. **Temizlik**: Excel'de düzenleyip tekrar içe aktarabilirsiniz
5. **Toplu İşlem**: Çok sayıda kişiyi Excel'de hazırlayıp tek seferde yükleyin

---

**Geliştirici**: Ebubekir Bastama  
**Tarih**: 31 Ocak 2026  
**Versiyon**: 1.2.0
