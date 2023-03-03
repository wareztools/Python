import time
import os



import vlc

def song():
    G = vlc.MediaPlayer("C:/Users/titan/Desktop/mermi.mp3")
    G.play()
    time.sleep(2)
    G.stop()