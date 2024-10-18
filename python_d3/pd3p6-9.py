#!/usr/bin/env python3

fastaDict  = {}
gene = ""

with open("Python_06.fasta", "r") as seq_fasta:
    for line in seq_fasta:

        if line.startswith(">"):

            seq = ""
            gene = line.replace(">", "")
            gene = gene.rstrip()

        else:
            
            seq = seq + line.rstrip()
            fastaDict[gene] = seq
    
    print(fastaDict)