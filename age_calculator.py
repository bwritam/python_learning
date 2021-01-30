# this programme will return the year when you'll turn 100.
# taking input for that many copies.
# copies of the previous message on separate lines.

# practice 1:

def person():
	name = input("Enter your name: ")
	age = int(input("Enter your age: "))
	years = (2021 - age) + 100
	copies = int(input("How many copies do you want? "))
	print(f"{name} you are now {age} years old. You will turn 100 years old in the year {years}.\n" * copies)


person()