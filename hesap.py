print("""
* çarpma işlemi
+ toplama işlemi
- çıkartma işlemi
/ bolme işlemi

""")

işlem = input("işlem seçiniz :")
sayi1 = float(input("sayi giriniz :"))
sayi2 = float(input("sayi giriniz :"))

if işlem == "*":
	sonuc = sayi1 * sayi2
	print("Çarpım sonuc ",sonuc)
elif işlem == "+":
	sonuc = sayi1 + sayi2
	print("Toplama Sonucu",sonuc)

elif işlem == "-":
	sonuc = sayi1 - sayi2
	print("Çıkartma sonucu",sonuc)

elif işlem == "/":
	sonuc = sayi1 / sayi2
	print("Bolme sonuc :",sonuc)

else:
	print("geçersiz işlem")