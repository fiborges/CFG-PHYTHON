'''
Starter: How do I output the species values for each of the dictionaries?
[
{'species': 'zebra', 'name': 'Penelope'},
{'species': 'penguin', 'name': 'Jenn'},
{'species': 'elephant', 'name': 'Harris'},
{'species': 'flamingo', 'name': 'Florence'},
]

'''
'''
animals = [
    {'species': 'zebra', 'name': 'Penelope'},
    {'species': 'penguin', 'name': 'Jenn'},
    {'species': 'elephant', 'name': 'Harris'},
    {'species': 'flamingo', 'name': 'Florence'},
]

# Loop through the list and print the 'species' value for each dictionary
for animal in animals:
    species = animal['species']
    print(species)
'''
'''

The with open statement in Python is used to work with files. 
It provides a convenient and clean way to open a file, perform operations on it 
(like reading or writing), and automatically close the file when the operations are done or if an exception is raised.

The syntax for using with open is as follows:

with open(filename, mode) as file_variable:
    # Code to work with the file using file_variable
    # The file is automatically closed when this block is exited
    
Here:

filename is the name of the file you want to open.
mode specifies the mode in which the file should be opened ('r' for read, 'w' for write, 'a' for append, etc.).
file_variable is a variable that will represent the opened file object within the indented block.
The key advantage of using with open is that it takes care of properly closing the file, even if an 
exception occurs within the indented block. This helps prevent resource leaks and makes the code 
more readable.

For example, when reading data from a file:

with open('example.txt', 'r') as file:
    content = file.read()
    # Do something with content
# File is automatically closed when the block is exited

And when writing data to a file:

data = "Hello, world!"
with open('output.txt', 'w') as file:
    file.write(data)
# File is automatically closed when the block is exited

Using with open is considered a best practice when working with files in Python.


with open('people.txt', 'w+') as text_file:
    people = 'Joanne \nSusan \nAmina'
    text_file.write(people)

with open('people.txt', 'r') as text_file:
    contents = text_file.read()
    print(contents)
    
The three methods read(), readline(), and readlines() are used to read data from a file in Python, 
but they have different behaviors and use cases:

read() Method:
This method reads the entire content of the file as a single string.
It reads from the current file position up to the end of the file.
If you don't pass an argument, it will read the entire file.
Useful when you want to process the entire file content as a single string.
Example:

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

readline() Method:
This method reads a single line from the file each time it's called.
It moves the file cursor to the beginning of the next line after reading.
Useful when you want to process the file line by line.
Example:

with open('example.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)

readlines() Method:
This method reads all lines from the file and returns them as a list of strings.
Each element in the list represents a line from the file, including the newline character \n.
Useful when you want to process each line individually or need to store them in a list.
Example:

with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
In summary:

Use read() when you want the entire content of the file as a single string.
Use readline() when you want to read lines one by one.
Use readlines() when you want all lines as a list of strings.
these methods move the file cursor as you read, so subsequent reads will start where the 
previous read left off. If you need to read from the beginning again, 
you'll need to close and reopen the file or use the seek() method to move the cursor.


'''   
'''
Exercise 5.1: Create a to-do list program that writes user input to a
le

The program should:

Ask the user to input a new to-do item
Read the contents of the existing to-do items
Add the new to do item to the existing to-do items
Save the updated to-do items
You will need to manually create a new

le called todo.txt in the same folder as your program

before you start
'''
# Ask the user to input a new to-do item
# Create an empty todo.txt file

