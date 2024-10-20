#/usr/bin/env python3
import re

fastaDict = {}

with open("/Users/pfb2024/PFB_data/Python_07_ApoI.fasta", "r") as seq_fasta:
    for line in seq_fasta:
        if line.startswith(">"):
            seq = ""
            info = re.search(r"^>(.*?)", line)
            gene = info.group(1)
            gene = gene.rstrip()

        else:
            
            seq = seq + line.rstrip()
            fastaDict[gene] = seq

    sites = []
    match = seq[0:]

    for gene in fastaDict:
        sequ = fastaDict[gene]
        
        for found in re.finditer(r"[GA](A)ATT[TC]", sequ):
            sites.append(found.group(0))
            
        for site in sites:
            match = re.sub(site, site[0]+"^"+site[1:], match)

        frags = match.split("^")
        print(sorted(frags, key=len))
        