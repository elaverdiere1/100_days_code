rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# getting the player and computer choices
import random
comp_choice = random.randint(0,2)

print('Let us play Rock Paper Scissors')
player_choice = int(input('What is your choice? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n'))

choices = [rock, paper, scissors]

# checking for a correct value entered

if player_choice >= 3 or player_choice < 0:
  print('invalid choice')
else:
  print(choices[player_choice])
  print('Computer choice:')
  print(choices[comp_choice])

# checking for who wins

  if player_choice == 0:
    if comp_choice == 0:
      print('Draw')
    elif comp_choice == 1:
      print('Computer Wins')
    elif comp_choice == 2:
      print('Player Wins')
  if player_choice == 1:
    if comp_choice == 1:
      print('Draw')
    elif comp_choice == 2:
      print('Computer Wins')
    elif comp_choice == 0:
      print('Player Wins')
  if player_choice == 2:
    if comp_choice == 2:
      print('Draw')
    elif comp_choice == 0:
      print('Computer Wins')
    elif comp_choice == 1:
      print('Player Wins')
