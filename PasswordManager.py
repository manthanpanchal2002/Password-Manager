from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


def main():
    # --> Password generator
    def generate_passwd():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                   'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # using list comprehension
        password_letters = [choice(letters) for i in range(randint(2, 4))]
        password_numbers = [choice(numbers) for j in range(randint(2, 4))]
        password_symbols = [choice(symbols) for k in range(randint(2, 4))]

        passwd_list = password_letters + password_numbers + password_symbols
        shuffle(passwd_list)

        # it will join all letters, numbers and symbols
        password = "".join(passwd_list)

        # it will insert password to Password Label
        passwd_entry.insert(0, password)

    # --> Save Password

    def save_password():
        website = website_entry.get()
        passwd = passwd_entry.get()
        email = email_entry.get()
        user_data = {
            website: {
                "Email": email,
                "Password": passwd,
            }
        }

        if len(website) == 0 or len(passwd) == len(email) == 0:
            messagebox.showwarning(
                message="Please make sure you have filled everything")
        else:
            store_data = messagebox.askokcancel(
                title=website, message="Do you want to store data to your File ?")
            if store_data:
                # try:
                #     with open("/Users/manthanpanchal/Documents/Python/Intermediate/Password manager/Your_Saved_Data.json",
                #               "r") as data_file:
                #         data = json.load(data_file)  # Reading old data
                #
                # except FileNotFoundError:
                #     with open("/Users/manthanpanchal/Documents/Python/Intermediate/Password manager/Your_Saved_Data.json","w") as data_file:
                #         json.dump(user_data, data_file, indent=4)  # Saving data
                #
                # else:
                #     data.update(user_data)  # Updating old data with new data
                #
                #     with open("/Users/manthanpanchal/Documents/Python/Intermediate/Password manager/Your_Saved_Data.json","w") as data_file:
                #         json.dump(data, data_file, indent=4)  # Saving updated data
                #
                # finally:
                #     website_entry.delete(0, END)
                #     passwd_entry.delete(0, END)
                #     email_entry.delete(0, END)

                # --> Method 2 to store data
                # with open("/Users/manthanpanchal/Documents/Python/Intermediate/Password manager/Your_Saved_Data.json", "w") as data_file:
                #         json.dump(user_data, data_file, indent=4) # Saving data

                with open("/Users/manthanpanchal/Documents/ICT/ICT_Projects/Password_Manager/Your_Saved_Data.json",
                          "r") as data_file:
                    data = json.load(data_file)  # Reading old data
                    data.update(user_data)  # Updating old data with new data
                with open("/Users/manthanpanchal/Documents/ICT/ICT_Projects/Password_Manager/Your_Saved_Data.json",
                          "w") as data_file:
                    json.dump(data, data_file, indent=4)  # Saving updated data

                website_entry.delete(0, END)
                passwd_entry.delete(0, END)
                email_entry.delete(0, END)

    # --> Find Password

    def find_passwd():
        website = website_entry.get()
        try:
            with open("Your_Saved_Data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data found")
        else:
            if website in data:
                email = data[website]["Email"]
                password = data[website]["Password"]
                messagebox.showinfo(
                    title=website, message=f"Email : {email}\nPassword: {password}")
            else:
                messagebox.showinfo(
                    title="Error", message=f"No details found for {website}")

    # --> Main
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(height=230, width=230)
    img = PhotoImage(file="/Users/manthanpanchal/Documents/ICT/ICT_Projects/Password_Manager/padlock.png")
    canvas.create_image(115, 115, image=img)
    canvas.grid(row=0, column=1)

    # --> Labels
    website_label = Label(text="Domain Name")
    website_label.grid(row=1, column=0)
    email_label = Label(text="Your Email")
    email_label.grid(row=2, column=0)
    passwd_label = Label(text="Password")
    passwd_label.grid(row=4, column=0)

    # --> Entries
    website_entry = Entry(width=21)
    website_entry.grid(row=1, column=1)
    website_entry.focus()
    email_entry = Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2)
    passwd_entry = Entry(width=21)
    passwd_entry.grid(row=4, column=1)

    # --> Button
    search_button = Button(text="Search", width=10, command=find_passwd)
    search_button.grid(row=1, column=2)
    generate_passwd_button = Button(
        text="Generate Password", width=15, command=generate_passwd)
    generate_passwd_button.grid(row=3, column=1)
    add_button = Button(text="Save To File", width=35, command=save_password)
    add_button.grid(row=5, column=1)

    window.mainloop()
