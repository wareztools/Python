import os


veritaban = list()

menü = ("""
1)ekle
2)sil
3)listele
4)kapat
""")

def bilgiekle(liste,bilgi):
    liste += [bilgi]
    print("{} bilgiler".format(bilgi))

def bilgisil():
    veritaban.clear()

def bilgilistele(listele):
    for i in listele:
        print("{} liste".format(i))

def kapat():
    quit()

while True:
    print(menü)
    os.system("cls")
    işlem = input("işlem seçin :")

    if işlem == "1":
        data = input("bilgi girin :")
        bilgiekle(veritaban,data)

    elif işlem == "2":
        bilgisil()

    elif işlem == "3":
        bilgilistele(veritaban)

    elif işlem == "q" and işlem == "Q":
        kapat()

    else:
        print("geçersiz işlem")