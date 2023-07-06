from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
FONT = ("Roboto", 15)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letter_list + number_list + symbol_list
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    get_username = username_entry.get()
    get_password = pass_entry.get()
    get_email = email_entry.get()
    get_website = website_entry.get()

  # Checking if any of the fields are empty

    if len(get_password) == 0 or len(get_website) == 0 or len(get_username) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.", icon="warning")

  # Confirming details before saving

    else:
        response = messagebox.askokcancel(title="Confirmation", message=f"Check Information Accuracy "
                                                             f"\nWebsite 👉 {get_website} \nUsername 👉 {get_username} "
                                                             f"\nEmail 👇 {get_email} \nPassword 👉 {get_password} "
                                                             f"\nDo you want to save?", icon="info")
      # Saving datas to a text file data.txt
        if response:

            with open("data.txt", "a") as file:
                file.write(f"{get_website} | {get_username} | {get_email} | {get_password}\n")
            pass_entry.delete(first=0, last=END)
            username_entry.delete(first=0, last=END)
            website_entry.delete(first=0, last=END)

# ---------------------------- COPY PASSWORD TO CLIPBOARD ------------------------------- #
def copy_password():
    pass_str = pass_entry.get()
    pyperclip.copy(pass_str)
    messagebox.showinfo(title="Clipboard", message="Password Copied to Clipboard")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager by Required")
window.config(bg="white", padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:", bg="white", highlightthickness=0, fg="black", font=FONT)
website.focus()
website.grid(row=1, column=0)

email = Label(text="Email:", bg="white", highlightthickness=0, fg="black", font=FONT)
email.grid(row=2, column=0)

username = Label(text="Username:", bg="white", highlightthickness=0, fg="black", font=FONT)
username.grid(row=3, column=0)

password = Label(text="Password:", bg="white", highlightthickness=0, fg="black", font=FONT)
password.grid(row=4, column=0)

email_entry = Entry(width=38, bg="white", highlightthickness=0, fg="black")
email_entry.insert(0, string="required@artificialevening.com")
email_entry.grid(row=2, column=1, columnspan=2)

website_entry = Entry(width=38, bg="white", highlightthickness=1, fg="black")
website_entry.grid(row=1, column=1, columnspan=2)

pass_entry = Entry(width=21, bg="white", highlightthickness=1, fg="black")
pass_entry.grid(row=4, column=1)

generate_pass_button = Button(text="Generate Password", highlightthickness=0, bg="white", command=password_generator)
generate_pass_button.grid(row=4, column=2)

username_entry = Entry(width=38, bg="white", highlightthickness=0, fg="black")
username_entry.grid(row=3, column=1, columnspan=2)

add_button = Button(width=36, text="Add", bg="white", highlightthickness=0, command=save)
add_button.grid(row=5, column=1, columnspan=2)

copy_password = Button(text="Copy Password to Clipboard", width=36, bg="white", highlightthickness=0, command=copy_password)
copy_password.grid(row=6, column=1, columnspan=2)

window.mainloop()
