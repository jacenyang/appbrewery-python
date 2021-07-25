from tkinter import *


def calculate():
    user_input_to_km = round(float(user_input.get()) * 1.609344)
    output_label.config(text=user_input_to_km)


window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)
window.resizable(width=False, height=False)

user_input = Entry(width=10, justify="center")
user_input.grid(row=0, column=1)

output_label = Label(text=0)
output_label.grid(row=1, column=1)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

label_1 = Label(text="is equal to")
label_1.grid(row=1, column=0)
label_2 = Label(text="mile")
label_2.grid(row=0, column=2)
label_3 = Label(text="km")
label_3.grid(row=1, column=2)

window.mainloop()
