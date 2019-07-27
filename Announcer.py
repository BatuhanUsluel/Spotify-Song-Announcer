import pyttsx3 
f = open("Snip.txt", "r", encoding="utf8")
song = f.read()
print(song)

engine = pyttsx3.init() 
engine.say(song) 
engine.runAndWait() 