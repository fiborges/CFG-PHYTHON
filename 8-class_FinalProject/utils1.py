import random
import csv
import time

class Spell:
    def __init__(self, name, description, power):
        self.name = name
        self.description = description
        self.power = power

class House:
    def __init__(self, name, characters):
        self.name = name
        self.characters = characters

    def get_random_character(self):
        return random.choice(self.characters)

def load_spells_from_csv(filename):
    spells = []

    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['Name']
                description = row['Description']
                power = int(row['Rank'])
                spell = Spell(name, description, power)
                spells.append(spell)
    except FileNotFoundError:
        print(f"O arquivo CSV '{filename}' não foi encontrado.")

    return spells

def load_characters_from_csv(filename):
    characters = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                species = row.get('Species', '')  # Use .get() to handle missing keys
                house = row.get('House', '')
                power = row.get('Power', '')

                # Check if the 'House' field is valid
                if house not in ('Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff'):
                    print(f"Invalid house '{house}' for character '{name}'. Skipping.")
                    continue

                character = {'name': name, 'species': species, 'house': house, 'power': power}
                characters.append(character)
    except FileNotFoundError:
        print(f"O arquivo CSV '{filename}' não foi encontrado.")
    return characters
