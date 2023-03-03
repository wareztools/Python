import time
import vlc

import os





Hamza = {"Güç" : 555,
         "HP"  : 933}
Samet = {"Güç" : 555,
         "HP"  : 654}

while True:

    os.system("cls")
    def song():
        G = vlc.MediaPlayer("C:/Users/titan/Desktop/mermi.mp3")
        G.play()
        time.sleep(1)
        G.stop()
    def saldır(vuran:dict,vurulan:dict):
        eksilen = vuran["Güç"]
        vurulan["HP"] = vurulan["HP"] -eksilen
    input("Saldırı için Enter'a basınız :")
    saldır(Hamza,Samet)
    print("Sametin Canı : ",Samet["HP"],song())

    input("Saldırı için Enter'a basınız :")
    saldır(Samet,Hamza)
    print("Hamza'nın canı :" ,Hamza["HP"],song())


