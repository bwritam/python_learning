# linear search

pos = -1 # to mention the position of searching value

def search(list1, key):
	i = 0 # use as counter in while loop
	while i < len(list1): # due to index number is start at 0th index in lists
	    if list1[i] == key:
	    	globals()["pos"] = i # use globals() because the pos is before the function and if local pos change global won't change but we need to impact on global too.
	    	return True
	    i = i+1
	return False


num = int(input("enter number of values: "))
list1 = [int(input("enter number: ")) for x in range(num)]
key = int(input("enter the key number you want to find: "))


if search(list1, key):
	print("found it at: ", pos+1) # as humans start counting from 1
else:
	print("not found")
