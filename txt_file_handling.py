# File Handling:

# Open files and Read files.

f = open(r"C:\Users\Anik\Desktop\demofile.txt", "r")

# To read the whole file use read() method.
print(f.read())

# To read the 6 first characters of the file
print(f.read(6))

# To read one line of the file. By calling readline two times, you can read the two first lines.
print(f.readline())

# By looping through the lines of the file, you can read the whole file, line by line.
for lines in f:
	print(lines)

# Close files:

# It is a good practice to always close the file when you are done with it.

f = open(r"C:\Users\Anik\Desktop\demofile2.txt", "r")
print(f.read())
f.close()

# Python file write, append

f = open(r"C:\Users\Anik\Desktop\demofile2.txt", "a")
f.write("Now the file has more content.")
f.close()
# Open and read the file after the appending
f = open(r"C:\Users\Anik\Desktop\demofile2.txt", "r")
print(f.read())

# Overwrite the content
f = open(r"C:\Users\Anik\Desktop\mydemo.txt", "w")
f.write("Oops! I have deleted the file....")
f.close
# After overwrite read the file.
f = open(r"C:\Users\Anik\Desktop\mydemo.txt", "r")
print(f.read())


# Create a new file.
f = open(r"C:\Users\Anik\Desktop\mydemo.txt", "x")

# Create a new file if it doesn't exist.
f = open(r"C:\Users\Anik\Desktop\mydemo2.txt", "w")

# Python Delete File.
# To delete a file, you must import the os module.
import os
os.remove(r"C:\Users\Anik\Desktop\mydemo2.txt")

# Check if the file exists, then delete it.
import os 
if os.path.exists(r"C:\Users\Anik\Desktop\mydemo.txt"):
	os.remove(r"C:\Users\Anik\Desktop\mydemo.txt")
else:
	print("The file does not exist.")

# Delete Folder:
# To delete an entire folder, use the os.rmdir() method.
import os 
os.rmdir("myfolder")

# You can only remove empty folders.