from tkinter import *

window = Tk()
window.title('Distance Converter')
window.config(padx=20, pady=20)

distance_label = Label(text='is equal to')
distance_label.grid(column=0, row=1)

miles_label = Label(text='Miles')
miles_label.grid(column=3, row=0)

km_label = Label(text='Km')
km_label.grid(column=3, row=1)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

conversion = Label(text='0')
conversion.grid(column=1, row=1)


def button_clicked():
    conv_input = float(miles_input.get())
    conv = round(conv_input * 1.609, 2)
    conversion.config(text=f'{conv}')


button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
