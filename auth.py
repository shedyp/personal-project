#register
#login

from multiprocessing.sharedctypes import Value
import random
import validation
import database

# database = {
#     9017057774: ['shedrack','nwoye','shed@zuri.team','password',400]
# }   


def init():

        print("Welcome to BankPHP")
        userInfo = int(input("Kindly login or register, enter 1 (Yes) for login and 2 (No) for register \n"))
        if userInfo == 1:
            login()
        elif userInfo == 2:
            
            register()
        else:
            print("The value entered is invalid. Try again")
            init()

def login():
    print("********** Login **********")

    accountNumberFromUser = input("What is your account number \n")

    isValidAccountNumber = validation.accountNumberValidation(accountNumberFromUser)

    if isValidAccountNumber:

        password = input("What is your password \n")

        for accountNumber,userDetails in database.items():
            if(accountNumber == int(accountNumberFromUser)):
                if(userDetails[3] == password):
                    bankOperation(userDetails)

        print("Invalid account or password")
        login()

    
def register():
    print("****** Register ******")
    email = input("Enter your email address \n")
    first_name = input("Eneter your First name \n")
    last_name = input("Enter your last name \n")
    password = input("Creat your password \n")

    accountNumber = accountGeneration()

    # using database module to create new user record
    isUserCreated = database.create(accountNumber, [first_name, last_name, email, password, 0])

    if isUserCreated:
        print("Your account has been created")
        print("== === ===== ===== ===")
        print("Your account number is: %d" % accountNumber)
        print("== === ===== ===== ===")

        login()
    else:
        print("Something went wrong, please try again")
        register()

def bankOperation(user):

    print("Welcome %s %s" % ( user[0], user[1]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))
    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        login()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    #get amount to withdraw
    #check if current balance > withdraw balacne
    #deduct withdrawn amount from current balance
    #display current balacne

    print("Widthrawal")
    withdrawalAmount = int(input("Enter amount to withdraw. \n"))
    balance = database.values()
    convertBalaneToList = list(balance)
    currentBalance = get_current_balance(convertBalaneToList)
    if currentBalance > withdrawalAmount:
        remainingBalance = currentBalance - withdrawalAmount
        print("Your remaining Balance is %s " % remainingBalance)
    else:
        print("You don't have sufficient funds in your Account")

def depositOperation():
    print("Deposit")
    depositAmount = int(input("Enter amount to withdraw. \n"))
    balance = database.values()
    convertBalanceToList = list(balance)
    currentBalance = get_current_balance(convertBalanceToList)
    newBalance = currentBalance+depositAmount
    print("Your balance is %s" % newBalance)

def accountGeneration():
    return random.randrange(1111111111,9999999999)


def get_current_balance(userDetails): 
    return userDetails[0][4]



#Function Call

init()

#depositOperation()

#withdrawalOperation()



