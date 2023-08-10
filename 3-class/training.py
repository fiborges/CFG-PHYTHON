'''
Leap Year Checker: Write a program that checks if a year provided by the user is a leap year.
A year is considered a leap year if it is divisible by 4, but not divisible by 100 unless it is also divisible by 400.
'''

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
    
'''
Number Guessing Game: Create a game where the computer selects a random number between 1 and 100. The player has a 
limited number of attempts to guess the correct number. The program should provide hints if the guess is too high or
too low.
'''

import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break


'''
Vowel Counter: Write a program that receives a sentence from the user and counts 
how many vowels (A, E, I, O, U) are in the sentence.

'''
phrase = input("Enter a phrase: ")
vowels = "AEIOUaeiou"
count = 0

for char in phrase:
    if char in vowels:
        count += 1

print(f"The phrase contains {count} vowels.")



'''
BMI Calculator: Create a program that calculates a person's Body Mass Index (BMI).
Ask the user to input their height (in meters) and weight (in kilograms). The program 
should then calculate and display the BMI.
'''

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}")

'''
Temperature Converter: Create a program that converts temperatures between Fahrenheit 
and Celsius. Ask the user to input a temperature and the unit (F or C). The program should 
calculate and display the converted temperature in the other unit.
'''

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (F or C): ")

if unit.upper() == "F":
    converted_temp = (temperature - 32) * 5 / 9
    print(f"{temperature}°F is {converted_temp:.2f}°C")
elif unit.upper() == "C":
    converted_temp = (temperature * 9 / 5) + 32
    print(f"{temperature}°C is {converted_temp:.2f}°F")
else:
    print("Invalid unit.")
