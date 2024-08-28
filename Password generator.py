# Ask if user wants to generate a password or not
# If Yes, ask password length
# Generate password
# If initial response is no, exit program

import string
import random

characters= list(string.ascii_letters+ string.digits + "!@#$%^&*()")

def generate_password():
    password_length=int(input("Enter the length of your password: "))

    random.shuffle(characters)

    password=[]

    for x in range (password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password="".join(password)

    print(password)


option= input("Do you want to generate a password? (Yes/ No):  ")

if option=="Yes":
    generate_password()
elif option=="No":
    print("Program Ended...")
    exit()
else:
    print("Invalid input...Please input Yes or No.")
    print("Program Ended.......")
    quit()
