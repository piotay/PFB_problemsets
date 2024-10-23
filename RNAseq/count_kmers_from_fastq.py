#!/usr/bin/env python

import os, sys, math

from sequence_to_kmer_list import *
from fastq_file_to_sequence_list import *


## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }


def count_kmers(kmer_list):

    kmer_count_dict = dict()

    ##################
    ## Step 2:
    ## begin your code
    for kmer in kmer_list:
        if kmer not in kmer_count_dict:
            kmer_count_dict[kmer] = 1
        else:
            kmer_count_dict[kmer] += 1

    ## end your code
    ################

    return kmer_count_dict


def main():

    progname = sys.argv[0]

    usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(
        progname
    )

    if len(sys.argv) < 4:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    kmer_length = int(sys.argv[2])
    num_top_kmers_show = int(sys.argv[3])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    all_kmers = list()

    #######################
    ## Step 1:
    ## begin your code, populate 'all_kmers' list with the
    ## collection of kmers from all sequences

    for sequ in seq_list:
        seq_kmer_list = sequence_to_kmer_list(sequ, kmer_length)
        for kmer in seq_kmer_list:
            all_kmers.append(kmer)
 ## end your code
    #######################

    kmer_count_dict = count_kmers(
        all_kmers
    )  # see step 2 above. You implement this. :-)

    

    #########################
    ## Step 3: sort unique_kmers by abundance descendingly
    ## (Note, you can run and test without first implementing Step 3)
    ## begin your code       hint: see the built-in 'sorted' method documentation

    #this line uses the sorted function to iterate through the dictionary entries as key value pairs 
    # and sorts them by value. we then call teh dict() funciton on this list of sorted tuples and reassing it to 
    #our dictionary variable
    kmer_count_dict = dict(sorted(kmer_count_dict.items(), key = lambda items : items[1], reverse = True))
    
    unique_kmers = list(kmer_count_dict.keys())

    #Shannon's Entropy Calculation

    negentropyval = {}
    entropy_nt = {}
    for key in unique_kmers:
        entropyval_calc = {}
        nt_list = ["A", "G", "C", "T"]
        for nt in nt_list:
            freqnt = (key.count(nt))/kmer_length
            entropyval_calc[nt] = freqnt
            
        for nt in nt_list:
            if entropyval_calc[nt] == 0:
                entropy_nt[nt] = 0
            else:
                entropy_nt[nt] = entropyval_calc[nt] * math.log2(entropyval_calc[nt])

        for nt in nt_list:
            if key not in negentropyval:
                negentropyval[key] = entropy_nt[nt]
            else:
                negentropyval[key] = entropy_nt[nt] + negentropyval[key]


    #unique_kmers = sorted(unique_kmers, key = lambda x : kmer_count_dict[x], reverse= True)

    ## end your code

    ## printing the num top kmers to show
    top_kmers_show = unique_kmers[0:num_top_kmers_show]

    for kmer in top_kmers_show:
        print("{}: {} Entropy val: {:.2}".format(kmer, kmer_count_dict[kmer], negentropyval[kmer]*-1))

    sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
    main()
