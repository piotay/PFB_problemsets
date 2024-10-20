#/usr/bin/env python3
#NOT DONEEEEEE THIS IS NUMBER 10

import re
import sys

fastaseq = sys.argv[1]
enzname = sys.argv[2]

lineno = 1
enzdict = {}

with open("/Users/pfb2024/PFB_data/bionet copy.txt", 'r') as enzs:
    for line in enzs:
        if lineno > 10:
            match = re.search(r"(\w+\s?\(?\w*\)?)\s*([\w\^]+)", line)
            
            if match:
                enz = match.group(1) 
                site = match.group(2)

                if enz not in enzdict:
                    enzdict[enz] = [site]
                
                else:
                    enzdict[enz].append(site)

    
            
        lineno += 1

fastaDict = {}

#here I build my dictionary of genes and sequences from teh fasta file
with open(fastaseq, "r") as seq_fasta:
    for line in seq_fasta:
        if line.startswith(">"):
            seq = ""
            info = re.search(r"^>(.*?)", line)
            gene = info.group(1)
            gene = gene.rstrip()

        else:
            
            seq = seq + line.rstrip()
            fastaDict[gene] = seq

    #now, I want to search each gene sequence, I want to check if 
    # any enzyme has a sequence contained

    for gene in fastaDict:
        for enzno in enzdict:
            if enzname in enzno:
                for site in enzdict[enzno]:
                    gene_sequence_to_check = fastaDict[gene]

                    site.replace("R")


    
    
    sites = []
    match = seq[0:]

    # for gene in fastaDict:
    #     sequ = fastaDict[gene]
        
        for found in re.finditer(r"[GA](A)ATT[TC]", sequ):
            sites.append(found.group(0))
            
    #     for site in sites:
    #         match = re.sub(site, site[0]+"^"+site[1:], match)

    #     frags = match.split("^")
    #     print(sorted(frags, key=len))