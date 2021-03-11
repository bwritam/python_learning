
# Find a numbers factorial value.
def factorial(num):
	f = 1
	for i in range(1, num+1):
		f = f*i

	return f

result = factorial(4)
print(result)