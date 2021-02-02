# asking for a number and returning a new list with smaller than the numbers from list a.
# Practice: 3

def elements(num):

	a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	# b = [i for i in a if i < 5] using list comprehension
	b = []

	for i in a:
		if i < num:
			b.append(i)
	return b


print(elements(19))