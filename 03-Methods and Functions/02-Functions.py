#Simple example of a function

def say_hello():
    print('hello')


say_hello()

#Accepting parameters (arguments)
#Let's write a function that greets people with their name.

def greeting(name):
    print(f'Hello {name}')

greeting('Jose')



#Using return Example: Addition function

def add_num(num1,num2):
    return num1+num2

print(add_num(4,5))

#** Let's use this to construct a function. Notice how we simply return the boolean check.**

def even_check(number):
    return number % 2 == 0

print(even_check(20))


#Check if any number in a list is even
#Let's return a boolean indicating if any number in a list is even. Notice here how return breaks out of the loop and exits the function

def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Otherwise we don't do anything
        else:
            pass

print(check_even_list([1,2,3]))

print(check_even_list([1,1,1]))



#** Correct Approach: We need to initiate a return False AFTER running through the entire loop**

def check_even_list1(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return False

print(check_even_list1([1,2,3]))

print(check_even_list1([1,3,5]))

#Return all even numbers in a list
#Let's add more complexity, we now will return all the even numbers in a list, otherwise return an empty list.

def check_even_list2(num_list):
    
    even_numbers = []
    
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even_numbers

print(check_even_list2([1,2,3,4,5,6]))

#Similarly, functions often return tuples, to easily return multiple results for later use.

#Let's imagine the following list:

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

#The employee of the month function will return both the name and number of hours worked for the top performer 
# (judged by number of hours worked).

def employee_check(work_hours):
    
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # Notice the indentation here
    return (employee_of_month,current_max)

print(employee_check(work_hours))