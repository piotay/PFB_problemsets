#/usr/bin/env python3

with open("beluga_all_genes.tsv", "r") as allgenes, open("beluga_stemcellproliferation_genes.tsv", "r") as prolifgenes, open("beluga_pigmentation_genes.tsv", "r") as piggenes, open("beluga_transcriptionFactors.txt", "r") as transcgenes:
    
    allgeneset = set()
    prolifgenesset = set()
    piggenesset = set()
    transcgenesset = set()


    for line in allgenes:
        
        if "Gene" not in line:
            line = line.rstrip()
            allgeneset.add(line)

    for line in prolifgenes:
        
        if "Gene" not in line:
            line = line.rstrip()
            prolifgenesset.add(line)

    for line in piggenes:

        if "Gene" not in line:
            line = line.rstrip()
            piggenesset.add(line)

    for line in transcgenes:
        if "Gene" not in line:
            line = line.rstrip()
            transcgenesset.add(line)

notcellprolif = allgeneset - prolifgenesset
prolifandpig = prolifgenesset & piggenesset
prolifandTF = prolifgenesset & transcgenesset

print(len(prolifandTF))

with open("beluga_TF_Stem", "r") as stemTFs:
    trans_stem_genesset = set()


    for line in stemTFs:
        
        if "Gene" not in line:
            line = line.rstrip()
            trans_stem_genesset.add(line)

    print(len(trans_stem_genesset))