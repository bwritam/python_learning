import random
j = 0
while j != 1:
	num = random.randint(1, 9)
	print(f"the guess number is {num}\n")
	a = 0
	count = 0
	while a != 1:
		count += 1
		guess = int(input("guess number 1 - 9: "))
		if guess < num:
			print("guess too low\n")
		elif guess > num:
			print("guess too high\n")
		elif guess == num:
			print("guess right\n")
			a = 1
		i = 0
		while i != 1:
			play = int(input("1. continue \n2. restart \n3. exit\n"))
			if play == 1:
				print("let's play again\n")
				i = 1
			elif play == 2:
				print("restarting")
				i = 1
				a = 1
			elif play == 3:
				print("exit\n")
				i = 1
				a = 1
				j = 1
			else:
				print("invalid input \ntry again: ")
print(f"you have quitted after {count} many times")
print("thanks for playing")