# Spotify Song Announcer
When it detects a song change in spotify, it reads out the song name and artist.

Does not use the spotify api which allows it to be used offline.

Uses SwSpotify to get the song & pyttsx3 for text to speech. 

Supported Platforms:
+ Windows
+ Linux
+ Mac

```
usage: Spotify Song Announcer [-h] [-l] [-s SET] [-d DELAY] [-r RATE]

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            Lists available voices, quits
  -s SET, --set SET     Sets the voice
  -d DELAY, --delay DELAY
                        Delay before announcement(seconds)
  -r RATE, --rate RATE  Speaking rate in words per minute[Default: 170]
```