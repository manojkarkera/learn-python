#Iterating through a list

# We'll learn how to automate this sort of list in the next lecture
list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    print(num)

print("========================================")
#Let's print only the even numbers from that list!

for num in list1:
    if num % 2 == 0:
        print(num)



print("========================================")
#Another common idea during a for loop is keeping some sort of running tally during multiple loops. For example, let's create a for loop that sums up the list:

# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum = list_sum + num

print(list_sum)


print("========================================")
#We've used for loops with lists, how about with strings? Remember strings are a sequence so when we iterate through them we will be accessing each item in that string.

for letter in 'This is a string.':
    print(letter)


#Let's now look at how a for loop can be used with a tuple:
print("========================================")
tup = (1,2,3,4,5)

for t in tup:
    print(t)


print("========================================")

#Tuples have a special quality when it comes to for loops. If you are iterating through a sequence that 
# contains tuples, the item can actually be the tuple itself, this is an example of tuple unpacking. 
# During the for loop we will be unpacking the tuple inside of a sequence and we can access the individual 
# items inside that tuple!

list2 = [(2,4),(6,8),(10,12)]

for tup in list2:
    print(tup)

print("========================================")

# Now with unpacking!
for (t1,t2) in list2:
    print(t1)

print("========================================")

#Let's start exploring iterating through Dictionaries to explore this further!
d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)

print("========================================")

# Create a dictionary view object
print(d.items())
print("========================================")

# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v) 

print("========================================")

#If you want to obtain a true list of keys, values, or key/value tuples, you can cast the view as a list:

print(list(d.keys()))
print("========================================")

#Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():

sorted(d.values())
print("========================================")