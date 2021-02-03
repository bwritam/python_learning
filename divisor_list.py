# input a number and find out a list of all its divisors.
# Practice: 4
def divisor(num):
	
	divi = range(1, num+1)
	divi_list = []
	
	for i in divi:
		if num % i == 0:
			divi_list.append(i)
	return divi_list


mydivisor = divisor(50)
print(mydivisor)