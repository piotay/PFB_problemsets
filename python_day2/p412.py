#!/usr/bin/env python3

import sys

min = int(sys.argv[1])
max = int(sys.argv[2])

listlen = list(range(max-min+1))

mylist = [listlen[dn]+min for dn in listlen]

for n in mylist:
	if n % 2 == 1:
		print (n)

