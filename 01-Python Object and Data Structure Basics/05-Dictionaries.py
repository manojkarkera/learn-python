#Dictionaries
#We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python. 
#If you're familiar with other languages you can think of these Dictionaries as hash tables.

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)

# Call values by their key
print(my_dict['key2'])

#Its important to note that dictionaries are very flexible in the data types they can hold. For example:

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
# Let's call items from the dictionary
print(my_dict['key3'])

# Can call an index on that value
print(my_dict['key3'][0])

# Can then even call methods on that value
print(my_dict['key3'][0].upper())

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])

# Set the object equal to itself minus 123 
my_dict['key1'] -= 123
print(my_dict['key1'])

#We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it:

# Create a new dictionary
d = {}
print(d)

# Create a new key through assignment
d['animal'] = 'Dog'
print(d)

# Can do this with any object
d['answer'] = 42
print(d)

#Nesting with Dictionaries
#Hopefully you're starting to see how powerful Python is with its flexibility of nesting objects and calling methods on them. 
# Let's see a dictionary nested inside a dictionary:

# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}

# Keep calling the keys
print(d['key1']['nestkey']['subnestkey'])

#A few Dictionary Methods
#There are a few methods we can call on a dictionary. Let's get a quick introduction to a few of them:

# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}
print(d)


# Method to return a list of all keys 
print(d.keys())

# Method to grab all values
print(d.values())

# Method to return tuples of all items  (we'll learn about tuples soon)
print(d.items())