'''
Question 1
I have a list of things I need to buy from my supermarket of choice.
shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]

print(shopping_list[1])
I want to know what the first thing I need to buy is. However, when I run the program it shows me a
different answer to what I was expecting?
What is the mistake? How do I fix it?
'''

'''
The mistake is that lists in Python are zero-indexed, which means the first item in the list has an index of 0, not 1.
When you print shopping_list[1], you're actually accessing the second item in the list, not the first.

To fix this and print the first item in the list, you should use shopping_list[0] instead of shopping_list[1]. 
Here's the corrected version of the code:
'''
shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board",
]

print(shopping_list[0])  # Accessing the first item in the list

'''
Question 2
I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of
different chocolates that I sell.
I've started the program and included the chocolates and their prices. Finish the program by asking
the user to input an item and then output its price.

chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}
'''
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

item = input("Enter the chocolate type: ")

if item in chocolates:
    price = chocolates[item]
    print(f"The price of {item} chocolate is ${price:.2f}")
else:
    print("Sorry, we don't have that chocolate type.")


'''
the user is prompted to enter a chocolate type. The program then
checks if the entered chocolate type exists in the chocolates dictionary. If it does, 
it retrieves and prints the corresponding price. If the entered chocolate type is not found, 
it prints a message saying that the chocolate type is not available.


'''

'''
Question 3

Write a program that simulates a lottery. The program should have a list of seven numbers that
represent a lottery ticket. It should then generate seven random numbers. After comparing the two
sets of numbers, the program should output a prize based on the number of matches:
● £20 for three matching numbers
● £40 for four matching numbers
● £100 for five matching numbers
● £10000 for six matching numbers
● £1000000 for seven matching numbers

'''

import random

# List representing the user's lottery ticket
user_ticket = [1, 5, 12, 18, 22, 30, 45]

# Generate seven random numbers for the draw
draw_numbers = [random.randint(1, 50) for _ in range(7)]

print("User's Ticket:", user_ticket)
print("Draw Numbers:", draw_numbers)

# Count the number of matching numbers
num_matches = len(set(user_ticket) & set(draw_numbers))

# Determine the prize based on the number of matches
prize = 0
if num_matches == 3:
    prize = 20
elif num_matches == 4:
    prize = 40
elif num_matches == 5:
    prize = 100
elif num_matches == 6:
    prize = 10000
elif num_matches == 7:
    prize = 1000000

print(f"You matched {num_matches} numbers. Your prize: £{prize:,}")


'''
the user's lottery ticket is represented as the user_ticket list. 
The program generates seven random numbers for the draw using random.randint().
It then compares the user's ticket with the draw numbers to count the number of matches. 
Based on the number of matches, the program determines the prize and outputs it.
'''

