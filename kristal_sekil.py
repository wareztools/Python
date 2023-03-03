def sag(adet):
	for a in range(int(adet)):
		print("/", end= "")

def sol(adet):
	for a in range(int(adet)):
		print("\\",end = "")

def bosluk(adet):
	for a in range(int(adet)):
		print(" ",end ="")

def atla(adet):
	for a in range(int(adet)):
		print()

def üst(cap):
	baslangıc = cap/2-1
	for a in range(int(cap/2)):
		bosluk(baslangıc-a)
		sag(1)
		bosluk(a*2)
		sol(1)
		atla(1)

def alt(cap):
	baslangıc = cap-2
	for a in range(int(cap/2)):
		bosluk(a)
		sol(1)
		bosluk(baslangıc-a*2)
		sag(1)
		atla(1)

def paralel(cap):
	üst(cap)
	alt(cap)

while True:
	boyut = int(input("Çapı giriniz :"))
	print()
	paralel(boyut)