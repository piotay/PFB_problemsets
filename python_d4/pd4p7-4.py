#!/usr/bin/env python3
#

import re

filepath = "/Users/pfb2024/PFB_data/Python_07.fasta"

gene = ""
seqs = {}

with open(filepath) as py7fasta:
    for line in py7fasta:
        if line.startswith(">"):
           
            sequ = ""
            info = re.search(r"^>(.*?)\s(.*?)\n", line)
            gene = info.group(1)
            desc = info.group(2)
            seqs[gene] = desc
            

        #else:


            #sequ = sequ + line.rstrip()

            #seqs[gene] = sequ

    print(seqs)

            

