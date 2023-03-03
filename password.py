username = input("user :")
password = input("pass :")

a = "ADMİN"
b = "aa77effea0"

#if username != a.lower():
  #  print("küçük harfler kullanın")

if username != a.upper():
    print("Büyük harfler kullanın")

elif username != a:
    print("Kullanıcı adı hatalı")

elif password != b:
    print("Şifre hatalı")

else:
    print("Hoşgeldiniz")