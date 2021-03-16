import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print(data_dict)

def generate_phonetic():
    user_word = input('Enter a word: ')

    try:
        answer = [data_dict[letter] for letter in user_word.upper()]
    except KeyError:
        print('Only use letters in the alphabet.')
        generate_phonetic()
    else:
        print(answer)

generate_phonetic()


