
# Sorting algorithm: Merge sort

def mergesort(list1):
	
	if len(list1)>1:
		mid = len(list1)//2 # to find out the middle element
		left_list = list1[:mid]
		right_list = list1[mid:]

		mergesort(left_list) # this is called recursive function
		mergesort(right_list)

		i = 0
		j = 0
		k = 0
		while i < len(left_list) and j < len(right_list):
			
			if left_list[i] < right_list[j]: # this "<" is for ascending order. ">" this is for descending order. only this sign need to change for descending order.

				list1[k] = left_list[i]
				i += 1
				k +=1
			else:
				list1[k] = right_list[j]
				j += 1
				k += 1

		while i < len(left_list):
			list1[k] = left_list[i]
			i += 1
			k += 1

		while j < len(right_list):
			list1[k] = right_list[j]
			j += 1
			k += 1


num = int(input("enter number of elements: "))
list1 = [int(input("enter values: ")) for x in range(num)]

mergesort(list1)
print(list1)