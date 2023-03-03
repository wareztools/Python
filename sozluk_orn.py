import os

os.system("cls")
supermen = {"Güç" : 400,
            "HP"  : 1000}

Batman =   {"Güç" : 200,
            "HP"  : 2000 }

while True:
    def attack(vuran:dict,vurulan:dict):
        eksilen = vuran["Güç"]
        vurulan["HP"] = vurulan["HP"] - eksilen
    input("Vurmak için Ente'ra basınız : ")
    attack(supermen,Batman)
    print("Batman'ın canı ",Batman["HP"])

    input("Vurmak için Ente'ra basınız : ")
    attack(Batman,supermen)
    print("Superman'n canı ",supermen["HP"])






