
testlist = [101,2,15,22,95,33,2,27,72,15,52]

for n in testlist:
	if n % 2 == 0:
		print(n)

testlist.sort()

evens = 0
odds = 0

for n in testlist:
	print(n)
	
	if n % 2 == 0:
		evens += n
	if n % 2 == 1:
		odds += n

print(f"Sum of even numbers: {evens}")
print(f"Sum of odd numbers: {odds}")

