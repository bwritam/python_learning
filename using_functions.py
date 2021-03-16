
# Find out using function that how many even and odd number has in a given list.
# Pass list to a function in python:
def count(lsts):

	even = 0
	odd = 0

	for i in lsts:

		if i % 2 == 0:
			even += 1

		else:
			odd += 1
	return even, odd

lsts = [20, 14, 15, 8, 3, 5, 9]
even, odd = count(lsts)
print("Even: {}, Odd: {}".format(even, odd))

