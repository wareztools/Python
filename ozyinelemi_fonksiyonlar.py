def karsılama(kisisayisi = 1):
    for i in range(kisisayisi):
        print("merhaba")
karsılama(5)
print(50*"/")
def karsılamaoz(kisisayisi = 1):
    if kisisayisi <= 1:
        print("merhaba")
    else:
        print("merhaba")
        karsılama(kisisayisi -1)

karsılamaoz(3)