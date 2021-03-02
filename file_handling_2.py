
# Take some numbers from a text file and put the sum of this numbers to a new text file.
f = open(r"C:\Users\Anik\Desktop\demofile.txt", "r")

c = 0
for i in f:
	c = c + int(i)
print(c)

f = open(r"C:\Users\Anik\Desktop\taskfile.txt", "w")
f.write(str(c))
f.close()

# Unknown length of a function argument
def arg(*x):
	c = 0
	for i in x:
		c = c + i

	print (c)


arg(5, 6, 1, 3)



