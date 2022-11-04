import ast
import json
import os
from os.path import exists

def send_message_prompt(usersName):
    existsMessages()
    existsFriendList()
    existsMembershipList()
    membershipStatus = get_membership_status(usersName)
    decide_message_type(usersName, membershipStatus)

def decide_message_type(usersName, membershipStatus):
    recipient = input("\nEnter the full name of the person you want to send a message to: ")
    message = input("\nEnter the message: ")
    existsRecipient = isRecipient(recipient)
    friendStatus = isFriend(usersName, recipient)
    sendMessageType(usersName, membershipStatus, existsRecipient, friendStatus, recipient)
    sendMessage(usersName, recipient, message)
    return

def sendMessage(usersName, recipient, message):
    obj = json.load(open("messagesList.json"))

    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == recipient) and obj["all-messages"][messageIndex]["message-from"] == usersName:
                    obj["all-messages"][messageIndex]["message-list"].append({"message":message})
                    obj["all-messages"][messageIndex]["new-count"] += 1
                    open("messagesList.json", "w").write(
                        json.dumps(obj, indent=4)
                    )
                    return

    return


def sendMessageType(usersName, membershipStatus, existsRecipient, friendStatus, recipient):
    if membershipStatus == "Standard":
        displayFriends()
        if friendStatus == True:
            setupMessage(usersName, recipient)
        else:
            print("I'm sorry, you are not friends with that person")
    elif membershipStatus == "Plus":
        if existsRecipient == True:
            displayAllUsers()
            setupMessage(usersName, recipient)
        else:
            print("User not found")
    else:
        print("membership status not found. Aborting")
        return

def searchMessage(sender, receiver, messageList):
    countSenderRecevier = 0
    countRecevierSender = 0
    print(os.stat("messagesList.json").st_size)
    if(os.stat("messagesList.json").st_size == 0):
        print("file is empty")
        createMessage(sender, receiver, messageList)
        createMessage(receiver, sender, messageList)
        return

    obj = json.load(open("messagesList.json"))
    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == sender and obj["all-messages"][messageIndex]["message-from"] == receiver):
                    countSenderRecevier += 1
                elif(obj["all-messages"][messageIndex]["user"] == receiver and obj["all-messages"][messageIndex]["message-from"] == sender):
                    countRecevierSender += 1
        
        if(countSenderRecevier == 1 and countRecevierSender == 1):
            print("Sending message")
        elif(countSenderRecevier == 0 and countRecevierSender == 0):
            createMessage(sender, receiver, messageList)
            createMessage(receiver, sender, messageList)
            print("\nCreating both message streams")
        elif(countSenderRecevier == 1 and countRecevierSender == 0):
            createMessage(receiver, sender, messageList)
        elif(countSenderRecevier == 0 and countRecevierSender == 1):
            createMessage(sender, receiver, messageList)
        else:
            print("error")

    else:
        print("\nNo messages")

    return

    
def setupMessage(sender, receiver):
    messageList = []
    searchMessage(sender, receiver, messageList)
    return

def createMessage(sender, receiver, messageList):

    new_data = {
        'all-messages' : [
            {
                "user": sender,
                "message-from": receiver,
                "original-count": 0,
                "new-count": 0,
                "message-list": messageList
            }
        ]
    }

    appendingData = {"user": sender,
                    "message-from": receiver,
                    "original-count": 0,
                    "new-count": 0,
                    "message-list": messageList
                    }

    writeMessage(new_data, appendingData, "messagesList.json")

def writeMessage(jobObject, appendingData, fileName):
    
    filesize = os.path.getsize(fileName)
    
    if filesize == 0:
        with open(fileName, 'w') as file:
            json.dump(jobObject, file)
    else:
        with open(fileName, "r+") as file:
            file_data = json.load(file)

            file_data["all-messages"].append(appendingData)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
    return

def existsMessages():
    messages = exists("messagesList.json")
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
            if(membershipList["fullName"] == usersName):
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
    fileExist = exists("friendList.txt")
    if fileExist == 0:
        file = open("friendList.txt", "a")
        file.close()

def existsMembershipList():
    fileExist = exists("membership.txt")
    if fileExist == 0:
        file = open("membership.txt", "a")
        file.close()