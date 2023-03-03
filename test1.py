

menü = ("""

1)bilgi ekle
2) sil
3) listele
4)veritabandaki 
5) q kapat
""")


liste = list()



def bilgiekle(bilgi,ekle):
    bilgi += [ekle]
    print("Bilgi : {}".format(ekle))
    input("ana menüye dönmek için Ente'ra basınız :")

def bilgisil():
    liste.clear()

def cikis():
    quit()

def listele(bilgi_listele):
    for i in bilgi_listele:
        print("liste :{}".format(i))





while True:
    print(menü)
    işlem = input("işlem seç :")
    root = open("deneme.txt", "w", encoding="utf8")


    if işlem == "1":
        data = input("gir :")
        root.write("""{}
                """.format(data))
        root.close()


        bilgiekle(liste,data)





    elif işlem == "2":
        bilgisil()

    elif işlem == "3":
        listele(liste)

    elif işlem == "4":
        root1 = open("deneme.txt", "r", encoding="utf8")
        print(root1.read())
        root1.close()







    elif işlem == "q" or işlem == "Q":
        cikis()

    else:
        print("Geçersiz işlem")




