
# Decorators, call a function between a function.
def div(a, b):
	print(a/b)

def smart_div(func):

	def inner_div(a, b):
		if a < b:
			a,b = b,a
		return func(a,b)
	return inner_div


div = smart_div(div)
div(4,8)

