import pyttsx3
import time
from SwSpotify import spotify
import argparse
prevsong = ""
prevartist = ""
engine = pyttsx3.init()


parser = argparse.ArgumentParser("CSV Splitter")
parser.add_argument("-l", "--list", help="Lists available voices, quits", required=False, action='store_true')
parser.add_argument("-s", "--set", help="Sets the voice", type=int, default=1, required=False)
args = parser.parse_args()

if (args.list):
    voices = engine.getProperty('voices')
    i=0
    for voice in voices:
        print (str(i) + ":")
        print(" - Name: %s" % voice.name)
        i=i+1
    quit()
    
if (args.set != None):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[args.set].id)

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