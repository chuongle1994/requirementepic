from os.path import exists
import os
import uuid
import json
import linkFunctions, friendList, profileFunctions
import ast

#search for job page
def searchForAJob():
    while(True):
        print("\nPlease select an option:")
        print("[1] Post a job")
        print("[2] Delete a job post")
        print("[3] Display all job titles")
        print("[4] Display jobs you have applied for")
        print("[5] Display jobs you have not applied for")
        print("[6] Display saved jobs")
        print("[7] Return to previous page")

        selection = input("Selection: ")
        if selection == "1":
            inputJobInfo()
            break
        elif selection == "2":
            existsJobs = displayAllJobTitles()
            if(existsJobs == True):
                inputJobID()
            break
        elif selection == "3":
            existsJobs = displayAllJobTitles()
            if(existsJobs == True):
                selectJobTitle()
            break
        elif selection == "4":
            displayApps()
            break
        elif selection == "5":
            displayNotApps()
            break
        elif selection == "6":
            displaySave()
            break
        elif selection == "7":
            displayOptions()
            break
        else:
            print("\nInvalid input. Try selecting an option again.")
            searchForAJob()
    return

def selectJobTitle():
    print("\nWould you like to select and display a job?")
    print("[1] Yes")
    print("[2] No")
    selection = input("Selection: ")

    if selection == "1":
        index = int(input("Enter the title index: "))
        displaySelectedJob(index-1)
        return
    elif selection == "2":
        print("Exiting")
        return
    else:
        print("\nInvalid input. Try selecting an option again.")
        selectJobTitle()

    return



def displaySelectedJob(index):
    if(os.stat("jobPosts.json").st_size == 0):
        print("No jobs found")
        return
    
    obj = json.load(open("jobPosts.json"))
    if(len(obj) != 0):
        print("Title: " + obj["job-posts"][index]["title"])
        print("Description: " + obj["job-posts"][index]["description"])
        print("Employer: " + obj["job-posts"][index]["employer"])
        print("Location: " + obj["job-posts"][index]["location"])
        print("Salary: " + obj["job-posts"][index]["salary"])
        applyInput = input("Which of the following would you like to do?\n[1] Apply for the job\n[2] Save the listing\n[3] Return\nInput: ")
        if applyInput == '1':
            applyForJob(index, getUsersName())
            return
        elif applyInput == '2':
            saveJob(index, getUsersName())
            return
        elif applyInput == '3':
            print("Returning...")
            return
        else:
            print("Invalid input, returning to home screen.")
            return


def displayAllJobTitles():
    isFound = False
    if(os.stat("jobPosts.json").st_size == 0):
        print("\nNo jobs found")
        return isFound
    obj = json.load(open("jobPosts.json"))
    if(len(obj["job-posts"]) != 0):
        for i in range(len(obj["job-posts"])):
            print("\n[" + str(i+1) + "] " + "ID(" + obj["job-posts"][i]["jobID"] + "): " + obj["job-posts"][i]["title"])
        isFound = True
    else:
        print("\nNo job posts to be displayed")
    return isFound

def inputJobID():
    jobID = input("\nEnter the Job ID you'd like to delete: ")  
    deleteJobByID(jobID)
    return

def deleteJobByID(id):
    found = False
    currentUser = getUsersName()

    obj = json.load(open("jobPosts.json"))
    if(len(obj) != 0):
        for i in range(len(obj["job-posts"])):
            if obj["job-posts"][i]["jobID"] == id:
                if(obj["job-posts"][i]["poster-name"] == currentUser):
                    obj["job-posts"].pop(i)
                    found = True
                    break
                else:
                    print("\nYou cannot delete a post you did not create.")
                    return
        if(found == True):
            print("\nDeleting ID: " + id)
            open("jobPosts.json", "w").write(
                json.dumps(obj, indent=4)
            )
        else:
            print("\nJob ID not found")
    else:
        print("\nJob ID not found")

    return

def inputJobInfo():

    filesize = os.path.getsize("jobPosts.json")
    if filesize != 0:
        if getNumberOfJobPosts() >= 10:
            print("\nThe system can only permit up to 10 jobs to be posted.")
            return "\nThe system can only permit up to 10 jobs to be posted."


    print("\nPlease provide the following information for the job posting.")
    jobID = str(uuid.uuid4())[:8]
    title = input("Title: ")                      
    description = input("Description: ")     
    employer = input("Employer: ")        
    location = input("Location: ")
    salary = input("Salary: ")    
    applicantsList = []
    createJobPost(jobID, title, description, employer, location, salary, applicantsList)
    return

def getNumberOfJobPosts():
    with open("jobPosts.json") as file:
        file_data = json.load(file)
        numberOfJobs = len(file_data["job-posts"])
        return numberOfJobs

