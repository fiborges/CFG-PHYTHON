""""
Question 1 
I am building some very high quality chairs and need exactly four nails for each chair. I've written a program to calculate how many nails I need to buy to build these chairs. 

chairs = '15' 
nails = 4 
total_nails = chairs * nails 

message = 'I need to buy {} nails'.format(total_nails) 
print('You need to buy {} nails'.format(message)) 

When I run the program it tells me that I need to buy 15151515 nails. 
This seems like a lot of nails. Is my program calculating the total number of nails correctly? What is the problem? How do I fix it? 
"""

#resolution:

""""
in the provided code, the variable chairs is assigned the value '15', which is a string. 
When you multiply a string by an integer, it doesn't perform numerical multiplication; instead, 
it repeats the string multiple times. Therefore, when you multiply '15' by 4, you get the string '15151515',
which is not the correct result for calculating the total number of nails needed.

To fix this issue, we need to convert the variable chairs from a string to an integer before 
performing the multiplication. We can use the int() function to do this conversion. 
The corrected code is as follows:
"""

chairs = '15'
nails = 4
total_nails = int(chairs) * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)


"""
Question 2
I'm trying to run this program, but I get an error. 
What is the error telling me is wrong? How do I fix the program? 

my_name = Penelope 
my_age = 29 
message = 'My name is {} and I am {} years old'.format(my_name, my_age) 
print(message)

"""

"""
    resolution:
    The error in the provided code is related to the assignment of my_name variable. 
    The variable my_name should be a string, but in the code, it is not enclosed in quotes, which makes 
    Python interpret it as a variable name instead of a string.

To fix this, you need to enclose the value assigned to my_name in quotes, either single or double quotes. 
Here's the corrected code:
"""

my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)


"""
Question 3 

I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make.
Write a program to calculate this. 
Assume that a box of eggs contains six eggs and I need four eggs for each omelette, 
but I should be able to easily change these values if I want. The output should say something like 
"You can make 9 omelettes with 6 boxes of eggs". 

"""

#resolution:   We'll assume that each box contains six eggs and you need four eggs for each omelette.

# Number of eggs in each box
eggs_per_box = 6

# Number of eggs needed for each omelette
eggs_per_omelette = 4

# Number of boxes of eggs in your fridge
boxes_of_eggs = 6

# Calculate the total number of eggs you have
total_eggs = eggs_per_box * boxes_of_eggs

# Calculate the maximum number of omelettes you can make
max_omelettes = total_eggs // eggs_per_omelette

# Output the result
print("You can make {} omelettes with {} boxes of eggs".format(max_omelettes, boxes_of_eggs))






