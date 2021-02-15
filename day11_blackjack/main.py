import random
import art
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# function for card drawing
def card_draw(draws):
  draw = random.choices(cards, k=draws)
  return draw

# check if need to change an ace to a value of 1
def calculate_score(card_list):
  if sum(card_list) >= 22 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
    return card_list
  else:
    return card_list
    
    
# checking the final score and changing the bet accordingly
def compare_score(player_score, dealer_score, player_bet, bet_value):
  if sum(player_cards) == sum(dealer_cards):
    print('Draw')
    return player_bet
  elif player_cards == 21:
    print('Blackjack! You Win! You get 2 times your bet.')
    player_bet += bet_value * 2
    return player_bet
  elif sum(player_cards) > 21:
    print('You lose.')
    player_bet -= bet_value
    return player_bet
  elif sum(dealer_cards) > 21:
    print('You Win!')
    player_bet += bet_value
    return player_bet
  elif sum(player_cards) > sum(dealer_cards):
    print('You Win!')
    player_bet += bet_value
    return player_bet
  else:
    print('You lose.')
    player_bet -= bet_value
    return player_bet

keep_playing = True
# setting the bet and checking it make sure you have money and desire to play
player_bet = 1000
while player_bet > 0 and keep_playing:
  bet_value = int(input(f'You have ${player_bet}, How much will you bet: $'))
  if bet_value > player_bet:
    bet_value = player_bet
    print(f'You only have ${player_bet} so your bet will be changed to that value.')
# initial card draws
  player_cards = card_draw(2)
  dealer_cards = card_draw(2)
  print(f'The players starting cards: {player_cards}')
  print(f'The dealers first card: {dealer_cards[0]}')
  player_continue = True
  player_under = True

#checking the player score and if they want to hit
  while player_continue:
    player_cards = calculate_score(player_cards)
    print(f'Your cards: {player_cards}, current score: {sum(player_cards)}')
    if sum(player_cards) == 21:
      player_continue = False
    elif sum(player_cards) < 21:
      hit_choice = input('Type "y" to get another card, type "n" to pass: ')
      if hit_choice == 'y':
        player_cards += card_draw(1)
      elif hit_choice == 'n':
        print(f'Your final cards: {player_cards}, final score: {sum(player_cards)}')
        player_continue = False
      else:
        print('Not a valid choice you pass by default')
        print(f'Your final cards: {player_cards}, final score: {sum(player_cards)}')
        player_continue = False
    else:
      player_continue = False
      player_under = False

  dealer_continue = True
  
# dealer logic
  while dealer_continue and player_under:
    dealer_cards = calculate_score(dealer_cards)
    if sum(dealer_cards) == 21:
      dealer_continue = False
    elif sum(dealer_cards) < 17:
      dealer_cards += card_draw(1)
    else:
      dealer_continue = False

  print(f'Dealers final hand: {dealer_cards}, final score: {sum(dealer_cards)}')
  
  player_bet = compare_score(sum(player_cards), sum(dealer_cards), player_bet, bet_value)

# checking if player wants to continue
  playing_choice = input('Continue playing? Type "y" or "n": ')
  if playing_choice == 'n':
    keep_playing = False
    print(f'Your final amount is ${player_bet}')
  elif playing_choice != 'y':
    keep_playing = False
    print(f'Invalid choice the game will end, your final amount ${player_bet}')
    
