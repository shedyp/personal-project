# Create record
# Update record
# read record
# Delete record
# CRUD

# Search for user

def create(accountNumber, userDetails):

    completion_state = False

    try:
        f = open("data/user_record/" + str(accountNumber) + ".txt", "x")

    except FileExistsError:

        print("User already exist")
        # delete the already created file, and print out the error, then return False
        return completion_state

    else:
            
        f.write(str(userDetails))
        completion_state = True

    finally:

        f.close()

    return completion_state


    #Create a file
    #name of the file would be accountNumber.txt
    #add user details to the file
    #if file saving fails, then delete the file.
    #return true

def read(userAccountNumber):
    print("read user record")

def update(userAccountNumber):
    print("update user records")
    #find user with account number
    #fetch the content of the file
    #update the content of the file
    #save the file
    #return true

def delete(userAccountNumber):
    print("delete user record")
    #find user with account number
    #delete user record (file)
    #return true

def find():
    print("find user")
    #find user record in the data folder


#create("9017057774", ['shedrack','nwoye','shed@zuri.team','password',400])