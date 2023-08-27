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
    print("Congratulations! You Win!\n")
    print("      \\o/")
    print("       |")
    print("      / \\")

def animate_lose():
    print("Oops! You Lose!\n")
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
    print("Welcome to the Pokemon Top Trumps Game!\n")
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
    total_rounds = int(input("How many rounds do you want to play? "))
    player_score = 0
    opponent_score = 0

    for round_num in range(1, total_rounds + 1):
        print(f"\nRound {round_num} of {total_rounds}")

        my_pokemon = random_pokemon()
        print('You were given {}'.format(my_pokemon['name']))
        stat_choice = input('Which stat do you want to use? (id, height, weight) ')
        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))

        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]

        print(f'Your {stat_choice}: {my_stat}')
        print(f'Opponent\'s {stat_choice}: {opponent_stat}')

        if my_stat > opponent_stat:
            player_score += 1
            animate_win()
        elif my_stat < opponent_stat:
            opponent_score += 1
            animate_lose()
        else:
            print('It\'s a Draw this round!')

    print("\nGame Over!")
    print(f"Your Score: {player_score}")
    print(f"Opponent's Score: {opponent_score}")

run()


