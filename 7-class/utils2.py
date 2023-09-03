import random
import csv
import time

def calculate_total_power(character, house_power):
    # Calculate total power of a character based on their base power and house power (if applicable)
    total_power = int(character['power'])
    if character['house'] in house_power:
        total_power += house_power[character['house']]
    return total_power

def calculate_total_intelligence(character, house_intelligence):
    # Calculate total intelligence of a character based on their house
    return house_intelligence.get(character['house'], 0)

def calculate_total_courage(character, house_courage):
    # Calculate total courage of a character based on their house
    return house_courage.get(character['house'], 0)

def display_spell_options(spells):
    # Display available spells and their power levels
    for i, spell in enumerate(spells, start=1):
        print(f"{i}. {spell.name}")


def duel_spell(player_house, computer_house, spells, house_power, house_intelligence, house_courage):
    # Simulate a duel between player and computer using random spells
    player_spell = random.choice(spells)
    computer_spell = random.choice(spells)

    player_power = player_spell.power + house_power[player_house.name]
    computer_power = computer_spell.power + house_power[computer_house.name]

    player_intelligence = house_intelligence[player_house.name]
    computer_intelligence = house_intelligence[computer_house.name]

    player_courage = house_courage[player_house.name]
    computer_courage = house_courage[computer_house.name]

    # Resto do código para determinar o vencedor com base no poder, inteligência e coragem
    if player_power > computer_power:
        return True
    elif player_power < computer_power:
        return False
    else:
        return None