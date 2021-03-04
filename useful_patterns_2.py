# To print inverted pyramid pattern with alphabet symbols in dictionary order
# Pattern:
'''A B C D E 
    A B C D 
     A B C 
      A B 
       A ''' 

n = int(input("enter n: "))
for i in range(n):
	print(" "*i, end=" ")
	for j in range(n-i):
		print(chr(65+j), end=" ")
	print()

# To print diamond pattern with * symbols
# Pattern:
'''  * 
    * * 
   * * * 
  * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * '''
n = int(input("enter n: "))
for i in range(n):
	print(" "*(n-i-1)+"* "*(i+1))
for i in range(n-1):
	print(" "*(i+1)+"* "*(n-i-1))    

 # To print right half diamond pattern with * symbols
 # Pattern:
 ''' * 
	 * * 
	 * * * 
	 * * * * 
	 * * * * * 
	 * * * * 
	 * * * 
	 * * 
	 * '''
n = int(input("enter n: "))
for i in range(n):
 	print("* "*(i+1))
for i in range(n-1):
 	print("* "*(n-i-1))

# To print left half diamond pattern with * symbols
# Pattern:
'''       * 
	    * * 
 	  * * * 
	* * * * 
  	  * * * 
        * * 
          * '''
n = int(input("enter n: "))
for i in range(n):
	print("  "*(n-i-1)+"* "*(i+1))
for i in range(n-1):
	print("  "*(i+1)+"* "*(n-i-1))

# To print left half diamond pattern with digits in ascending order
# Pattern:
'''       1 
        1 2 
      1 2 3 
    1 2 3 4 
      1 2 3 
        1 2 
          1'''
n = int(input("enter n: "))

for i in range(n):
	print("  "*(n-i-1), end=" ")
	for j in range(i+1):
		print(j+1, end=" ")
	print()

for i in range(n-1):
	print("  "*(i+1), end=" ")
	for j in range(n-i-1):
		print(j+1, end=" ")
	print()

# To print top half hollow diamnd pattern with * symbols
# Pattern:
'''		        * 
		      *   *  
		    *       *  
		  *           *  
		*               *  '''
n = int(input("enter n: "))

for i in range(n):
	print("  "*(n-i-1)+"* ", end="")

	if i >= 1:
		print("  "*(2*i-1)+"* ", end=" ")
	print()

# To print bottom half hollow diamond pattern with * symbols
# Pattern:
'''			*           *  
			  *       *  
			    *   *  
			      *   '''
n = int(input("enter n: "))

for i in range(n):
	print("  "*i+"* ", end="")

	if i != n-1:
		print("  "*(2*n-2*i-3)+"* ", end=" ")
	print()

# To print bottom half hollow diamond pattern with alphabet symbols in reverse
# Pattern:
'''			A               A 
			  B           B 
			    C       C 
			      D   D 
			        E     '''

n = int(input("enter n: "))

for i in range(n):
	print("  "*i+chr(65+i), end=" ")

	if i != n-1:
		print("  "*(2*n-2*i-3)+chr(65+i), end=" ")
	print()

# To print inverted digits rightangle triangle
# Pattern:
''' 	1 
		2 1 
		3 2 1 
		4 3 2 1 
		5 4 3 2 1 '''
n = int(input("enter n: "))

for i in range(n):
	for j in range(i, -1, -1):
		print(j+1, end=" ")
	print()
