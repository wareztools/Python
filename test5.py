rehber = {
    "Kisi1" :{
        "isim" : "Hamza Kılıç",
        "tel"  : "04333234433",
        "sehir": "İstanbul"

    },
    "Kisi2" : {
        "isim" : "Tarık yazılım",
        "tel"  : "02342343243",
        "sehir": "bursa"
    },
}

while True:
    bilgiler = rehber.keys()
    kisi = input("kisi ismi giriniz :")
    sorgu = input("bilgileri sorgula {} :".format(kisi))

    if kisi in bilgiler:
        flag = True
    else:
        flag = False

    if flag == True:
        print(rehber.get(kisi,"geçersiz islem1").get(sorgu,"{} geçersiz işlem2").format(sorgu))
    else:
        print("Geçersiz işlem")



