# Rock Paper Scissors game (initial)
# While loops, Infinite loops, Break statements
# Practice: 8
a = 0
while a != 1:
	player1 = input("Rock - Paper - Scissors: ").title()
	player2 = input("Rock - Paper - Scissors: ").title()

	if (player1 == "Rock" and player2 == "Scissors") or (player1 == "Paper" and player2 == "Rock") or (player1 == "Scissors" and player2 == "Paper"):
		print("player1 wins")
	elif (player2 == "Rock" and player1 == "Scissors") or (player2 == "Paper" and player1 == "Rock") or (player2 == "Scissors" and player1 == "Paper"):
		print("player2 wins")
	elif player1 == player2:
		print("it's a draw")
	else:
		print("invalid input")

	i = 1
	while i != 0:
		play = input("1. for continue \n2.for exit\n")
		if play == "1":
			a = 0
			i = 0
		elif play == "2":
			a = 1
			i = 0
		else:
			print("invalid")
			i = 1
			
print("thanks for playing")
