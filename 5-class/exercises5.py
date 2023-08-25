'''
Exercise 5.1
Create a to-do list program that writes user input to a file
The program should:
 Ask the user to input a new to-do item
 Read the contents of the existing to-do items

 Add the new to do item to the existing to-do items
 Save the updated to-do items
You will need to manually create a new file called todo.txt in the same folder as your program
before you start

'''

# Ask the user for a new to-do item
new_item = input("Enter a new to-do item: ")

# Read the contents of the existing to-do items
try:
    with open("todolist.txt", "r") as todo_file:
        existing_items = todo_file.read()
except FileNotFoundError:
    existing_items = ""

# Add the new to-do item to the existing items
updated_items = existing_items + new_item + "\n"

# Write the updated to-do items back to the file
with open("todolist.txt", "w") as todo_file:
    todo_file.write(updated_items)

print("To-do item added successfully!")

'''
It asks the user to input a new to-do item.
It attempts to read the contents of the existing todo.txt file. 
If the file doesn't exist, it initializes existing_items as an empty string.
The new item is appended to the existing_items.
The updated to-do items are written back to the todo.txt file.
A success message is printed.

'''

'''
Exercise 5.2
This program is supposed to read data about trees from a file to find the shortest tree. Complete
the program adding code to open trees.csv.
The trees.csv file included with your student guides. Save the csv file in the same folder as your
Python program.
spreadsheet = # Add code to open the csv file
heights = []
for row in spreadsheet:
tree_height = row['height']
heights.append(tree_height)
shortest_height = min(heights)
print(shortest_height)
'''
import csv

# Open the CSV file and read its contents
with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    
    # Create a list to store tree heights
    heights = []
    
    # Iterate through the rows and extract tree heights
    for row in spreadsheet:
        tree_height = int(row['height'])  # Convert height to integer
        heights.append(tree_height)
    
    # Find the shortest tree height using the min function
    shortest_height = min(heights)
    
    # Print the shortest tree height
    print(f"The shortest tree height is: {shortest_height}")


'''
First, make sure you have the trees.csv file in the same folder as your Python program.
Use the csv module to open and read the CSV file.
Iterate through the rows of the CSV file and extract the tree heights.
Calculate the shortest tree height using the min function.
Print the shortest tree height.

opens the trees.csv file, reads its contents using csv.DictReader, 
extracts the tree heights, finds the shortest tree height, and prints the 
result. Make sure to adjust the column name 'height' to match the actual column name 
in your CSV file if it's different.
'''
'''
Exercise 5.3
Get the height and weight of a specific Pokemon and print the output
Extension: Print the names of all of a specific Pokemon's moves
'''

'''
import requests

# Pokemon API endpoint
pokemon_name = "pikachu"  # Replace with the desired Pokémon name
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"

# Send a GET request to the API
response = requests.get(url)
data = response.json()

# Extract height and weight
height = data['height']
weight = data['weight']

# Print the output
print(f"{pokemon_name.capitalize()} has a height of {height / 10} meters and a weight of {weight / 10} kilograms.")
'''
'''
For the extension, here's how you can print the names of all the moves of the specified Pokémon
'''
'''
import requests

# Pokemon API endpoint
pokemon_name = "pikachu"  # Replace with the desired Pokémon name
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"

# Send a GET request to the API
response = requests.get(url)
data = response.json()

# Extract and print the names of all moves
print(f"{pokemon_name.capitalize()}'s moves:")
for move in data['moves']:
    move_name = move['move']['name']
    print(move_name.capitalize())
    
'''    
'''
Make sure to replace 'pikachu' with the name of the Pokémon you're interested in. 
This code retrieves the height and weight of the specified Pokémon and prints them, and then it retrieves 
and prints the names of all the moves of the same Pokémon.
'''
