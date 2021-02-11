# give a number that many fibonacci numbers you want
# practice: 13

#using for loop
def myfibonacci(num):
	a = 0
	b = 1
	print(b)
	for i in range(1, num):
		c = a + b
		a = b
		b = c
		print(c)


myfibonacci(10)