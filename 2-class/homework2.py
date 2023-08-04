'''
     # Question 1
Explain what this program does:

for number in range(100):
    output = 'o' * number
print(output)

Aswer:

- for number in range(100):
This creates a loop that iterates over numbers from 0 to 99 (100 is not included).
In each iteration, the variable number takes on the value of the current number 
in the loop.

- output = 'o' * number: 
This line creates a string variable named output that consists of the letter 'o' 
repeated number times. In the first iteration (number = 0), the string is empty.
In the second iteration (number = 1), the string contains one 'o'. In the third 
iteration (number = 2), the string contains two 'o's, and so on.

- print(output): 
This line prints the output string on each iteration of the loop.
So, in the first iteration, it prints an empty string, in the second iteration, 
it prints 'o', in the third iteration, it prints 'oo', and so on until it prints 'o' 
repeated 99 times.

# output:

o
oo
ooo
oooo
ooooo
oooooo
ooooooo
oooooooo
ooooooooo
oooooooooo
... (and so on, up to 99 repetitions of 'o')

'''

'''
# Question 2
Your boss really likes calculating VAT on their purchases. It is their favourite hobby. They've written this code to calculate VAT and need your help to fix it. 

def calculate_vat(amount): 
amount * 1.2 

total = calculate_vat(100)
print(total) 

When your boss runs the program they get the following output: 

None 
Your boss expects the program to output the value 120. What is wrong? How do you fix it? 

VAT stands for "Value Added Tax."  = IVA PORTUGAL

'''

def calculate_vat(amount):
    return amount * 1.2

# def calculate_vat(amount):
# This line defines a function named calculate_vat. 
# The function takes one parameter amount, which represents the initial amount on which we want
# to calculate the VAT.

# return amount * 1.2: 
# Inside the function, this line calculates the VAT amount by multiplying the amount with 1.2 
# (equivalent to adding 20% VAT). 
# The result is returned by the function.

total = calculate_vat(100)
print(total)

# total = calculate_vat(100): 
# In this line, the calculate_vat function is called with the argument 100. 
# The function calculates the VAT for the initial amount of 100 and returns the result, 
# which is then assigned to the variable total.

# print(total): 
# Finally, this line prints the value of the total variable, which contains the 
# calculated VAT amount.

'''
However, there is a problem with the original code. The function calculate_vat correctly 
calculates the VAT amount, but it doesn't return the result. 
So, when we call calculate_vat(100) and assign the result to the variable total, the value of total becomes 
None because the function didn't explicitly return anything.

'''

# To fix this, we need to modify the function to include a return statement:
# By adding the return statement, the function now returns the calculated VAT amount, 
# and the output will be 120.0, which is the correct VAT amount for an initial amount of 100.

