def palindrome():
	
	a = 0
	while a != 1:

		word = input("Enter word: ")
		reverse_word = word[::-1]
		
		if word == reverse_word:
			print("It's a palindrome.")
		else:
			print("It's not a palindrome.")

		ply_agn = int(input("1. Continue, 2. Exit:  "))
		
		i = 0
		while i != 1:

			if ply_agn == 1:
				print("Continue your search...")
				i = 1
			elif ply_agn == 2:
				print("Exit..")
				i = 1
				a = 1


palindrome ()
			



