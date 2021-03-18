num = int(input("enter number of values: "))
l = [int(input("enter number: ")) for x in range(num)]

print("unsorted list: ", l)

# for i in range(len(l)-1, 0, -1): # this is for not the extra iteration.
for i in range(len(l)-1):
    for j in range(len(l)-1-i):	# this is a different method for not extra iteration.
	# for j in range(i): 
	    if l[j] > l[j+1]: # > uses here for ascending order,    <    uses for descending order.
		    l[j], l[j+1] = l[j+1], l[j]

print("bubble sorted list: ",l)