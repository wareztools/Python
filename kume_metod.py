# kume.remove("komodor") silinmiş ögeye girindinde hata verecektir remove

# remove 1 defa için geçerlidir

# discard hata vermeden silinir


kume = {'python','root'}
kume2 = {'Yazılım','Kılıç',33,44,55,'root',"python"}

print(type(kume))

#kume.add("test")



#kume.remove("python")

print(50* "/")

kume.discard(33)
print(kume)

#kume.add("Komodor")
print(kume)

#kume.discard("komodor")
print(100 * "=")
print(kume2)



print(kume.difference(kume2)) #kume 1 kume 2 farklarını gosteriyor difference

print(kume.symmetric_difference_update(["root"]))

#symmetric_difference_update aynı olan degerleri yansıtmıyor...
print(kume)
print(kume.symmetric_difference(kume2))

#symmetric_difference aynı olan degerleri algılamıyor

print(kume.intersection(kume2))

#print(kume.isdisjoint(kume2)) false true deger verir ayn ıveya degıl






