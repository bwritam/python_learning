
# Practice: 12
# List ends, function to find out the 1st & last elements of a list.

def list_ends(list1):

	return [list1[0], list1[len(list1)-1]]


a = [1, 5, 10, 15, 25]
print(list_ends(a))