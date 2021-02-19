# Pattern 14: Mirrored Pyramid(Right-angled Triangle) Pattern of Numbers
# Pattern:
   # 		  1 
   #        1 2 
   #      1 2 3 
   #    1 2 3 4 
   #  1 2 3 4 5

rows = 6

for row in range(1, rows):
	num = 1
	for j in range(rows, 0, -1):
		if j > row:
			print(" ", end=" ")
		else:
			print(num, end=" ")
			num += 1
	print()


# Pattern 15: Equilateral Triangle with Stars(Asterisk Symbol)
# # Pattern:
#  			  * 
#            * * 
#           * * * 
#          * * * * 
#         * * * * * 
#        * * * * * * 
#       * * * * * * *

size = 7 
m = (2*size)-2

for i in range(0, size):
	for j in range(0, m):
		print(end=" ")

	m = m-1 # decrementing m after each loop

	for j in range(0, i+1):
		# printing full Triangle pyramid using stars
		print("* ", end="")
	print()


# Pattern 16: Downward Triangle Pattern of stars
# Pattern:
  #		  * * * * * * 
  #        * * * * * 
  #         * * * * 
  #          * * * 
  #           * * 
  #            * 

rows = 5
k = 2*rows - 2

for i in range(rows, -1, -1):
	for j in range(k, 0, -1):
		print(end=" ")

	k = k+1
	for j in range(0, i+1):
		print("*", end=" ")

	print()


# Pattern 17: Pyramid Pattern of Stars
# Pattern:

rows = 5
for i in range(rows):
	for j in range(0, i+1):
		print("*", end=" ")

	print()
