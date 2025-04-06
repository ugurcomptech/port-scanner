
# PRO Port Scanner

Bu, ağ üzerinde port taraması yaparak açık portları tespit eden bir Python betiğidir. Port taramasının yanı sıra, her açık port için servis bilgileri, bannerlar ve reverse DNS bilgilerini de toplar ve belirtilen formatta kaydeder.

## Özellikler

- **Port Taraması:** Belirtilen bir IP adresinde port taraması yapar.
- **Servis Tespiti:** Her açık port için servis türünü tespit eder.
- **Reverse DNS Lookup:** Her açık port için reverse DNS sorgulaması yapar.
- **Banner Tespiti:** Her açık port için banner alır (HTTP, FTP, IMAP, SMTP vb.).
- **Çoklu Format Desteği:** Sonuçları `txt`, `html`, `json` ve hepsi bir arada kaydetme seçenekleriyle dışa aktarır.

## Kullanım

### Gereksinimler

Bu betiği çalıştırmak için aşağıdaki Python kütüphanelerini yüklemeniz gerekmektedir:

- `colorama`
- `tqdm`

Bu kütüphaneleri yüklemek için şu komutu çalıştırabilirsiniz:

```bash
pip install colorama tqdm
```

### Betik Kullanımı

1. **Port Taraması Başlatma:**

   Betiği çalıştırmak için, terminal veya komut satırında şu komutu kullanabilirsiniz:

   ```bash
   python port_scanner.py
   ```

2. **Sonuçları Kaydetme:**

   Sonuçları farklı formatlarda kaydedebilirsiniz:
   - **TXT Formatı:** Klasik düz metin formatında.
   - **HTML Formatı:** Tarayıcıda görüntülenebilecek renkli formatta.
   - **JSON Formatı:** API ve geliştiriciler için yapılandırılmış veri.
   - **Hepsi Bir Arada:** Tüm formatlarda sonuçları kaydeder.

3. **Tarama Seçenekleri:**
   - Hedef IP adresi
   - Başlangıç ve bitiş portları

   Tarama işlemi bittikten sonra, sonuçlar belirtilen formatta `logs` klasörüne kaydedilecektir.

### Örnek

Bir IP adresindeki 80 ile 443 arasındaki portları taramak ve sonuçları HTML formatında kaydetmek için şu adımları izleyebilirsiniz:

1. Betiği çalıştırın:
   ```bash
   python port_scanner.py
   ```

2. Format seçin: `2` (HTML)
3. Tarama modu: `1` (Tek IP tarama)
4. Hedef IP adresini girin: `192.168.1.1`
5. Başlangıç Portu: `80`
6. Bitiş Portu: `443`

Betiği çalıştırdıktan sonra, sonuçlar `logs/sonuclar.html` dosyasına kaydedilecektir.

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen şu adımları izleyin:

1. Bu projeyi çatallayın (fork).
2. Yeni bir özellik ekleyin veya hata düzeltmesi yapın.
3. Değişikliklerinizi commit edin ve pull request gönderin.

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
