import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print(data_dict)

user_word = input('Enter a word: ')
answer = [data_dict[letter] for letter in user_word.upper()]
print(answer)


