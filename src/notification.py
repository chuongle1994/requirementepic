import ast, loginfunctions

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
