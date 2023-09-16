import random
import csv
import time
from opening import display_ascii_art, magical_welcome, print_centered, sorting_hat_ascii
from utils2 import play_power_game , play_item_correspondence_game, print_stars, courage_challenge
from utils1 import load_spells_from_csv, load_characters_from_csv, House, Spell
from grafic import show_result
from API_to_CSV import collect_character_data, create_character_csv, collect_spell_data, create_spell_csv

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
    
    create_character_csv()
    create_spell_csv()
    
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
    
    available_houses = list(houses.keys())
    
    player_house = random.choice(available_houses)
    available_houses.remove(player_house)
    opponent_house0 = random.choice(available_houses)
    current_house = houses[player_house]
    opponent_house = houses[opponent_house0]

    sorting_hat_ascii()
    Sorting =f"\n{Cyan}The Sorting Hat is deciding your fate...{reset}"
    print_centered(Sorting)
    time.sleep(2)
    decide =f"\n{Cyan}The Sorting Hat has decided... You will be placed in the house of... {reset}"
    result =f"\n{green_B}{player_house.upper()}!{reset}"
    print_centered(decide)
    for _ in range(2):
        print(".", end="", flush=True)
        time.sleep(2)
    print("\n")
    print_centered(result)
    time.sleep(2)
    
    num_rounds = int(input("\nHow many rounds do you want to play? Enter a number: ").upper())

    # Add a pause before starting the game
    input(f"\n{yellow}Press Enter to continue...{reset}")

    for character in characters:
        house = houses[character['house']]
        house.characters.append(character)

    points = {house.name: 0 for house in houses.values()}
    print("Initial Points:")
    print(points)

    for round_num in range(1, num_rounds + 1):
        Round = f"\n{blue_B}Round {round_num}:{reset}"
        print_centered(Round)

        player_character = current_house.get_random_character()
        opponent_character = opponent_house.get_random_character()

        Player_name =f"\n{pink_B}Your character is: {reset}"
        name_user=f"\n{green_B}{player_character['name'].upper()}{reset}"
        print_centered(Player_name)
        print_centered(name_user)
        houseuser = f"\n{green_B}{current_house.name.upper()}{reset}"
        print_centered(houseuser)
        
        Opponent_name7 =f"\n{pink_B}Your opponent's character is: {reset}"
        name_o =f"\n{green_B}{opponent_character['name'].upper()}{reset}"
        print_centered(Opponent_name7)
        print_centered(name_o)
        opponent_house9 = f"\n{green_B}{opponent_house.name.upper()}{reset}"
        print_centered(opponent_house9)
        
        time.sleep(2)
    
        # Challenge 1: Power
        print("Points before power:")
        print(points)
        
        quote_P = f"\n{Cyan}You are challenging your opponent in a battle of Power...\n"
        quote_same = (f"Who will emerge victorious?{reset}")
        print_stars(quote_P)
        print_centered(quote_same)
        # Pause to create suspense
        for _ in range(2):
            print(".", end="", flush=True)
            time.sleep(2)
        print("\n")
        
        player_power, oponent_power = play_power_game()
        print("Player power: ", player_power)
        print("Oponent power: ", oponent_power)
        
        
        if player_power > oponent_power:
            print_centered(f"{green_B}{player_character['name'].upper()}{reset}")
            print_centered(f"{green_B}{current_house.name.upper()}{reset}")
            points[current_house.name] += 1
        elif player_power < oponent_power:
            print_centered(f"{Red}{opponent_character['name'].upper()}{reset}")
            print_centered(f"{Red}{opponent_house.name.upper()}{reset}")
            points[opponent_house.name] += 1
        elif(player_power == oponent_power):
            print_centered(f"{yellow}It's a tie!{reset}")
            points[current_house.name] += 1
            points[opponent_house.name] += 1
        
        input(f"\n{yellow}Press Enter to continue...{reset}")
        
        # Challenge 2: Intelligence
            
        print("Points before inteligence:")
        print(points)
        quote_P1 = f"\n{Cyan}You are challenging your opponent in a battle of Inteligence...\n"
        print_stars(quote_P1)
        print_centered(quote_same)
        
        # Pause to create suspense
        for _ in range(2):
            print(".", end="", flush=True)
            time.sleep(2)
        print("\n")

        player_intelligence = play_item_correspondence_game()
        if player_intelligence:
            print_centered(f"{green_B}{player_character['name'].upper()}{reset}")
            print_centered(f"{green_B}{current_house.name.upper()}{reset}")
            points[current_house.name] += 1
        else:
            print_centered(f"{Red}{opponent_character['name'].upper()}{reset}")
            print_centered(f"{Red}{opponent_house.name.upper()}{reset}")
            points[opponent_house.name] += 1
    
        input(f"\n{yellow}Press Enter to continue...{reset}")
        
        # Challenge 3: courage

        print("Points before courage:")
        print(points)
        
        quote_P2 = f"\n{Cyan}You are challenging your opponent in a battle of Courage...\n"
        print_stars(quote_P2)
        print_centered(quote_same)
       
        time.sleep(2)
        print("\n")
        
        player_courage = courage_challenge()
        if player_courage:
            print_centered(f"{green_B}{player_character['name'].upper()}{reset}")
            print_centered(f"{green_B}{current_house.name.upper()}{reset}")
            points[current_house.name] += 1
        else:
            print_centered(f"{Red}{opponent_character['name'].upper()}{reset}")
            print_centered(f"{Red}{opponent_house.name.upper()}{reset}")
            points[opponent_house.name] += 1
    
        input(f"\n{yellow}Press Enter to continue...{reset}")

        quote_P2 = f"\n{Cyan}You are challenging your opponent in a duel...\n"
        print_stars(quote_P2)
     
        time.sleep(2)
        
        input(f"\n{yellow}Press Enter to continue...{reset}")
        
        # Challenge 4: Spell
        print("Points before spell:")
        print(points)
        
        final_speach =f"\n{Cyan}We've reached the final challenge!!!!"
        final2 = f"{Cyan}You will choose a spell with great care and wisdom!!!{reset}"
        final3 = f"\n{blue_B}May the odds be in your favor.{reset}"
        print_centered(final_speach)
        time.sleep(2)
        print_centered(final2)
        time.sleep(2)
        print_centered(final3)
        # Pause to create suspense
        for _ in range(2):
            print(".", end="", flush=True)
            time.sleep(2)
        print("\n")
        
        print(f"{Cyan}Choose a spell to cast (Enter the number of the spell): {reset}\n")
        for i, spell in enumerate(spells[:10], start=1):
            print(f"{green}{i}.{reset} {spell.name}")

        # Peça ao usuário para escolher um feitiço
        user_choice = int(input(f"\n{Cyan}Enter the number of the spell you want to cast: {reset}\n")) - 1

        # Verifique se a escolha do usuário é válida
        if user_choice < 0 or user_choice >= len(spells[:10]):
            print_centered(f"{Red}Invalid choice. You failed to cast a spell.{reset}\n")
        else:
            # O computador escolhe um feitiço aleatório
            computer_spell = random.choice(spells)

            # Exibe os feitiços escolhidos
            print_centered(f"{blue}You cast {blue_B}{spells[user_choice].name}.{reset}\n")
            print_centered(f"{blue}The computer casts {blue_B}{computer_spell.name}.{reset}\n")

            # Determine o vencedor com base nos poderes dos feitiços
            if spells[user_choice].power > computer_spell.power:
                print_centered(f"{green_B}You win the spell duel!{reset}\n")
                points[current_house.name] += 1
            elif spells[user_choice].power < computer_spell.power:
                print_centered(f"{Red}You lose the spell duel!{reset}\n")
                points[opponent_house.name] += 1
            else:
                print_centered(f"{yellow}It's a draw! The spell duel ends in a tie.{reset}\n")

        input(f"\n{yellow}Press Enter to continue...{reset}")
   
    
    print("Points after spell:")
    print(points)
    
    
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
    while True:
        main()
        play_again = input("\033[1;92mWant to play again? (y/n): \033[0m").lower()
        if play_again != 'y':
            break
