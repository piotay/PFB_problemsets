#/usr/bin/env python3
import re
import sys

file = "/Users/pfb2024/PFB_data/Python_08.fasta"

seqsfr1  = {}
seqsfr2  = {}
seqsfr3  = {}


with open(file, "r") as fasta:
    for line in fasta:

        if line.startswith(">"):
            
            sequ = ""
            gene = re.search(r"^>(.*?)\s", line)
            gene = gene.group(1)
            gene = gene.rstrip()

        else:


            sequ = sequ + line.rstrip()

            seqsfr1[gene] = []
            seqsfr1[gene] = re.findall(r"\w\w\w", sequ)

            seqsfr2[gene] = []
            sequ2 = sequ[1:]
            seqsfr2[gene] = re.findall(r"\w\w\w", sequ2)

            seqsfr3[gene] = []
            sequ3 = sequ[2:]
            seqsfr3[gene] = re.findall(r"\w\w\w", sequ3)


codondict = {}

with open("Python_08.codons-frame-1.nt","w") as write_codons:

    for gene in seqsfr1:
        codon_list = seqsfr1[gene]
        
        codons = " ".join(codon_list)

        write_codons.write(f"{gene}-frame-1-codons\n{codons}\n")




with open("Python_08.codons-3frames.nt","w") as write_codons:

        for gene in seqsfr1:
            codon_list1 = seqsfr1[gene]
            codons1 = " ".join(codon_list1)
            
            codon_list2 = seqsfr2[gene]
            codons2 = " ".join(codon_list2)

            codon_list3 = seqsfr2[gene]
            codons3 = " ".join(codon_list3)

            write_codons.write(f"{gene}-frame-1-codons\n{codons1}\n")
            write_codons.write(f"{gene}-frame-2-codons\n{codons2}\n")
            write_codons.write(f"{gene}-frame-3-codons\n{codons3}\n")

    

