#/usr/bin/env python3
import re
import sys

file = "/Users/pfb2024/PFB_data/Python_08.fasta"

seqsfr1  = {}
seqsfr2  = {}
seqsfr3  = {}


with open(file, "r") as fasta:
    for line in fasta:

        if line.startswith(">"):
            
            sequ = ""
            gene = re.search(r"^>(.*?)\s", line)
            gene = gene.group(1)
            gene = gene.rstrip()

        else:

            sequ = sequ + line.rstrip()

            seqsfr1[gene] = []
            seqsfr1[gene] = re.findall(r"\w\w\w", sequ)

            seqsfr2[gene] = []
            sequ2 = sequ[1:]
            seqsfr2[gene] = re.findall(r"\w\w\w", sequ2)

            seqsfr3[gene] = []
            sequ3 = sequ[2:]
            seqsfr3[gene] = re.findall(r"\w\w\w", sequ3)


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



with open("Python_08.codons-6frames.nt","w") as write_codons, open("Python_08_translated.txt", "w") as write_aa:

        for gene in seqsfr1:
            
            codon_list1 = seqsfr1[gene]
            codons1 = " ".join(codon_list1)
            
            codon_list2 = seqsfr2[gene]
            codons2 = " ".join(codon_list2)

            codon_list3 = seqsfr2[gene]
            codons3 = " ".join(codon_list3)

            write_codons.write(f"{gene}-frame-1-codons\n{codons1}\n")
            write_codons.write(f"{gene}-frame-2-codons\n{codons2}\n")
            write_codons.write(f"{gene}-frame-3-codons\n{codons3}\n")

            codons_list = [codons1, codons2, codons3]
            copy_codons_list = codons_list.copy()

            num = 4

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

                copy_codons_list.append(revcomp)

                write_codons.write(f"{gene}-frame-{num}-codons\n{revcomp}\n")

                num += 1

            num = 1

            for codon_unit in copy_codons_list:
                listy = codon_unit.split(" ")

                aa = []

                for codon in listy:
                     aa.append(translation_table[codon])

                write_aa.write(f"{gene}-frame-{num}-aminoacids\n{aa}\n")
                num += 1


    