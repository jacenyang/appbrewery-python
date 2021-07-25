from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=5, pady=5)

# Button

my_button = Button(text="Click me here", command=button_clicked)
my_button.grid(column=1, row=1)
my_button.config(padx=5, pady=5)

# New Button

new_button = Button(text="Click me here", command=button_clicked)
new_button.grid(column=3, row=0)
new_button.config(padx=5, pady=5)

# Entry

input = Entry(width=10)
input.grid(column=4, row=3)
window.config(padx=5, pady=5)

window.mainloop()
