#WHILE LOOP
#A while loop in python is used to iterate over a block of code or statements as long as the test expression is true.

store_capacity = 5
while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    store_capacity = store_capacity - 1
print("\nPlease wait for someone to exit the store.")

'''
# Example INFINITE 'while loop' that runs forever until the memory is 'blown'
store_capacity = 10
while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
# store_capacity = store_capacity - 1 ---> imagine that we forgot to add this logic!!!
print("\nPlease wait for someone to exit the store.")

'''

#Countdown

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blastoff!")


#Number Guessing Game:

import random

secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 100): "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the secret number.")


#Fibonacci Sequence
a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, a + b


#Rock, Paper, Scissors Game

import random

choices = ["rock", "paper", "scissors"]
player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(choices)

while player_choice not in choices:
    print("Invalid choice. Please try again.")
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations! You win!")
else:
    print("Sorry, you lose. Better luck next time!")


