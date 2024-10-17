#!/usr/bin/env python3
import sys

min = int(sys.argv[1])
max = int(sys.argv[2])

listofnum = [min]

listlen = max - min + 1

count = 1

while count < listlen:
	listofnum.append(count+listofnum[0])
	count+=1

print(listofnum)

for n in listofnum:
	if n % 2 == 1:
		print(n)


