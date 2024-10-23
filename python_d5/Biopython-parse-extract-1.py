#!/usr/bin/env python3

from Bio import SeqIO
import re

id_dict = SeqIO.to_dict(SeqIO.parse("/Users/pfb2024/PFB_data/uniprot_sprot.fasta", "fasta"))

id_list = []
desc_list = []
species_list = []

for entry in id_dict:
    id_list.append(entry)
    desc_list.append(id_dict[entry].description)

for entry in desc_list:
    found = re.search(r"\sOS=(\w+\s+\w+.*\s)OX", entry)
    
    if found:
        if found.group(1) not in species_list:
            species_list.append(found.group(1))

seq_count = {}

for entry in id_dict:
    found = re.search(r"\sOS=(.*)\sOX", id_dict[entry].description)
    if found:
        species = found.group(1)
    if not found:
        print(f"Not found: {id_dict[entry].description}")

    if species not in seq_count:
        seq_count[species] = 1
    else:
        seq_count[species] += 1

#print(seq_count)

with open("s_paratyphi.prot.fa", "w") as salmon:
    for entry in id_dict:
        if ("Salmonella paratyphi B") in id_dict[entry].description:
            salmon.write(f">{id_dict[entry].description}\n{id_dict[entry].seq}\n")


    

