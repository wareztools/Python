try:
    root = open("deneme.txt","r")


except IOError:
    print("Bir Hata Olustu!")
finally:
    root.close()

with open("deneme.txt","r",encoding="utf8") as root:
    print(root.read())