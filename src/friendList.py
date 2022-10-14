import os
import ast
import loginfunctions

# Function for creating an empty friend list and pending list for user
def createFriendList(username):
    friendList = {"Username": username, "Friend Lists": [], "Pending Lists": []}
    friendListFile = open("friendList.txt", "a")
    friendListFile.write("{}\n".format(friendList))
    friendListFile.close()

# Function for providing options to search students
def search():
    #clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\nDo you want to connect with other students?")
    print("[1] Search by lastname")
    print("[2] Search by university")
    print("[3] Search by major")

    select = input("Please pick an option(0 to exit): ")
    if select == "1":
        inputLastName()
    elif select == "2":
        inputUniversity()
    elif select == "3":
        inputMajor()
    elif select == "0":
        return
    else:
        print("Invalid input. Try selecting an option again.")
        search()

def inputLastName():
    usersName = loginfunctions.getUsersName()
    lastname = input("\nEnter the lastname to search for students: ")
    found = searchLastName(usersName, lastname)
    if found == 0:
        enterAgain("User not found", inputLastName)
    elif found == 1:
        requestOption()

# Function to search for students by lastname
def searchLastName(usersName, lastname):  
    print("\nHere is the search result:")
    found = 0
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Lastname"] == lastname and data["Username"] != usersName:
                print(data["Username"])
                found = 1
    return found


# When result no found (callback funct)
def enterAgain(searchMsg, callback):
    # message for not found result
    print(searchMsg)
    print("\nDo you want to search again?")
    #yes
    print("[1] Yes")
    #no
    print("[2] No")
    select = input("Select an option: ")
    if select == "1":
        #do the action again
        callback()
    elif select == "2":
        #jump to next screen
        return
    else:
        print("Invalid selection. Please try again.")
        enterAgain(searchMsg, callback)
  

def inputUniversity():
    usersName = loginfunctions.getUsersName()
    university = input("\nEnter the university to search for students: ")
    found = searchUniversity(usersName, university)
    if found == 0:
        enterAgain("User not found", searchUniversity)
    elif found == 1:
        requestOption()

# search for students by university
def searchUniversity(usersName, university):
    found = 0
    print("\nHere is the search result:")
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["University"] == university and data["Username"] != usersName:
                print(data["Username"])
                found = 1
    return found

def inputMajor():
    usersName = loginfunctions.getUsersName()
    major = input("\nEnter the major to search for students: ")
    found = searchMajor(usersName, major)
    if found == 0:
        enterAgain("User not found", searchMajor)
    elif found == 1:
        requestOption()

# search for students by major
def searchMajor(usersName, major):  
    found = 0
    print("\nHere is the search result:")
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Major"] == major and data["Username"] != usersName:
                print(data["Username"])
                found = 1
    return found
    

def requestOption():
    print("\nDo you want to request friend with people you find?")
    print("[1] Yes")
    print("[2] No")

    select = input("Please pick an option: ")
    if select == "1":
        inputFriend()
        userNetwork()
    elif select == "2":
        userNetwork()
    else:
        print("Invalid input. Try selecting an option again.")
        requestOption()


def inputFriend():
    currentUser = loginfunctions.getUsersName()
    friend = input("\nEnter the name you want to send friend request: ")
    found, inFriendList, inPendingList = requestFriend(currentUser, friend)
    if found == 0:
        enterAgain("User not found", inputFriend)
    elif inFriendList == 0 and inPendingList == 0:
        print("You successfully send friend request!")
    elif inFriendList == 1 or inPendingList == 1:
        enterAgain("You already sent request before!", inputFriend)


