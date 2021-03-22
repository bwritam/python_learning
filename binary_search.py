# Binary search
pos = -1 # to mention the position of searching value

def search(list1, key):
	
	l = 0 # lower value of the list
	u = len(list1)-1 # upper value of the list
	
	while l <= u: # lower value will always smaller or equal to than upper value	     
	    mid = (l+u) // 2 # first you need to find the middle value
	    
	    if list1[mid] == key: #check if mid is equal to searched value
	        globals()["pos"] = mid # use globals() because the pos is before the function and it won't change with the local function
	        return True
	    else:
	    	
	    	if list1[mid] < key:
	    		l = mid + 1
	    	else:
	    		u = mid -1
	    return False

num = int(input("enter number of values: "))
list1 = [int(input("enter number: ")) for x in range(num)]
key = int(input("enter the key number you want to find: "))


if search(list1, key):
	print("found it at: ", pos+1) # as humans start counting from 1
else:
	print("not found")

