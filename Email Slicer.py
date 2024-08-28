# collect email from user
# slice email using the @, save first part as user name, 2nd part save as domain
# split domain using .

def main():
    print("Welcome to Email Slicer... ")
    print(" ")

    while True:
        email_input=input("Input your email address: ")

        (username, domain)= email_input.split("@")
        (domain, extension)= domain.split(".")

        print("Username: ", username)
        print("Domain: ", domain)
        print("Extension: ", extension, "\n")

main()