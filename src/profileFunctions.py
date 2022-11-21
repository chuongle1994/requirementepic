from curses.ascii import isdigit
import os
import ast
import loginfunctions, homeFunctions, apiFunctions
from os.path import exists

# Function to create a personal profile with friend lists
def createProfile(username, lastname):
    profile = {"Username": username, "Lastname": lastname, "Title": "", "University": "", "Major": "", "About": "", "Experience": "None", "Education": "None"}
    profileFile = open("profile.txt", "a")
    profileFile.write("{}\n".format(profile))
    profileFile.close()

    apiFunctions.outputProfileApi()

# Function to write data into the base profile
def writeProfileBase(name, title, major, university, information, experience, education):
    profile = []

    # Read file and add it to array
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            profile.append(data)

    # Retrieve data from the array
    for user in profile:
        if user["Username"] == name:
            user["Title"] = title
            user["Major"] = major.title()
            user["University"] = university.title()
            user["About"] = information
            user["Experience"] = experience
            user["Education"] = education
    
    # Write the data into the file
    for index in range(len(profile)):
        profile[index] = str(profile[index]) + "\n"

    with open("profile.txt", "w") as fw:
        fw.writelines(profile)

    # Re-run the output API
    apiFunctions.outputProfileApi()

# Function to write data into the experience
def writeExperience(name, title, employer, start, end, location, desc, newtitle):
    # If the file does not exist, then create it
    fileExist = exists("profExperience.txt")
    if fileExist == 0:
        file = open("profExperience.txt", 'w')
        file.close()

    experience = []

    # Read file and add it to array
    with open("profExperience.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            experience.append(data)

    # Retrieve data from the array
    for user in experience:
        if user["Name"] == name:
            if user["Title"] == title:
                user["Title"] = newtitle
                user["Employer"] = employer
                user["Start"] = start
                user["End"] = end
                user["Location"] = location
                user["Description"] = desc
    
    # Write the data into the file
    for index in range(len(experience)):
        experience[index] = str(experience[index]) + "\n"

    with open("profExperience.txt", "w") as fw:
        fw.writelines(experience)

    apiFunctions.outputProfileApi()

# Function to write data into the education
def writeEducation(name, university, degree, years, newuni):
    # If the file does not exist, then create it
    fileExist = exists("profEducation.txt")
    if fileExist == 0:
        file = open("profEducation.txt", 'w')
        file.close()

    education = []

    # Read file and add it to array
    with open("profEducation.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            education.append(data)

    # Retrieve data from the array
    for user in education:
        if user["Name"] == name:
            if user["School"] == university:
                user["School"] = newuni
                user["Degree"] = degree
                user["Years"] = years
    
    # Write the data into the file
    for index in range(len(education)):
        education[index] = str(education[index]) + "\n"

    with open("profEducation.txt", "w") as fw:
        fw.writelines(education)

    apiFunctions.outputProfileApi()

# Function to add data into the profile
def personalProfile():
    flag = 6
    profileList = []
    userName = loginfunctions.getUsersName()

    # Read data from file to array
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            profileList.append(data)

    # Retrieve save data from the file
    for user in profileList:
        if user["Username"] == userName:
            expFlag = user["Experience"]
            eduFlag = user["Education"]
            if user["Title"] == "":
                flag = 0
            elif user["Major"] == "":
                title = user["Title"]
                flag = 1
            elif user["University"] == "":
                title = user["Title"]
                major = user["Major"]
                flag = 2
            elif user["About"] == "":
                title = user["Title"]
                major = user["Major"]
                university = user["University"]
                flag = 3
    file.close()

    # Perform functions based on saved data
    if flag == 0:
        title = input("Enter your title, or enter 'x' to exit: ")
        if title == 'x':
            return
        flag = 1
        writeProfileBase(userName, title, "", "", "", "None", "None")

    if flag == 1:
        major = input("Enter your major, or enter 'x' to exit: ")
        if major == 'x':
            return
        flag = 2
        writeProfileBase(userName, title, major, "", "", "None", "None")

    if flag == 2:
        university = input("Enter your University, or enter 'x' to exit: ")
        if university == 'x':
            return
        flag = 3
        writeProfileBase(userName, title, major, university, "", "None", "None")
    
    if flag == 3:
        information = input("Enter your information about yourself, or enter 'x' to exit: ")
        if information == 'x':
            return
        writeProfileBase(userName, title, major, university, information, "None", "None")

    if expFlag == "None":
        while(True):
            expCont = input("Would you like to continue to 'Experiences'? [Y/N]: ")
            if expCont == 'Y':
                getExperience()
                break
            elif expCont == 'N':
                return
            else:
                print("Invalid input.")
        flag = 4
        writeProfileBase(userName, title, major, university, information, "-", "None")
    if eduFlag == "None":
        while(True):
            expCont = input("Would you like to continue to 'Education'? [Y/N]: ")
            if expCont == 'Y':
                getEducation()
                break
            elif expCont == 'N':
                return
            else:
                print("Invalid input.")
        flag = 5
        writeProfileBase(userName, title, major, university, information, "-", "-")

    if flag == 6:
        print("Profile already created.")

# Function that allows the user to modify their profile
def editProfile():
    profileList = []
    userName = loginfunctions.getUsersName()

    # Check if the profile has been completely created
    if checkComplete(userName) == 0:
        homeFunctions.goBackToMainOption()
        return

    # Read data from the file to the array
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            profileList.append(data)

    # Retrieve data from the array
    for user in profileList:
        if user["Username"] == userName:
                title = user["Title"]
                major = user["Major"]
                university = user["University"]
                information = user["About"]

    file.close()

    editInput = input("Which of the following would you like to edit?\n[1] Title\n[2] Major\n[3] University\n[4] About me\n[5] Add Experiences\n[6] Add Education\n[7] Edit Experiences\n[8] Edit Education\nInput: ")

    # The allowed actions, the user is allowed to make
    if editInput == '1':
        newTitle = input("New title: ")
        title = newTitle
        writeProfileBase(userName, title, major, university, information, "-", "-")
    elif editInput == '2':
        newMajor = input("New major: ")
        major = newMajor
        writeProfileBase(userName, title, major, university, information, "-", "-")
    elif editInput == '3':
        newUni = input("New university: ")
        university = newUni
        writeProfileBase(userName, title, major, university, information, "-", "-")
    elif editInput == '4':
        newAbout = input("New about me: ")
        information = newAbout
        writeProfileBase(userName, title, major, university, information, "-", "-")
    elif editInput == '5':
        getExperience()
    elif editInput == '6':
        getEducation()
    elif editInput == '7':
        experiences = []
        count = 0
        flag = 0
        with open("profExperience.txt", "r") as file:
            for line in file:
                data = ast.literal_eval(line)
                experiences.append(data)
        file.close()

        print("Here are your experience(s) by title:")
        for user in experiences:
            if user["Name"] == userName:
                print(user["Title"])
                count += 1

        if count == 0:
            print("None")
            return

        selection = input("Please select a title to modify: ")
        for user in experiences:
            flag += 1
            if user["Name"] == userName:
                if user["Title"] == selection:
                    titlein = user["Title"]
                    empin = user["Employer"]
                    startin = user["Start"]
                    endin = user["End"]
                    locationin = user["Location"]
                    descin = user["Description"]
                    break
                elif flag == experiences.count:
                    print("Invalid input")
                    return
        
        expModify = input("[1] Title\n[2] Employer\n[3] Start date\n[4] End date\n[5] Location\n[6] Description\nInput: ")
        if expModify == '1':
            titlein = input("New title: ")
        elif expModify == '2':
            empin = input("New employer: ")
        elif expModify == '3':
            startin = input("New start date: ")
        elif expModify == '4':
            endin = input("New end date: ")
        elif expModify == '5':
            locationin = input("New location: ")
        elif expModify == '6':
            descin = input("New description: ")
        else:
            print("Invalid input")
            return
        writeExperience(userName, selection, empin, startin, endin, locationin, descin, titlein)
    elif editInput == '8':
        education = []
        flag = 0
        with open("profEducation.txt", "r") as file:
            for line in file:
                data = ast.literal_eval(line)
                education.append(data)
        file.close()

        print("Here are your education(s) by university:")
        for user in education:
            if user["Name"] == userName:
                print(user["School"])
        
        selection = input("Please select a university to modify: ")
        for user in education:
            flag += 1
            if user["Name"] == userName:
                if user["School"] == selection:
                    school = user["School"]
                    degree = user["Degree"]
                    years = user["Years"]
                    break
                elif flag == education.count:
                    print("Invalid input")
                    return

        expModify = input("[1] University\n[2] Degree\n[3] Years\nInput: ")
        if expModify == '1':
            school = input("New school: ")
        elif expModify == '2':
            degree = input("New Degree: ")
        elif expModify == '3':
            years = input("New years attended: ")
        else:
            print("Invalid input")
            return
        writeEducation(userName, selection, degree, years, school)
    else:
        print("Invalid input")

# Prompts user if they want to add a profile
def addProfile():
    print("\nDo you want to add your profile?")
    print("[1] Yes")
    print("[2] No")
    
    select = input("Please select an option: ")
    if select == "1":
        personalProfile()
    elif select == "2":
        return
    else:
        print("\nInvalid input. Try selecting an option again.")
        addProfile()

# Allows user to view profile
def printProfile():
    print("\n[1] Do you want to view your profile?")
    print("[2] Do you want to view your friends's profile?")
    print("[3] No")
    select = input("Please pick an option: ")
    if select == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        userName = loginfunctions.getUsersName()
        currentProfile(userName)
        currentExp(userName)
        currentEdu(userName)
    elif select == "2":
        printFriendProfile()
    elif select == "3":
        return
    else:
        print("Invalid input. Try selecting an option again.")
        printProfile()

# Prints the current user profile
def currentProfile(usersName):
    # usersName = loginfunctions.getUsersName()
    print("\nHere is the profile: ")
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Username"] == usersName:
                # print(data)
                break
    print("\nProfile:\n")
    for info in data:
        if info == "Experience" or info == "Education":
            if data[info] == "-":
                break
        print(info + ": " + data[info])
    
    return data

# Prints the current user experience
def currentExp(usersName):
    expList = []
    found = 0
    fileExist = exists("profExperience.txt")
    if fileExist == 0:
        return

    with open("profExperience.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Name"] == usersName:
                expList.append(data)
                found = 1

    if found == 0:
        return
        
    print("\nExperience information:")
    for edu in expList:
        print("")
        for info in edu:
            if info == "Name":
                continue
            print(info + ": " + edu[info])
    
    return expList

# Prints the current user education
def currentEdu(usersName):
    eduList = []
    found = 0
    fileExist = exists("profEducation.txt")
    if fileExist == 0:
        return

    with open("profEducation.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Name"] == usersName:
                eduList.append(data)
                found = 1
    if found == 0:
        return

    print("\nEducation information:")
    for edu in eduList:
        print("")
        for info in edu:
            if info == "Name":
                continue
            print(info + ": " + edu[info])
    
    return eduList


#   user's friends profile interface
def printFriendProfile():
    usersName = loginfunctions.getUsersName()
    print("\n-----Friends Profile-----")
    if displayFriendProfileOption(usersName) == 0:
        return
    option = input("\nWhich profile do you want to view?\nPress [x] to exit\n")

    if option == "x":
        return
    elif option.isdigit() == False:
        print("Inputed option is not a digit. Please choose again")
        printFriendProfile()
    elif friendProfile(int(option), usersName) == 0:
        print("Invalid option. Please choose again")
        printFriendProfile()
    return


# print out the friend's profile based on selected input
def friendProfile(friendIndex, usersName):
    with open("friendList.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Username"] == usersName:
                break
    
    # in the terminal, option starts at 1
    friendIndex-=1

    if friendIndex > len(data["Friend Lists"]) or friendIndex < 0:
        return 0
        
    friendName =  data["Friend Lists"][friendIndex]

    # quit if friend has not create profile
    if checkComplete(friendName) == 0:
        return 0

    print("\nProfile of: ", friendName)
    currentProfile(friendName)
    currentExp(friendName)
    currentEdu(friendName)
    return 1
    
# display the friend list with profile option
def displayFriendProfileOption(usersName):
    numFriends = 0
    option = 1
    print("\nHere is your friend list: \n")
    with open("friendList.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Username"] == usersName:
                if data["Friend Lists"]:
                    numFriends = len(data["Friend Lists"])
                    for friend in data["Friend Lists"]:
                        if checkComplete(friend) == 0:
                            print(f"{friend:20}  No profile")
                            option+=1
                        else:
                            print(f"{friend:20} [{option}]View profile")
                            option+=1
                else:
                    print("You have no friend to view their profile")
                    break
    return numFriends

def saveEducation(name, school_name, degree, years):
    education = {"Name": name, "School": school_name, "Degree": degree, "Years": years}
    eduFile = open("profEducation.txt", "a")
    eduFile.write("{}\n".format(education))
    eduFile.close()

# Function that retrieves education data from user
def getEducation():
    userName = loginfunctions.getUsersName()
    print("Please list your education: ")
    contFlag = 0
    while True:
        # Retrieve input and write into file
        school_name = input("School name: ")
        degree = input("Degree: ")
        years = input("Years attended: ")
        saveEducation(userName, school_name, degree, years)
        while True:
            continueFlag = input("Would you like to add more education? [Y/N]: ")
            if continueFlag == 'Y':
                break
            elif continueFlag == 'N':
                contFlag = 1
                break
            else:
                print("Invalid input, try again.")
        if contFlag == 0:
            continue
        elif contFlag == 1:
            contFlag = 0
            break

def saveExperience(name, title, employer, start, end, location, description):
    experience = {"Name": name, "Title": title, "Employer": employer, "Start": start, "End": end, "Location": location, "Description": description}
    expFile = open("profExperience.txt", "a")
    expFile.write("{}\n".format(experience))
    expFile.close()

# Function that retrieves experience data from user
def getExperience():
    addCount = 0
    contFlag = 0
    userName = loginfunctions.getUsersName()
    # Checks if the user wants to add an experience
    while True:
        expFlag = input("Would you like to add your experience? [Y/N]: ")
        if expFlag == 'Y':
            break
        elif expFlag == 'N':
            return
        else:
            print("Invalid input, try again.")

    # Allows the user to continue adding account until the limit of 3
    while addCount <= 3:
        # Retrieve input, and write into file
        title = input("Title: ")
        employer = input("Employer: ")
        start_date = input("Date started: ")
        end_date = input("Data ended: ")
        location = input("Location: ")
        description = input("Description: ")
        saveExperience(userName, title, employer, start_date, end_date, location, description)
        addCount += 1
        print("Experience entry added!")
        if addCount == 3:
            print("You have met the limit of 3 entries of experience.")
            break
        while True:
            continueFlag = input("Would you like to add more experience? [Y/N]: ")
            if continueFlag == 'Y':
                break
            elif continueFlag == 'N':
                contFlag = 1
                break
            else:
                print("Invalid input, try again.")
        if contFlag == 0:
            continue
        elif contFlag == 1:
            contFlag = 0
            break

def checkComplete(name):
    complete = 1
    profileList = []

    # Read data from the file to the array
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            profileList.append(data)

    # Retrieve data from the array
    for user in profileList:
        if user["Username"] == name:
                title = user["Title"]
                major = user["Major"]
                university = user["University"]
                information = user["About"]
                experience = user["Experience"]
                edu = user["Education"]

    # If the profile creation is incomplete, terminate
    if title == "" or major == "" or university == "" or information == "" or experience == "None" or edu == "None":
        complete = 0
        print("\nDon't forget to complete creating your profile")
        file.close()
        return complete
    file.close()
    return complete
