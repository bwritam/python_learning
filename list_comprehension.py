# List comprehennsions
# Practice: 7

def lists(list_a):
	
	list_b = [i for i in list_a if i % 2 == 0]
	return list_b


x = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(lists(x))