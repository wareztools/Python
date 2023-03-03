import time

username = input("Username :")
password = input("Password :")

a = "admin"
b = "aa77effea0"

if username != a:
    time.sleep(2)
    print("Şifre hatalı.")
elif password != b:
    time.sleep(2)
    print("Şifre hatalıdır.")

else:
    print("Giriş başarılı")
