# Reverse Word Order
# Practice: 15

def rvrs_wrd(words):

	splt = words.split()
	splt.reverse()
	nwstr = ""

	for i in splt:
		nwstr += i + " "

	return nwstr


a = "Python is cool"
print("your reverse sentence is : ", rvrs_wrd(a))

