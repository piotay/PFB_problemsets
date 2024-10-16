#!usr/bin/env python3
import sys

seq = sys.argv[1]

subseq = seq[99:200]

print(f"""
Here are nucleotides between 100 and 200:
{subseq}
""")


gcount = subseq.count("G")

print(f"""There are {gcount} Gs in nucleotides 100-200.
""")

