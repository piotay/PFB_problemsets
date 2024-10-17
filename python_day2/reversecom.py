#!usr/bin/env python3

import sys

seq = sys.argv[1]
comp = seq.replace("A", "1") #Replace A with 1
comp = comp.replace("T", "2") #Replace T with 2
comp = comp.replace("G", "3") #Replace G with 3
comp = comp.replace("C", "4") #Replace C with 4

comp = comp.replace("1", "T") #Replace A with T
comp = comp.replace("2", "A") #Replace T with A
comp = comp.replace("3", "C") #Replace G with C
comp = comp.replace("4", "G") #Replace C with G

revcomp = comp[::-1]

print(f"{"Original Sequence":<25}", f"5' {seq} 3'")
print(f"{"Complement":<25}", f"3' {comp} 5'")
print(f"{"Reverse Complement":<25}", f"5' {revcomp} 3'")
