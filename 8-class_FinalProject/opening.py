import random
import csv
import time
import shutil
import re
import os

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
    
    Intruduction1 = f"{yellow}You are standing at the entrance of Hogwarts School of Witchcraft and Wizardry.\n{yellow}The massive oak doors swing open slowly, revealing the majestic castle.\n{reset}"
    print_centered(Intruduction1)
    time.sleep(3)
    Intruduction2 = f"{yellow}As you step inside, the enchanted ceiling of the Great Hall mirrors the night sky with thousands of stars.\n{reset}"
    print_centered(Intruduction2)
    time.sleep(3)
    Intruduction3 = f"{yellow}You are greeted by Professor McGonagall, who leads you to the front of the hall.\n{yellow}And the Sorting Hat awaits, ready to place you into one of the four legendary houses.\n{reset}"
    print_centered(Intruduction3)
    time.sleep(3)
    Intruduction4 = f"{yellow}You are nervous, but excited. You have been waiting for this moment for a long time.\n{yellow}You walk towards the Sorting Hat, and sit down on the stool.\n{reset}"
    print_centered(Intruduction4)
    
    title =f"{green}WELCOME TO HOGWARTS!{reset}"
    print_centered(title)
    
    time.sleep(3)
    sorting_hat_speech = f"\n{Cyan}I am the Sorting Hat, and I will determine your destiny at Hogwarts.\n{Cyan}I will place you in a house according to your abilities and qualities.\n{Cyan}Let me delve into your thoughts...\n{reset}"
    print_centered(sorting_hat_speech)
    
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(2)
    print("\n")
    
def center_ascii_art(ascii_art):
    # Obtém o tamanho da janela do terminal
    terminal_width = os.get_terminal_size().columns

    # Calcula o número de espaços à esquerda para centralizar o texto
    left_padding = (terminal_width - len(ascii_art.splitlines()[0])) // 2

    # Imprime os espaços à esquerda seguidos do ASCII art
    for line in ascii_art.splitlines():
        print(" " * left_padding + line)

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
    
def sorting_hat_ascii():
    ascii_art_1 ="""                                                               
    
                                ..--      ::                          
                                  ##  mmMM                            
                              ##    ::  ##++++..                      
                                  ######..##      ::++..              
                            ..  ....######--                          
                            ++      ##mm                              
                                mm..@@++                              
                        ##        ..####                              
                            ::mmMM##MM  ::                          
                            MM--::@@####  mm                          
                            ..--::MM####mmmm                          
                      ##@@####    mm####                              
                      ::  @@####    ####  ..                          
                          mm######--MM##  ##--                        
                    mm@@--::######  ..mm::##                          
                    MMmm  MM@@########mm    @@                        
                    MM::    ++######  MM  ##@@                        
                   ##..      ..::##########MM                        
                    mm      ..++##::    MM  --                        
                    ..        ::mm        @@..--                      
                    MM  --      MMmm::..  --mmMM                      
                --  ::mm++--################  --                      
                ++################################                    
                  @@..####@@mm..--  --##@@@@####                      
                ##++######MM..    --  mmMM  ..                        
                  --MM##MM          ++##..@@  ::--                    
      ::  @@  ####    --@@########@@        ..@@##                    
    ::    mm::..          ----  ::--  ..########                      
    ++--..                                            ..--  ##--      
    ++..                      ..@@::mm##@@mm--    ..  ##########      
      --..                ##@@##@@::MM##--..  ..################      
        @@..                @@mm..        ##::##############          
              ::  MMMM  ..        ##                                  
                                                                  
                                                                                      
"""
    center_ascii_art(ascii_art_1)