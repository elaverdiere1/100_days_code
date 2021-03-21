import time
import random
import pandas as pd
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

card_text = {}
words_data = {}


try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    words_data = original_data.to_dict('records')
else:
    words_data = data.to_dict('records')


def next_card():
    global card_text, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(language_text, text='French', fill='black')
    card_text = random.choice(words_data)
    canvas.itemconfig(word_text, text=card_text['French'], fill='black')
    canvas.itemconfig(card, image=card_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_img_back)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=card_text['English'], fill='white')


def is_known():
    words_data.remove(card_text)
    new_data = pd.DataFrame(words_data)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = PhotoImage(file='./images/card_front.png')
card_img_back = PhotoImage(file='./images/card_back.png')
card = canvas.create_image(400, 263, image=card_img)
language_text = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, columnspan=2, row=0)

true_image = PhotoImage(file='./images/right.png')
true_button = Button(image=true_image, highlightthickness=0, command=is_known)
true_button.grid(column=1, row=1)

false_image = PhotoImage(file='./images/wrong.png')
false_button = Button(image=false_image, highlightthickness=0, command=next_card)
false_button.grid(column=0, row=1)

next_card()

window.mainloop()
