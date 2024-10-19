#/usr/bin/env python3
import sys
import re

file = sys.argv[1]

seqs  = {}


with open(file, "r") as fasta:
    for line in fasta:

        if line.startswith(">"):
            
            sequ = ""
            gene = re.search(r"^>(.*?)\s", line)
            gene = gene.group(1)
            gene = gene.rstrip()

        else:


            sequ = sequ + line.rstrip()

            seqs[gene] = {}

            Acount = sequ.count("A")
            seqs[gene]["A"] = Acount
            Tcount = sequ.count("T")
            seqs[gene]["T"] = Tcount
            Gcount = sequ.count("G")
            seqs[gene]["G"] = Gcount
            Ccount = sequ.count("C")
            seqs[gene]["C"] = Ccount



    for gene in seqs:
            print(f"{gene}\tA count:{seqs[gene]["A"]}\tT count:{seqs[gene]["T"]}\tC count:{seqs[gene]["C"]}\tG count:{seqs[gene]["G"]}")
        
