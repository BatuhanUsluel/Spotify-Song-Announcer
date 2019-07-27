import pyttsx3
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
old = 0
class MyHandler(PatternMatchingEventHandler):
    patterns = ["*./Snip.txt"]
    file_cache = {}
    def on_modified(self, event):
        seconds = int(time.time())
        key = (seconds, event.src_path)
        if key in self.file_cache:
            return
        print ("MODIFIED")
        self.file_cache[key] = True
		
event_handler = MyHandler()
my_event_handler = PatternMatchingEventHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=False)
observer.start()

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer.stop()
observer.join()
	
# f = open("Snip.txt", "r", encoding="utf8")
# song = f.read()
# print(song)

# engine = pyttsx3.init() 
# engine.say(song) 
# engine.runAndWait() 