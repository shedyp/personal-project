name = input("What is your name? \n")
allowedUsers = ["Seyi","Mike","Tolu","Paul"]
allowedPassword = "Password"

if(name in allowedUsers):
    password = input("Enter you password please. \n")

    if(password in allowedPassword):
        print("You are logged in Successfully!")

else:
    print("The input is wrong")