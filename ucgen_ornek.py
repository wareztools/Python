def hipo(a,b,c):
	if a ** 2 + b **2 == c **2:
		return "bu bir üçgendir."
	else:
		return "bu bir üçgen değildir."

bir = int(input("ilk üçgen gir :"))
iki = int(input("iki üçgen gri :"))
uc = int(input("üçüncü üçgen gir :"))

print(hipo(bir,iki,uc))
