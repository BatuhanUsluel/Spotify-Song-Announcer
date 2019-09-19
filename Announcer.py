import pyttsx3
import time
from SwSpotify import spotify
import argparse
prevsong = ""
prevartist = ""
engine = pyttsx3.init()


parser = argparse.ArgumentParser("Spotify Song Announcer")
parser.add_argument("-l", "--list", help="Lists available voices, quits", required=False, action='store_true')
parser.add_argument("-s", "--set", help="Sets the voice", type=int, default=1, required=False)
parser.add_argument("-d", "--delay", help="Delay before announcement(seconds)", type=float, default=0, required=False)
parser.add_argument("-r", "--rate", help="Speaking rate in words per minute[Default: 170]", type=int, default=170, required=False)
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
    if (args.set > len(voices)-1):
        print ("Input voice out of range. Please input a number from 0 to " + str(len(voices)-1))
        quit()
    engine.setProperty('voice', voices[args.set].id)

engine.setProperty('rate', args.rate)

while True:
	try:
		song = spotify.song()
		artist = spotify.artist()
		if (not(song == None or artist == None) and (song != prevsong or artist!=prevartist)):
			if (args.delay!=0):
				time.sleep(args.delay)
			engine.say("Playing " + song + " by " + artist)
			engine.runAndWait()
			print("Playing " + song + " by " + artist)
			prevsong = song
			prevartist = artist
	except spotify.SpotifyNotRunning as e:
		pass
	time.sleep(1)