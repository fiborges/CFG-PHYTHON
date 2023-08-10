# 1 exercise slides

'''
print('~' * 0)
print('~' * 1)
print('~' * 2)
print('~' * 3)
print('~' * 4)
print('~' * 5)
print('~' * 6)
print('~' * 7)
print('~' * 8)

# Gerar uma sequência de números de 0 a 4 (não inclui o 5)
for i in range(5):
    print(i)

# Gerar uma sequência de números de 3 a 10 (não inclui o 11)
for j in range(3, 11):
    print(j)

# Gerar uma sequência de números pares de 0 a 10
for k in range(0, 11, 2):
    print(k)

'''
for i in range(9):
    print('~' * i)
    
today = input('What day is it? ')
is_monday = today == 'Monday'
print('Today is Monday: {}'.format(is_monday))
    

temperature = input('What is the temperature? ')
is_freezing = float(temperature) <= 0.0
print('The temperature is freezing: {}'.format(is_freezing))


'''
Exercise 3.1: You have a budget of £10 and want to write a program to decide which burger
restaurant to go to.

1. Input the price of a burger using input()
2. Check whether the price is less than or equal (<=) 10.00
3. Print the result in the format below
Burger is within budget: True

Hint: remember to convert the input from a string to a decimal with float()

'''

# Input the price of a burger
price = float(input('Enter the price of a burger: '))

# Check if the price is within budget
within_budget = price <= 10.00

# Print the result
print('Burger is within budget:', within_budget)

'''
There are logical operators to combine multiple checks

Python What it does
and both expressions are True
or at least one expression is True
not reverse the expression (True becomes False and vice-versa)
'''

mars_choice = input('Would you like to visit Mars? y/n ')
is_willing = mars_choice == 'y'
affordable = input('Can you afford to visit Mars? y/n ')
can_afford = affordable == 'y'
should_visit_mars = is_willing and can_afford
print('You should visit Mars: {}'.format(should_visit_mars))

'''
Exercise 3.2: Add code to your burger program to input whether the restaurant has a vegetarian
option The output should say whether the cost is within budget AND has a vegetarian option
'''

# Input the price of a burger
price = float(input('Enter the price of a burger: '))

# Input whether the restaurant has a vegetarian option
vegetarian_option = input('Does the restaurant have a vegetarian option? (y/n): ')
has_vegetarian = vegetarian_option.lower() == 'y'

# Check if the price is within budget and has a vegetarian option
within_budget = price <= 10.00
is_good_choice = within_budget and has_vegetarian

# Print the result
print('Restaurant meets criteria:', is_good_choice)

#------------------------------------------------------------

#if statement: used to run a block of code depending on whether a condition is True or False

password = input('password: ')
if password == 'jumanji':
    print('Success!')

#   if condition:
name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'
if is_admin and is_password_correct:
    print('Welcome')
if not is_admin or not is_password_correct:
    print('Go away')

'''
Exercise 3.3: Rewrite the output of your burger program to use if statements
If it is a good choice it should be:
This restaurant is a great choice!

If it is not a good choice it should be:
Probably not a good idea

'''

# Input the price of a burger
price = float(input('Enter the price of a burger: '))

# Input whether the restaurant has a vegetarian option
vegetarian_option = input('Does the restaurant have a vegetarian option? (y/n): ')
has_vegetarian = vegetarian_option.lower() == 'y'

# Check if the price is within budget and has a vegetarian option
within_budget = price <= 10.00
is_good_choice = within_budget and has_vegetarian

# Print the result using if statements
if is_good_choice:
    print('This restaurant is a great choice!')
if not is_good_choice:
    print('Probably not a good idea')   
    
    
#else statement: Used with an if statement and will run when the if condition is False

password = input('password: ')
if password == 'jumanji':
    print('Success!')
else:
    print('Failure!')
    
# Here's the admin program rewritten to use else :

name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'
if is_admin and is_password_correct:
    print('Welcome')
else:
    print('Go away')
    
'''
Exercise 3.4: Now that you've nished your burger, you want to pay for your food. 
Let's write a program to calculate your meal and apply a discount if applicable.
If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%.
The program should print "Discount applied" or "No discount" depending on whether the discount
criteria was met.


'''

# Input the cost of the meal
meal_price = float(input('How much did the meal cost? '))

# Input whether the user has a discount
discount_choice = input('Do you have a discount? (y/n): ')
is_discount = discount_choice.lower() == 'y'

