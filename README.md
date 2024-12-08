# Monte-Carlo-Simulator
DS 5100 Project 

Metadata

This project is a Monte Carlo Simulator implemented in Python. It contains three primary classes (Die, Game, and Analyzer) that work together to simulate and analyze games involving dice rolls.
Author: Joshua Hall
Language: Python 3.6+
Dependencies: numpy, pandas
	
Synopsis

The following examples demonstrate how to use each class and its methods:

from Die_Game_Analyzer_Class import Die, Game, Analyzer

1. Die Class
# Create a die with six sides
faces = np.array([1, 2, 3, 4, 5, 6])
die = Die(faces)

# Change the weight of face 1
die.change_weight(1, 2.0)

# Roll the die 5 times
rolls = die.roll(5)
print(rolls)

# Show the current state of the die
print(die.show())


2. Game Class
# Create two dice
faces = np.array([1, 2, 3, 4, 5, 6])
die1 = Die(faces)
die2 = Die(faces)

# Create a game with the two dice
game = Game([die1, die2])

# Play the game (roll both dice 10 times)
game.play(10)

# Show the results in wide format
print(game.show('wide'))

# Show the results in narrow format
print(game.show('narrow'))


3. Analyzer Class
# Create two dice
faces = np.array([1, 2, 3, 4, 5, 6])
die1 = Die(faces)
die2 = Die(faces)

# Create a game and play it
game = Game([die1, die2])
game.play(10)

# Analyze the game results
analyzer = Analyzer(game)

# Number of jackpots (all dice show the same face)
print("Jackpots:", analyzer.jackpot())

# Face counts per roll
print("Face counts per roll:")
print(analyzer.face_counts_per_roll())

# Combination counts
print("Combination counts:")
print(analyzer.combo_count())

# Permutation counts
print("Permutation counts:")
print(analyzer.permutation_count())

API Documentation

1. Die Class
__init__(self, faces):
    Initializes a die with N faces and equal weights.
change_weight(self, face, new_weight):
    Changes the weight of a specific face.
roll(self, num_rolls=1):
    Rolls the die one or more times.
show(self):
    Displays the current state of the die.

2. Game Class
__init__(self, dice):
    Initializes a game with a list of similar dice.
play(self, num_rolls):
    Rolls all dice in the game a specified number of times.
show(self, form='wide'):
	Displays the results of the most recent game in wide or narrow format.

3. Analyzer Class
__init__(self, game):
	Initializes the analyzer with a game object.
jackpot(self):
	Counts the number of jackpots (all faces the same).
face_counts_per_roll(self):
	Computes the counts of each face per roll.
combo_count(self):
	Computes distinct combinations of faces per roll.
permutation_count(self):
	Computes distinct permutations of faces per roll.
