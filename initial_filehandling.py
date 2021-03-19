import os # only use when you need to delete any file

f = open(r"C:\Users\Anik\Desktop\demofile.txt", "r") # you have to mention the file path if it is not the right python files
print(f.readline()) # readline is used for read the first line

f. close() # after openning file always close it, its a good practice


#################################################################
#################################################################

f = open(r"C:\Users\tomlini\Desktop\DSC_0105.JPG", "rb") # when you want to read a image use rb, read binary

f1 = open(r"C:\Users\tomlini\Desktop\copy_dsc.JPG", "wb") # you can copy a image using wb, write binary

for i in f:
	print(i)
