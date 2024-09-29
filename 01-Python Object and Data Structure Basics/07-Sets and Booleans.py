#Set and Booleans
#There are two other object types in Python that we should quickly cover: Sets and Booleans.

#Sets
#Sets are an unordered collection of unique elements. We can construct them by using the set() function. Let's go ahead and make a set to see how it works

x = set()

# We add to sets with the add() method
x.add(1)

print(x)

# Add a different element
x.add(2)

print(x)

# Try to add the same element
x.add(1)

#Notice how it won't place another 1 there. 
# That's because a set is only concerned with unique elements! We can cast a list with multiple 
# repeat elements to a set to get the unique elements.

# Create a list with repeats
list1 = [1,1,2,2,3,4,5,6,1,1]
print(set(list1))


#Booleans
#Python comes with Booleans (with predefined True and False displays that are basically just the integers 1 and 0). 
# It also has a placeholder object called None

# Set object to be a boolean
a = True

#We can use None as a placeholder for an object that we don't want to reassign yet:
# None placeholder
b = None

