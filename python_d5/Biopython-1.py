#!/usr/bin/env python3

from Bio import SeqIO

id_dict = SeqIO.to_dict(SeqIO.parse("/Users/pfb2024/PFB_data/Python_08.fasta", "fasta"))

totalnuccount = 0
shortest = 0
longest = 0
totalgccont = 0
highestgc = 0
lowestgc = 0

for entry in id_dict:
    curlen = len(str(id_dict[entry].seq))

    if shortest == 0:
        shortest = curlen
    elif curlen < shortest:
        shortest = curlen

    if curlen > longest:
        longest = curlen

    gccont = str(id_dict[entry].seq).count("G")+str(id_dict[entry].seq).count("C")
    
    totalgccont += gccont

    if curlen > highestgc:
        highestgc = gccont/curlen
    
    if lowestgc == 0:
        lowestgc = gccont/curlen

    elif curlen < lowestgc:
        lowestgc = curlen

    totalnuccount += curlen

avglength = totalnuccount/len(id_dict)

print(f"\nTotal # Nucleotides: {totalnuccount}")
print(f"Sequence Count: {len(id_dict)}")
print(f"Avg Sequence Length: {avglength:.2}")
print(f"Shortest Sequence Length: {shortest}")
print(f"Longest Sequence Length: {longest}")
print(f"Average GC content: {totalgccont/totalnuccount:.2%}")
print(f"Highest GC content: {highestgc:.2%}")
print(f"Lowest GC content: {lowestgc:.2%}\n")