# Check if the meal price is over £20 and a discount is applicable
if meal_price > 20.0 and is_discount:
    # Apply a 10% discount
    discounted_price = meal_price * 0.9
    print('Discount applied')
    print('Total cost after discount: £{:.2f}'.format(discounted_price))
else:
    print('No discount')
    print('Total cost: £{:.2f}'.format(meal_price))

#elif statement: used after if statements to check whether another condition is True or False

dog_size = int(input('How big is the dog? '))
if dog_size > 75:
    print('That is a big dog')
elif dog_size < 25:
    print('That is a small dog')
else:
    print('That is an average dog')
    
    

dog_size = int(input('How big is the dog? '))
if dog_size > 75:
    print('That is a big dog')
elif dog_size < 10:
    print('That dog could fit in my pocket')
elif dog_size < 25:
    print('That is a small dog')
else:
    print('That is an average dog')
    

'''
Exercise 3.5: You're cooking a pizza and need to check that the oven is at the right temperature.
Write a program to:

Ask the user to input the temperature
Prints "The oven is too hot" if the temperature is over 200
Prints "The oven is too cold" if the temperature is under 150
Prints "The oven is at the perfect temperature" if the temperature is 180
Prints "The temperature is close enough" for any other temperature

'''

# Input the temperature of the oven
temperature = float(input('What is the temperature of the oven? '))

# Check the temperature and print the appropriate message
if temperature > 200:
    print('The oven is too hot')
elif temperature < 150:
    print('The oven is too cold')
elif temperature == 180:
    print('The oven is at the perfect temperature')
else:
    print('The temperature is close enough')


#Python has a built-in library for random data

import random
random_integer = random.randint(1, 100)
print(random_integer)



import random
sides = int(input('How many sides does the die have? '))
random_integer = random.randint(1, sides)
print('You rolled a {}'.format(random_integer))


'''
Exercise 3.6: This program uses random to simulate a coin ip.
To nish the program you will need to add the following:

If the random coin ip matches the choice input by the user then they win
Ohterwise if the random coin ip does not match the choice input by the user then they lose

'''

import random
def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side
choice = input('heads or tails: ')
result = flip_coin()
print('The coin landed on {}'.format(result))


'''
Exercise 3.7: This program simulates rock, paper, scissors. The rst winning condition has been
added.
To nish the program you'll need to add all of the other winning and losing conditions.
'''

import random

def random_choice():
    choice_number = random.randint(1, 3)
    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'
    return choice

my_choice = input('Choose rock, scissors, or paper: ')
opponent_choice = random_choice()

print('Your opponent chose', opponent_choice)

if my_choice == opponent_choice:
    print('It\'s a tie!')
elif my_choice == 'rock':
    if opponent_choice == 'scissors':
        print('You win!')
    else:
        print('You lose!')
elif my_choice == 'scissors':
    if opponent_choice == 'paper':
        print('You win!')
    else:
        print('You lose!')
elif my_choice == 'paper':
    if opponent_choice == 'rock':
        print('You win!')
    else:
        print('You lose!')
else:
    print('Invalid choice. Please choose rock, scissors, or paper.')


'''
Exercise 3.8: Not Quite Roulette
Ask the user to enter the following three things using input() :

The amount they want to bet
A colour (red or black)
A number between 1 and 100
After generating a random number and colour:

If the colour matches, the users keeps the amount that was bet
If the number matches, the users wins double the amount that was bet
If the colour and number matches, the users wins 100 times the amount that was bet
When neither the colour or number matches the user wins 0
Output the amount the user won
The following code will generate a random number and colour:
'''

import random

# Input the amount to bet
bet_amount = float(input('Enter the amount you want to bet: '))

# Input the colour (red or black)
colour_choice = input('Choose a colour (red or black): ')

# Input a number between 1 and 100
number_choice = int(input('Choose a number between 1 and 100: '))

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Generate a random colour
random_colour = random.choice(['red', 'black'])

print('The random number is:', random_number)
print('The random colour is:', random_colour)

# Check the outcomes and calculate the amount won
amount_won = 0

if colour_choice.lower() == random_colour:
    amount_won += bet_amount
if number_choice == random_number:
    amount_won += bet_amount * 2
if colour_choice.lower() == random_colour and number_choice == random_number:
    amount_won += bet_amount * 100

print('You won £{:.2f}'.format(amount_won))




