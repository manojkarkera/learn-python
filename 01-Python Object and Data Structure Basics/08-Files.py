#Files
#Python uses file objects to interact with external files on your computer. These file objects can be any sort of file you have on your computer, 
#whether it be an audio file, a text file, emails, Excel documents, etc. 
#Note: You will probably need to install certain libraries or modules to interact with those various file types, but they are easily available.

#IPython Writing a File
#This function is specific to jupyter notebooks! Alternatively, quickly create a simple .txt file with sublime text editor.

# %%writefile test.txt
# Hello, this is a quick test file.


#Python Opening a file
#Let's being by opening the file test.txt that is located in the same directory as this notebook. For now we will work with 
#files located in the same directory as the notebook or .py script you are using.
#It is very easy to get an error on this step:

#myfile = open('whoops.txt') #No such file or directory: 'whoops.txt'
#pwd

# Open the text.txt we made earlier
my_file = open('test.txt')

# We can now read the file
print(my_file.read())


# But what happens if we try to read it again?
print(my_file.read())

#This happens because you can imagine the reading "cursor" is at the end of the file after having read it. So there is nothing left to read. We can reset the "cursor" like this:

# Seek to the start of file (index 0)
my_file.seek(0)
print(my_file.read())


#You can read a file line by line using the readlines method. Use caution with large files, 
# since everything will be held in memory. We will learn how to iterate over large files later in the course.

# Readlines returns a list of the lines in the file
my_file.seek(0)
print(my_file.readlines())

#When you have finished using a file, it is always good practice to close it.
my_file.close()

#Writing to a File
#By default, the open() function will only allow us to read the file. We need to pass the argument 'w' to write over the file. For example:

# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

my_file = open('test.txt','w+')

#Use caution!
#Opening a file with 'w' or 'w+' truncates the original, meaning that anything that was in the original file is deleted!

# Write to the file
my_file.write('This is a new line')

# Read the file
my_file.seek(0)
print(my_file.read())

my_file.close()  # always do this when you're done with a file

#Appending to a File
#Passing the argument 'a' opens the file and puts the pointer at the end, so anything written is appended. Like 'w+', 'a+' lets us read and write to a file. If the file does not exist, one will be created.

my_file = open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')


my_file.seek(0)
print(my_file.read())

#By not calling .read() on the file, the whole text file was not stored in memory.
#Notice the indent on the second line for print. This whitespace is required in Python.

print("===============================================")
for line in open('test.txt'):
    print(line)