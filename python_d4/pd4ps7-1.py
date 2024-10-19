#/usr/bin/env python3
import re

with open("Python_07_nobody.txt") as py7no:
    linepo=1
    for line in py7no:
        for found in re.finditer(r"nobody", line, re.I):
            whole = found.group(0)
            startpo = found.start(0)+1
            endpo = found.end(0)
            print(f"{whole} Line:{linepo} {startpo} {endpo}")
            linepo+=1

