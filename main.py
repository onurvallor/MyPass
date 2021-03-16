from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers =  ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!', '@', '#', '$', '%', '*', '+', '&']

    password_list = []

    ln_letters = random.randint(8,10)
    ln_numbers = random.randint(2,4)
    ln_symbols = random.randint(2,4)


    for char in range(ln_letters):
        password_list.append(random.choice(letters))
    for char in range(ln_numbers):
        password_list.append(random.choice(numbers))
    for char in range(ln_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password_result = ''.join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password_result)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Empty Fields', message='Please fill out all of the empty fields.')
    else: 
        is_ok = messagebox.askokcancel(title=website, message=f'There are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?')
        
        if is_ok == True:
            with open("data.txt", mode='a') as data:
                data.write('------------------------------\n')
                data.write(f'website: {website}\n')
                data.write(f'email: {email}\n')
                data.write(f'password: {password}\n')
            website_input.delete(0, END)
            password_input.delete(0, END)

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
website_input.focus()

#EMAIL FIELD
email_label = Label(text='Email:', bg='white')
email_label.grid(column=0, row=2)

email_input = Entry(width=41)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0, "youremailhere@email.com")

#PASSWORD FIELD
password_label = Label(text='Password:', bg='white')
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.grid(column=1, row=3)

password_generate_btn = Button(text='Generate Password', command=password_generator)
password_generate_btn.grid(column=2, row=3)

#ADD BUTTON
add_btn = Button(text='Add', width=38, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()