def applyForJob(index, name):
    fileExist = exists("applications.txt")
    jobListing = []

    if fileExist == 0:
        file = open("applications.txt", "a")
        file.close()

    obj = json.load(open("jobPosts.json"))
    print(obj["job-posts"][index]["poster-name"])
    if obj["job-posts"][index]["poster-name"] == name:
        print("You cannot apply for your own posted job")
        return

    with open("applications.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            jobListing.append(data)
    file.close()

    for user in jobListing:
        if user["Name"] == name:
            if user["Index"] == index:
                print("You have already applied for this job")
                return

    gradDate = input("Enter your graduation date: ")
    workDate = input("Enter the your preferred starting date: ")
    desc = input("Why do you think you're fit for this job?\nInput: ")
    writeApp(index, name, gradDate, workDate, desc)

def writeApp(index, name, gradDate, workDate, desc):
    output = { "Index" : index, "Name" : name, "gradDate" : gradDate, "workDate" : workDate, "Desc" : desc}
    appFile = open("applications.txt", "a")
    appFile.write("{}\n".format(output))
    appFile.close()

def displayApps(name):
    jobListing = []
    indices = []
    fileExist = exists("applications.txt")
    if fileExist == 0:
        file = open("applications.txt", "a")
        file.close()

    if os.stat("jobPosts.json").st_size == 0:
        print("\nNo jobs found")
        return

    with open("applications.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            jobListing.append(data)
    file.close()

    if len(jobListing) == 0:
        print("You have not applied to any jobs")
        return

    for user in jobListing:
        if user["Name"] == name:
            indices.append(user["Index"])
    
    obj = json.load(open("jobPosts.json"))
    if(len(obj["job-posts"]) != 0):
        for i in range(len(obj["job-posts"])):
            flag = 0
            for j in range(len(indices)):
                if i == indices[j]:
                    flag = 1
                    break
            if flag == 1:
                print("\n[" + str(i+1) + "] " + "ID(" + obj["job-posts"][i]["jobID"] + "): " + obj["job-posts"][i]["title"])

    selectJobTitle()

def displayNotApps(name):
    jobListing = []
    indices = []
    fileExist = exists("applications.txt")
    if fileExist == 0:
        file = open("applications.txt", "a")
        file.close()
        
    if os.stat("jobPosts.json").st_size == 0:
        print("\nNo jobs found")
        return

    with open("applications.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            jobListing.append(data)
    file.close()

    if len(jobListing) == 0:
        print("You have not applied to any jobs")
        return

    for user in jobListing:
        if user["Name"] == name:
            indices.append(user["Index"])
    
    obj = json.load(open("jobPosts.json"))
    if(len(obj["job-posts"]) != 0):
        for i in range(len(obj["job-posts"])):
            flag = 0
            for j in range(len(indices)):
                if i == indices[j]:
                    flag = 1
                    break
            if flag == 0:
                print("\n[" + str(i+1) + "] " + "ID(" + obj["job-posts"][i]["jobID"] + "): " + obj["job-posts"][i]["title"])

    selectJobTitle()

def saveJob(index, name):
    output = { "Index" : index, "Name" : name}
    saveFile = open("savedListings.txt", "a")
    saveFile.write("{}\n".format(output))
    saveFile.close()

def displaySave(name):
    saved = []
    indices = []

    with open("savedListings.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saved.append(data)

    if len(saved) == 0:
        print("You have nothing saved")
        return
    
    for user in saved:
        if user["Name"] == name:
            indices.append(user["Index"])

    obj = json.load(open("jobPosts.json"))
    if(len(obj["job-posts"]) != 0):
        for i in range(len(obj["job-posts"])):
            flag = 0
            for j in range(len(indices)):
                if i == indices[j]:
                    flag = 1
                    break
            if flag == 1:
                print("\n[" + str(i+1) + "] " + "ID(" + obj["job-posts"][i]["jobID"] + "): " + obj["job-posts"][i]["title"])
    
    selectJobTitle()

def getUsersName():
    usersName = ""
    with open("currentUserData.txt") as file:                 
        while (line := file.readline().rstrip()):   # go through all lines in file, where line = username value in file
            usersName = line
            break
    return usersName

def createJobPost(jobID, title, description, employer, location, salary, applicantsList):

    usersName = getUsersName()

    new_data = {
        'job-posts' : [
            {
                "jobID": jobID,
                "title": title,
                "description": description,
                "employer": employer,
                "location": location,
                "salary": salary,
                "poster-name": usersName,
                "applicants-list": applicantsList
            }
        ]
    }

    appendingData = {"jobID": jobID,
                    "title": title,
                    "description": description,
                    "employer": employer,
                    "location": location,
                    "salary": salary,
                    "poster-name": usersName,
                    "applicants-list": applicantsList
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

            file_data["job-posts"].append(appendingData)
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
    print("[4] Show my network")
    print("[5] Create profile")
    print("[6] Edit profile")
    print("[7] View profile")
    print("[8] Return to previous level")
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
        friendList.userNetwork()
        return
    elif selection == "5":
        profileFunctions.addProfile()
        return
    elif selection == "6":
        profileFunctions.editProfile()
        return
    elif selection == "7":
        profileFunctions.printProfile()
        return 
    elif selection == "8":
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
            friendList.pendingScreen()
            friendList.search()
            isSuccessfulLogin = True
        else:                                                      
            print("Incorrect username / password, please try again\n")

    displayOptions()