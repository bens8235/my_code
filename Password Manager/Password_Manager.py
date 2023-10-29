from tkinter import *
from tkinter import messagebox
import random
import json


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= lock_img)
canvas.grid(column=1, row= 0)


def search():
    keymatch = False
    try:
        with open("pass_manager.json",mode="r") as pm:
            data = json.load(pm)
        for key,value in data.items():
            if key == website_entry.get().lower():
                keymatch= True
                website = key
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
                break
        if keymatch == False:
            messagebox.showinfo(message="No website in database.")

    except:
        messagebox.showinfo(message="No website in database")


def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] 
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)

    password_entry.insert(0, password)
    

def save_info():
    website_info = website_entry.get().lower()
    email_info = email_entry.get().lower()
    pass_info = password_entry.get().lower()
    new_data = {website_info: {"email": email_info, 
                            "password": pass_info }
            }

    if len(website_info) < 1 or len(pass_info) < 1:
        messagebox.showwarning(title="Opps", message="Please don't leave any fields empty!")
    
    else:
        is_ok = messagebox.askokcancel(title=website_info, message=f"These are the details entered: \nEmail: {email_info} \nPassword: {pass_info}\nIs it okay to save?")

        if is_ok:
            try:
                with open("pass_manager.json",mode="r") as pm:
                    data = json.load(pm)
                    data.update(new_data)
            except:
                with open("pass_manager.json", mode="w") as pm:
                    json.dump(new_data, pm, indent=4)
            else:
                with open("pass_manager.json", mode="w") as pm:
                    json.dump(data, pm, indent=4)

                
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
            messagebox.showinfo(message="Details Saved")


website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="EW")
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW")
search = Button(text="Search", command=search)
search.grid(column=2, row=1, sticky="EW")
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="EW")
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "test@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="EW")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

Generate_password = Button(text="Generate Password", command=password_generator)
Generate_password.grid(column=2, row=3, sticky="EW")

add = Button(text="Add", width=35, command=save_info)
add.grid(column=1, row = 4, columnspan=2, sticky="EW")


window.mainloop()