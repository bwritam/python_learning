# Pattern printing in Python.


# Pattern 4: Inverted Pyramid of Descending Numbers
# Pattern: 	5 5 5 5 5 
# 		   	4 4 4 4 
# 		   	3 3 3 
# 		   	2 2 
# 		   	1 

for i in range(5, 0, -1):
	for j in range(0, i):
		print(i, end=" ")

	print()


# Pattern 5: Inverted Pyramid of the Same Digit
# Pattern:
#				5 5 5 5 5 
#				5 5 5 5 
#				5 5 5 
#				5 5 
#				5

for i in range(5, 0, -1):
	for j in range(i):
		print(5, end=" ")

	print()


# Pattern 6: Reverse Pyramid of Numbers
# Pattern: 
# 			1 
# 			2 1 
# 			3 2 1 
# 			4 3 2 1 
# 			5 4 3 2 1

for i in range(1, 6):
	for j in range(i, 0, -1):
		print(j, end=" ")

	print()


# Pattern 7: Inverted Half Pyramid Number Pattern
# Pattern:
# 			0 1 2 3 4 5 
# 			0 1 2 3 4 
# 			0 1 2 3 
# 			0 1 2 
# 			0 1

for i in range(5, 0, -1):
	for j in range(0, i + 1):
		print(j, end=" ")

	print()
