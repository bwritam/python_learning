
def function(string):
	
	a = int(input("enter a number: "))
	b = int(input("enter a number: "))
	c = a+b
	print("summation is: ",c)
	print("length is: ",len(string))
	flag = 0
	for i in range(c):# if range is 5, the possible values are, 0, 1, 2, 3, 4
	
		if i > len(string)-1:# if the length is 5, it will loop five times but 0 to 4. so you need to -1 from the length of string.
			flag =1
			break
	if flag == 0:
		print("Congratulation!")

	elif flag == 1:
		print("Noob")




function("writam")

