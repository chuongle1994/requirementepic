from os.path import exists

#Checks if the user file exists, if not create one
userExists = exists("users.txt")
if userExists == 0:
    userFile = open("users.txt", "w")
    userFile.close()

#Checks if the password file exists, if not create one
passExists = exists("passwords.txt")
if passExists == 0:
    passFile = open("passwords.txt", "w")
    passFile.close()

#Home screen
print("Please select an option:")
print("[1] Log in")
print("[2] Create an Account")
select = input("Selection: ")

#Selection functions
if select == "1":
    user = input("Username: ")
    password = input("Password: ")
elif select == "2":
    #Count the current number of account created
    numAccounts = 0
    with open("users.txt") as file:
        while (line := file.readline().rstrip()):
            numAccounts += 1
    file.close()

    #Check if the user is able to create an account
    if numAccounts == 5:
        print(
            "All permitted accounts have been created, please come back later")
    else:
        flag = 0
        upperFlag = 0
        digitFlag = 0
        specialFlag = 0
        while True:
            newUser = input("Enter your desired username: ")
            #Check if there is a duplicate username
            with open("users.txt") as file:
                while (line := file.readline().rstrip()):
                    if line == newUser:
                        print("Username already exists, try again")
                        flag = 1
            #Restart if there is a duplicate
            if flag == 1:
                flag = 0
                file.close()
                continue
            else:
                break
        userFile = open("users.txt", "a")
        userFile.write("{}\n".format(newUser))
        userFile.close()
        #Check if password meets requirements
        while True:
            newPass = input("Enter your desired password: ")
            if (len(newPass) < 8 or len(newPass) > 12):
                print("Please enter a password between 8-12 characters")
                continue
            for letter in newPass:
                if letter.isupper():
                    upperFlag = 1
                if letter.isdigit():
                    digitFlag = 1
                if not letter.isalnum():
                    specialFlag = 1
            if upperFlag == 1 and digitFlag == 1 and specialFlag == 1:
                break
            else:
                upperFlag = 0
                digitFlag = 0
                specialFlag = 0
                print(
                    "Please have an uppercase, digit, or special character in your password"
                )
                continue
        passFile = open("passwords.txt", "a")
        passFile.write("{}\n".format(newPass))
        passFile.close()
else:
    print("Invalid option, terminating program")
    exit()