'''
with open('todolist.txt', 'w') as todo_file:
    pass

print("todolist.txt file created.")

new_item = input("Enter a new to-do item: ")
'''
# Read the contents of the existing to-do items if is existing already
# Ask the user to input a new to-do item
'''
new_item = input("Enter a new to-do item: ")

try:
    with open("todolist.txt", "r") as todo_file:
        existing_items = todo_file.readlines()
except FileNotFoundError:
    existing_items = []

# Add the new to-do item to the existing to-do items
existing_items.append(new_item + "\n")

# Save the updated to-do items
with open("todolist.txt", "w") as todo_file:
    todo_file.writelines(existing_items)

print("To-do item added:", new_item)
'''
'''

'w' (Write Mode):
This mode is used to open a file for writing.
If the file already exists, it will be truncated (its content will be cleared).
If the file doesn't exist, a new file will be created.
If you try to read from the file opened in write mode, it will raise an UnsupportedOperation error.
Example:


with open('file.txt', 'w') as file:
    file.write('Hello, world!')
'w+' (Write and Read Mode):
This mode is used to open a file for both writing and reading.
If the file already exists, it will be truncated (content cleared) before writing.
If the file doesn't exist, a new file will be created.
You can both read from and write to the file in this mode.
However, the file pointer will initially be at the beginning of the file, so if you read immediately after opening, you'll get an empty string.
Example:

with open('file.txt', 'w+') as file:
    file.write('Hello, world!')
    file.seek(0)  # Move the file pointer to the beginning
    content = file.read()
    print(content)  # Output: Hello, world!
    
In summary, if you want to open a file for writing only, use 'w'. If you want to open 
it for both writing and reading, use 'w+'. Just keep in mind the behavior of truncating the file's content when opening in write modes.

'''
'''
CSV stands for "Comma-Separated Values." It's a simple and widely used file format for 
storing tabular data (numbers and text) in a plain-text form. Each line of the file represents 
a row of data, and the values in each row are separated by commas (or other specified delimiters).

CSV files are often used to store structured data that can be easily imported and exported between 
different software applications and systems. They are commonly used for tasks like data exchange
between databases, spreadsheet applications, and statistical analysis tools.

Here's an example of how CSV data looks:

Name,Age,Location
John,28,New York
Jane,32,Los Angeles
Michael,24,Chicago
In this example, the first row contains the column headers (Name, Age, Location), and 
subsequent rows contain the corresponding values for each column.

Python provides built-in modules (csv) to work with CSV files, allowing you to 
read and write data easily in this format.

'''
'''
import csv
field_names = ['name', 'age']
data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]
with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)

import csv
with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))
        
'''     
'''
Exercise 5.2: This program is supposed to read data about trees from a
file to find the shortest tree.
Complete the program adding code to open trees.csv .
The trees.csv file included with your student guides. Save the csv
file in the same folder as your
'''

import csv

'''
csv_content = """species,height
oak,100
pine,80
maple,90
willow,70
"""

with open('trees.csv', 'w') as csv_file:
    csv_file.write(csv_content)

print("File 'trees.csv' created successfully.")
'''
# Open the trees.csv file for reading
with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    
    heights = []
    
    # Iterate through each row in the CSV file
    for row in spreadsheet:
        tree_height = float(row['height'])  # Convert the height to a float
        heights.append(tree_height)
    
    # Find the shortest tree height
    shortest_height = min(heights)
    
    print("Shortest tree height:", shortest_height)

'''
The PokéAPI is an online service that provides a comprehensive and structured collection of 
data related to Pokémon, which are fictional creatures from the popular Pokémon franchise. 
The API offers a wide range of information about Pokémon species, abilities, moves, types, 
evolutions, and more. It's a valuable resource for developers, enthusiasts, and researchers 
who want to access and utilize Pokémon-related data in various applications.

Key features of the PokéAPI include:

Pokémon Information: The API offers detailed information about each Pokémon species, including their names,
types, abilities, base stats, and more. This data can be used to create comprehensive Pokédex applications, 
educational tools, or fan websites.

Moves and Abilities: The API provides information about various moves 
that Pokémon can learn and the effects of those moves. It also includes details 
about abilities that Pokémon can possess, enhancing the depth of Pokémon battle simulations 
or strategy guides.

Evolution Chains: The API offers data on the evolutionary relationships between different Pokémon species. 
This information is crucial for building evolution trees and understanding how Pokémon evolve from one species 
to another.

Type Chart: The API includes a type chart that defines the strengths and weaknesses 
of different Pokémon types in battles. This data is useful for creating battle simulators or 
strategy guides.

Images and Sprites: The API provides image URLs for Pokémon sprites, which can be used 
to display images of Pokémon in various applications.

Possible use cases for the PokéAPI include:

Pokédex Applications: Developers can create digital Pokédex applications that allow users to 
search and browse information about different Pokémon species.

Gaming Tools: Gamers and developers can use the API to create tools for analyzing and strategizing 
Pokémon battles, taking advantage of type matchups and move effects.

Educational Resources: The API can be used to build educational resources for learning about Pokémon,
their abilities, and the mechanics of the Pokémon games.

Fan Websites and Apps: Enthusiasts can build fan websites, apps, or communities that 
showcase Pokémon data, artwork, and lore.

Research and Analysis: Researchers interested in the Pokémon franchise can use 
the API to gather data for analysis and studies related to game mechanics, evolution patterns, 
and more.

Overall, the PokéAPI serves as a centralized source of Pokémon-related data, enabling 
developers and fans to access and utilize information about these beloved creatures in 
creative and informative ways.





'''