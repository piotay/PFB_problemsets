#!/usr/bin/env python3
import sys

#my function takes in a string
def lessthanx(file, maxlength):
    with open(file, 'r') as fasta_r, open("modified_fasta.txt",  "w") as write_fasta:
        
        sequ = ""
        seq1 = {}
        
        for line in fasta_r:
        #iterate through each line and find out if it is a gene header or sequence line
        #if the line starts with >, then its a gene header and I write that gene to the file
            if line.startswith(">"):
                
                gene_head = line                

            #otherwise, its a sequence line and I need to get the full sequence for that gene.
            else:
                sequ = sequ + line.rstrip()
                seq1[gene_head] = sequ
            
        for gene in seq1:
        #take the length of input string
            dna = seq1[gene]
            dna_len = len(dna)

            #I want to insert a line this many times
            no_iter = dna_len/maxlength+1

            startpos = 0
            endpos = 1
            count = 1

            line_list = []

            while count <= no_iter:
                
                line = dna[startpos*maxlength:(endpos*maxlength)]

                line_list.append(line)

                startpos += 1
                endpos += 1
                count += 1

            write_fasta.write(gene)
            write_fasta.write("\n".join(line_list)+"\n")



filename = sys.argv[1]
maxlen = int(sys.argv[2])

lessthanx(filename, maxlen)



