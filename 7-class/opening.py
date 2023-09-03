import random
import csv
import time
import shutil
import re

def print_centered(text):
    # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns

    # Split the text into lines
    lines = text.split('\n')

    for line in lines:
        # Regular expression to match ANSI escape codes
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

        # Remove ANSI escape codes and calculate text width
        text_without_ansi = ansi_escape.sub('', line)
        text_width = len(text_without_ansi)

        # Calculate left margin for centering
        left_margin = (terminal_width - text_width) // 2

        # Print spaces with the same escape codes as text
        spaces = f"\033[0m{' ' * left_margin}"
        print(f"{spaces}{line}")


def magical_welcome():
    blue = "\033[94m"
    pink = "\033[95m"
    green = "\033[92m"
    yellow = "\033[93m"
    Cyan = "\033[1;36m"
    reset = "\033[0m"
    
    print(f"{yellow}You are standing at the entrance of Hogwarts School of Witchcraft and Wizardry.\n")
    time.sleep(3)  # Pause for dramatic effect
    print(f"{yellow}The massive oak doors swing open slowly, revealing the majestic castle.\n")
    time.sleep(3)
    print(f"{yellow}As you step inside, the enchanted ceiling of the Great Hall mirrors the night sky with thousands of stars.\n")
    time.sleep(3)
    print(f"{yellow}The Sorting Hat awaits, ready to place you into one of the four legendary houses.\n")
    time.sleep(3)
    print(f"{yellow}You walk towards the Sorting Hat, and sit down on the stool.\n")
    
    title =f"{green}WELCOME TO HOGWARTS!{reset}"
    print_centered(title)
    
    time.sleep(3)
    
    sorting_hat_speech = f"{Cyan}\nI am the Sorting Hat, and I will determine your destiny at Hogwarts.\nI will place you in a house according to your abilities and qualities.\nLet me delve into your thoughts...\n{reset}"
    print_centered(sorting_hat_speech)
    
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(2)
    print("\n")

def display_ascii_art():
    # Your ASCII art here
    ascii_art ="""
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⣀⣠⡀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⡿⢿⣿⣦⡀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡏⠉⠀⠀⢸⣿⣿⣿⣦⡀⠀⠀
                    ⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣆⠀
                    ⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣷
                    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿
                    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
                    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
                    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
                    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣴⣶⣶⣶⣦⣄⣿⣿⣿⣿⣿⣿⡀⢀⠀⠀⠀⣿⣿⣿⣿⣿⣿
                    ⠀⣀⣀⣤⠄⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡟⠉⠁⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⢷⣄⣰⣿⣿⣿⣿⡿⠋
                    ⢹⣟⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠻⣿⡿⠿⠛⠉⠀⠀
                    ⠀⠙⢿⣦⣄⡀⠀⢿⣿⣿⣿⣿⣿⣿⣧⣶⣿⣿⣿⡿⢻⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠁⠀⠘⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⠻⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⡀⠸⣿⣿⣿⣿⣿⡄⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢹⣦⣿⣿⣿⣿⣿⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⡏⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠓⠂⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢹⣿⣿⡇⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠿⠿⠿⠿⠿⠿⠿⠿⠿⢷⣄⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    print(ascii_art)