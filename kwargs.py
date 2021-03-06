
# When you want to take a variable than an argument
def person(name, **data):

	print(name)

	for i, j in data.items():
		print(i, j)


person(name="Writam", age=28, mob=99999, city="Badkulla")


