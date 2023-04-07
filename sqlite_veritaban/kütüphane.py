import sqlite3

import time

class Kitap():
    def __init__(self,isim,yazar,yayınevi,türü,baskı):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.türü = türü
        self.baskı = baskı

    def __str__(self):
        return "Kitap ismi: {}\nyazar: {}\nyayınevi: {}\ntürü: {}\nbaskı: {}\n".format(self.isim,self.yazar,self.yayınevi,self.türü,self.baskı)

class Kütüphane():
    def __init__(self):
        self.baglantı_olustur()

    def baglantı_olustur(self):
        self.baglantı = sqlite3.connect("Kütüphane.db")
        self.cursor = self.baglantı.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar(isim TEXT,yazar TEXT,yayınevi TEXT,türü TEXT,baskı INT)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()
    def baglantı_kes(self):
        self.baglantı.close()

    def kitap_goster(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Kütüphane'de boyle bir kitap bulunamadı!")

        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Bulunamadı.")

        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)

    def kitap_ekle(self,kitap):
        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.türü,kitap.baskı))
        self.baglantı.commit()

    def kitap_sil(self,isim):
        sorgu = "Delete From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglantı.commit()

    def kitap_baskı(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Bulunamadı.")
        else:
            baskı = kitaplar[0][4]
            baskı += 1
            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"
            self.cursor.execute(sorgu2,(baskı,isim))
            self.baglantı.commit()

