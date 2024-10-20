#!/usr/bin/env python3
import re

fastaDict  = {}
gene = ""

with open("/Users/pfb2024/PFB_data/Python_07.fasta", "r") as seq_fasta:
    for line in seq_fasta:

        if line.startswith(">"):

            seq = ""
            info = re.search(r"^>(.*?)\s(.*?)\n", line)
            gene = info.group(1)
            gene = gene.rstrip()

        else:
            
            seq = seq + line.rstrip()
            fastaDict[gene] = seq
    
    print(fastaDict)