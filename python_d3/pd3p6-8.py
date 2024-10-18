#/usr/bin/env python3

with open("Python_06.fastq", "r") as read_fastq:
    
    linecount = 0
    charcount = 0
    sumlen = 0
    
    for line in read_fastq:
        line.rstrip()
        linecount += 1
        charcount += len(line)
        sumlen += charcount

avglen = sumlen/linecount

print(f"{linecount}\t{charcount}\t{avglen}")