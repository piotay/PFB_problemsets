#/usr/bin/env python3

with open("Python_06.seq.txt", "r") as read_seq:
    print(f"The following are reverse complement sequences.\n")

    for line in read_seq:
        line = line.rstrip()
        seqname, sequence = line.split()
        
        comp = sequence.replace("T", "1")
        comp = comp.replace("G", "2")
        comp = comp.replace("C", "3")
        comp = comp.replace("A", "4")

        comp = comp.replace("1", "A")
        comp = comp.replace("2", "C")
        comp = comp.replace("3", "G")
        comp = comp.replace("4", "T")

        revcomp = comp[::-1]

        print(f">{seqname}\t{revcomp}\n")