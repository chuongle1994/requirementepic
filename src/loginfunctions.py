from os.path import exists
import os
import uuid
import json
import linkFunctions, friendList, profileFunctions, message, homeFunctions, notification, apiFunctions
import ast
from datetime import date

#search for job page
def searchForAJob():
    displayNotifications()
    notification.total_appliedJob(getUsersName())

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
                jobIndex = inputJobIndex()
                deleteJobByIndex(int(jobIndex) - 1)
            break
        elif selection == "3":
            existsJobs = displayAllJobTitles()
            if(existsJobs == True):
                selectJobTitle()
            break
        elif selection == "4":
            displayApps(getUsersName())
            selectJobTitle()
            break
        elif selection == "5":
            displayNotApps(getUsersName())
            selectJobTitle()
            break
        elif selection == "6":
            displaySave(getUsersName())
            selectJobTitle()
            break
        elif selection == "7":
            displayOptions()
            break
        else:
            print("\nInvalid input. Try selecting an option again.")
            searchForAJob()
    return

def deleteApplicationsByIndex(index):

    fileExist = exists("applications.txt")

    # Checks if the save file exists
    if fileExist == 0:
        file = open("applications.txt", "a")
        file.close()

    
    obj = json.load(open("jobPosts.json"))
    jobID = obj["job-posts"][index]["jobID"]

    countIndex = 1
    arrIndexes = []

    with open("applications.txt", 'r') as file:
        lines = file.readlines()
    file.close()
    
    with open("applications.txt", 'r') as file:
        for line in file:
            data = ast.literal_eval(line)
            if(data["jobID"] == jobID):
                arrIndexes.append(countIndex)
            countIndex = countIndex + 1 


    lineNumber = 1
    with open("applications.txt", 'w') as file:
        for line in (lines):
            for position in arrIndexes:
                if(lineNumber != position):
                    file.write(line)
                lineNumber += 1

    print("Successfully removed applications from job post")

def deleteSavedJobByIndex(index):

    fileExist = exists("savedListings.txt")

    # Checks if the save file exists
    if fileExist == 0:
        file = open("savedListings.txt", "a")
        file.close()

    
    obj = json.load(open("jobPosts.json"))
    jobID = obj["job-posts"][index]["jobID"]

    countIndex = 1
    arrIndexes = []

    with open("savedListings.txt", 'r') as file:
        lines = file.readlines()
    file.close()
    
    with open("savedListings.txt", 'r') as file:
        for line in file:
            data = ast.literal_eval(line)
            if(data["jobID"] == jobID):
                arrIndexes.append(countIndex)
            countIndex = countIndex + 1 


    lineNumber = 1
    with open("savedListings.txt", 'w') as file:
        for line in (lines):
            for position in arrIndexes:
                if(lineNumber != position):
                    file.write(line)
                lineNumber += 1
                

    print("Successfully removed saved status from users for this job posting")

def selectJobTitle():
    print("\nWould you like to select and display a job?")
    print("[1] Yes")
    print("[2] No")
    selection = input("Selection: ")

    if selection == "1":
        index = input("Enter the title index: ")
        numJobs = getNumberOfJobPosts()
        if(index.isdigit()):
            if(int(index) <= numJobs and int(index) > 0):
                displaySelectedJob(int(index)-1)
            else:
                print("Incorrect input. Please try again.")
                selectJobTitle()
            return
        else:
            print("Input is not an integer. Try again.")
            selectJobTitle()
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
        print("\nTitle: " + obj["job-posts"][index]["title"])
        print("Description: " + obj["job-posts"][index]["description"])
        print("Employer: " + obj["job-posts"][index]["employer"])
        print("Location: " + obj["job-posts"][index]["location"])
        print("Salary: " + obj["job-posts"][index]["salary"])
        applyInput = input("\nWhich of the following would you like to do?\n[1] Apply for the job\n[2] Save the listing\n[3] Unsave the listing\n[4] Return\nInput: ")
        if applyInput == '1':
            jobID, jobindex, name, str_date, access = applyForJob(index, getUsersName())
            if(access == "access denied"):
                return
            else:
                fillJobApplication(jobID, jobindex, name, str_date)
                return
        elif applyInput == '2':
            saveJob(index, getUsersName())
            return
        elif applyInput == '3':
            unsaveJob(index)
            return
        elif applyInput == '4':
            print("Returning...")
            return
        else:
            print("Invalid input, returning to home screen.")
            return
    else:
        print("No jobs found")


