alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, direction_choice):
  new_text = ''
  for x in plain_text:
    if x in alphabet:
      index = alphabet.index(x)
      if direction_choice == 'encode':
        new_index = index + shift_amount
      elif direction_choice == 'decode':
        new_index = index - shift_amount
      new_text += alphabet[new_index % len(alphabet)]
    else:
      new_text += x
  print(f'The {direction_choice}d text is {new_text}')

import art
print(art.logo)
continue_choice = ''

while continue_choice != 'no':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(plain_text=text, shift_amount=shift, direction_choice=direction)
  continue_choice = input('Would you like to go again, "yes" or "no"?\n')
print("Goodbye")
