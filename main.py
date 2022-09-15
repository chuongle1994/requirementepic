from os.path import exists

#search for job page
def searchForJob():
    return print("\nunder construction")

#find someone you know page
def findSomeone():
    return print("\nunder construction")

#skill1 page
def frontendDevelopment():
    return print("\nunder construction")

#skill2 page
def backendDevelopment():
    return print("\nunder construction")

#skill3 page
def databaseDesign():
    return print("\nunder construction")

#skill4 page
def agileMethodologies():
    return print("\nunder construction")

#skill5 page
def gitVersionControl():
    return print("\nunder construction")

#select skill menu
def learnSkill():
    print("\nPlease select a skill:")
    print("[1] Frontend Development")
    print("[2] Backend Development")
    print("[3] Database Design")
    print("[4] Agile Methodologies")
    print("[5] Git Version Control")
    print("[6] Return to previous level")
    selection = input("Selection: ")

    if selection == "1":
        frontendDevelopment()
        return
    elif selection == "2":
        backendDevelopment()
        return
    elif selection == "3":
        databaseDesign()
        return
    elif selection == "4":
        agileMethodologies()
        return
    elif selection == "5":
        gitVersionControl()
        return
    elif selection == "6":
        displayOptions()
        return
    else:
        print("\nInvalid input. Try selecting a skill again.")
        learnSkill()
        return

#select options menu
def displayOptions():
    print("\nPlease select an option:")
    print("[1] Search for a job / internship")
    print("[2] Find someone you know")
    print("[3] Learn a new skill")
    selection = input("Selection: ")

    if selection == "1":
        searchForJob()
        return
    elif selection == "2":
        findSomeone()
        return
    elif selection == "3":
        learnSkill()
        return
    else:
        print("\nInvalid input. Try selecting an option again.")
        displayOptions()
        return
    


def main():
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
        userIndex = 0;              # get username index in file
        passwordIndex = 0;          # get password index in file
        isSuccessfulLogin = False     
        userFound = False   
        passwordFound = False

        while(isSuccessfulLogin == False):  

            # check username
            user = input("Username: ")                      # input username
            with open("users.txt") as file:                 
                while (line := file.readline().rstrip()):   # go through all lines in file, where line = username value in file
                    if line == user:                        # if line matches username input
                        userFound = True
                        break
                    else:
                        userIndex += 1                      # keep track of username index in file
                        continue

            # check password    
            password = input("Password: ")                  # input password
            with open("passwords.txt") as file:
                while (line := file.readline().rstrip()):   # go through all lines in file where line = password value in file
                    if line == password:                    # if line matches password input
                        passwordFound = True
                        break
                    else:
                        passwordIndex += 1                  # keep track of password index in file
                        continue

            # both username and password were found and are on same index                
            if userFound == True and passwordFound == True and userIndex == passwordIndex: 
                print("\nYou have successfully logged in")
                isSuccessfulLogin = True
            else:                                                      
                print("Incorrect username / password, please try again\n")
                userIndex = 0
                passwordIndex = 0

        displayOptions()

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

main()