#!/usr/bin/env python3
import sys
import re

file = "/Users/pfb2024/PFB_data/canu/ecoli_0.25.contigs.fasta"

contigs  = {}
shortestcontig = ""
longestcontig = ""
totalcontiglen = 0

with open(file, "r") as fasta:
    for line in fasta:
        if line.startswith(">"):
            sequ = ""
            gene = re.search(r"^>(.*?)\s", line)
            gene = gene.group(1)
            gene = gene.rstrip()

        else:
            sequ = sequ + line.rstrip()
            contigs[gene] = sequ

#here I find the longest, shortest, and total contig length
    for entry in contigs:
        cur_len = len(contigs[gene])
        totalcontiglen += len(contigs[entry])
        if shortestcontig == "":
            shortestcontig = entry
        elif cur_len <= len(contigs[shortestcontig]):
            shortestcontig = entry
        if longestcontig == "":
            longestcontig = entry
        if cur_len > len(contigs[longestcontig]):
            longestcontig = entry

#here I will calculate the N50 length omg I have to SORT AGAINNNNNNN
sortedcontigs = dict(sorted(contigs.items(), key = lambda items : items[1]))
the50 = totalcontiglen/2
entryn50 = 0
contiglen = 0
contig_count = 0

for entry in sortedcontigs:
    
    contig_count += 1
    contiglen += len(sortedcontigs[entry])

    if contiglen >= the50:
        entryn50 = entry
        break
        

print(f"Number of contigs: {len(contigs)}")
print(f"Shortest contig: {shortestcontig}\t{len(contigs[shortestcontig])}")
print(f"Longest contig: {longestcontig}\t{len(contigs[longestcontig])}")
print(f"Total contig length: {totalcontiglen}")
print(f"The N50 size: {len(contigs[entryn50])}")
print(f"The L50 contig count: {contig_count}")

#get all your contigs, sort, find your shortest, 
# your longest. once you find you longest how many are above that
#B. we will have a large file, we wnat to know how many masks (lowercase) 