#/usr/bin/env python3
import sys
from random import randrange

seq = sys.argv[1]

n = len(seq)

seq2 = [x for x in seq]

for i in range(n):

	a = randrange(n)
	b = randrange(n)

	seqa = seq2[a]
	seqb = seq2[b]
	
	seq2[a] = seqb
	seq2[b] = seqa

print(seq2)
