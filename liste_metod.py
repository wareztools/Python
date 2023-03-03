liste = ["python","Hamza",28,"test"]

liste.append("wareztools.com")

liste.remove("wareztools.com")


liste2 = liste

liste3 = liste.copy() # liste 3 yedeğini kopyaladık

liste.remove(28)

print(liste)

#print(liste3)  yedek silinmedi

print(liste2)
print(50* "=")

print(liste.count("Hamza"))
# count içinde aynı değerden kaç adet olduğunu gosterir. aynı deger yok ise 0 'degeri verir.

a = [2,5,6,8,9,11]

a.sort()
print(a)

b = ["python","Yazılım","Ogreniyoruz"]
b.sort()
print(b)

print(liste.index("python"))


c = int(liste.index("test"))

c += 0
print(c)



