import random
import time

def oyunu_baslat():
    secenekler = ["taş", "kağıt", "makas"]
    
    # Skorları tutacağımız değişkenler
    oyuncu_skor = 0
    bilgisayar_skor = 0

    print("=" * 40)
    print("🎮  TAŞ - KAĞIT - MAKAS OYUNUNA HOŞGELDİNİZ  🎮")
    print("=" * 40)
    print("Çıkmak için 'q' tuşuna basabilirsiniz.\n")

    while True:
        kullanici_secim = input("Seçiminiz (Taş/Kağıt/Makas): ").lower()

        # Çıkış kontrolü
        if kullanici_secim == 'q':
            print("\nOyun sonlandırılıyor...")
            time.sleep(1)
            break

        # Geçersiz giriş kontrolü
        if kullanici_secim not in secenekler:
            print("⚠️  Lütfen geçerli bir hamle yapın: taş, kağıt veya makas.")
            continue

        # Bilgisayarın hamlesi
        bilgisayar_secim = random.choice(secenekler)
        
        print(f"\nSen: {kullanici_secim.capitalize()} 🆚 Bilgisayar: {bilgisayar_secim.capitalize()}")
        time.sleep(0.5) # Heyecan yaratmak için yarım saniye bekleme

        # Sonuç kontrolü
        if kullanici_secim == bilgisayar_secim:
            print("🤝 Berabere!\n")
        elif (kullanici_secim == 'taş' and bilgisayar_secim == 'makas') or \
             (kullanici_secim == 'kağıt' and bilgisayar_secim == 'taş') or \
             (kullanici_secim == 'makas' and bilgisayar_secim == 'kağıt'):
            print("🎉 Tebrikler, bu turu kazandınız!\n")
            oyuncu_skor += 1
        else:
            print("🤖 Bilgisayar kazandı!\n")
            bilgisayar_skor += 1

        # Güncel skor durumu
        print(f"📊 SKOR -> Sen: {oyuncu_skor} | Bilgisayar: {bilgisayar_skor}")
        print("-" * 40)

    # Oyun bittiğinde genel toplamı göster
    print(f"\n🏁 OYUN BİTTİ! Genel Skor -> Sen: {oyuncu_skor} - Bilgisayar: {bilgisayar_skor}")

if __name__ == "__main__":
    oyunu_baslat()
