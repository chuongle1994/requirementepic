import json, os
import ast, loginfunctions, profileFunctions, message
from datetime import date, datetime

# Notification for a student has not yet created a profile
def profileNotification(name):
    notification = 0
    if profileFunctions.checkComplete(name) == 0:
        notification = 1
        # profileFunctions.addProfile()
    return notification


# Creating an empty new student data list for user
def createNewStudentList(name):
    setting = {"Name": name, "newStudent": []}
    settingFile = open("newStudent.txt", "a")
    settingFile.write("{}\n".format(setting))
    settingFile.close()

# Add new student info to current user
def addNewStudentList(name):
    saveList = []

    with open("newStudent.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)
            saveList.append(data)
    
    for user in saveList:
        if user["Name"] != name:
            user["newStudent"].append(name)
    
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"
    
    with open("newStudent.txt", "w") as fw:
        fw.writelines(saveList)

# Notification with new user
def newStudentNotification(name):
    notification = 0
    saveList = []

    with open("newStudent.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saveList.append(data)
    
    for user in saveList:
        if user["Name"] == name and user["newStudent"]:
            print("\nNew Student Notification: ")
            for newStudent in user["newStudent"]:
                print("{} has joined InCollege".format(newStudent))
                notification += 1
            user["newStudent"].clear()
            
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"
        
    with open("newStudent.txt", "w") as file:
        file.writelines(saveList)
    
    return notification


# Creating the file for saving current date
def createDate(name):
    today = date.today()
    dateFormat = today.strftime("%m/%d/%Y")
    setting = {"Name": name, "Last Date": dateFormat}
    settingFile = open("checkDate.txt", "a")
    settingFile.write("{}\n".format(setting))
    settingFile.close()

# Checking the date that have not applied for job in the past 7 days and notified
def NotApplyNotification(name, str_date):
    check = 0

    with open("checkDate.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Name"] == name:
                str_date1 = data["Last Date"]
                # change type for calculation
                date1 = datetime.strptime(str_date1, "%m/%d/%Y")
                today = datetime.strptime(str_date, "%m/%d/%Y")
                delta = today - date1
                if delta.days >= 7:
                    check = 1
                    break

    if check == 1:
        print("\nRemember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
        # applyJobOption()

    return check

# def applyJobOption():
#     print("\nDo you want to apply job now?")
#     print("[1] Yes")
#     print("[2] No")
#     select = input("Please pick an option: ")

#     if select == "1":
#         existsJobs = loginfunctions.displayAllJobTitles()
#         if(existsJobs == True):
#             loginfunctions.selectJobTitle()
#     elif select == "2":
#         return
#     else:
#         print("Invalid selection. Try again")
#         applyJobOption()



# Update the date when applied a job
def updateDate(name, today):
    saveList = []

    with open("checkDate.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saveList.append(data)

    for user in saveList:
        if user["Name"] == name:
            user["Last Date"] = today
            break
    
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"

    with open("checkDate.txt", "w") as fw:
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
        print("You have messages waiting for you.")
    return numNewMessages


#Notify number of applied job
def total_appliedJob():
    name = loginfunctions.getUsersName()
    with open("application.txt", 'r') as fp:
        for line in fp:
            data = ast.literal_eval(line)
            x = len(fp.readlines())
            if data['Name'] == name:
                print("You have currently applied for" + x +"jobs")
