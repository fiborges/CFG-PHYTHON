'''
Exercise 4.1: When I'm travelling in the winter I often forget to pack warm clothes. Let's write a
program to help me to remember the right clothes.
The program should check if the

rst item in the clothes list is "shorts" . If it is it should change

the value to "warm coat" .


'''
'''
clothes = [
    "shorts",
    "shoes",
    "t-shirt"
]

if clothes[0] == 'shorts':
    clothes[0] = 'warm coat'

print(clothes)

'''
'''
Exercise 4.2: Make a list of game scores. Using list functions write code to output information of the
scores in the following format:

Extension: Output all of the scores in descending order
'''
'''
game_scores = [87, 65, 92, 78, 200, 82, 70, 3, 91, 68]

print("Number of scores:", len(game_scores))
print("Highest score:", max(game_scores))
print("Lowest score:", min(game_scores))

# Sorting in descending order
game_scores.sort(reverse=True)
print("All scores in descending order:", game_scores)

'''
'''
In this program, we first create a list named game_scores containing some
scores. Then, we use list functions to calculate and output various information 
about the scores. Finally, we sort the scores in descending order using the sort() 
method with the reverse=True parameter and print the sorted list.

can use:

game_scores.sort()
And to sort the list in descending order, you can use either:

game_scores.sort(reverse=True)
or

descending_scores = sorted(game_scores, reverse=True)
Both of these methods will give you the game scores in descending order.

'''

'''
You can check if an value is in a list using the in operator. If the value is in the list it will result in True
and False if it is not.

student_name = input('Which student are you looking for? ')
students = [
'Diedre', 'Hank', 'Helena', 'Salome',
]
if student_name in students:
print('{} is in the class'.format(student_name))
else:
print('{} is not in the class'.format(student_name))
'''

'''
The .append() method is used to add items to a list

students = [
'Diedre', 'Hank', 'Helena', 'Salome',
]
student_name = input('What is the name of the new student? ')
students.append(student_name)
print(students)
What is the name of the new student? Jo
['Diedre', 'Hank', 'Helena', 'Salome', 'Jo']

'''

'''
Exercise 4.3: Whenever I'm shopping and I buy some bread I always forget to buy butter. Create a list
and if 'bread' is in the list, add 'butter' to the shopping list.
Try running the program with and without bread in the list to check that your program works.
Remember the in operator checks if an item is in a list and the .append() method adds an item to a
list.

'''
shopping_list = [
    'bread',
    'cheese',
    'pop tarts',
    'carrots'
]

if 'bread' in shopping_list:
    shopping_list.append('butter')

print(shopping_list)

'''
In this program, we have a list called shopping_list that contains various items. 
The program uses the in operator to check if the string 'bread' is present in the list. If it is, 
the program uses the append() method to add the string 'butter' to the list. Finally,
it prints the updated shopping list.

To check if an item is not in a list

fridge = [
'cheese',
'pizza',
'coke',
]
if 'milk' not in fridge:
print('You have no milk in the fridge')
You have no milk in the fridge

'''

'''
Using lists and for loops together

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
for student_name in student_names:
print(student_name)
Diedre
Hank
Helena
Salome

Counting the total number of items in a list using a for loop

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
count = 0
for student_name in student_names:
count = count + 1
print(count)
4
'''

'''
Exercise 4.4: I want to work out how much money I've spent on lunch this week. I've created a list of
what I spent each day.
Write a program that uses a for loop to calculate the total cost

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost

'''
costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for cost in costs:
    total_cost += cost

print("Total cost:", total_cost)

'''
we have a list named costs containing the costs of lunch for each day of the week. 
The program uses a for loop to iterate through each cost in the list and adds it to
the total_cost variable. Finally, it prints the total cost of lunch for the week.

There is an easier way to do the last program without a for loop. The sum() function can be used to
add up all of the values in a list:

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total = sum(costs)
print(total)
31.839999999999996

'''
'''
Dictionary: Stores a colleciton of labelled items. Each item has a key and a value

person = {
'name': 'Jessica',
'age': 23,
'height': 172
}

Values in a dictionary are accessed using their keys

person = {
'name': 'Jessica',
'age': 23,
'height': 172
}
print(person['name'])


'''

'''
Exercise 4.5: Print the values of name , post_code and street_number from the dictionary

place = {
'name': 'The Anchor',
'post_code': 'E14 6HY',
'street_number': '54',
'location': {
'longitude': 127,
'latitude': 63,
}
}

Extension: Print the values of longitude and latitude from the inner dictionary

'''

place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

print("Name:", place['name'])
print("Post Code:", place['post_code'])
print("Street Number:", place['street_number'])

# Extension
location = place['location']
print("Longitude:", location['longitude'])
print("Latitude:", location['latitude'])

'''
Putting dictionaries inside a list is very common

people = [
{'name': 'Jessica', 'age': 23},
{'name': 'Trisha', 'age': 24},
]
for person in people:
print(person['name'])
print(person['age'])

'''
'''
Exercise 4.6: Using a for loop, output the values name , colour and price of each dictionary in the
list

fruits = [
{'name': 'apple', 'colour': 'red', 'price': 0.12},
{'name': 'banana', 'colour': 'yellow', 'price': 0.2},
{'name': 'pear', 'colour': 'green', 'price': 0.19},
]

'''

fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19}
]

for fruit in fruits:
    print("Name:", fruit['name'])
    print("Colour:", fruit['colour'])
    print("Price:", fruit['price'])
    print()


'''
The choice() function in the random module returns a random item from a list

import random
colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)
print(chosen_colour)
green

Exercise 4.7: Write a program to create a random name. You should have a list of random

rstnames

and a list of lastnames. Choose a random item from each and display the result.
Extension: Using list of verbs and a list of nouns, create randomised sentences

'''

import random

first_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']

random_first_name = random.choice(first_names)
random_last_name = random.choice(last_names)

print("Random Name:", random_first_name, random_last_name)

# Extension
verbs = ['runs', 'jumps', 'eats', 'sleeps', 'laughs']
nouns = ['dog', 'cat', 'apple', 'tree', 'book']

random_verb = random.choice(verbs)
random_noun = random.choice(nouns)

random_sentence = f"The {random_noun} {random_verb}."

print("Random Sentence:", random_sentence)


'''
Question 3: This program raises an error when I run it. What do I need to change to get it to run?

trees = [
{'leaf_colour': 'green', 'height': 2120},
{'leaf_colour': 'green', 'height': 2300},

new_tree = {
'leaf_colour': 'green',
'height': 1020
}
trees.append(new_tree)
print(trees)

----

trees = [
    {'leaf_colour': 'green', 'height': 2120},
    {'leaf_colour': 'green', 'height': 2300},
]

new_tree = {
    'leaf_colour': 'green',
    'height': 1020
}
trees.append(new_tree)
print(trees)

In this corrected version, I added a closing curly brace } to properly 
close the dictionary within the list. This should now run without errors and output the 
list of dictionaries with the new tree added.
'''





