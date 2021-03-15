from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50, bg='white')

#LOGO CANVAS
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0,row=0, columnspan=3)

#WEBSITE FIELD
website_label = Label(text='Website:', bg='white')
website_label.grid(column=0, row=1)

website_input = Entry(width=41)
website_input.grid(column=1, row=1, columnspan=2)

#EMAIL FIELD
email_label = Label(text='Email:', bg='white')
email_label.grid(column=0, row=2)

email_input = Entry(width=41)
email_input.grid(column=1,row=2,columnspan=2)

#PASSWORD FIELD
password_label = Label(text='Password:', bg='white')
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.grid(column=1, row=3)

password_generate_btn = Button(text='Generate Password')
password_generate_btn.grid(column=2, row=3)

#ADD BUTTON
add_btn = Button(text='Add', width=38)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()