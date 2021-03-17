# selection sort
# asecending order:
num = int(input("enter how many value you want in the list: "))
l = [int(input("enter numbers: ")) for x in range(num)]
print("unsorted list: ", l)
# without the help of min(), max(), index() methods
for i in range(len(l)-1):
 	m_index = i
	
 	for j in range(i+1, len(l)):
		
 		if l[j] < l[m_index]:
 			m_index = j

 	if l[i] != l[m_index]:
 		l[i], l[m_index] = l[m_index], l[i]

print("selection sort, sorted list in ascending order: ", l)



# with the help of min(), max(), index() methods
for i in range(len(l)-1):
	m_val = min(l[i:])
	m_index = l.index(m_val, i)
	l[i], l[m_index] = l[m_index], l[i]
print(l)




# descending order:
num = int(input("how many values you want in to the list: "))
l = [int(input("enter numbers: ")) for x in range(num)]
print("unsorted list: ", l)
# without the help of min(), max(), index() methods
for i in range(len(l)-1):
	m_index = i

	for j in range(i+1, len(l)):
		
		if l[j] > l[m_index]:
			m_index = j

	if l[i] != l[m_index]:
		l[i], l[m_index] = l[m_index], l[i]

print("selection sort, sorting list in desecending order is: ", l)



# with the help of min(), max(), index() methods
for i in range(len(l)-1):
	m_val = max(l[i:])
	m_index = l.index(m_val, i)
	l[i], l[m_index] = l[m_index], l[i]
print(l)
