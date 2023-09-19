import os

files = os.listdir("./")

for song in files:
    if song.endswith(".mp3"):
        wm_removed = song.split(" ")[1]
        
        if not wm_removed.endswith(".mp3"):
            wm_removed = wm_removed + ".mp3"

        os.rename(f"./{song}", f"./{wm_removed}")
