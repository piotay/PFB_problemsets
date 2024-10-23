#!usr/bin/env python3
#Not done!!! on number 6

class DNAseq(object):
    def __init__(self, sequence, name, organism):
        #define class attributes
        self.sequence = sequence
        self.name = name
        self.organism = organism

    #define methods
    def length(self):
        length = len(self.sequence)
        return length
    
    def nt_comp(self):
        acount = self.sequence.count("A")
        tcount = self.sequence.count("T")
        gcount = self.sequence.count("G")
        ccount = self.sequence.count("C")

        return {"A" : acount, "T": tcount, "G" : gcount, "C" : ccount}


SOX10_gene = DNAseq(sequence="ABCGTCGATCG", name = "SOX10", organism="hoomin")

print(f"\nSequence: {SOX10_gene.sequence}\nName: {SOX10_gene.name}\nOrganism: {SOX10_gene.organism}")
print(f"The sequence length is {SOX10_gene.length()} nts girlypop\n")
print(f"As: {SOX10_gene.nt_comp()["A"]}\tTs: {SOX10_gene.nt_comp()["T"]}\tGs: {SOX10_gene.nt_comp()["G"]}\tCs: {SOX10_gene.nt_comp()["C"]}")
