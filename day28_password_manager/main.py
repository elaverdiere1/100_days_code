from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# Password generator

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)

# Saving the information to a text file

def add_to_file():
    if len(website_input.get()) == 0 or len(email_input.get()) == 0 or len(pass_input.get()) == 0:
        messagebox.showinfo(title='Oops', message='Please do not leave any fields empty')
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f'These are the details entered:\n'
                                                                          f'Email: {email_input.get()}\n'
                                                                          f'Password: {pass_input.get()}\n'
                                                                          f'Is it ok to save?')

        if is_ok:
            f = open('data.txt', 'a')
            f.write(f'{website_input.get()} | {email_input.get()} | {pass_input.get()}\n')
            f.close()
            website_input.delete(0, END)
            pass_input.delete(0, END)

# UI setup

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, columnspan=2, row=1)
website_input.focus()

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_input = Entry(width=35, )
email_input.grid(column=1, columnspan=2, row=2)
email_input.insert(0, 'default@default.com')

pass_label = Label(text='Password:')
pass_label.grid(column=0, row=3)

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

pass_button = Button(text='Generate Password', command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=add_to_file)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
