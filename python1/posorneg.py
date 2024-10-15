#!/usr/bin/env python3

mynum = 50

if mynum > 0:
	print("Positive")
	if mynum < 50:
		if mynum % 2 == 0:
			print("it is an even number that is smaller than 50")
	elif mynum > 50:
		if mynum % 3 == 0:
			print("it is larger than 50 and divisible by 3")
elif mynum < 0:
	print("Negative")
elif mynum == 0:
	print("0")
