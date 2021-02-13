# designed to be run in repl.it as it uses the clear function from replit
from replit import clear
import art

print(art.logo)
print()
# setting variable and empty dictionary
continue_choice = ''
bids = {}
# running until all bids are made
while continue_choice != 'no':
  player_name = input('What is your name?: ')
  player_bid = int(input('What is your bid?: $'))
  bids[player_name] = player_bid
  continue_choice = input('Are there any other bids? Type "yes" or "no": ')
# using clear from replit to clear screen
  clear()
# base line to check
winner = 0
#check dictionary for winner
for x in bids:
  if bids[x] > winner:
    winner_person = x
    winner = bids[x]
print(f'{winner_person} is the winner with a bid of ${winner}')
