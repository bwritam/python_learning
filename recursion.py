import sys
sys.setrecursionlimit(2000) # the given limit by python is normally 1000 in a infinite loop.
print(sys.getrecursionlimit())

count = 0

def greet():
	global count 
# if you use the global keyword, the variable belongs to the global scope. 
# it makes the variable outside to inside if you took the variable outside of a function.	
	count+= 1
	print("Hello World", count)
	greet()

greet()
