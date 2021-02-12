# Without duplicates lists, list overlap.
# Practice: 5
def two_list(list_1, list_2):

	list_3 = []
	for i in list_1:
		if i in list_2:
			if i not in list_3:
				list_3.append(i)
	return list_3


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(two_list(a,b))


# Randomly generate two lists to test this.
import random as rd

def rndm_list():

	list_1 = rd.sample(range(1, 100), rd.randint(5, 20))
	list_2 = rd.sample(range(50, 100), rd.randint(10, 15))
	list_3 = []

	for i in list_1:
		if i in list_2:
			if i not in list_3:
				list_3.append(i)
	return list_3


in_list = rndm_list()
print(in_list)


#List overlap using sets
def ovrlp_st(list1, list2):

	nwst1 = set(list1)
	nwst2 = set(list2)
	nwst3 = nwst1.intersection(nwst2)
	return list(nwst3)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(ovrlp_st(a, b))