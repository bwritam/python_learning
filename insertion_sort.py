# Insertion sort
# ascending order
def insertionsort(l):
	for index in range(1, len(l)):
		current_element = l[index]
		pos = index

		while current_element < l[pos-1] and pos > 0: # for descending order use ">"
			l[pos] = l[pos-1]
			pos = pos-1

		l[pos] = current_element


num = int(input("enter number of values: "))
l = [int(input("enter number: ")) for x in range(num)]

insertionsort(l)
print(l)