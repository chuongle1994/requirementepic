# import ast
# import loginfunctions

# Function for create a personal profile with friend lists
def createProfile(username, lastname):
    profile = {"Username": username, "Lastname": lastname, "University": "", "Major": ""}
    profileFile = open("profile.txt", "a")
    profileFile.write("{}\n".format(profile))
    profileFile.close()

######################## save for later ############################
# # add information in personal profile
# def personalProfile():
#     university = input("Enter your University: ")
#     major = input("Enter your major: ")

#     usersName = loginfunctions.getUsersName()
#     listControl = []
#     with open("profile.txt", "r") as f:
#         for line in f:
#             data = ast.literal_eval(line)
#             listControl.append(data)
#     # Modify data
#     for user in listControl:
#         if user["Username"] == usersName:
#             user["University"] = university
#             user["Major"] = major
    
#     for index in range(len(listControl)):
#         listControl[index] = str(listControl[index]) + "\n"
#     with open("profile.txt", "w") as fw:
#         fw.writelines(listControl)

#     printProfile()
        

# def addProfile():
#     print("\nDo you want to add your profile?")
#     print("[1] Yes")
#     print("[2] No")
    
#     select = input("Please select an option: ")
#     if select == "1":
#         personalProfile()
#     elif select == "2":
#         return
#     else:
#         print("\nInvalid input. Try selecting an option again.")
#         addProfile()


# def printProfile():
#     print("\nDo you want to view your profile?")
#     print("[1] Yes")
#     print("[2] No")
#     select = input("Please pick an option: ")
#     if select == "1":
#         currentProfile()
#     elif select == "2":
#         return
#     else:
#         print("Invalid input. Try selecting an option again.")
#         printProfile()

# def currentProfile():
#     usersName = loginfunctions.getUsersName()
#     print("\nHere is your profile: ")
#     with open("profile.txt", "r") as file:
#         for line in file:
#             data = ast.literal_eval(line)
#             if data["Username"] == usersName:
#                 print(data)
#                 break
        