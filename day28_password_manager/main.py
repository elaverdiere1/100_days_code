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

    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please do not leave any fields empty')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)
            
def search():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found.')
    else:
        if website_input.get() in data:
            email = data[website_input.get()]["email"]
            password = data[website_input.get()]["password"]
            messagebox.showinfo(title=website_input.get(), message=f'Email: {email}\n'
                                                                   f'Password: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website_input.get()} exists.')
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

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
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

search_button = Button(text='Search', width=13, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
