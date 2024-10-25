#!/usr/bin/env python3
import sys
import re

input_type = sys.argv[1]
file = sys.argv[2]
field_names = ["qseqid", "sseqid", "percid", "alen", "mismat", "gaps", "q_start", "q_end", "s_start", "s_end", "evalue", "bits"]
hits_list = []

with open(file, "r") as output2parse:
    for line in output2parse:
        line = line.rstrip()

        if line.startswith("#") is False:
            this_data=dict(zip(field_names, line.split('\t')))
            this_data["file"] = file
            hits_list.append(this_data)
            break

for entry in hits_list:

    print(f"File: {entry["file"]}\tPercid: {entry['percid']}\tAlen: {entry["alen"]}\tEval: {entry["evalue"]}")


# hit_files = []
# field_str = ["qseqid", "sseqid", "percid", "alen", "mismat", "gaps", "q_start", "q_end", "s_start", "s_end", "evalue", "bits"]
# hits_list = []

# #run in command line 
# #python3 parse_tab.py *.txt

# for hit_file in sys.argv[1:]:
#     with open(hit_file, "r") as fin:
#         for line in fin:
#             if line[0]== "#":
#                 continue
#             hit_data = dict(zip(field_names, line.rstrip("\n").split("\t")))
#             hit_data["file"] = hit_file
#             hits_list.append(hit_data)
#             break

#     print(hits_list)
    

