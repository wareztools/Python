print("""
NOT DEFTERİ

1)Bilgi ekle
2)Oku
3)Sil
4)Kapat q


""")

while True:
    işlem = input("işlem seç :")

    if işlem == "1":

        isim_soyisim = input("isim :")
        sehir = input("sehir :")
        telefon = int(input("telefon"))
        print("Bilgiler eklendi ")


        root = open("deneme.txt","w",encoding="utf8")
        root.write("""{}\n {}\n {}\n
        """.format(isim_soyisim,sehir,telefon))
        root.close()


    elif işlem =="2":
        root = open("deneme.txt","r",encoding="utf8")
        print(root.read())
        root.close()

    elif işlem == "3":
        root = open("deneme.txt","w",encoding="utf8")

        root.close()

    elif işlem == "q":
        print("program sonlandırılıyor")
        break

    else:
        print("Geçersiz işlem")









