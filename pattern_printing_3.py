# Pattern 8: Pyramid of Natural Numbers Less Than 10
# Pattern: 
# 			1 
# 			2 3 4 
# 			5 6 7 8 9 

currentNumber = 1
stop = 2
rows = 3

for row in range(rows):
	for column in range(1, stop):
		print(currentNumber, end=" ")
		# print("{:02d}".format(currentNumber), end=" ") you may use it here format gives you a 0 before your single number
		# to make that two numbers as 01, 02, 03..10, 11, 12
		currentNumber += 1

	print()
	stop += 2


# Pattern 9: Revers Pattern of Digits from 10
# Pattern: 
# 				1 
# 				3 2 
# 				6 5 4 
# 				10 9 8 7

start = 1
stop = 2
currentNumber = stop

for row in range(2, 6):
	for col in range(start, stop):
		
		currentNumber -= 1
		print(currentNumber, end=" ")
	print()
	start = stop
	stop += row
	currentNumber = stop


# Pattern 10: Unique Pyramid Pattern of Digits
# Pattern:

# 			1 
# 			1 2 1 
# 			1 2 3 2 1 
# 			1 2 3 4 3 2 1 
# 			1 2 3 4 5 4 3 2 1

for i in range(1, 7):
	for j in range(1, i-1):
		print(j, end=" ")

	for j in range(i-1, 0, -1):
		print(j, end=" ")

	print()


# Pattern 11: Even Number Pyramid Pattern
# Pattern: 
# 			10 
# 			10 8 
# 			10 8 6 
# 			10 8 6 4 
# 			10 8 6 4 2

rows = 5
lst_evnNum = 2 * rows
evnNum = lst_evnNum

for i in range(1, rows + 1):
	evnNum = lst_evnNum
	
	for j in range(i):
		print(evnNum, end=" ")
		evnNum -= 2

	print()


# Pattern 12: Pyramid of Horizontal Tables
# Pattern:
# 			0  
# 			0 1  
# 			0 2 4  
# 			0 3 6 9  
# 			0 4 8 12 16  
# 			0 5 10 15 20 25  
# 			0 6 12 18 24 30 36

rows = 7 
for i in range(rows):
	for j in range(i+1):
		print(i*j, end=" ")

	print()


# Pattern 13: Pyramid Pattern of Alternate Numbers
# Pattern:
# 			1 
# 			3 3 
# 			5 5 5 
# 			7 7 7 7 
# 			9 9 9 9 9

rows = 5
i = 1
while i <= rows:
	j = 1
	while j <= i:
		print((i * 2 - 1), end=" ")
		j += 1
	i += 1
	print()