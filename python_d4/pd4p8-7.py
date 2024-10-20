#!/usr/bin/env python3

#Not done!!! working on no7

import re
import sys

file = "/Users/pfb2024/PFB_data/Python_08.fasta"

seq1 ={}
seq2 = {}
seq3 = {}
seq4 = {}
seq5 = {}
seq6 = {}
sequ = ""

#Opening my fasta file
with open(file, "r") as fasta:
    for line in fasta:
        
        #iterate through each line and find out if it is a gene header or sequence line
        #if the line starts with >, then its a gene header and I extract the gene from it
        if line.startswith(">"):
            
            sequ = ""
            gene = re.search(r"^>(.*?)\s", line)
            gene = gene.group(1)
            gene = gene.rstrip()

        #otherwise, its a sequence line and I need to get the full sequence for that gene. I also need to get the two
        #shifted open reading frames from it. Since I use find all, it stores them as a bunch of codons per each gene.
        else:

            sequ = sequ + line.rstrip()

            seq1[gene] = []
            seq1[gene] = re.findall(r"\w\w\w", sequ)

            seq2[gene] = []
            sequ2 = sequ[1:]
            seq2[gene] = re.findall(r"\w\w\w", sequ2)

            seq3[gene] = []
            sequ3 = sequ[2:]
            seq3[gene] = re.findall(r"\w\w\w", sequ3)

#after this, I have three sequences one for each reading frame, the sequences are stored as a list of codons

#here is my translation table for each codon
translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}


#Now I am going to write  three files with each of the 3 ORFs (1-3) and their reverse compelements (4-6) for each gene
#first file is each codon
#second file is translated
#third file is only the longest ORF

with open("Python_08.codons-6frames.nt","w") as write_codons, open("Python_08_translated.txt", "w") as write_aa, open("Python_08.translated-longest.txt", "w") as long_aa, open("Python_08.orf-longest.nt", "w") as longest_aa_codon:
        #since each file is organized by gene, I will iterate through each gene in seq 1. the same genes are in all six seqs 
        # so it doesnt matter which I do

        for gene in seq1:
            
            #here I take the list of codons by calling the gene entry from that sequence
            #then, I join the list into a single sequence with spaces between codons
            #I do this for each of my three sequences
            codon_list1 = seq1[gene]
            codons1 = " ".join(codon_list1)
            
            codon_list2 = seq2[gene]
            codons2 = " ".join(codon_list2)

            codon_list3 = seq3[gene]
            codons3 = " ".join(codon_list3)

            #now I write to the file the codons string (1-3)
            write_codons.write(f"{gene}-frame-1-codons\n{codons1}\n")
            write_codons.write(f"{gene}-frame-2-codons\n{codons2}\n")
            write_codons.write(f"{gene}-frame-3-codons\n{codons3}\n")

            #here I make a list of my codon strings, tehn make a copy of that list
            codons_list = [codons1, codons2, codons3]
            copy_codons_list = codons_list.copy()

            #I make a number four because I will start with sequence 4 (reverse complement of 1)
            num = 4
            #for each of my three sequences, I find the reverse complement
            for sequence in codons_list:
                comp = sequence.replace("T", "1")
                comp = comp.replace("G", "2")
                comp = comp.replace("C", "3")
                comp = comp.replace("A", "4")

                comp = comp.replace("1", "A")
                comp = comp.replace("2", "C")
                comp = comp.replace("3", "G")
                comp = comp.replace("4", "T")

                revcomp = comp[::-1]

                #here I add the reverse complement to my codons list so it will 
                #have ALL 6 sequences!!!
                copy_codons_list.append(revcomp)

                #I finihs writing 4-6 to my codons file
                write_codons.write(f"{gene}-frame-{num}-codons\n{revcomp}\n")

                #add a count to my number so it goes up to  and 6
                num += 1

            #here I resent number to 1
            num = 1

            #initialize this list to find the longest amino acid
            find_longest = []

            #iterate through 6 codons strings and split each string of into list 
            # so that I can translate using dictionary
            for codon_unit in copy_codons_list:
                
                #here I split a codon string into a list with a bunch of codons
                listy = codon_unit.split(" ")

                #here I want a list of all the amino acids just tfor that sequence (1 out of
                #the 6)
                aa = []

                # here I iterate through each codon in the list and translate it to an amino acid,
                #then append the aa to my empty list of aas
                for codon in listy:
                     aa.append(translation_table[codon])
                
                #once aa is its full size for this one frame read, I want to find the longest M to Stop. 
                #So i need to join all my aa entries together without spaces, then add that to a list of my aa sequences
                aaseq = "".join(aa)
                find_longest.append(aaseq)

                write_aa.write(f"{gene}-frame-{num}-aminoacids\n{aa}\n")
                num += 1

            #so close!! Now I need to find the longest ORF peptide sequence
            #i will need the sequence and length
            longestlen = 0
            longestseq = ""

            #at this point, find longest should be a list of have six aa sequences

            for entry in find_longest:
                
                #here I have six strings in my list and I will iterate thorugh 
                # each to find the longest ORF pep seq
                long = re.search(r"(M\w*\*)", entry)
                
                if long != None:

                    found_aaseq = long.group(0)
                    cur_len = len(found_aaseq)

                #using if statements to see if the single longest found M to stop is 
                #longer than any others for this gene
                    if longestlen == 0:
                        longestlen = cur_len
                        longestseq = found_aaseq

                    elif cur_len > longestlen:
                        longestlen = cur_len
                        longestseq = found_aaseq

                    location_long = entry.find(longestseq)

                    if location_long >= 0:
                        thecodons = listy[location_long:(location_long+longestlen+1)]

                        longest_aa_codon.write(f"{gene}\nLongest ORF Codons\n{thecodons}\n")
                       
                

            long_aa.write(f"{gene} aminoacids\nLongest ORF Peptide Sequence\n{longestseq}\n")


                 


    