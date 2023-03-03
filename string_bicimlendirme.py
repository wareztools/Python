
a = """

istanbul : fethi 1453
ankara   : {}
samsun   : {}
izmir    : {}


""".format("Başkent","Pidesi meşhur","Sahili güzel")
print(a)

a = "123456"

for i in a:
    print("Hayata {} - 0 önce başla".format(i))
    print("Hayata",i,"0 önce basla")


a = 10
b = "Python"
c = "Ogreniyorum"

#run = "{0}\n {1}\n {2}\n".format(a,b,c)
run = "{orta} {ilk} {son}".format(ilk = a,orta =b,son = c)
print(run)
print(50*"/")
T = "|{:b}|".format(a)
print(T)
S = "|{:s}|".format(b)
print(S)
# < sol, > sag ,^ orta

