bilgiler = {"isim" : "Hamza","Soyisim" : "Kılıç","Tel" : 5543334355}

#d = input("Bilgileri sorgula :")

#print(bilgiler[d]) program çökmemesi için get komutunu kullanalım!

#print(bilgiler.get(d,"Geçersiz işlem"))

for i in bilgiler.items():
    print(i)
print(50* "=")

for i in bilgiler.keys():
    print(i)
print(50* "=")

for i in bilgiler.values():
    print(i)

