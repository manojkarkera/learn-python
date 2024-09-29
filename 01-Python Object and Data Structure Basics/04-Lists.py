#Lists
#Lists can be thought of the most general version of a sequence in Python. 
#Unlike strings, they are mutable, meaning the elements inside a list can be changed!

#Lists are constructed with brackets [] and commas separating every element in the list.

# Assign a list to an variable named my_list
my_list = [1,2,3]
print(my_list)

#We just created a list of integers, but lists can actually hold different object types. For example:

my_list = ['A string',23,100.232,'o']
print(my_list)

print(len(my_list))


#Indexing and Slicing
#Indexing and slicing work just like in strings. Let's make a new list to remind ourselves of how this works:

my_list = ['one','two','three',4,5]

# Grab element at index 0
print(my_list[0])

# Grab index 1 and everything past it
print(my_list[1:])

# Grab everything UP TO index 3
print(my_list[:3])

#We can also use + to concatenate lists, just like we did for strings.
#Note: This doesn't actually change the original list!
print(my_list + ['new item'])


#You would have to reassign the list to make the change permanent.

# Reassign
my_list = my_list + ['add new item permanently']
print(my_list)

#We can also use the * for a duplication method similar to strings:

# Make the list double
print(my_list * 2)

#Basic List Methods

# Create a new list
list1 = [1,2,3]
print(list1)

#Use the append method to permanently add an item to the end of a list:
# Append
list1.append('append me!')
print(list1)

#Use pop to "pop off" an item from the list. By default pop takes off the last index, 
# but you can also specify which index to pop off. Let's see an example:
# Pop off the 0 indexed item
list1.pop(0)
print(list1)

# Assign the popped element, remember default popped index is -1
popped_item = list1.pop()
print(list1)

#It should also be noted that lists indexing will return an error if there is no element at that index. For example:
#print(list1[100])


#We can use the sort method and the reverse methods to also effect your lists:
new_list = ['a','e','x','b','c']
# Use reverse to reverse order (this is permanent!)
new_list.reverse()
print(new_list)

# Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
new_list.sort()
print(new_list)

#Nesting Lists
#A great feature of of Python data structures is that they support nesting. 
# This means we can have data structures within data structures. For example: A list inside a list.
# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
print(matrix)

# Grab first item in matrix object
print(matrix[0])

# Grab first item of the first item in the matrix object
print(matrix[0][0])


#List Comprehensions
#Python has an advanced feature called list comprehensions. They allow for quick construction of lists
# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
print(first_col)