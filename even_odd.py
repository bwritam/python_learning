# Ask the user for a number and tell them if it is an even or odd number.
# If the number is a multiple of 4, just put number 4 in change of 2 at line 8. And print some different messages.
# Practice: 2
def oddeven():
	i = 0
	while i != 1:
		number = int(input("Enter a number: "))
		if number % 2 == 0:
			print("Input number is an even number.")
		else:
			print("Input number is an odd number.")
		j = 0
		while j != 1:
			run = int(input("1. Continue \n2. Exit \nOption: "))
			if run == 1:
				i = 0
				j = 1
			elif run == 2:
				print("Programme closed.")
				i = 1
				j = 1
			else:
				print("Press 1 or 2 agin")

oddeven()


# Ask the user for two numbers. Show user if the numbers divides evenly or not.
def ifDivided(num, check):
	if num % check == 0:
		print("It is divides evenly.")
	else:
		print("It is not divides evenly.")


ifDivided(20, 4)

