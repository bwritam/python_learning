import random as rd

i = 0
while i != 1:
	a = 0
	rdm_dgt = rd.sample(range(10), 4)
	# this print is use to get the random number for make the guess easy at initial stage.
	print(rdm_dgt)
	while a != 1: 
		
		j = 0
		while j != 1:
			gss_nmb = input("guess a 4 - digit number: ")
			if len(gss_nmb) != 4:
				print("invalid input!")
			elif len(gss_nmb) == 4:
				j = 1
		flag = 0
		cow  = 0
		bull = 0
		for i in range(4):
			if rdm_dgt[i] == int(gss_nmb[i]):
				cow += 1
				# a = 1
			else:
				bull += 1
		
		print(f"{cow} cows, {bull} bulls")
		if cow == 4:
			# j = 1
			flag = 1
			# a = 1
			# i = 0
			print("you have guessed all digits correctly.")


		k = 0
		while k != 1:

			ply_agn = int(input("1. continue or 2. exit: "))
			
			if ply_agn == 1:
				
				k = 1
				# j = 1
				# print(flag)
				if flag == 1:
				    a = 1
				    print("new game started...")
			# elif cow == 4:
			#  	k = 1
			# # 	a = 1
			#  	j = 1
			elif ply_agn == 2:
				i = 1
				k = 1
				a = 1
				print("game over...exit.")
			else:
				print("please press 1 or 2...")