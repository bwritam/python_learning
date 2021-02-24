# Pattern printing in Python.


# Pattern 1: Simple Number Triangle Pattern
#Pattern: 
		#	1
		#	22
		#	333
		#	4444
		#	55555

for numbers in range(1,6):
	
	for nums in range(numbers):
		print(numbers, end=" ")# end= uses to make the output in one line.
	
	print() # empty print functions used for enter after every loop on numbers.

#Or we can use some other way like below.

n = int(input("enter n: "))

for i in range(n):
	print((str(i+1)+" ")*(i+1))

# Pattern 2: Inverted Pyramid of Numbers
#Pattern:
		# 	11111
		# 	2222
		# 	333
		# 	44
		# 	5

for i in range(1, 6):
	for j in range(6 - i):
		print(i, end=" ")

	print()

#Or we can use some other way like below.

n = int(input("enter n: "))

for i in range(n):
	print((str(n-i)+" ")*(n-i))


# Pattern 3: Half Pyramid Pattern of Numbers
# Pattern:
			# 	1
			# 	12
			# 	123
			# 	1234
			# 	12345

for i in range(1, 6):
	for j in range(1, i+1):
		print(j, end=" ")

	print()

#Or we can use some other way like below.

n = int(input("enter n: "))

for i in range(n):
	for j in range(i+1):
		print(j+1, end=" ")

	print()