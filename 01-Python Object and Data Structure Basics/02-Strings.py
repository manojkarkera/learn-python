#String Basics
#We can also use a function called len() to check the length of a string!
print(len('Hello World'))


#String Indexing
#We know strings are a sequence, which means Python can use indexes to call parts of the sequence. Let's learn how this works.
# Assign s as a string
s = 'Hello World'

# Show first element (in this case a letter)
print(s[0])

# Grab everything past the first term all the way to the length of s which is len(s)
print(s[1:])

# Grab everything UP TO the 3rd index
print(s[:3])

#Everything
s[:]

# Last letter (one index behind 0 so it loops back around)
print(s[-1])

# Grab everything, but go in steps size of 1
print(s[::1])

# Grab everything, but go in step sizes of 2
print(s[::2])


#String Properties
#It's important to note that strings have an important property known as immutability. 
# This means that once a string is created, the elements within it can not be changed or replaced. For example:
# Let's try to change the first letter to 'x'
#s[0] = 'x' #error TypeError: 'str' object does not support item assignment
print(s)

# Concatenate strings!
s = s + ' concatenate me!'
print(s)



#We can use the multiplication symbol to create repetition!
letter = 'z'
print(letter*10)

# Upper Case a string
print(s.upper())

# Lower case
print(s.lower())

# Split a string by blank space (this is the default)
print(s.split())

# Split by a specific element (doesn't include the element that was split on)
print(s.split('W'))

#Print Formatting
#We can use the .format() method to add formatted objects to printed string statements.
#The easiest way to show this is through an example:
print('Insert another string with curly brackets: {}'.format('The inserted string'))

#The .format() method has several advantages over the %s placeholder method:
#1. Inserted objects can be called by index position:
print('The {2} {1} {0}'.format('fox','brown','quick'))

#2. Inserted objects can be assigned keywords:
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))

#3. Inserted objects can be reused, avoiding duplication:
print('A %s saved is a %s earned.' %('penny','penny'))
# vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))


#Alignment, padding and precision with .format()
#Within the curly braces you can assign field lengths, left/right alignments, rounding parameters and more
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

#By default, .format() aligns text to the left, numbers to the right. You can pass an optional <,^, or > to set a left, center or right alignment:
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

#You can precede the aligment operator with a padding character
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

#Field widths and float precision are handled in a way similar to placeholders. The following two print statements are equivalent:
print('This is my ten-character, two-decimal number:%10.2f' %13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))

#Formatted String Literals (f-strings)
#Introduced in Python 3.6, f-strings offer several benefits over the older .format() string method described above. 
# or one, you can bring outside variables immediately into to the string rather than pass them as arguments through .format(var).

name = 'Fred'

print(f"He said his name is {name}.")

#Pass !r to get the string representation:
print(f"He said his name is {name!r}")

#Float formatting follows "result: {value:{width}.{precision}}"
#Where with the .format() method you might see {value:10.4f}, with f-strings this can become {value:{10}.{6}}
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

print("==========================================================")

#Note that with f-strings, precision refers to the total number of digits, not just those following the decimal. 
# This fits more closely with scientific notation and statistical analysis. 
# Unfortunately, f-strings do not pad to the right of the decimal, even if precision allows it:
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

print("==========================================================")

#If this becomes important, you can always use .format() method syntax inside an f-string:
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")