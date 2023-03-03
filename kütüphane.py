import os
os.system("cls")


liste_bilgi = list()

menü = ("""

1) Bilgi ekle
2) Sil
3) Listele
4) Kapat q

""")

def bilgiekle(liste,bilgi):
    liste += [bilgi]
    print("Bilgiler eklendi {}".format(bilgi))

def bilgisil():
    liste_bilgi.clear()
    input("Ana menüye dönmek için ente'ra basınız : ")


def listele(liste_bilgi):
    for i in liste_bilgi:
        print("Liste sorgulanıyor {}".format(i))

def cikis():
    quit()

while True:
    print(menü)

    islem = input("islem seç :")

    if islem == "1":
        bilgi_ad = input("Bilgileri giriniz :")
        bilgiekle(liste_bilgi,bilgi_ad)

    elif islem == "2":
        print("Silmek istediğiniz bilgi")

        print("Silindi.")
        bilgisil()

    elif islem == "3":
        listele(liste_bilgi)

    elif islem == "q" or islem == "Q":
        cikis()

    else:
        print("Geçersiz islem...")
        input("Ana menüye dönmek için Ente'ra basınız...")




