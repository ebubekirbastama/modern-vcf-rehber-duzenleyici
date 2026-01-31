# 📊 İstatistikler Özelliği - Kullanım Kılavuzu

## Genel Bakış

Modern VCF Rehber Düzenleyici'ye eklenen **İstatistikler** özelliği, rehberiniz hakkında detaylı analiz ve bilgi sağlar.

## Nasıl Kullanılır?

1. **VCF Dosyası Yükleyin**
   - Ana ekranda "VCF Yükle" butonuna tıklayın
   - Rehber dosyanızı seçin

2. **İstatistikleri Görüntüleyin**
   - "📊 İstatistikler" butonuna tıklayın
   - Detaylı analiz penceresi açılacaktır

## İstatistik Kategorileri

### 📁 Genel Bilgiler
- **Orijinal Kayıt Sayısı**: VCF dosyasındaki toplam kayıt sayısı
- **Mükerrer Temizlenen**: Kaldırılan tekrar eden numara sayısı (kırmızı renkte)
- **Temiz Kayıt Sayısı**: Mükerrerler temizlendikten sonra kalan kayıt sayısı (yeşil renkte)

### 👤 İsim İstatistikleri
- **En Uzun İsim**: Rehberdeki en uzun isim (30 karakterden uzunsa kısaltılır)
- **En Kısa İsim**: Rehberdeki en kısa isim
- **Ortalama İsim Uzunluğu**: Tüm isimlerin ortalama karakter sayısı

### 📱 Numara Analizi
- **Türk Mobil Numaralar**: +90 5xx ile başlayan numaralar (yüzde ve adet)
- **Diğer Numaralar**: Yurtdışı veya farklı formattaki numaralar
- **İsimsiz Kişiler**: İsim bilgisi olmayan kayıtlar

## Özellikler

✅ **Gerçek Zamanlı Hesaplama**: İstatistikler her VCF yüklendiğinde otomatik güncellenir
✅ **Görsel Renk Kodları**: Önemli bilgiler farklı renklerle vurgulanır
✅ **Yüzdelik Dağılım**: Numara formatları yüzdelik olarak gösterilir
✅ **Temiz Arayüz**: Modern dark tema ile kolay okunabilir

## Teknik Detaylar

### Hesaplama Mantığı

```python
# Mükerrer tespiti
- Aynı numara birden fazla kez varsa sadece biri tutulur
- Farklı formatlardaki aynı numara normalize edilir

# İsim analizi
- En uzun/kısa isim: max() ve min() fonksiyonları ile
- Ortalama: Toplam karakter / Kişi sayısı

# Numara formatı
- Türk mobil: +90 5xx ile başlayanlar
- Diğer: Geri kalan tüm numaralar
```

### Veri Yapısı

```python
stats = {
    "total_contacts": 0,        # Temiz kayıt sayısı
    "duplicates_removed": 0,    # Kaldırılan mükerrer sayısı
    "original_count": 0         # Orijinal toplam
}
```

## Örnek Çıktı

```
📊 Rehber Analizi

📁 Orijinal Kayıt Sayısı        18
🗑️ Mükerrer Temizlenen          3
✅ Temiz Kayıt Sayısı           15

👤 En Uzun İsim                 Mustafa Özdemir
👤 En Kısa İsim                 Ali Yıldız
📏 Ortalama İsim Uzunluğu       12.4 karakter

📱 Türk Mobil Numaralar         13 (86.7%)
🌍 Diğer Numaralar              2 (13.3%)
❓ İsimsiz Kişiler              1
```

## Gelecek Geliştirmeler

- [ ] Grafik/chart desteği
- [ ] PDF rapor çıktısı
- [ ] Zaman bazlı analiz (ekleme tarihi)
- [ ] Grup/kategori bazlı istatistikler
- [ ] Excel export

## Sorun Giderme

**Soru**: İstatistikler butonu çalışmıyor?
**Cevap**: Önce bir VCF dosyası yüklediğinizden emin olun.

**Soru**: Mükerrer sayısı yanlış görünüyor?
**Cevap**: Uygulama numaraları normalize eder (0532, +90532, 90532 aynı kabul edilir).

**Soru**: İsimsiz kişi nedir?
**Cevap**: FN, N veya ORG alanı olmayan kayıtlar "İsimsiz" olarak işaretlenir.

---

**Geliştirici**: Ebubekir Bastama  
**Tarih**: 31 Ocak 2026  
**Versiyon**: 1.1.0
