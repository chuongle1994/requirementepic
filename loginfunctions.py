from os.path import exists

#search for job page
def searchForJob():
    print("\nunder construction")
    response = "\nunder construction"
    return response

#find someone you know page
def findSomeone():
    print("\nunder construction")
    response = "\nunder construction"
    return response
def frontendDevelopment():
    print("\nunder construction")
    response = "\nunder construction"
    return response

#skill2 page
def backendDevelopment():
    print("\nunder construction")
    response = "\nunder construction"
    return response

#skill3 page
def databaseDesign():
    print("\nunder construction")
    response = "\nunder construction"
    return response

#skill4 page
def agileMethodologies():
    print("\nunder construction")
    response = "\nunder construction"
    return response

#skill5 page
def gitVersionControl():
    print("\nunder construction")
    response = "\nunder construction"
    return response

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
def existsUserPasswordFile():
    userExists = exists("users.txt")
    if userExists == 0:
        userFile = open("users.txt", "w")
        userFile.close()
    #Checks if the password file exists, if not create one
    passExists = exists("passwords.txt")
    if passExists == 0:
        passFile = open("passwords.txt", "w")
        passFile.close()
    fnameExists = exists("firstname.txt")
    if fnameExists ==0:
        fnameFile = open("firstname.txt","w")
        fnameFile.close()
    lnameExists = exists("lastname.txt")
    if lnameExists ==0:
        lnameFile = open("lastname.txt","w")
        lnameFile.close()
    fullnameExists = exists("fullname.txt")
    if fullnameExists ==0:
        fullnameFile = open("fullname.txt","a+")
        fullnameFile.close()

def validateLogin(user, password):
    userIndex = 0              # get username index in file
    passwordIndex = 0          # get password index in file
    userFound = False   
    passwordFound = False

    with open("users.txt") as file:                 
        while (line := file.readline().rstrip()):   # go through all lines in file, where line = username value in file
            if line == user:                        # if line matches username input
                userFound = True
                break
            else:
                userIndex += 1                      # keep track of username index in file
                continue

    with open("passwords.txt") as file:
        while (line := file.readline().rstrip()):   # go through all lines in file where line = password value in file
            if line == password and userIndex == passwordIndex:                    # if line matches password input
                passwordFound = True
                break
            else:
                passwordIndex += 1                  # keep track of password index in file
                continue

    if userFound == True and passwordFound == True:
        return True
    else:
        return False
    

    
def loginPage():

    isSuccessfulLogin = False     

    while(isSuccessfulLogin == False):  
        # check username
        user = input("Username: ")                      # input username

        # check password    
        password = input("Password: ")                  # input password

        # validate login
        validation = validateLogin(user, password)

        # both username and password were found and are on same index                
        if validation == True: 
            print("\nYou have successfully logged in")
            isSuccessfulLogin = True
        else:                                                      
            print("Incorrect username / password, please try again\n")


    displayOptions()