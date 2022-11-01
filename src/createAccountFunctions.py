import linkFunctions, friendList, profileFunctions, loginfunctions, ast
def membership(username):
    membershipList = {"Username": username, "type": ""}
    membershipFile = open("membership.txt", "a")
    membershipFile.write("{}\n".format(membershipList))
    membershipFile.close()      
def membershipOption():
    userName = loginfunctions.getUsersName()    
    option_membership = input("Do you want to be a plus member? You will be charged $10 per month.(1 = yes or 0 = no):")
    if (option_membership == "1"):
        #membership_type = "Plus"
        write_membership(userName,"Plus)")
    elif (option_membership == "0"):
        #membership_type = "Standard"
        write_membership(userName,"Standard")
    else:
        print("Invalid input")
def write_membership(username,type):
    memberOption =[]
    with open("membership.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            memberOption.append(data)
    # Retrieve data from the array
    for user in memberOption:
        if user["Username"] == username:
            user["type"] = type           
    # Write the data into the file
    for index in range(len(memberOption)):
        memberOption[index] = str(memberOption[index]) + "\n"
    with open("membership.txt", "w") as fw:
        fw.writelines(memberOption)
def checkAccNum():
    #Count the current number of account created
        numAccounts = 0
        with open("users.txt") as file:
            while (line := file.readline().rstrip()):
                numAccounts += 1
        file.close()
        # student account can be created upto 10
        if numAccounts >= 10:
            return 1
        else:
            return 0
            
def createAcc():
    #Check account number does not exceed limit
    accLimit = checkAccNum()
    if accLimit == 1:
            print("All permitted accounts have been created, please come back later")
    else:
        #Create username
        while(True):
            newUser = input("Enter your username: ")
            userFlag = checkUser(newUser)
            if(userFlag == 1):
                continue
            else:
                break
        #Create password
        while(True):
            newPass = input("Enter your desired password: ")
            passFlag = checkPass(newPass)

            if passFlag == 1:
                continue
            else:
                break
        newFirstname = input("Enter your first name: ")
        newLastname = input("Enter your last name: ")
        newFullname = newFirstname + " " + newLastname
        membership(newUser)
        membershipOption()
        #If requirements are met, store data into files
        storeData(newUser, newPass, newFirstname, newLastname, newFullname)
        linkFunctions.firstControlsSetting(newFullname)
        linkFunctions.firstLanguageSetting(newFullname)
        profileFunctions.createProfile(newFullname, newLastname)
        friendList.createFriendList(newFullname)

    return

def checkUser(newUser):
    #Check if there is a duplicate username
    with open("users.txt") as file:
        while (line := file.readline().rstrip()):
            if line == newUser:
                print("Username already exists, please try again")
                return 1
    return 0

def checkPass(newPass):
        upperFlag = 0
        digitFlag = 0
        specialFlag = 0
        #Check if the password meets character limit
        if (len(newPass) < 8 or len(newPass) > 12):
            print("Please enter a password between 8-12 characters")
            return 1

        #Checks if the password meet minimum requirements
        for letter in newPass:
            if letter.isupper():
                upperFlag = 1
            if letter.isdigit():
                digitFlag = 1
            if not letter.isalnum():
                specialFlag = 1

        if upperFlag == 1 and digitFlag == 1 and specialFlag == 1:
            return 0
        else:
            upperFlag = 0
            digitFlag = 0
            specialFlag = 0
            print("Please have an uppercase, digit, or special character in your password")
            return 1

def storeData(newUser, newPass, newFirstname, newLastname, newFullname):
    userFile = open("users.txt", "a")
    userFile.write("{}\n".format(newUser))
    userFile.close()
    passFile = open("passwords.txt", "a")
    passFile.write("{}\n".format(newPass))
    passFile.close()
    passFile = open("firstname.txt", "a")
    passFile.write("{}\n".format(newFirstname))
    passFile.close()
    passFile = open("lastname.txt", "a")
    passFile.write("{}\n".format(newLastname))
    passFile.close()
    passFile = open("fullname.txt", "a")
    passFile.write("{}\n".format(newFullname))
    passFile.close()
    return