#/bash/bin/env python3

with open("Python_06.txt", "r") as song_obj, open("Python_06_uc.txt", "w") as lyrics_write:
    for line in song_obj:
        line = line.rstrip()
        
        lyrics_write.write(f"{line}\n")
        
        