# When the search successes, option for sending a request to connect
def requestFriend(currentUser, friend):
    found = 0
    inFriendList = 0
    inPendingList = 0
    profileList = []
    
    with open("friendList.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            profileList.append(data)
    
    for user in profileList:
        if user["Username"] == friend:
            found = 1
            if currentUser in user["Pending Lists"]:
                inPendingList = 1
            elif currentUser in user["Friend Lists"]:
                inFriendList = 1
        if found == 1 and inFriendList == 0 and inPendingList == 0:
            user["Pending Lists"].append(currentUser)
            break
    
    # write pending list to profile
    for index in range(len(profileList)):
        profileList[index] = str(profileList[index]) + "\n"

    with open("friendList.txt", "w") as fw:
        fw.writelines(profileList)

    return found, inFriendList, inPendingList


# after login, check the pending list
# if there is pending list, go to function they can decide you accept or reject
def pendingData():
    os.system('cls' if os.name == 'nt' else 'clear')
  
    usersName = loginfunctions.getUsersName()
    with open("friendList.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Username"] == usersName:
              break
    
    if data["Pending Lists"]:
        print("\nYou have a friend request!")
        print("Here is the list who want to connect wih you: ")
        print(data["Pending Lists"])
        decision()
          
                
# Function for deciding to accept or reject
def decision():
    print("\nPlease select the options to deicde to accept or reject: ")
    print("[1] Accept")
    print("[2] Reject")
    print("[3] Skip")
    select = input("Please select an option: ")

    if select == "1": 
        inputAccept()
    elif select == "2":
        inputReject()
    elif select == "3":
        return
    else:
        print("Invalid input. Try selecting an option again.")
        decision()

def inputAccept():
    usersName = loginfunctions.getUsersName()
    friend = input("\nEnter the name you want to accept: ")
    found = accept(usersName, friend)

    if found == 0:
        enterAgain("Cannot accept friend request. User not found", inputAccept)

    # check again if there is any pending left
    pendingData()


# Function for accpeting of friend request
def accept(usersName, friend):
    found = 0
    listControl = []
    
    with open("friendList.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)
            listControl.append(data)

    # Modify data
    for user in listControl:
        if user["Username"] == usersName and friend in user["Pending Lists"]:
            user["Friend Lists"].append(friend)
            user["Pending Lists"].remove(friend)
            found = 1
        if user["Username"] == friend:
            user["Friend Lists"].append(usersName)
            found = 1
        
    for index in range(len(listControl)):
        listControl[index] = str(listControl[index]) + "\n"
        
    with open("friendList.txt", "w") as fw:
        fw.writelines(listControl)

    return found

def inputReject():
    usersName = loginfunctions.getUsersName()
    friend = input("\nEnter the name you want to reject: ")
    found = reject(usersName, friend)

    if found == 0:
        enterAgain("Cannot reject friend request. User not found", inputReject)

      #may need to call pending again
    pendingData()

    
# Function for rejecting of friend request
def reject(usersName, friend):
    found = 0
    listControl = []
    
    with open("friendList.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)
            listControl.append(data)

    # Modify data
    for user in listControl:
        if user["Username"] == usersName and friend in user["Pending Lists"]:
            user["Pending Lists"].remove(friend)
            found = 1
          
    for index in range(len(listControl)):
        listControl[index] = str(listControl[index]) + "\n"
        
    with open("friendList.txt", "w") as fw:
        fw.writelines(listControl)
    
    return found

    
        
# Function for option of "show my network"
def userNetwork():
    print("\nDo you want to see your network?")
    print("[1] Yes")
    print("[2] No")
    select = input("Please select an option: ")

    if select == "1":
        currentFriendList()
        disconnectOption()
    elif select == "2":
        return
    else:
        print("Invalid input. Please try again.")
        userNetwork()

    
# Function for print the current friend list
def currentFriendList():
    usersName = loginfunctions.getUsersName()
    print("\nHere is your friend list: ")
    with open("friendList.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Username"] == usersName:
                if data["Friend Lists"]:
                    print(*data["Friend Lists"], sep = ",")
                else:
                    print("None")
                break


def disconnectOption():
    print("\nDo you want to disconnect with someone?")
    print("[1] Yes")
    print("[2] No")
    select = input("Please select an option: ")

    if select == "1":
        inputDisconnect()
    elif select == "2":
        return
    else:
        print("Invalid input. Please try again.")
        disconnectOption()

def inputDisconnect():
    usersName = loginfunctions.getUsersName()
    friend = input("\nEnter the name you want to disconnect: ")
    found = disconnect(usersName, friend)

    if found == 0:
        enterAgain("User does not in your Friend List", inputDisconnect)


# Function for option of disconnecting
def disconnect(usersName, friend):
    found = 0
    listControl = []
    
    with open("friendList.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)
            listControl.append(data)

    # Modify data
    for user in listControl:
        if user["Username"] == usersName and friend in user["Friend Lists"]:
            found = 1
            user["Friend Lists"].remove(friend)
        if user["Username"] == friend and usersName in user["Friend Lists"]:
            found = 1
            user["Friend Lists"].remove(usersName)
        
    for index in range(len(listControl)):
        listControl[index] = str(listControl[index]) + "\n"
        
    with open("friendList.txt", "w") as fw:
        fw.writelines(listControl)

    return found