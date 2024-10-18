#!/usr/bin/env python3

with open("Python_06.seq.txt", "r") as py6:
    #structure seqName\tsequence\n
    for line in py6:
        line = line.rstrip()
        seqname, seq = line.split()

        Gcount = seq.count("G") 
        Ccount = seq.count("C")
        Tcount = seq.count("T")
        Acount =seq.count("A")

        gccont = 100*(Gcount+Ccount)/(Gcount+Ccount+Tcount+Acount)

        print(seqname)
        print(f"G: {Gcount}\tC: {Ccount}\tT: {Tcount}\tA: {Acount}")
        print(f"GC content: {gccont:.2f}%\n")