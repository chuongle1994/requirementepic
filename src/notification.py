import json, os
import ast, profileFunctions, message
from os.path import exists
from datetime import date, datetime

# Notification for a student has not yet created a profile
def profileNotification(name):
    notification = 0
    if profileFunctions.checkComplete(name) == 0:
        notification = 1
        # profileFunctions.addProfile()
    return notification


# Add new student info to current user
def addNewStudentList(name):
    saveList = []

    with open("friendList.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)
            saveList.append(data)
    
    for user in saveList:
        if user["Username"] != name:
            user["newStudent"].append(name)
    
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"
    
    with open("friendList.txt", "w") as fw:
        fw.writelines(saveList)

# Notification with new user
def newStudentNotification(name):
    notification = 0
    saveList = []

    with open("friendList.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saveList.append(data)
    
    for user in saveList:
        if user["Username"] == name and user["newStudent"]:
            print("\nNew Student: ")
            for newStudent in user["newStudent"]:
                print("{} has joined InCollege".format(newStudent))
                notification += 1
            user["newStudent"].clear()
            
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"
        
    with open("friendList.txt", "w") as file:
        file.writelines(saveList)
    
    return notification


# Creating the file for saving current date, empty list for new job
def storeJobData(name):
    today = date.today()
    dateFormat = today.strftime("%m/%d/%Y")
    setting = {"Name": name, "Last Date": dateFormat, "New Job": []}
    settingFile = open("jobNotification.txt", "a")
    settingFile.write("{}\n".format(setting))
    settingFile.close()

# Checking the date that have not applied for job in the past 7 days and notified
def NotApplyNotification(name, str_date):
    notification = 0

    with open("jobNotification.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Name"] == name:
                str_date1 = data["Last Date"]
                # change type for calculation
                date1 = datetime.strptime(str_date1, "%m/%d/%Y")
                today = datetime.strptime(str_date, "%m/%d/%Y")
                delta = today - date1
                if delta.days >= 7:
                    notification = 1
                    break

    if notification == 1:
        print("\nRemember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")

    return notification

# Update the date when applied a job
def updateDate(name, today):
    saveList = []

    with open("jobNotification.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saveList.append(data)

    for user in saveList:
        if user["Name"] == name:
            user["Last Date"] = today
            break
    
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"

    with open("jobNotification.txt", "w") as fw:
        fw.writelines(saveList)


# Notification for a student who has new messages from another studet
def messageNotification(name):
    message.existsMessages()
    numNewMessages = 0

    if(os.stat("messagesList.json").st_size == 0):
        return
    obj = json.load(open("messagesList.json"))

    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == name):
                    if(obj["all-messages"][messageIndex]["original-count"] != obj["all-messages"][messageIndex]["new-count"]):
                        numNewMessages = obj["all-messages"][messageIndex]["new-count"] - obj["all-messages"][messageIndex]["original-count"]

    if numNewMessages > 0:
        print("\nYou have messages waiting for you.")
    return numNewMessages


# Save the new job info in user data
def saveNewJob(name, jobTitle):
    saveList = []

    with open("jobNotification.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saveList.append(data)

    for user in saveList:
        if user["Name"] != name:
            user["New Job"].append(jobTitle)
    
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"

    with open("jobNotification.txt", "w") as fw:
        fw.writelines(saveList)

# Notification for a new job
def newJobNotification(name):
    notification = 0
    saveList = []

    with open("jobNotification.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saveList.append(data)

    for user in saveList:
        if user["Name"] == name and user["New Job"]:
            print("\nNew Job: ")
            for job in user["New Job"]:
                print("A new job {} has been posted".format(job))
                notification += 1
            user["New Job"].clear()
            
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"

    with open("jobNotification.txt", "w") as fw:
        fw.writelines(saveList)
    
    return notification


# Notification for the number of applied job
def total_appliedJob(name):
    numAppliedJob = 0
    fileExist = exists("applications.txt")

    # Checks if the save file exists
    if fileExist == 0:
        file = open("applications.txt", "a")
        file.close()

    with open("applications.txt", 'r') as fp:
        for line in fp:
            data = ast.literal_eval(line)
            numAppliedJob = len(fp.readlines())
            if numAppliedJob > 0 and data['Name'] == name:
                print("\nYou have currently applied for {} jobs".format(numAppliedJob))
    
    return numAppliedJob

#Add notification when students already applied for a deleted job
def delete_job(name):
    notification = 0
    fileExist = exists("userNotifications.txt")

    if fileExist == 0:
        file = open("userNotifications.txt", "a")
        file.close()
    
    with open("userNotifications.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["name"] == name and data["status"] == "deleted":
                print ("A job " + data["title"] + " that you applied for has been deleted")
                notification = 1

    return notification
