import pyttsx3
import time
from SwSpotify import spotify
prevsong = ""
prevartist = ""
engine = pyttsx3.init() 
while True:
    song = spotify.song()
    artist = spotify.artist()
    if (not(song == None or artist == None) and (song != prevsong or artist!=prevartist)):
        engine.say("Playing " + song + " by " + artist)
        engine.runAndWait()
        print("Playing " + song + " by " + artist)
        prevsong = song
        prevartist = artist
    time.sleep(1)