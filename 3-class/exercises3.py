'''
Exercise 3.1
You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

1. Input the price of a burger using input()
2. Check whether the price is less than or equal (<=) 10.00
3. Print the result in the format below

Burger is within budget: True
Hint: remember to convert the input from a string to a decimal with float()

'''


# Input the price of a burger
burger_price = float(input('Enter the price of a burger: '))

# Check if the price is within budget
is_within_budget = burger_price <= 10.00

# Print the result
print('Burger is within budget:', is_within_budget)


'''
Exercise 3.2
Add code to your burger program to input whether the restaurant has a vegetarian option
The output should say whether the cost is within budget AND has a vegetarian option

Restaurant meets criteria: True
Extension: Add a check to see it the restaurant's rating is 3 or more
'''

# Input the price of a burger
burger_price = float(input('Enter the price of a burger: '))

# Input whether there is a vegetarian option (y/n)
has_vegetarian_option = input('Is there a vegetarian option? (y/n): ')

# Input the restaurant's rating
restaurant_rating = float(input('Enter the restaurant rating (0 to 5): '))

# Check if the price is within budget
is_within_budget = burger_price <= 10.00

# Check if the criteria are met (within budget, vegetarian option, and rating >= 3)
meets_criteria = is_within_budget and has_vegetarian_option.lower() == 'y' and restaurant_rating >= 3

# Print the result
print('Restaurant meets criteria:', meets_criteria)


'''
Exercise 3.3
Rewrite the output of your burger program to use if statements
If it is a good choice it should be:
This restaurant is a great choice!
If it is not a good choice it should be:
Probably not a good idea
'''

# Input the price of a burger
burger_price = float(input('Enter the price of a burger: '))

# Input whether there is a vegetarian option (y/n)
has_vegetarian_option = input('Is there a vegetarian option? (y/n): ')

# Input the restaurant's rating
restaurant_rating = float(input('Enter the restaurant rating (0 to 5): '))

# Check if the price is within budget
is_within_budget = burger_price <= 10.00

# Check if the criteria are met (within budget, vegetarian option, and rating >= 3)
meets_criteria = is_within_budget and has_vegetarian_option.lower() == 'y' and restaurant_rating >= 3

# Print the result
print('Restaurant meets criteria:', meets_criteria)


'''
Exercise 3.4
Now that you've finished your burger, you want to pay for your food. Let's write a program to
calculate your meal and apply a discount if applicable.
If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%.
The program should print "Discount applied" or "No discount" depending on whether the discount
criteria was met.
meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'
'''

meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')

if discount_choice.lower() == 'y':
    discount_applicable = True
else:
    discount_applicable = False

if meal_price > 20 and discount_applicable:
    meal_price *= 0.9  # Apply a 10% discount
    print('Discount applied')

else:
    print('No discount')

print('Total cost:', meal_price)


'''
Exercise 3.5
You're cooking a pizza and need to check that the oven is at the right temperature.
Write a program to:
● Ask the user to input the temperature
● Prints "The oven is too hot" if the temperature is over 200
● Prints "The oven is too cold" if the temperature is under 150
● Prints "The oven is at the perfect temperature" if the temperature is 180 ●
Prints "The temperature is close enough" for any other temperature
Extension: Ask at the start of the program whether you're cooking a cake or a pizza. The suggested
temperatures for a cake should be different from the pizza.
'''

def check_oven_temperature(target_temp, min_temp, max_temp, ideal_temp, item_name):
    temperature = float(input('Enter the oven temperature: '))

    if temperature > max_temp:
        print('The oven is too hot')
    elif temperature < min_temp:
        print('The oven is too cold')
    elif temperature == ideal_temp:
        print('The oven is at the perfect temperature')
    else:
        print('The temperature is close enough for', item_name)

item_name = input('Are you cooking a cake or a pizza? ').lower()

if item_name == 'cake':
    check_oven_temperature(target_temp=180, min_temp=160, max_temp=200, ideal_temp=180, item_name='cake')
