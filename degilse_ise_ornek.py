

a = "admin"
b = "ASLAN"

user = input("username :")
pas = input("password :")

if user != a:
	print("Kullanıcı adı hatalı.")
elif pas != b:
	print("Şifre hatalı")

elif user != a.lower():
	print("Kullanıcı adı  küçük harfler ile yazılmalıdır")
elif pas != b.upper():
	print("Şifre büyük harfler ile yazılmalıdır.")

else:
	print("WELCOME BRO")