def displayAllJobTitles():
    isFound = False
    currentUser = getUsersName()
    if(os.stat("jobPosts.json").st_size == 0):
        print("\nNo jobs found")
        return isFound
    obj = json.load(open("jobPosts.json"))
    if(len(obj["job-posts"]) != 0):
        for i in range(len(obj["job-posts"])):
            if(len(obj["job-posts"][i]["applicants-list"]) != 0):
                for j in range(len(obj["job-posts"][i]["applicants-list"])):
                    if( obj["job-posts"][i]["applicants-list"][j]["name"] == currentUser):
                        print("\n[" + str(i+1) + "] " + "[Applied] " + "ID(" + obj["job-posts"][i]["jobID"] + "): " + obj["job-posts"][i]["title"])
                        continue
                    else:
                        print("\n[" + str(i+1) + "] " + "ID(" + obj["job-posts"][i]["jobID"] + "): " + obj["job-posts"][i]["title"])
            else:
                print("\n[" + str(i+1) + "] " + "ID(" + obj["job-posts"][i]["jobID"] + "): " + obj["job-posts"][i]["title"])
        isFound = True
    else:
        print("\nNo job posts to be displayed")
    return isFound

def inputJobIndex():
    jobIndex = input("\nEnter the Job index you'd like to delete: ")
    numJobs = getNumberOfJobPosts()
    if(jobIndex.isdigit()):
        if(int(jobIndex) >= 1 and int(jobIndex) <= numJobs):
            return str(jobIndex)
        else:
            print("Input is out of bounds. Try again.")
            return inputJobIndex()
    else:
        print("Input is not an integer. Try again.")
        return inputJobIndex()


def deleteJobByIndex(index):
    found = False
    currentUser = getUsersName()

    obj = json.load(open("jobPosts.json"))
    if(len(obj) != 0):
        if(len(obj["job-posts"]) != 0):
            if(obj["job-posts"][index]["poster-name"] == currentUser):
                sendNotificationsToUsers("deleted", index)
                deleteSavedJobByIndex(index)
                deleteApplicationsByIndex(index)
                obj["job-posts"].pop(index)
                found = True
            else:
                print("\nYou cannot delete a post you did not create.")
                return
        if(found == True):
            open("jobPosts.json", "w").write(
                json.dumps(obj, indent=4)
            )
        else:
            print("\nJob ID not found")
    else:
        print("\nJob ID not found")

    return

def sendNotificationsToUsers(status, index):
    fileExist = exists("userNotifications.txt")
    if fileExist == 0:
        file = open("userNotifications.txt", "a")
        file.close()

    obj = json.load(open("jobPosts.json"))
    if(len(obj) != 0):
        if(len(obj["job-posts"]) != 0):
            for i in range(len(obj["job-posts"])):
                if(i == index):
                    for j in range(len(obj["job-posts"][i]["applicants-list"])):
                        name = obj["job-posts"][i]["applicants-list"][j]["name"]
                        jobID = obj["job-posts"][i]["jobID"]
                        title = obj["job-posts"][i]["title"]
                        employer = obj["job-posts"][i]["employer"]
                        writeNotification(status, name, jobID, title, employer)


def writeNotification(status, name, jobID, title, employer):
    output = {"status": status, "name": name, "jobID" : jobID, "title" : title, "employer" : employer}
    notificationFile = open("userNotifications.txt", "a")
    notificationFile.write("{}\n".format(output))
    notificationFile.close()

def displayNotifications():
    # Adds file information into array
    currentUser = getUsersName()
    fileExist = exists("userNotifications.txt")
    notifications = []


    # Checks if the file exists in the system
    if fileExist == 0:
        file = open("userNotifications.txt", "a")
        file.close()

    with open("userNotifications.txt", "r") as file:
         for line in file:
             data = ast.literal_eval(line)
             notifications.append(data)
    file.close()

    # Checks if the user has already applied to a job
    for user in notifications:
         if user["name"] == currentUser:
            print("Your application " + user["jobID"] + " for " + user["title"] + " at " + user["employer"] + " has been " + user["status"])
            deleteNotificationPrompt(user["jobID"])
    return

