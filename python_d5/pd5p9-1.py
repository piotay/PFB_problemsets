#!usr/bin/env python3
import sys
import re

file = ""

class CHARERROR(Exception):
     pass

try:
    file = sys.argv[1]
    print("User provided file: ", file)

    if not (file.endswith(".fa") or file.endswith(".fasta") or file.endswith(".nt")):
        raise ValueError("Not a FASTA file. Must end in .fa .fasta or .nt")
    

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

                allowed_chars = "ATGCN"

                for char in sequ:
                    if char not in allowed_chars:
                        raise CHARERROR(f"{gene} sequence contains non-ATGCN character")

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
        
except IndexError:
     print("Please provide a file name")
except IOError:
     print("Can't find/open file.")