elif item_name == 'pizza':
    check_oven_temperature(target_temp=220, min_temp=200, max_temp=250, ideal_temp=220, item_name='pizza')
else:
    print('Invalid input. Please enter "cake" or "pizza".')


'''
Exercise 3.6
This program uses random to simulate a coin flip.
To finish the program you will need to add the following:
● If the random coin flip matches the choice input by the user then they win ● Otherwise if
the random coin flip does not match the choice input by the user then they lose
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
Extension: The program should show a message to the user if they enter a choice that isn't heads
or tails
'''

import random

def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side

def main():
    choice = input('heads or tails: ').lower()
    
    if choice != 'heads' and choice != 'tails':
        print('Invalid choice. Please choose "heads" or "tails".')
    else:
        result = flip_coin()
        print('The coin landed on', result)
        
        if result == choice:
            print('You win!')
        else:
            print('You lose.')

if __name__ == '__main__':
    main()


'''
Exercise 3.7
This program simulates rock, paper, scissors. The first winning condition has been added. To finish
the program you'll need to add all of the other winning and losing conditions.
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
my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()
print('Your opponent chose {}'.format(opponent_choice))
if my_choice == 'rock' and opponent_choice == 'scissors':
print('You win!')
Extension: the program should show a message to the user if they enter a choice that isn't rock,
paper or scissors
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

def main():
    choices = ['rock', 'scissors', 'paper']
    my_choice = input('Choose rock, scissors, or paper: ').lower()
    
    if my_choice not in choices:
        print('Invalid choice. Please choose "rock", "scissors", or "paper".')
    else:
        opponent_choice = random_choice()
        print('Your opponent chose', opponent_choice)
        
        if my_choice == opponent_choice:
            print('It\'s a tie!')
        elif (my_choice == 'rock' and opponent_choice == 'scissors') or \
             (my_choice == 'scissors' and opponent_choice == 'paper') or \
             (my_choice == 'paper' and opponent_choice == 'rock'):
            print('You win!')
        else:
            print('You lose.')

if __name__ == '__main__':
    main()


'''
Exercise 3.8
Not Quite Roulette
Ask the user to enter the following three things using input():

● The amount they want to bet
● A colour (red or black)
● A number between 1 and 100
After generating a random number and colour:
● If the colour matches, the users keeps the amount that was bet
● If the number matches, the users wins double the amount that was bet ● If the colour
and number matches, the users wins 100 times the amount that was bet ● When neither
the colour or number matches the user wins 0
● Output the amount the user won
The following code will generate a random number and colour:
import random

def colour():
random_number = random.randint(1, 2)
if random_number == 1:
colour = 'red'
else:
colour = 'black'
return colour

random_number = random.randint(1, 100)
random_colour = colour()
'''

import random

def colour():
    random_number = random.randint(1, 2)
    if random_number == 1:
        colour = 'red'
    else:
        colour = 'black'
    return colour

def main():
    # Input the amount to bet
    bet_amount = float(input('Enter the amount you want to bet: '))
    
    # Input the colour choice (red or black)
    user_colour = input('Enter the colour (red or black): ').lower()
    
    # Input the number choice (between 1 and 100)
    user_number = int(input('Enter a number between 1 and 100: '))
    
    # Generate a random number and colour
    random_number = random.randint(1, 100)
    random_colour = colour()
    
    # Check if the colour and number matches
    if user_colour == random_colour and user_number == random_number:
        win_amount = bet_amount * 100
        print('Congratulations! You won', win_amount)
    # Check if the colour matches
    elif user_colour == random_colour:
        win_amount = bet_amount
        print('You won', win_amount)
    # Check if the number matches
    elif user_number == random_number:
        win_amount = bet_amount * 2
        print('You won', win_amount)
    else:
        print('Sorry, you didn\'t win anything.')

if __name__ == '__main__':
    main()
