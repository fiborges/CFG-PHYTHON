import random
import csv
import time
from opening import print_centered
    
def print_stars(message):
    # Function to print messages centered on the screen
    print_centered(f"\n\033[95m{' <3 ' * 20}\033[0m")
    print("\n")
    print_centered(f"{message.center(100)}")
    print_centered(f"{'.' * 70}\n")

def play_power_game():
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
    # Initialize player and computer scores
    player_score = 0
    computer_score = 0

    print_centered(f"{blue_B}Power is only useful when used wisely. Use the right potion to beat your opponent.{reset}\n")
    print_centered(f"Strength {yellow}beats{reset} Foresight, \nForesight {Cyan}beats{reset} Invisibility, \nInvisibility {green}beats{reset} Strength.\n")

    for round_number in range(1, 4):  # Agora sempre jogará 3 rodadas
        # Define the list of magical potions with descriptions
        potion_list = [
            {'name': 'Strength Potion', 'description': 'A shimmering elixir that enhances your might.'},
            {'name': 'Invisibility Potion', 'description': 'A potion that renders you invisible to the naked eye.'},
            {'name': 'Mopsus Foresight Potion', 'description': 'A mystical brew that grants glimpses into the future.'}
        ]

        print_centered(f"{Cyan}Round {round_number}:{reset}")
        print_centered(f"{pink_B}Let's see who is stronger...{reset}\n")
        time.sleep(3)  # Pause for suspense

        # Display the potion choices
        if round_number == 1:
            print_centered(f"{blue_B}Choose your potion wisely: {reset}")
            for i, potion in enumerate(potion_list, 1):
                print_centered(f"{green_B}{i}.{reset} {yellow}{potion['name']} - {reset}{potion['description']}")
            print("\n")
        else:
            print_centered(f"{blue_B}Choose your potion wisely: {reset}")
            for i, potion in enumerate(potion_list, 1):
                print(f"{green_B}{i}.{reset} {yellow}{potion['name']}{reset}")
            print("\n")

        # Player's choice with input validation
        while True:
            try:
                player_choice = int(input(f"{Cyan}Enter the number of your chosen potion: {reset}")) 
                if 1 <= player_choice <= 3:
                    break
                else:
                    print_centered(f"{Red}Invalid choice. Please enter a number between 1 and 3.{reset}")
            except ValueError:
                print_centered(f"{Red}Invalid input. Please enter a number.{reset}")

        player_potion = potion_list[player_choice - 1]

        # Simulate computer's choice with suspense
        print_centered(f"\n{yellow_B}Your opponent is choosing a potion...{reset}\n")
        time.sleep(2)  # Pause for suspense

        computer_potion = random.choice(potion_list)

        print_centered(f"Your opponent chose {Red}{computer_potion['name']}. {reset}\n")

        # Determine the round outcome
        if player_potion['name'] == computer_potion['name']:
            print_centered(f"{yellow} It's a tie! {reset}\n")
            player_score += 1
            computer_score += 1

        elif (
            (player_potion['name'] == 'Strength Potion' and computer_potion['name'] == 'Invisibility Potion') or
            (player_potion['name'] == 'Invisibility Potion' and computer_potion['name'] == 'Mopsus Foresight Potion') or
            (player_potion['name'] == 'Mopsus Foresight Potion' and computer_potion['name'] == 'Strength Potion')
        ):
            print_centered(f"{green_B}You won the round! {reset}\n")
            player_score += 1

        else:
            print_centered(f"{Red}You lost the round.{reset}\n")
            computer_score += 1

        print_centered(f"{Cyan}Score: {reset} Player: {player_score}  Oponent: {computer_score}\n")

    return player_score, computer_score

#inteligence game
def play_item_correspondence_game():
    blue = "\033[94m"
    pink = "\033[95m"
    green_B = "\033[1;92m"
    yellow = "\033[93m"
    Cyan = "\033[1;36m"
    Red = "\033[1;31m"
    reset = "\033[0m"
    
    # Define the lists of items and corresponding items
    item_list = ['mandrake', 'dragon', 'gillyweed', 'Marauder`s Map', 'Elder Wand', 'Fluffy']
    corresponding_items_list = ['earmuffs', 'hidegloves', 'grindylow', 'I solemnly swear that I am up to no good', 'Deathly Hallows', 'Play Music']

    # Initialize player and computer scores
    player_score = 0
    computer_score = 0

    # Randomly select an item from item_list
    chosen_item = random.choice(item_list)

    # Display the chosen item to the player
    Item = f"{pink}The chosen item is: {reset}\n{green_B}{chosen_item}\n{reset}"
    print_centered(Item)

    # Prompt the player for their choice
    print("Choose the corresponding item:")
    for i, item in enumerate(corresponding_items_list, 1):
        print(f"{blue}{i}.{reset} {item}")

    # Get the player's choice
    print("\n")
    player_choice = int(input(f"{Cyan}Enter the number of your choice: {reset}")) - 1

    if player_choice < 0 or player_choice >= len(corresponding_items_list):
        erro = f"{Red}Invalid choice.{reset}"
        print_centered(erro)
        
    else:  
        # Check if player_choice matches the corresponding item
        if (
            (chosen_item == 'mandrake' and player_choice == 0) or
            (chosen_item == 'dragon' and player_choice == 1) or
            (chosen_item == 'gillyweed' and player_choice == 2) or
            (chosen_item == 'Marauder`s Map' and player_choice == 3) or
            (chosen_item == 'Elder Wand' and player_choice == 4) or
            (chosen_item == 'Fluffy' and player_choice == 5)
        ):
            player_score += 1
            win = f"{green_B}You win this round!{reset}"
            print_centered(win)
            return True
        else:
            computer_score += 1
            lose = f"{Red}You lost this round.{reset}"
            print_centered(lose)
            return False
            

    
def courage_challenge():
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
    
    # Define the lists of items and corresponding items
    Itens_creatures = ['Phoenix', 'Hippogriff', 'Basilisk', 'Dementor']
    corresponding_items_list = ['Approach the creature cautiously.', 'Make a bow to calm the creature.', 'Cast a spell and run away from the creature.', 'Retreat, DONT LOOK!! and call for help.']
    
    player_score = 0
    computer_score = 0
    
    chosen_creature = random.choice(Itens_creatures)
    
    print_centered(f"{Cyan}You find yourself deep in the Hogwarts Forbidden Forest.{reset}\n")
    
    creature = f"{Cyan}Suddenly, you come across {reset}\n{green_B}{chosen_creature}\n{reset}"
    print_centered(creature)
    

    time.sleep(3)
    # Present choices to the player
    print("Choose the corresponding Aproach:")
    for i, item in enumerate(corresponding_items_list, 1):
        print(f"{blue}{i}.{reset} {item}")
    print("\n")

    player_choice = int(input(f"{Cyan}Enter the number of your choice: {reset}")) - 1
    # Get the player's choice

    if player_choice < 0 or player_choice >= len(corresponding_items_list):
        erro = f"{Red}Invalid choice.{reset}"
        print_centered(erro)
        
    else:  
        # Check if player_choice matches the corresponding item
        if (
            (chosen_creature == 'Phoenix' and player_choice == 0) or
            (chosen_creature == 'Hippogriff' and player_choice == 1) or
            (chosen_creature == 'Dementor' and player_choice == 2) or
            (chosen_creature == 'Basilisk' and player_choice == 3)
        ):
            player_score += 1
            win = f"{green_B}You win this round!{reset}"
            print_centered(win)
            return True
        else:
            computer_score += 1
            lose = f"{Red}You lost this round.{reset}"
            print_centered(lose)
            return False

