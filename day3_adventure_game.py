print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# starting the game and making the first check
cross_road = input('You are at a cross road. Where do you go left or right? Type "left" or "right"\n')
# using lower to make sure case is not important
if cross_road.lower() == 'left':
  lake_choice = input('You reach a lake do you swim or wait for a boat? Type "swim" or "wait"\n')
  if lake_choice.lower() == 'wait':
    door_choice = input('You cross the lake safely and are now at 3 doors.  Do you choose the red, blue, or yellow door? Type "red", "blue", or "yellow"\n')
    if door_choice.lower() == 'yellow':
      print('You have found the treasure you win!')
    elif door_choice.lower() == 'blue':
      print('Water fills the room and you drown. Game Over')
    elif door_choice.lower() == 'red':
      print('Fire fills the room and you perish.  Game Over')
    else:
      print('Your indecision has failed you and you go home with nothing. Game Over')
  
  elif lake_choice.lower() == 'swim':
    print('The lake had a moster and you were eaten.  Game Over')
  else:
    print('You walk away from the treasure and get nothing. Game Over')

elif cross_road.lower() == 'right':
  print('You get lost in a forest. Game Over')
# covering the case of no choice
else:
  print('You gave up on the quest early. Game Over')
