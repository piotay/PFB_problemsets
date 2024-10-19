#!/usr/bin/env python3
import sys

def gccont(dna):
    dna = dna.upper()
    ccount = dna.count("C")
    gcount = dna.count("G")

    gccont = (ccount+gcount)/len(dna)

    return f"{gccont:.2%}"

dna = sys.argv[1]

print(gccont(dna))

