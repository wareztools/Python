print("""

isim  :{}
sehir :{}
Tel   :{}

""".format("Hamza","İstanbul","05383436753"))

a = "123456789"

#for i in a:
     #print("Hayata {} : 0'dan once basla".format(i))
     #print("Hayata",i,"0'dan once basla")
print(50*"/")

a = "python"
b = "yazılım"
c = "10"

sirala = "{ilk}\n {orta}\n {son}\n".format(ilk = b,orta = c,son = a)
print(sirala)
print(50*"/")

D = "|{:^20}|".format(a)
print(D)

S = "|{:>30}|".format(b)
print(S)


F = "|{:s}|".format(c)
print(F)

#d str
#s int