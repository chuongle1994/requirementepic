from os.path import exists
import os
import json
import linkFunctions

#search for job page
def searchForAJob():
    while(True):
        print("\nPlease select an option:")
        print("[1] Post a job")
        print("[2] Return to previous page")

        selection = input("Selection: ")
        if selection == "1":
            inputJobInfo()
            break
        elif selection == "2":
            displayOptions()
            break
        else:
            print("\nInvalid input. Try selecting an option again.")
            searchForAJob()
    return


def inputJobInfo():

    filesize = os.path.getsize("jobPosts.json")
    if filesize != 0:
        if getNumberOfJobPosts() >= 5:
            print("\nThe system can only permit up to 5 jobs to be posted.")
            return "\nThe system can only permit up to 5 jobs to be posted."


    print("\nPlease provide the following information for the job posting.")
    title = input("Title: ")                      
    description = input("Description: ")     
    employer = input("Employer: ")        
    location = input("Location: ")
    salary = input("Salary: ")    
    createJobPost(title, description, employer, location, salary)
    return

def getNumberOfJobPosts():
    with open("jobPosts.json") as file:
        file_data = json.load(file)
        numberOfJobs = len(file_data["jobs"])
        return numberOfJobs;

def getUsersName():
    usersName = ""
    with open("currentUserData.txt") as file:                 
        while (line := file.readline().rstrip()):   # go through all lines in file, where line = username value in file
            usersName = line
            break
    return usersName

def createJobPost(title, description, employer, location, salary):

    usersName = getUsersName()

    new_data = {
        'jobs' : [
            {
                "title": title,
                "description": description,
                "employer": employer,
                "location": location,
                "salary": salary,
                "poster-name": usersName
            }
        ]
    }

    appendingData = {"title": title,
                    "description": description,
                    "employer": employer,
                    "location": location,
                    "salary": salary,
                    "poster-name": usersName
                    }

    writeJobPost(new_data, appendingData, "jobPosts.json")

def writeJobPost(jobObject, appendingData, fileName):
    
    filesize = os.path.getsize(fileName)
    
    if filesize == 0:
        with open(fileName, 'w') as file:
            json.dump(jobObject, file)
    else:
        with open(fileName, "r+") as file:
            file_data = json.load(file)

            file_data["jobs"].append(appendingData)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
    print("\nYour job has been posted.") 
    return


#find someone you know page
def findSomeone():
    print("\nunder construction")
    response = "\nunder construction"
    return response

#skill1 page
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
    # Add navigation links
    linkFunctions.navigationLinks()
    linkFunctions.selectLinks()
    
    print("\nPlease select an option:")
    print("[1] Search for a job / internship")
    print("[2] Find someone you know")
    print("[3] Learn a new skill")
    print("[4] Return to previous level")
    selection = input("Selection: ")

    if selection == "1":
        searchForAJob()
        return
    elif selection == "2":
        findSomeone()
        return
    elif selection == "3":
        learnSkill()
        return
    elif selection == "4":
        clearFile("currentUserData.txt")
        return
    else:
        print("\nInvalid input. Try selecting an option again.")
        displayOptions()

def existsJobPostsFile():
    jobPosts = exists("jobPosts.json")
    if jobPosts == 0:
        userFile = open("jobPosts.json", "w")
        userFile.close()

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

def existsFirstLastFullNameFile():
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

def existsCurrentUserData():
    currentUserData = exists("currentUserData.txt")
    if currentUserData ==0:
        currentUserData = open("currentUserData.txt","w")
        currentUserData.close()

def existsLanguageFile():
    currentLanguage = exists("language.txt")
    if currentLanguage ==0:
        currentLanguage = open("language.txt","w")
        currentLanguage.close()

def clearFile(filename):
    open(filename, 'w').close()
    return

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

def storeUserData(user):
    print("storing user data")
    userIndex = 0
    nameIndex = 0
    userFullName = ""
    with open("users.txt") as file:                 
        while (line := file.readline().rstrip()):   # go through all lines in file, where line = username value in file
            if line == user:                        # if line matches username input
                break
            else:
                userIndex += 1                      # keep track of username index in file
                continue

    with open("fullname.txt") as file:                 
        while (line := file.readline().rstrip()):   
            if userIndex == nameIndex:
                userFullName = line
                break
            else:
                nameIndex += 1
                continue

    userDataFile = open("currentUserData.txt", "a")
    userDataFile.write("{}\n".format(userFullName))
    userDataFile.close()
    return
    

    
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
            storeUserData(user)
            isSuccessfulLogin = True
        else:                                                      
            print("Incorrect username / password, please try again\n")


    displayOptions()