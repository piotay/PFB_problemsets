#!/usr/bin/env python3
import sys

listed = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for n in listed: 
	print(f"{listed.index(n)}\t{len(n):<20}\t{n}")



