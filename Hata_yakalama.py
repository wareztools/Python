a = float(input("sayi :"))
b = float(input("sayi :"))

try:
    print(a/b)
except ZeroDivisionError as hata:
    print("Deger asla 0'a bolunemez.",hata)

finally:
    print("Wareztools")

