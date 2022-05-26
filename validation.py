def accountNumberValidation(accountNumber):
    # check if account number is not empty
    # check if account number is 10 digit
    # check if account number is an integer
    if accountNumber:

        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
                return True
            except ValueError:
                print("Invalid Account number, account number should only be an Integer") 
                return False
            except TypeError:
                print("Invalid Account Type")
                return False

        else:
            print("Account Number should only be an Integer")
            return False
    else:
        print("Account number is a required filled")
        return False