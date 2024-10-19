#!/usr/bin/env python3
#NOT DONEEEEEEEEEEE---------

import re

filepath = "/Users/pfb2024/PFB_data/Python_07.fasta"

gene = ""
fastadic = {}

with open(filepath) as py7fasta:
    for line in py7fasta:
        for (gene, desc) in re.findall(r"(^>.*?\s)(.*)", line):

            if gene:
                seq = ""
                gene = gene.replace(">", "")
                print(f"id: {gene} desc: {desc}")
            else:
                seq = seq + line.rstrip()
                fastadic[gene] = seq

