#!/usr/bin/env python3
import sys

seq = sys.argv[1]

seq = seq.upper()

nas = seq.count('A')
nts = seq.count("T")
ncs = seq.count("C")
ngs = seq.count("G")

print(f"""
There are {nas} As, {nts} Ts, {ncs} Cs, and {ngs} Gs in your sequence
""")

rna = seq.replace("T", "U")

print(f"""Here is your sequence with Ts replaced with Us: {rna}
""")

print(f"""The AT content of your sequence is {(nas+nts)/len(seq):.1%}.
The GC content of your sequence is {(ncs+ngs)/len(seq):.1%}
""")



