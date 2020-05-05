# This is a small scrabble program project that is a prompt from Codecademy.com. Code written by John Adam Gordon Whited. 

# Declaring two lists that will be zipped into a dictionary storing key: values for the Scrabble games' point system.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


# Zipping the letters and points list into a dictionary names letter_to_points.
# dict(zip(letters, points)) could be used, but I wanted to demonstrate knowledge of a for loop with zip()
letter_to_points = {
  key: value
  for key, value
  in zip(letters, points)
}

# Appending a value for empty space tile to the dictionary.
letter_to_points[" "] = 0

# This function takes in a parameter of word, which will be a user input or even taken from a defined list/diction of users and their words. It returns the point value of the users word.
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# Test word/value for the 'score_word' function.
brownie_points = score_word("BROWNIE")

# Defining the players and their entered words into a dictionary.
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# This dictionary will store the players to their points values.
player_to_points = {}
  
# For Loop that will take the players and their words and iterate through the list to determine their total points with the score_word() function.
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# Test Print
# print(player_to_points)

# End Program
"""
Planned Updates to Program

play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
update_point_totals() — turn your nested loops into a function that you can call any time a word is played
make your letter_to_points dictionary able to handle lowercase inputs as well
"""