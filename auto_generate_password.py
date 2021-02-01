import random as rd


# to make a list with random length
password = rd.sample(range(17), rd.randint(8, 12)) 
# make a list of all symbols
symbol = ["<",">",",",".","?","/","|",'"',"'",":",";","}","{","]","[","+","=","_","-",")","(","*","&","^","%","$","#","@","!"]
# and a list of alphabets
alpha = ["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


# running the loop using index of list password
for i in range(len(password)):
# take a new variable to get random numbers within 1, 2, 3
	r = rd.randint(1, 3)
# and put the numbers in many random conditions
	if r == 1:
# i th element of list password is a random integer if r == 1
		password[i] = rd.randint(0, 9)
	elif r == 2:
# here if r == 2 i th password element will be a random symbol from symbol variable by indexing
		password[i] = symbol[rd.randint(0, len(symbol) - 1)]
	elif r == 3:
# here if r == 3 i th password element will take a random alphabet from its index number
		password[i] = alpha[rd.randint(0, len(alpha) - 1)]


# making a list to string using a for loop
for i in password:
# end='' is a argument of print function, and is used for make the string in one line
	print(i, end='')
# for looking better
print()
