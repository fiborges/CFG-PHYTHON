'''
Question 1 
You're having coffee/tea/beverage of your choice with a friend that is learning to program in Python.
They're curious about why they would use pip. 
Explain what pip is and one benefit of using pip. 


Answer 1

Imagine pip as a "delivery service" for Python. When you're working on a 
programming project, you might need additional tools or libraries to help you 
accomplish specific tasks, like making HTTP requests or working with data in a 
more efficient way.

Here's where pip comes in. It's a package manager for Python that allows you to easily 
search for, install, and manage these additional tools, which we call "packages" or "libraries.
" Instead of spending time hunting down the right code from various sources, you can use pip to
quickly find the right packages, download them, and integrate them into your project.

One key benefit of using pip is efficiency and time-saving. Let's say you're building a web scraping
application to extract information from websites. Instead of coding everything from scratch, you can 
use a library like requests to simplify the HTTP requests process. With pip, you just need to run a 
simple command like pip install requests, and the library will be automatically downloaded and installed. 
This saves you from reinventing the wheel and speeds up your development process significantly.

So, in a nutshell, pip is your go-to tool for effortlessly expanding the capabilities of Python
by adding pre-built functionality from other developers. It's like having a vast collection of tools 
at your disposal that you can easily integrate into your own projects, making your coding journey 
smoother and more efficient.

'''

'''
Question 2 
This program should save my data to a file, but it doesn't work when I run it. What is the problem and how do I fix it? 
poem = 'I like Python and I am not very good at poems' 
with open('poem.txt', 'r') as poem_file: 
poem_file.write(poem) 
'''

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)


'''
answer 2:

The issue here is that you're trying to open the file in read mode ('r'), which means you can only read from the file and 
not write to it. If you want to write data to the file, you need to open it in write mode ('w').
In this corrected code, the open function is used with 'w' mode, which allows you to write data to the file. The existing 
contents of the file (if any) will be overwritten with the new content provided in the poem variable.
'''

'''
In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can retrieve multiple 
Pokemon and save their names and moves to a file. 
Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each Pokemon. 
Save their names and moves into a file called 'pokemon.txt'

'''

# pip install requests

# import requests

# List of Pokémon IDs
pokemon_ids = [1, 2, 3, 4, 5, 6]

# Function to fetch data for a Pokémon and save to file
def fetch_and_save_pokemon_data(pokemon_id, file):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        moves = [move['move']['name'] for move in data['moves']]
        file.write(f"Name: {name}\n")
        file.write(f"Moves: {', '.join(moves)}\n\n")
    else:
        print(f"Error fetching data for Pokémon with ID {pokemon_id}")

# Open 'pokemon.txt' file for writing
with open('pokemon.txt', 'w') as pokemon_file:
    for pokemon_id in pokemon_ids:
        fetch_and_save_pokemon_data(pokemon_id, pokemon_file)

print("Pokémon data saved to 'pokemon.txt'")

# This program fetches data for each Pokémon ID in the pokemon_ids list, extracts their names and moves, and then writes this information to the 'pokemon.txt' file.