def deleteNotificationPrompt(jobID):
    print("Would you like to delete this notification?")
    print("[1] Yes")
    print("[2] No")
    answer = input("Selection: ")
    if(answer == "1"):
        deleteNotification(jobID)
    elif answer == "2":
        return
    else:
        print("Invalid input. Try again")
        deleteNotificationPrompt(jobID)

def deleteNotification(jobID):
    index = 0
    with open("userNotifications.txt", 'r') as file:
        for line in file:
            data = ast.literal_eval(line)
            if(data["jobID"] == jobID):
                print("index found: " + str(index))
                break
            index = index + 1
        lines = file.readlines() 

    with open("userNotifications.txt", 'w') as file:
        for id, line in enumerate(lines):
            if(id == index):
                file.write(line)

    print("Successfully deleted notification")
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
    createJobPost(jobID, title, description, employer, location, salary, getUsersName(), applicantsList)
    notification.saveNewJob(getUsersName(), title)
    return

def getNumberOfJobPosts():
    with open("jobPosts.json") as file:
        file_data = json.load(file)
        numberOfJobs = len(file_data["job-posts"])
        return numberOfJobs

def applyForJob(index, name):
    # save date of today with string format
    today = date.today()
    str_date = today.strftime("%m/%d/%Y")

    fileExist = exists("applications.txt")
    jobID = ""

    # Checks if the file exists in the system
    if fileExist == 0:
        file = open("applications.txt", "a")
        file.close()

    obj = json.load(open("jobPosts.json"))
    if obj["job-posts"][index]["poster-name"] == name:
        print("You cannot apply for your own posted job")
        return jobID, index, name, str_date, "access denied"
    else:
        jobID = obj["job-posts"][index]["jobID"]

    if(len(obj) != 0):
        if(len(obj["job-posts"]) != 0):
            for i in range(len(obj["job-posts"])):
                if (i == index):
                    for j in range(len(obj["job-posts"][i]["applicants-list"])):
                        if(name == obj["job-posts"][i]["applicants-list"][j]["name"]):
                            print("You have already applied for this job")
                            return jobID, index, name, str_date, "access denied"

    print("Poster: " + obj["job-posts"][index]["poster-name"])
    obj["job-posts"][index]["applicants-list"].append({"name":name})
    open("jobPosts.json", "w").write(
                json.dumps(obj, indent=4)
    )
    return jobID, index, name, str_date, "access granted"

def fillJobApplication(jobID, index, name, str_date):
    # Input for job application
    gradDate = input("Enter your graduation date: ")
    workDate = input("Enter the your preferred starting date: ")
    desc = input("Why do you think you're fit for this job?\nParagraph: ")
    writeApp(jobID, index, name, gradDate, workDate, desc)
    notification.updateDate(getUsersName(), str_date)
    # Re-run the output API
    apiFunctions.outputAppliedJobsAPI()

def writeApp(jobID, index, name, gradDate, workDate, desc):
    output = { "jobID": jobID, "Index" : index, "Name" : name, "gradDate" : gradDate, "workDate" : workDate, "Desc" : desc}
    appFile = open("applications.txt", "a")
    appFile.write("{}\n".format(output))
    appFile.close()

    # api.appliedJobsApi()

