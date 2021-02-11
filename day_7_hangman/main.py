import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Create blank list
word_empty = ['_'] * len(chosen_word)

#checking for end condition
while lives != 0 and '_' in word_empty:
  guess = input('Guess a letter, make sure it is only one letter and not a number or symbol: ').lower()
# checking edge cases
  if guess in word_empty:
    print('You have already guessed this letter.')
  elif len(guess) != 1:
    print('Invalid Guess')
# for good guess
  elif guess in chosen_word:
    for x in range(len(chosen_word)):
      if guess == chosen_word[x]:
        word_empty[x] = guess
# for bad guess
  else:
    lives -= 1
    print('Bad Guess -1 life')

  print(hangman_art.stages[lives])
  print(f"{' '.join(word_empty)}")
# end result 
if lives == 0:
  print('You Lose')
else:
  print('You Win')
