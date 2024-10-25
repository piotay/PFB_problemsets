#!/usr/bin/env python3
import sys
import re

file = "/Users/pfb2024/PFB_data/canu/D_melano_filtered_0.6.fastq"

contigs  = {}
totalseq = ""

with open(file, "r") as fasta:
    for line in fasta:
        if line.startswith(">"):
            sequ = ""
            gene = re.search(r"^>(.*?)\s", line)
            gene = gene.group(1)
            gene = gene.rstrip()

        else:
            sequ = sequ + line.rstrip()
            totalseq += line.rstrip()
            contigs[gene] = sequ

chars = ["A", "T", "C", "G", "g", "c", "a", "t", "N"]
charcount = {}
for char in chars:
    charcount[char] = totalseq.count(char)


print(f"{charcount}")
print(f"Contigs: {len(contigs)}")
print(f"{charcount["N"]/len(totalseq):%}")

#The output was pfb2024@info18 canu % python3 canu-2.py
#{'A': 4685622, 'T': 4684038, 'C': 3964240, 'G': 3964411, 'g': 633601, 'c': 635344, 'a': 1515569, 't': 1509495, 'N': 0}
#Contigs: 1
#0.000000%
