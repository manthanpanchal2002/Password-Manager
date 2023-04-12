import json
import re  # module to check space in string
from getpass import getpass  # module to hide password input
import smtplib  # module to send mails
import random  # module to generate random number
import PasswordManager

print("\n1. SignUp\n2. LogIn")
print("----------------------------------------------------")
user_ = input("Press Key :  ")
print("----------------------------------------------------")

# ------------------------------------------------------ function to create new account ------------------------------------------------------


def newAccount():
    # mail = input("Enter your email address : ")
    # print("----------------------------------------------------")
    # fullname = input("Enter your full name : ")
    # print("----------------------------------------------------")

    # -----------------------------------------------------  Storing user data -----------------------------------------------------
    # user_info = {
    #     fullname: {
    #         "Email": mail,
    #         "FullName": fullname
    #     }

    # }

    # with open('user_data.json', 'r') as user_data_file:
    #     data = json.load(user_data_file)
    #     data.update(user_info)

    # with open('user_data.json', 'w') as user_data_file:
    #     json.dump(data, user_data_file, indent=4)

    try:
        with open('user_data.json', 'r') as user_data_file:
            data = json.load(user_data_file)
            mail = input("Enter your email address : ")
            print("----------------------------------------------------")
            fullname = input("Enter your full name : ")
            print("----------------------------------------------------")

            newData = {
                "User" + str(len(data)+1):
                {"Email": mail, "Name": fullname}
            }
            data.update(newData)
    except:
        mail = input("Enter your email address : ")
        print("----------------------------------------------------")
        fullname = input("Enter your full name : ")
        print("----------------------------------------------------")
        newData = {
            'User1': {"Email": mail, "Name": fullname}
        }
        data = newData
    with open('user_data.json', 'w') as user_data_file:
        json.dump(data, user_data_file, indent=4)


    print(f"Mr/ Mrs. {fullname} your account is successfully created")

# ------------------------------------------------------ accessing system ------------------------------------------------------
    PasswordManager.main()


# ------------------------------------------------------ function to check valid user ------------------------------------------------------
def mailChecker():
    recevier = input("Email : ")
    print("----------------------------------------------------")

# -----------------------------------------------------  Verification of email from json file -----------------------------------------------------
    with open('user_data.json') as user_data_file:
        data = json.load(user_data_file)
        for i in range(len(data)):
            num = 1
            str_1 = "User"
            str_2 = num
            user_confirm = f"{str_1}{str_2}"
            if data[user_confirm] == data[user_confirm]["Email"]:
                stored_email = data[user_confirm]["Email"]
                stored_name = data[user_confirm]["Name"]
                print(f"Welcome back, Mr/Mrs. {stored_name}")

            elif recevier != data[user_confirm]["Email"]:
                print("User not found! Create new account")
                print("----------------------------------------------------")
                newAccount()
                # else:
                #     print(f"Welcome back, Mr/Mrs. {stored_name}")

            num += 1

        num = random.randint(9999, 99999)
        # print(num)

        my_email = "pm921322@gmail.com"
        password = "cnniqouugstvbrbh"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recevier,
                msg=f"Subject: Verification OTP\n\nHi\nPlease enter the below OTP for logging in the software.\n\n{num}\n\nWARNING : PLEASE DO NOT SHARE THIS OTP WITH ANYONE!!"
            )

        print("----------------------------------------------------")
        print("Just check your mail we have sent you an OTP 🔐")
        print("----------------------------------------------------")
        verify = input("Enter OTP : ")

        if verify == str(num):
            print("----------------------------------------------------")
            print("Verified successfully")

# ------------------------------------------------------ accessing system ------------------------2------------------------------
            PasswordManager.main()
            # print("----------------------------------------------------")
            # print("Press 0 to get back to Main Menu")
            # input()

        else:
            print("----------------------------------------------------")
            print("Failed to verify")


if user_ == '1':
    print("Your are new user")
    print("----------------------------------------------------")
    newAccount()


elif user_ == '2':
    print("You are old user")
    print("----------------------------------------------------")
    mailChecker()

else:
    print("Invalid input!")
