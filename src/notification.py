import ast, loginfunctions
from datetime import date, datetime

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
def newStudentNotification():
    name = loginfunctions.getUsersName()
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
            user["newStudent"].clear()
            
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"
        
    with open("newStudent.txt", "w") as file:
        file.writelines(saveList)

# Creating the file for saving current date
def createDate(name):
    today = date.today()
    dateFormat = today.strftime("%m/%d/%Y")
    setting = {"Name": name, "Last Date": dateFormat}
    settingFile = open("checkDate.txt", "a")
    settingFile.write("{}\n".format(setting))
    settingFile.close()

# Checking the date that have not applied for job in the past 7 days and notified
def NotApplyNotification():
    check = 0
    today = date.today()
    name = loginfunctions.getUsersName()

    with open("checkDate.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Name"] == name:
                str_date1 = data["Last Date"]
                str_date2 = today.strftime("%m/%d/%Y")
                date1 = datetime.strptime(str_date1, "%m/%d/%Y")
                date2 = datetime.strptime(str_date2, "%m/%d/%Y")
                delta = date2 - date1
                if delta.days >= 7:
                    check = 1
                    break

    if check == 1:
        print("\nRemember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")

    return check

# Update the date when applied a job
def updateDate():
    today = date.today()
    dateFormat = today.strftime("%m/%d/%Y")
    name = loginfunctions.getUsersName()
    saveList = []

    with open("checkDate.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            saveList.append(data)

    for user in saveList:
        if user["Name"] == name:
            user["Last Date"] = dateFormat
            break
    
    for index in range(len(saveList)):
        saveList[index] = str(saveList[index]) + "\n"

    with open("checkDate.txt", "w") as fw:
        fw.writelines(saveList)