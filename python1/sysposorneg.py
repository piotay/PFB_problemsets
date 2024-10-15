#!/usr/bin/env python3
import sys

mynum=float(sys.argv[1])

print(f"The number you are testing is {mynum}")

if mynum > 0:
	print("positive")
	if mynum < 50:
		if mynum % 2 == 0:
			print("it is an even number that is smaller than 50")
	if mynum > 50:
		if mynum % 3 == 0:
			print("it is larger than 50 and divisible by 3")
elif mynum < 0:
	print("negative")
elif mynum == 0:
	print("0")

