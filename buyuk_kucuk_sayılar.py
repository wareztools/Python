tahmin = int(input("sayi giriniz :"))

if tahmin < 1:
	print("1'den düşük deger girdiniz")

elif tahmin <= 10:
	print("Tebrikler \1")

elif tahmin > 10:
	print("10 üzeri bir deger girdiniz")

else:
	print("Geçersiz işlem")