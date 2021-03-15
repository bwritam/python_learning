
from functools import reduce
# Anonymous Function| Lambda
f = lambda a: a*a
i = lambda a,b: a+b

result = f(5)
opt = i(5, 5)

print(result)
print(opt)

##############################################################################################################
# Uses of lambda() function and lessons on	 filter(), map() & reduce() functions
##############################################################################################################

# filter(), map() and rduce() these functions takes two arguments. a function and a sequence.

# suppose we have a list name - 	nums	 and we want even values from this list to a new list.

# we can define a function before and then call it while using filter()
def is_even(n):
	return n % 2 == 0

nums = [1, 2, 3, 4, 6, 7, 8]
evens = list(filter(is_even, nums)) # as we want a list of even numbers in return
evens = list(filter(lambda n: n % 2 == 0, nums)) # using lambda() function we don't need to define it before
print(evens)

# to our next examples we will use only lambda()

# when we want to change values we use 	map() function

doubles = list(map(lambda n : n * 2, evens)) # we want a new list of double the evens lists value.
print(doubles)

# reduce() function belongs to a module called 	functools. so you have to import it before use.

summation = reduce(lambda a,b: a + b, doubles) # we need summation of dobles list values.
print(summation)
