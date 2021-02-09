def myPrime(num):
	is_prime = True
	for i in range(2, num):
		if num % i == 0:
			is_prime = False
	return is_prime


print(myPrime(7))