# SMTP - Simple Mail Transfer Protocol
import smtplib
import random
# ------------------------------------------------------ function check valid user ------------------------------------------------------
def mailChecker():
    recevier = "manthanppanchal21@gnu.ac.in"
    # subject = input("Enter subject : ")

    num = random.randint(1,5)
    # print(num)


    my_email = "pm921322@gmail.com"
    password = "cnniqouugstvbrbh"
    with smtplib.SMTP("smtp.gmail.com") as connection:  # it will close automatically
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recevier,
            msg=f"Subject:OTP for verification\n\n{num}"
        )

    verify = input("Enter OTP : ")


    if verify == str(num) :
        print("Verified successfully")

    else:
        print("Failed to verify")
