# Top Trumps Game with Pokemon API

This project involves creating a simple game similar to the Top Trumps card game, where players compare stats of different cards. In this version, the game uses the Pokemon API to fetch and compare attributes of different Pokemon. The core gameplay includes:

## Random Pokemon Card Generation: 
  A random Pokemon card is selected based on a generated ID between 1 and 151.

## Pokemon API Integration: 
  The program interacts with the Pokemon API to retrieve details about each selected Pokemon, including its name, ID, height, and weight.

## Player vs. Opponent: 
  Both the player and the computer (opponent) are given random Pokemon cards to play with.

## Stat Comparison: 
  The player selects a stat (ID, height, or weight) to compare. The program then compares the chosen stat between the player's and opponent's Pokemon cards.

## Outcome Determination: 
  Based on the comparison, the winner of the round is determined. The player with the higher stat wins the round.

## Scoring and Rounds: 
  The game progresses through multiple rounds, and the player's and opponent's scores are updated based on each round's outcome.

## Instructions to Play

Run the script.
A welcome animation introduces the game.
Enter the number of rounds you want to play.

### For each round:
A random Pokemon is assigned to you and your opponent.
Choose a stat to compare (ID, height, or weight) by entering the corresponding number.
The winner of the round is announced.
After all rounds are completed, the game displays your final score and the opponent's score.
Readme

## Top Trumps Game with Pokemon API
This project implements a Top Trumps-style card game using the Pokemon API. The game randomly assigns Pokemon cards to the player and an AI opponent, allowing them to compare different stats and determine the winner based on user-selected attributes.

## Gameplay
### Random Card Generation: 
  At the start of each round, a random Pokemon card is generated for both the player and the AI opponent. The selection is based on a random ID between 1 and 151.

### API Integration: 
  The program utilizes the Pokemon API to retrieve comprehensive details about each selected Pokemon card, including its name, ID, height, and weight.

### Comparison Mechanism: 
  The player chooses a specific stat (ID, height, or weight) to compare between their Pokemon card and the opponent's card.

### Outcome Determination: 
  After the comparison, the program determines the winner of the round based on the selected stat. If the player's stat is higher, they win the round.

### Rounds and Scoring: 
  The game progresses through multiple rounds, and the player's score is updated based on each round's outcome. The final scores of both the player and the AI opponent are displayed at the end of the game.

### How to Play
Run the provided script.
Experience an animated welcome to the game.
Input the number of rounds you wish to play.

### During each round:
Receive a random Pokemon card for both you and your opponent.
Choose a stat (ID, height, or weight) to compare by entering the corresponding number.
The program will announce the winner of the round.
Upon completing all rounds, the game will display your total score and the AI opponent's score.

### Requirements
This project requires Python 3.x and the requests library for API interaction. You can install the required library using the following command:

```bash

pip install requests
```
Note: The game uses the Pokemon API for data retrieval and comparison. You might need an internet connection for the API to function correctly.

Feel free to explore and modify the code to enhance the game or customize the user experience. Enjoy the game of Top Trumps with your favorite Pokemon!




