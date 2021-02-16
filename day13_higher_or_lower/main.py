import random
import art
import game_data
from replit import clear

data = game_data.data

# random option from list of dictionaries
def random_choice():
  choice = random.choice(data)
  return choice
  
# comparing the user choice
def compare(first, second):
  print(f'Compare A: {first["name"]}, {first["description"]}, from {first["country"]}.')
  print(art.vs)
  print(f'Compare B: {second["name"]}, {second["description"]}, from {second["country"]}.')
  player_decides = input('Who has more followers? Type "A" or "B": ').upper()
  if player_decides == 'A' and first["follower_count"] > second["follower_count"]:
    return True
  elif player_decides == 'A' and first["follower_count"] < second["follower_count"]:
    return False
  elif player_decides == 'B' and first["follower_count"] > second["follower_count"]:
    return False
  elif player_decides == 'B' and first["follower_count"] < second["follower_count"]:
    return True
  else:
    print('Invalid choice you lose.')
    return False

# main game code
def game():
  print(art.logo)
  current_score = 0
  first_option = random_choice()
  second_option = random_choice()
  while second_option == first_option:
      second_option = random_choice
  player_correct = compare(first_option, second_option)
  
# checking if correct to continue
  while player_correct:
    clear()
    print(art.logo)
    current_score += 1
    print(f'You\'re correct! Current score: {current_score}')
    first_option = second_option
    while second_option == first_option:
      second_option = random_choice()
    player_correct = compare(first_option, second_option)

# what to do when wrong
  clear()
  print(art.logo)
  print(f'Sorry that is wrong. Final score {current_score}')  
  
game()
