import ast
from os.path import exists
# def send_message(usersName):
#     recipient = input("\nEnter the username of the person you want to send a message to: ")
#     with open("membership.txt", "r") as file:
#         for line in file:
#             data = ast.literal_eval(line)
#     with open("friendList.txt", "r") as f:
#         for FriendLine in f:
#             FriendData = ast.literal_eval(FriendLine)
#     with open("profile.txt", "r") as file1:                                  
#         for data1 in file1:
#             lines = ast.literal_eval(data1)    
#             if data["Membership_Type"] == "Standard" and data["Username"] == usersName:
#                 if FriendData["Friend Lists"] == recipient and FriendData["Username"] != usersName:
#                         message = input("\nPlease enter your message: ")
#                         #store_message(sender, recipient, message)
#                         print("\nMessage Has Been Sent.\n")
#                         return
#                 else: 
#                         print("I'm sorry, you are not friends with that person.")
#             if data["Membership_Type"] == "Plus" and data["Username"] == usersName:   
#                 if lines["Username"] == recipient and lines["Username"] != usersName:
#                     message = input("\nPlease enter your message: ")
#                     #store_message(sender, recipient, message)
#                     print("\nMessage Has Been Sent.\n")
#                     return
#                 else:
#                     print("I'm sorry, This person is not in the system yet.")
#                     return

def send_message_prompt(usersName):
    existsMessages()
    existsFriendList()
    existsMembershipList()
    membershipStatus = get_membership_status(usersName)
    decide_message_type(usersName, membershipStatus)

def decide_message_type(usersName, membershipStatus):
    recipient = input("\nEnter the username of the person you want to send a message to: ")
    message = input("\nEnter the message: ")
    existsRecipient = isRecipient(recipient)
    friendStatus = isFriend(usersName, recipient)
    sendMessageType(usersName, membershipStatus, existsRecipient, friendStatus, recipient, message)
    return

def sendMessageType(usersName, membershipStatus, existsRecipient, friendStatus, recipient, message):
    if membershipStatus == "Standard":
        displayFriends()
        if friendStatus == True:
            sendMessage(usersName, recipient, message)
        else:
            print("I'm sorry, you are not friends with that person")
    elif membershipStatus == "Plus":
        if existsRecipient == True:
            displayAllUsers()
            sendMessage(usersName, recipient, message)
        else:
            print("User not found")
    else:
        print("membership status not found. Aborting")
        return

    
def sendMessage(sender, receiver, message):
    return

def existsMessages():
    messages = exists("messageslist.json")
    if messages == 0:
        userFile = open("messagesList.json", "w")
        userFile.close()

    
def isRecipient(recipient):
    found  = False
    with open("friendList.txt", "r") as file:
        for line in file:
            friendsList = ast.literal_eval(line)
            if(friendsList["Username"] == recipient):
                found = True
    return found

def displayFriends(usersName):
    with open("friendList.txt", "r") as file:
        for line in file:
            friendsList = ast.literal_eval(line)
            if(friendsList["Username"] == usersName):
                if(len(friendsList["Friend Lists"]) != 0):
                    for friend in friendsList["Friend Lists"]:
                        print(friend)
                else:
                    #print("You have no friends to display.")
                    return

def displayAllUsers():
    with open("friendList.txt", "r") as file:
        for line in file:
            friendsList = ast.literal_eval(line)
            print(friendsList["Username"])


def get_membership_status(usersName):
    found = False
    with open("membership.txt", "r") as file:
        for line in file:
            membershipList = ast.literal_eval(line)
            print(membershipList)
            if(membershipList["fullName"] == usersName):
                print("membership is: " + membershipList["Membership_Type"])
                found = True
                return membershipList["Membership_Type"]
    if found == False:
        print("User's membership cannot be found. Aborting.")
    return found


def isFriend(usersName, recipient):
    isFriend = False
    with open("friendList.txt", "r") as file:
        for line in file:
            friendsList = ast.literal_eval(line)
            print(friendsList)
            if(friendsList["Username"] == usersName):
                if(len(friendsList["Friend Lists"]) != 0):
                    for friend in friendsList["Friend Lists"]:
                        if(friend == recipient):
                            print("friend has been found!")
                            isFriend = True
                        else:
                            print("friend not found")
                else:
                    print("You have no friends")
    return isFriend

def existsFriendList():
    fileExist = exists("friendsList.txt")
    if fileExist == 0:
        file = open("friendsList.txt", "a")
        file.close()

def existsMembershipList():
    fileExist = exists("membership.txt")
    if fileExist == 0:
        file = open("membership.txt", "a")
        file.close()