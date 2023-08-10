# Python Basics: Conditionals and Logic

In this lesson, we covered several fundamental concepts related to conditionals and logic in Python. We explored how to make decisions in code, perform comparisons, and use logical operators.

## Boolean Values and Comparison Operators
### Boolean Values: 
  Booleans are data types that can be either True or False. They represent binary states, often used for decision-making.

### Comparison Operators: 
  These operators help compare values to determine whether a condition is True or False. Examples include == (equal to), != (not equal to), >, <, >=, and <=.

#### Example:

```python

x = 5
y = 10
equal_check = x == y  # False
greater_than_check = x > y  # False
If Statements and Logical Operators
If Statements: These are used to execute a block of code based on whether a condition is True or False.

```

### Logical Operators: 
  They include and (both expressions are true), or (at least one expression is true), and not (reverses the expression's truth value).

#### Example:

```python

name = input("What is your name? ")
is_admin = name == 'admin'
if is_admin:
    print('Welcome')
else:
    print('Go away')

```

## Elif and Else Statements
### Elif Statements: 
Used after an if statement to check additional conditions if the initial condition is false.

#### Else Statements: 
Run when the preceding if and elif conditions are false.

#### Example:

```python

temperature = float(input('What is the temperature of the oven? '))
if temperature > 200:
    print('The oven is too hot')
elif temperature < 150:
    print('The oven is too cold')
else:
    print('The temperature is just right')

```

## Randomization with the random Module
The random module can generate random numbers and choices.

#### Example:

```python

import random
random_integer = random.randint(1, 100)  # Generates a random number between 1 and 100

```

## Putting It All Together: Exercise Samples
Coin Flip Simulation

```python

import random

def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side

choice = input('Heads or tails? ')
result = flip_coin()
print('The coin landed on {}'.format(result))
```

### Rock, Scissors, Paper Game
```python

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
print('Your opponent chose {}'.format(opponent_choice))
if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')
```

### Add more winning and losing conditions

#### Temperature Check and Discount Application
```python

meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')
is_discount = discount_choice == 'y'
is_over_twenty = meal_price >= 20.0
discount_applicable = is_discount and is_over_twenty

if discount_applicable:
    meal_price = meal_price * 0.9
    print('Discount applied')
else:
    print('No discount')
print('Total cost: {}'.format(meal_price))

```

#### Pizza Oven Temperature Check
```python

temperature = float(input('What is the temperature of the oven? '))

if temperature > 200:
    print('The oven is too hot')
elif temperature < 150:
    print('The oven is too cold')
elif temperature == 180:
    print('The oven is at the perfect temperature')
else:
    print('The temperature is close enough')

```
