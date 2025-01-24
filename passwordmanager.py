import random
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip


#+*----------------------Password Generator-------------------------*+
def generate_password():
    # Check if there's already a password in the entry field
    current_password = password_entry.get()

    if current_password:  # If a password exists, ask the user to confirm
        has_copied = messagebox.askyesno(
            title="Copy Password",
            message="Have you copied the current password? Generating a new password will overwrite it."
        )
        if not has_copied:
            return  # Do nothing if the user has not copied the password
    # clear the password field before generating a new one
    password_entry.delete(0, END)
    #password generator project
    letters =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    # random.shuffle shuffles the characters so that they don't follow a certain random order that can be hacked.
    shuffle(password_list)
    #print(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


#-------------------------SAVE PASSWORD------------------------------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Rada", "Unaacha mablanks manze?")

    else:
        is_okay = messagebox.askokcancel(title=website, message=f'These are the details that you entered:\n website: {website}\n '
                                                  f'email : {email}\n password: {password}\n Is it ok to save?')
        if is_okay:
            with open("data.txt", "a") as data_file:
                data_file.write(f'{website} -- |-- {email} -- |-- {password}\n')
                website_entry.delete(0, END)
                email_entry.delete(0, END)



#-------------------------UI SET UP----------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Allow the window to resize
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.columnconfigure(2, weight=1)

canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file="download.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, sticky="nsew")

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")
email_label = Label(text="Email:")
email_label.grid(column=0, row=2, sticky="e")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")

#Entries
website_entry = Entry(width = 38)
website_entry.grid(column = 1, row=1, columnspan=2, sticky="ew")
website_entry.focus()
email_entry = Entry(width = 38)
email_entry.grid(column = 1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "<EMAIL>")
password_entry = Entry(width = 20)
password_entry.grid(column= 1, row=3, sticky="ew")

#Buttons
generate_password_button = Button(text="Generate Password", command= generate_password)
generate_password_button.grid(column=2, row=3, sticky="ew")
add_button = Button(text="Add",width=35, command= save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

# Allow rows and columns to expand
for i in range(5):  # Add flexibility for all rows
    window.rowconfigure(i, weight=1)
window.columnconfigure(1, weight=2)  # Make column 1 expandable


window.mainloop()



