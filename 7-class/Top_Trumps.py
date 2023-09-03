import random
import csv
import time
from opening import display_ascii_art, magical_welcome, print_centered
from utils2 import calculate_total_power, calculate_total_intelligence, calculate_total_courage, display_spell_options, duel_spell
from utils1 import load_spells_from_csv, load_characters_from_csv, House, Spell
from grafic import show_result

def main():
    blue = "\033[94m"
    blue_B = "\033[1;94m"
    Red = "\033[1;31m"
    pink = "\033[95m"
    pink_B = "\033[1;95m"
    green = "\033[92m"
    green_B = "\033[1;92m"
    yellow = "\033[93m"
    yellow_B = "\033[1;93m"
    Cyan = "\033[1;36m"
    reset = "\033[0m"
    
    welcome =f"\n{green}Welcome to the Hogwarts Houses Challenge!{reset}"
    print_centered(welcome)

    display_ascii_art()
    
    magical_welcome()

    houses = {
        "Gryffindor": House("Gryffindor", []),
        "Slytherin": House("Slytherin", []),
        "Ravenclaw": House("Ravenclaw", []),
        "Hufflepuff": House("Hufflepuff", [])
    }

    spells = load_spells_from_csv('harry_potter_spells.csv')
    characters = load_characters_from_csv('harry_potter_characters.csv')

    # Define house-specific attributes
    house_power = {
        "Gryffindor": 10,
        "Slytherin": 8,
        "Ravenclaw": 7,
        "Hufflepuff": 6
    }

    house_intelligence = {
        "Gryffindor": 7,
        "Slytherin": 8,
        "Ravenclaw": 10,
        "Hufflepuff": 6
    }

    house_courage = {
        "Gryffindor": 10,
        "Slytherin": 8,
        "Ravenclaw": 7,
        "Hufflepuff": 9
    }
    
    # Sorting Hat's decision
    selected_house = random.choice(list(houses.keys()))
    player_house = selected_house
    Sorting =f"\n{Cyan}The Sorting Hat is deciding your fate...{reset}"
    print_centered(Sorting)
    time.sleep(2)
    decide =f"\n{Cyan}The Sorting Hat has decided... You will be placed in the house of... {reset}"
    result =f"\n{green_B}{selected_house.upper()}!{reset}"
    print_centered(decide)
    print_centered(result)
    time.sleep(2)
    
    num_rounds = int(input("\nHow many rounds do you want to play? Enter a number: ").upper())

    # Add a pause before starting the game
    input(f"\n{yellow}Press Enter to continue...{reset}")

    for character in characters:
        house = houses[character['house']]
        house.characters.append(character)

    points = {house.name: 0 for house in houses.values()}

    starting_house = random.choice(list(houses.values()))
    current_house = starting_house

    for round_num in range(1, num_rounds + 1):
        Round = f"\n{blue_B}Round {round_num}:{reset}"
        print_centered(Round)

        player_character = current_house.get_random_character()
        opponent_house = random.choice(list(houses.values()))
        opponent_character = opponent_house.get_random_character()

        Player_name =f"\n{pink_B}Your character is: {reset}"
        name=f"\n{green_B}{player_character['name'].upper()}{reset}"
        print_centered(Player_name)
        print_centered(name)
        
        Opponent_name =f"\n{pink_B}Your opponent's character is: {reset}"
        name_o =f"\n{green_B}{opponent_character['name'].upper()}{reset}"
        print_centered(Opponent_name)
        print_centered(name_o)
        
        time.sleep(2)

        quote_P = f"\n{Cyan}You are challenging your opponent in a battle of Power..."
        quote_same = (f"Who will emerge victorious?{reset}")
        print_centered(quote_P)
        print_centered(quote_same)
        # Pause to create suspense
        for _ in range(2):
            print(".", end="", flush=True)
            time.sleep(2)
        print("\n")
        
        # Challenge 1: Power
        player_power = calculate_total_power(player_character, house_power)
        opponent_power = calculate_total_power(opponent_character, house_power)
        if player_power > opponent_power:
            victory = f"{green}You won the Power challenge for the{reset}"
            house_name = f"\n{green_B}{current_house.name.upper()}{reset}"
            print_centered(victory)
            print_centered(house_name)
            points[current_house.name] += 1
        elif player_power < opponent_power:
            defeat = f"{Red}The opponent won the Power challenge for the{reset}"
            defeat_house = f"\n{Red}{opponent_house.name.upper()}{reset}"
            print_centered(defeat)
            print_centered(defeat_house)
            points[opponent_house.name] += 1
        else:
            Tie = f"\n{yellow}The Power challenge is a tie!{reset}"
            print_centered(Tie)
            
                 
        input(f"\n{yellow}Press Enter to continue...{reset}")
            
        quote_P1 = f"\n{Cyan}You are challenging your opponent in a battle of Inteligence..."
        print_centered(quote_P1)
        print_centered(quote_same)
        # Pause to create suspense
        for _ in range(2):
            print(".", end="", flush=True)
            time.sleep(2)
        print("\n")

        # Challenge 2: Intelligence
        player_intelligence = calculate_total_intelligence(player_character, house_intelligence)
        opponent_intelligence = calculate_total_intelligence(opponent_character, house_intelligence)
        if player_intelligence > opponent_intelligence:
            victory1 = f"{green}You won the Inteligence challenge for the{reset}"
            house_name1 = f"\n{green_B}{current_house.name.upper()}{reset}"
            print_centered(victory1)
            print_centered(house_name1)
            points[current_house.name] += 1
        elif player_intelligence < opponent_intelligence:
            defeat1 = f"{Red}The opponent won the Inteligence challenge for the{reset}"
            defeat_house1 = f"\n{Red}{opponent_house.name.upper()}{reset}"
            print_centered(defeat1)
            print_centered(defeat_house1)
            points[opponent_house.name] += 1
        else:
            Tie1 = f"\n{yellow}The Inteligence challenge is a tie!{reset}"
            print_centered(Tie1)
            
        input(f"\n{yellow}Press Enter to continue...{reset}")

        quote_P2 = f"\n{Cyan}You are challenging your opponent in a battle of Courage..."
        print_centered(quote_P2)
        print_centered(quote_same)
        # Pause to create suspense
       
        time.sleep(2)
        print("\n")
        
        # Challenge 3: Courage
        player_courage = calculate_total_courage(player_character, house_courage)
        opponent_courage = calculate_total_courage(opponent_character, house_courage)
        if player_courage > opponent_courage:
            victory2 = f"{green}You won the Courage challenge for the{reset}"
            house_name2 = f"\n{green_B}{current_house.name.upper()}{reset}"
            print_centered(victory2)
            print_centered(house_name2)
            points[current_house.name] += 1
        elif player_courage < opponent_courage:
            defeat2 = f"{Red}The opponent won the Courage challenge for the{reset}"
            defeat_house2 = f"\n{Red}{opponent_house.name.upper()}{reset}"
            print_centered(defeat2)
            print_centered(defeat_house2)
            points[opponent_house.name] += 1
        else:
            Tie2 = f"\n{yellow}The Courage challenge is a tie!{reset}"
            print_centered(Tie2)
            
        input(f"\n{yellow}Press Enter to continue...{reset}")

        final_speach =f"\n{Cyan}We've reached the final challenge!!!!"
        final2 = f"{Cyan}You will choose a spell with great care and wisdom!!!{reset}"
        final3 = f"\n{blue_B}May the odds be in your favor.{reset}"
        print_centered(final_speach)
        print_centered(final2)
        print_centered(final3)
        # Pause to create suspense
        for _ in range(2):
            print(".", end="", flush=True)
            time.sleep(2)
        print("\n")
        # Challenge 4: Spell
    if round_num <= num_rounds:
        random_spells = random.sample(spells, 10)
    else:
        random_spells = spells

    print(f"{pink}Choose a spell: {reset}\n")
    for i, spell in enumerate(random_spells, start=1):
        print(f"{blue}{i}.{reset} {spell.name}")

    spell_choice = int(input("Enter the number of your chosen spell: ")) - 1
    player_spell = random_spells[spell_choice]
    

    winner = max(points, key=points.get)
    if player_house == winner:
        result_game = "WINNER"
    else:
        result_game = "LOSER"
    print("\n")
    
    winning = f"{blue_B}The winning house is: {reset}"
    winning_house = f"{green}{winner.upper()}!{reset}"
    print_centered(winning)
    print_centered(winning_house)
    time.sleep(2)
    
    victory_messages = {
    "Gryffindor": "Congratulations, brave Gryffindor members, you are the winners!",
    "Slytherin": "The Slytherins have shown their cunning and triumphed!",
    "Ravenclaw": "The Ravenclaws have used their intelligence for victory!",
    "Hufflepuff": "Hufflepuff, you are loyal and have achieved victory!"
}
    if winner in victory_messages:
        print(victory_messages[winner])
    else:
        print("Unfortunately, victory narrowly escaped. Don't give up!")
    
    show_result(result_game)

    
if __name__ == "__main__":
    main()
    while True:
        play_again = input("\033[1;92mWant to play again? (y/n): \033[0m").lower()
        if play_again != 'y':
            break
        main()
