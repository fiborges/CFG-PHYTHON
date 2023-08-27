import random
import requests
import time

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

def animate_win():
    print("\033[96mCongratulations! You Win!\033[0m\n")
    print("      \\o/")
    print("       |")
    print("      / \\")

def animate_lose():
    print("\033[91mOops! You Lose!\033[0m\n")
    print("    ______________")
    print("   /              \\")
    print("  /  X         X   \\")
    print(" |      /\\      /\\   |")
    print("  \\_____|  |____|  /")
    print("        \\__/")
    print("        /  \\")
    print("       /_/\\_\\")
    print("       \\____/")

def welcome_animation():
    print("\033[96mWelcome to the Pokemon Top Trumps Game!\033[0m\n")
    print("                                                     ")
    print("                 .\"-,.__")
    print("                 `.     `.  ,")
    print("              .--'  .._,'\"-' `.")
    print("             .    .'         `'") 
    print("             `.   /          ,'")
    print("               `  '--.   ,-\"'")
    print("                `\"`   |  \\")
    print("                   -. \\, |")
    print("                    `--Y.'      ___.")
    print("                         \\     L._, \\")
    print("               _.,        `.   <  <\\                _")
    print("             ,' '           `, `.   | \\            ( `")
    print("          ../, `.            `  |    .\\`.           \\ \\_")
    print("         ,' ,..  .           _.,'    ||\\l            )  '\".")
    print("        , ,'   \\           ,'.-.`-._,'  |           .  _._`.")
    print("      ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\")
    print("    .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.")
    print("    |  '          ..         `-...-\"  |  `-'      / /        . `.")
    print("    | /           |L__           |    |          / /          `. `.")
    print("   , /            .   .          |    |         / /             ` `")
    print("  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\")
    print(" / .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.")
    print(".  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\")
    print("' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`")
    print("|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\")
    print("||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|")
    print("||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||")
    print("|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||")
    print("||/            _,-------7 '              . |  `-'    l         /    `||")
    print(". |          ,' .-   ,' ||               | .-.        `.      .'     ||")
    print(" `'        ,'    `\".'    |               |    `.        '. -.'       `'")
    print("          /      ,'      |               |,'    \\-.._,.'/")
    print("          .     /        .               .       \\    .''.")
    print("        .`.    |         `.             /         :_,'.'")
    print("          \\ `...\\   _     ,'-.        .'         /_.-'")
    print("           `-.__ `,  `'   .  _.>----''.  _  __  /")
    print("                .'        /\"'          |  \"'   '_")
    print("               /_|.-'\\ ,\".             '.'`__'-( \\")
    print("                 / ,\"'\"\\,'               `/  `-.|\" mh\n")
    time.sleep(2)

def run():
    welcome_animation()
    total_rounds = int(input("\033[95mHow many rounds do you want to play? \033[0m"))
    player_score = 0
    opponent_score = 0

    for round_num in range(1, total_rounds + 1):
        print(f"\n\033[93mRound {round_num} of {total_rounds}\033[0m")

        my_pokemon = random_pokemon()
        print('\033[1;94mYou were given\033[0m \033[1;4m\033[92m{}\033[0m'.format(my_pokemon['name']))

        print('Select a statistic:')
        print('1 - id')
        print('2 - height')
        print('3 - weight')
        stat_choice = input('\033[95mEnter the number of the stat you want to use: \033[0m')

        if stat_choice == '1':
            stat_name = 'id'
        elif stat_choice == '2':
            stat_name = 'height'
        elif stat_choice == '3':
            stat_name = 'weight'
        else:
            print('Invalid choice. Skipping round.')
            continue

        opponent_pokemon = random_pokemon()
        print('\033[94mThe opponent chose \033[0m\033[1;4m\033[92m{}\033[0m'.format(opponent_pokemon['name']))

        my_stat = my_pokemon[stat_name]
        opponent_stat = opponent_pokemon[stat_name]

        print(f'Your {stat_name}: \033[92m{my_stat}\033[0m')
        print(f'Opponent\'s {stat_name}: \033[92m{opponent_stat}\033[0m')

        if my_stat > opponent_stat:
            player_score += 1
            animate_win()
        elif my_stat < opponent_stat:
            opponent_score += 1
            animate_lose()
        else:
            print('\033[94mIt\'s a Draw this round!\033[0m')

    print("\n\033[95mGame Over!\033[0m")
    print(f"Your Score: \033[92m{player_score}\033[0m")
    print(f"Opponent's Score: \033[91m{opponent_score}\033[0m")

run()


