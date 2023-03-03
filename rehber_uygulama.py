rehber = {

    "Kisi1" : {

        "isim" : "Hamza Kııç",
        "cep"  : "05383324233",
        "ev"   : "02126184444",
        "sehir": "istanbul"
    },
    "Kisi2" : {

        "isim" : "Samet albayrak",
        "cep"  : "04334322233",
        "ev"   : "02124445544",
        "sehir": "ankara"
    },
}

while True:
    isimler = rehber.keys()
    kisi = input("Kisi ismini giriniz :")
    sorgula = input("isimdekini sorgula {} :".format(kisi))
    if kisi in isimler:
        flag = True
    else:
        flag = False
    if flag == True:
        print(rehber.get(kisi,"Geçersiz islem").get(sorgula,"{} bulunamadı ").format(sorgula))
    else:
        print("Kisi ismi yanlış girdiniz Tekrar deneyin.")