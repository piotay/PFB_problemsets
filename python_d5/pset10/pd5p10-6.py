#!/usr/bin/env python3


def get_revcomp(dna):
    comp = dna.replace("T", "1")
    comp = comp.replace("G", "2")
    comp = comp.replace("C", "3")
    comp = comp.replace("A", "4")

    comp = comp.replace("1", "A")
    comp = comp.replace("2", "C")
    comp = comp.replace("3", "G")
    comp = comp.replace("4", "T")

    revcomp = comp[::-1]

    return(revcomp)

dna_seq = "GTCAGCTAATAGCTAGATCGAT"
print(get_revcomp(dna_seq))
