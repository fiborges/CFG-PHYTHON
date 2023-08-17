'''
Exercise 4.1
When I'm travelling in the winter I often forget to pack warm clothes. Let's write a program to help
me to remember the right clothes.
The program should check if the first item in the clothes list is "shorts". If it is it should change the
value to "warm coat".
clothes = [

"shorts",
"shoes",
"t-shirt",
]
Extension: Change the other items in the list to clothing more appropriate to winter if the first
item is shorts

'''

clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]

# Check if the first item is "shorts" and update it to "warm coat"
if clothes[0] == "shorts":
    clothes[0] = "warm coat"

# Extension: Change other items based on the value of the first item
if clothes[0] == "warm coat":
    clothes[1] = "winter boots"
    clothes[2] = "sweater"

print(clothes)


'''
Exercise 4.2
Make a list of game scores. Using list functions write code to output information of the scores in
the following format:
Number of scores: 10
Highest score: 200
Lowest score: 3
Extension: Output all of the scores in descending order
'''

game_scores = [120, 85, 200, 45, 150, 3, 90, 60, 75, 110]

# Calculate the number of scores
num_scores = len(game_scores)

# Find the highest and lowest scores
highest_score = max(game_scores)
lowest_score = min(game_scores)

# Output the results
print(f"Number of scores: {num_scores}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")

# Extension: Output all scores in descending order
game_scores.sort(reverse=True)
print("All scores in descending order:", game_scores)

'''
the program calculates the number of scores using the len() function.
It also finds the highest and lowest scores using the max() and min() functions. 
Then, it outputs the information in the specified format. For the extension, it sorts the game_scores 
list in descending order using the sort() function with the reverse=True argument and outputs all the 
scores in descending order.
'''

'''
Exercise 4.3
Whenever I'm shopping and I buy some bread I always forget to buy butter. Create a list and if
'bread' is in the list, add 'butter' to the shopping list.
Try running the program with and without bread in the list to check that your program works.
Remember the in operator checks if an item is in a list and the .append() method adds an item to a
list.
Extension: only add butter to the list if it is not already in the list
'''

shopping_list = [
    "cheese",
    "milk",
    "bread",
    "eggs",
]

# Check if 'bread' is in the shopping list and add 'butter' if needed
if "bread" in shopping_list and "butter" not in shopping_list:
    shopping_list.append("butter")

print(shopping_list)

'''
the program first checks if "bread" is in the shopping_list using the in 
operator. If "bread" is in the list and "butter" is not already in the list, it adds "butter" 
to the list using the .append() method. Finally, it prints the updated shopping list.

For the extension, this solution also ensures that "butter" is only added if it's not already 
in the list.
'''


'''
Exercise 4.4
I want to work out how much money I've spent on lunch this week. I've created a list of what I spent
each day.
Write a program that uses a for loop to calculate the total cost
costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0
Extension: work out the average that I spend on lunch for the week

'''

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

# Calculate the total cost using a for loop
for cost in costs:
    total_cost += cost

# Calculate the average cost
average_cost = total_cost / len(costs)

print(f"Total cost: £{total_cost:.2f}")
print(f"Average cost: £{average_cost:.2f}")

'''
the program uses a for loop to iterate through the costs list and 
calculate the total cost by adding up each individual cost. Then, it 
calculates the average cost by dividing the total cost by the number of 
days (length of the costs list). Finally, it outputs both the total cost 
and the average cost, each formatted with two decimal places.
'''

'''
Exercise 4.5
Print the values of name, post_code and street_number from the dictionary
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

# Print the values of name, post_code, and street_number
print("Name:", place['name'])
print("Post Code:", place['post_code'])
print("Street Number:", place['street_number'])

# Extension: Print the values of longitude and latitude from the inner dictionary
location = place['location']
print("Longitude:", location['longitude'])
print("Latitude:", location['latitude'])

'''
the program directly accesses the values associated with the keys 
'name', 'post_code', and 'street_number' in the place dictionary and 
prints them. For the extension, it accesses the inner dictionary 'location' 
and prints the values of 'longitude' and 'latitude'.
'''

'''
Exercise 4.6
Using a for loop, output the values name, colour and price of each dictionary in the list
fruits = [
{'name': 'apple', 'colour': 'red', 'price': 0.12},
{'name': 'banana', 'colour': 'yellow', 'price': 0.2},
{'name': 'pear', 'colour': 'green', 'price': 0.19},
]
Extension: Add more items to the list

'''

fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
    # Add more items to the list
    {'name': 'grape', 'colour': 'purple', 'price': 0.15},
    {'name': 'orange', 'colour': 'orange', 'price': 0.25},
]

# Using a for loop to output the values name, colour, and price of each dictionary
for fruit in fruits:
    print("Name:", fruit['name'])
    print("Colour:", fruit['colour'])
    print("Price:", fruit['price'])
    print()


'''
a for loop iterates through each dictionary in the fruits list. For each 
dictionary, it prints the values associated with the keys 'name', 'colour', and 'price', 
followed by a newline to separate the output of each fruit. The extension is fulfilled by 
adding two more fruit dictionaries to the fruits list.
'''

'''
Exercise 4.7
Write a program to create a random name. You should have a list of random first names and a list of
last names. Choose a random item from each and display the result.
Extension: Using list of verbs and a list of nouns, create randomised sentences

'''

import random

# Lists of random first names and last names
first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Fiona']
last_names = ['Johnson', 'Smith', 'Brown', 'Miller', 'Williams', 'Davis']

# Choose a random first name and last name
random_first_name = random.choice(first_names)
random_last_name = random.choice(last_names)

# Display the result
print("Random Name:", random_first_name, random_last_name)

# Extension: Lists of random verbs and nouns for creating random sentences
verbs = ['runs', 'jumps', 'eats', 'sleeps', 'reads', 'watches']
nouns = ['dog', 'cat', 'book', 'car', 'tree', 'phone']

# Choose a random verb and noun
random_verb = random.choice(verbs)
random_noun = random.choice(nouns)

# Create and display a random sentence
random_sentence = f"The {random_noun} {random_verb}."
print("Random Sentence:", random_sentence)

'''
the program first chooses a random first name and last name from the 
respective lists and displays the result. Then, for the extension, it chooses a 
random verb and noun from the lists and creates a random sentence using an f-string,
which is displayed as well.
'''


