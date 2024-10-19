#/usr/bin/env python3
import re

file = ""

with open("Python_07_nobody.txt", 'r') as pyno, open("Python_07_nobody_sub.txt", "w") as pyfloss:
    for line in pyno:
        
        line2 = re.sub(r"nobody", "Flossy",line, flags=re.I)
        
        file = file + line2

    pyfloss.write(file)
    