def displayApps(name):
    jobListing = []
    indices = []
    fileExist = exists("applications.txt")

    # Checks if the file exists
    if fileExist == 0:
        file = open("applications.txt", "a")
        file.close()

    # Check if there are any job posts
    if os.stat("jobPosts.json").st_size == 0:
        print("\nNo jobs found")
        return

    # Reads file into job listing
    with open("applications.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            jobListing.append(data)
    file.close()

    # Check if there are any jobs you have applied to
    if len(jobListing) == 0:
        print("You have not applied to any jobs")
        return

    # Stores applied jobs indices in array
    for user in jobListing:
        if user["Name"] == name:
            indices.append(user["Index"])
    
    # Prints the jobs with the indices in the array
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

    return indices

def displayNotApps(name):
    jobListing = []
    indices = []
    fileExist = exists("applications.txt")

    # Checks if the file exists
    if fileExist == 0:
        file = open("applications.txt", "a")
        file.close()

    # Checks if there are any job postings
    if os.stat("jobPosts.json").st_size == 0:
        print("\nNo jobs found")
        return

    # Reads file into an array
    with open("applications.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            jobListing.append(data)
    file.close()

    # Checks if the user has applied to every job
    if len(jobListing) == os.stat("jobPosts.json").st_size:
        print("You have applied to every single job posting")
        return

    # Stores applied indices into array
    for user in jobListing:
        if user["Name"] == name:
            indices.append(user["Index"])
    
    # Prints the job listings that are not in the indices array
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

    return indices
    

def saveJob(index, name):
    saved = []
    fileExist = exists("savedListings.txt")
    obj = json.load(open("jobPosts.json"))
    jobID = obj["job-posts"][index]["jobID"]

    # Checks if the save file exists
    if fileExist == 0:
        file = open("savedListings.txt", "a")
        file.close()

    # Stores file into an array
    with open("savedListings.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saved.append(data)
    file.close()

    # Check if the user has already saved this job
    for user in saved:
        if user["Name"] == name:
            if user["Index"] == index:
                print("You have already saved this job")
                return

    # Write job saved listing into file
    output = {"jobID": jobID, "Index" : index, "Name" : name}
    saveFile = open("savedListings.txt", "a")
    saveFile.write("{}\n".format(output))
    saveFile.close()

    print("Successfully saved the job listing")
    # Re-run the output API
    apiFunctions.outputSavedJobsAPI()

def unsaveJob(index):
    currentUser = getUsersName()
    fileExist = exists("savedListings.txt")

    # Checks if the save file exists
    if fileExist == 0:
        file = open("savedListings.txt", "a")
        file.close()

    obj = json.load(open("jobPosts.json"))
    jobID = obj["job-posts"][index]["jobID"]

    countIndex = 1
    found = False

    with open("savedListings.txt", 'r') as file:
        lines = file.readlines()
    file.close()
    
    with open("savedListings.txt", 'r') as file:
        for line in file:
            data = ast.literal_eval(line)
            if(data["jobID"] == jobID and data["Name"] == currentUser):
                found = True
                break
            countIndex = countIndex + 1 

    if(found == False):
        print("This job was not saved originally")
        return

    lineNumber = 1
    with open("savedListings.txt", 'w') as file:
        for line in (lines):
            if(lineNumber != countIndex):
                file.write(line)
            lineNumber += 1

    print("Successfully removed saved job")

def displaySave(name):
    saved = []
    indices = []
    fileExist = exists("savedListings.txt")

    # Checks if the file exists
    if fileExist == 0:
        file = open("savedListings.txt", "a")
        file.close()

    # Writes file data into an array
    with open("savedListings.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saved.append(data)

    # Check if the user has anything saved
    if len(saved) == 0:
        print("You have nothing saved")
        return
    
    # Store indices of saved jobs into array
    for user in saved:
        if user["Name"] == name:
            indices.append(user["Index"])

    # Print the indices (saved) of job posts that have been saved
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
    
    return indices

def getUsersName():
    usersName = ""
    with open("currentUserData.txt") as file:                 
        while (line := file.readline().rstrip()):   # go through all lines in file, where line = username value in file
            usersName = line
            break
    return usersName

def createJobPost(jobID, title, description, employer, location, salary, postername, applicantsList):

    # usersName = getUsersName()

    new_data = {
        'job-posts' : [
            {
                "jobID": jobID,
                "title": title,
                "description": description,
                "employer": employer,
                "location": location,
                "salary": salary,
                "poster-name": postername,
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
                    "poster-name": postername,
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
    # Re-run the output API
    apiFunctions.outputJobApi()
    return


#find someone you know page
def findSomeone():
    homeFunctions.connectPeople()
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
    #clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

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
    print("[8] Send message")
    print("[9] View message")
    print("[0] Return to previous level")
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
        message.send_message_prompt(getUsersName())
        return
    elif selection == "9":
        message.displayInbox()
        return
    elif selection == "0":
        displayOptions()
        # clearFile("currentUserData.txt")
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
    # save date of today with string format
    today = date.today()
    str_date = today.strftime("%m/%d/%Y")

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
            notification.NotApplyNotification(getUsersName(), str_date)
            notification.profileNotification(getUsersName())
            notification.messageNotification(getUsersName())
            notification.newJobNotification(getUsersName())
            notification.delete_job(getUsersName())
            notification.newStudentNotification(getUsersName())
            friendList.pendingScreen()
            friendList.search()
            isSuccessfulLogin = True
        else:                                                      
            print("Incorrect username / password, please try again\n")

    displayOptions()
