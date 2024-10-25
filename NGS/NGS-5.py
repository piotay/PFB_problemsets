#!/usr/bin/env python3
import sys
import re

file = "/Users/pfb2024/PFB_problemsets/NGS/Ecoli.fasta"

totalseq = ""

with open(file, "r") as fasta:
    for line in fasta:
        if line.startswith(">"):
            if "DNA" in line:
                sequ = ""
                header = line

        else:
            sequ = sequ + line.rstrip()
            totalseq += line.rstrip()

print(f"{len(sequ)}")
print(f"{len(totalseq)}")

