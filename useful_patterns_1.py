
# To print given number of *s in a row
# Pattern: * * * * *
n = int(input("enter n: "))
for i in range(n):
	print("* ", end=" ")

# To print square pattern with * symbols
# Pattern: 
""" * * * * 
 	* * * * 
 	* * * * 
 	* * * * """ 
n = int(input("enter n: "))
for i in range(n):
	print("* "*n)

# Square pattern with provided fixed digit
# Pattern:
''' 5 5 5 5 5 
	5 5 5 5 5 
	5 5 5 5 5 
	5 5 5 5 5 
	5 5 5 5 5 '''
n = int(input("enter n: "))
for i in range(n):
	print((str(n)+" ")*n)

# Square pattern with provided fixed digit in every row
# Pattern:
''' 1 1 1 1 1 
	2 2 2 2 2 
	3 3 3 3 3 
	4 4 4 4 4 
	5 5 5 5 5 '''
n = int(input("enter n: "))
for i in range(n):
	print((str(i)+" ")*n)

# To print square pattern with fixed alphabet symbol
# Pattern:
''' A A A A A 
	A A A A A 
	A A A A A 
	A A A A A 
	A A A A A '''
n = int(input("enter n: "))
for i in range(n):
	print ("A "*n)

# Right angle triangle pattern with fixed alphabet symbol
# Pattern:
''' A 
	B B 
	C C C 
	D D D D 
	E E E E E '''
n = int(input("enter n: "))
for i in range(n):
	print((chr(65+i)+" ")*(i+1))

# Inverted right angle triangle pattern with * symbols
# Pattern:
''' * * * * * 
	* * * * 
	* * * 
	* * 
	*  '''
n = int(input("enter n: "))
for i in range(n):
	print("* "*(n-i))

# Inverted right angle triangle pattern with digits
# Pattern:
''' 1 2 3 4 5 
	1 2 3 4 
	1 2 3 
	1 2 
	1 '''
n = int(input("enter n: "))
for i in range(n):
	for j in range(n-i):
		print(str(j+1), end=" ")
	print()

# To print pyramid pattern with fixed digit in every row
# Pattern:
'''  1 
    2 2 
   3 3 3 
  4 4 4 4 
 5 5 5 5 5 '''
n = int(input("enter n: "))
for i in range(n):
	print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))

# Pyramid pattern with alphabet symbols in reverse of dictionary order
# Pattern:
'''   E       
     E D 
    E D C 
   E D C B 
  E D C B A '''
n = int(input("enter n: "))
for i in range(n):
	print(" "*(n-i-1), end=" ")
	for j in range(i+1):
		print(chr(64+n-j), end=" ")
	print()

# Right half diamond pattern with alphabet symbols in dictionary order
# Pattern:
''' A 
	A B 
	A B C 
	A B C D 
	A B C D E 
	A B C D 
	A B C 
	A B 
	A ''' 
n = int(input("enter n: "))
for i in range(n):
	for j in range(i+1):
		print(chr(65+j), end=" ")
	print()
for i in range(n-1):
	for j in range(n-i-1):
		print(chr(65+j), end=" ")
	print()