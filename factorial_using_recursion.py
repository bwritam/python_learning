
# Factorial using Recursion
def fact(num):
	if num == 0:
		return 1

	return num*fact(num-1)


result = fact(4)
print(result)