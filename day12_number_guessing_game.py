import random
# setting the number to guess
actual_number = random.randint(1,100)

# function for difficulty
def set_difficulty():
  difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  attempt_number = 0
  if difficulty_choice == 'easy':
    attempt_number = 10 
  elif difficulty_choice == 'hard':
    attempt_number = 5
  else:
    print('Not a valid difficulty choice. Game Over')
  return attempt_number

# intro statements
print('Welcome to the number guessing game.')
print("I am thinking of a number between 1 and 100.")

# running the game
def game():
  # setting the difficulty
  attempts = set_difficulty()

# win and loss condition based on attempts remaining
  while attempts > 0:
    print(f'You have {attempts} attempts remaining to guess the number.')
    player_guess = int(input('Make a guess: '))
    if player_guess < 1 or player_guess > 100:
      print('Out of the bounds of the choosen number.')
      attempts -= 1
    elif player_guess == actual_number:
      print('You guessed correctly. You Win!')
      return
    elif player_guess > actual_number:
      print('Too high.')
      attempts -= 1
    elif player_guess < actual_number:
      print('Too low.')
      attempts -= 1

# conditional text based on if player has guesses left
    if attempts == 0:
      print('You\'ve run out of guesses, you lose')
    elif attempts > 0:
      print('Guess again.')

game()
