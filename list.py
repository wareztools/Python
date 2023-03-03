while True:
    liste = ["istanbul"]

    sehir = input("Sehir gir :")

    liste += [sehir]

    for i in liste:
        print(i)
    if sehir == "q":
        print("Program sonlandırılıyor...")
        quit()

    else:
        print("Geçersiz islem")
