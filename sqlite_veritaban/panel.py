import time

from kütüphane import *

print("""

1. kitap goster

2. kitap sorgula

3. kitap ekle

4. kitap sil

5. baskı yükselt

çıkmak için q basın.

""")

kütüphane = Kütüphane()

while True:
    işlem = input("işlem şeçin: ")
    if(işlem == "q"):
        print("Program sonlandırılıyor...")
        time.sleep(2)
        print("yine bekleriz")
        break

    elif(işlem == "1"):

       kütüphane.kitap_goster()

    elif(işlem == "2"):
        isim = input("Kitap sorgula :")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)

    elif(işlem == "3"):
        isim = input("İsim : ")
        yazar = input("Yazar :")
        yayınevi = input("Yayınevi :")
        türü = input("Türü :")
        baskı = input("Baskı :")

        yeni_kitap = Kitap(isim,yazar,yayınevi,türü,baskı)
        print("Güncelleniyor...")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")

    elif(işlem == "4"):
        isim = input("Kitap sil: ")
        cevap = input("Emin misiniz ? (E/H) :")
        if(cevap == "E"):
            print("Kitap siliniyor...")
            time.sleep(2)
        kütüphane.kitap_sil(isim)
        print("kitap silindi.")

    elif(işlem == "5"):
        isim = input("Hangi kitap :  ")
        print("Baskı yükseltiliyor.")
        time.sleep(2)
        kütüphane.kitap_baskı(isim)
        print("işlem basarılı.")
    else:
        print("Geçersiz işlem")



