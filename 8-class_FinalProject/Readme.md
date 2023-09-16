
# Harry Potter Top Trumps Game


Welcome to the Hogwarts Houses Challenge! This Python project is a Harry Potter-themed Top Trumps game that I developed as the final project for a Python course. 
The game is designed to be fun and engaging while allowing me to apply various programming concepts that I learned during the course.

## Project Overview
### What is Top Trumps?
Top Trumps is a popular card game that features a deck of cards, each representing a character or item with specific attributes. Players take turns comparing one of these attributes (e.g., power, intelligence, courage) with their opponent's card. The player with the highest value wins the round.

### Game Objective
In this Harry Potter-themed Top Trumps game, the objective is to compete in various challenges against computer-controlled opponents, representing different Hogwarts houses, and accumulate points to determine the ultimate winner.

## Key Features and Concepts Learned
Here are some of the key features and concepts that I applied and learned while working on this project:

### Object-Oriented Programming: 
  I structured the code using classes for Spell and House, each with its attributes and methods. This allowed me to organize and manage the game's data effectively.

### CSV Data Loading: 
  I implemented functions to load character and spell data from CSV files, making it easy to expand the game with additional characters and spells in the future.

### User Interaction: 
  The game interacts with the user by displaying messages, choices, and accepting user input to make decisions.

### Randomization: 
  Randomization is used in various aspects of the game, such as sorting the player into a Hogwarts house and selecting random opponents and spells.

### Text-Based Graphics: 
  I incorporated ASCII art and text formatting to enhance the visual experience of the game.

### Error Handling: 
  I included error handling to gracefully handle situations where the required CSV files are not found or invalid data is encountered.

Looping and Decision Making: The game is structured using loops and conditional statements to control the flow of the game and determine the winner.

## How to Play
The game starts with the Sorting Hat deciding which Hogwarts house the player will belong to.

The player then selects the number of rounds they want to play.

In each round, the player faces off against a computer-controlled opponent from a different Hogwarts house in various challenges.

The challenges include Power, Intelligence, Courage, and a final Spell Duel.

For each challenge, the player and computer select a character, and the winner is determined based on the specified attribute.

In the Spell Duel, the player chooses a spell to cast, and the computer selects a random spell. The winner of the duel is determined by the power of the spells.

Points are awarded based on the outcome of each challenge, and the house with the most points at the end of the rounds wins the game.

The game displays the winning house and a congratulatory message.

## How to Run the Game
To play the game, you can run the provided Python script Top_Trumps.py. Make sure you have Python installed on your system.

```python
python3 Top_Trumps.py

```
Follow the on-screen instructions to interact with the game.

## Conclusion
This Harry Potter-themed Top Trumps game allowed me to apply the Python programming skills I learned during the course in a fun and creative way. I hope you enjoy playing the game and exploring the code. Feel free to expand and enhance the game further or use it as a learning resource to deepen your Python knowledge.

If you have any questions or feedback, please don't hesitate to reach out. Thank you for checking out my project!


EXTRA:

## Installation and Dependencies
Before running the Harry Potter Top Trumps game, you may need to install some Python libraries and create a virtual environment to manage the dependencies. Here are the steps to set up the game:

### 1. Create a Virtual Environment (Optional but Recommended)
Creating a virtual environment helps keep your project's dependencies isolated and ensures compatibility. You can use venv, which is included with Python:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (on Windows)
venv\Scripts\activate

# Activate the virtual environment (on macOS and Linux)
source venv/bin/activate

```
### 2. Install Required Libraries
While inside your virtual environment (if you created one), install the required libraries using pip:


```bash

pip install PIP
pip install etc... install everything that the programe need...

```

### 3. Run the Game
Now that you have set up the virtual environment and installed the necessary libraries, you can run the game using the provided Python script:


Note: If you encounter any issues or missing dependencies during installation, you may need to install additional libraries based on the error messages. Refer to the library documentation or use pip to install them as needed.

Enjoy playing the Harry Potter Top Trumps game!
