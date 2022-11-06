import ast
import json
import os
from os.path import exists
import loginfunctions

def displayInbox():
    existsMessages()
    currentUser = loginfunctions.getUsersName()
    if(os.stat("messagesList.json").st_size == 0):
        #print("No new notifications")
        return

    obj = json.load(open("messagesList.json"))
    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == currentUser):
                    if(obj["all-messages"][messageIndex]["original-count"] != obj["all-messages"][messageIndex]["new-count"]):
                        numNewMessages = obj["all-messages"][messageIndex]["new-count"] - obj["all-messages"][messageIndex]["original-count"]
                        print("\nYou have " + str(numNewMessages) +  " new message(s) from: " + obj["all-messages"][messageIndex]["message-from"])
                        decision = decideReadMessage(currentUser, obj["all-messages"][messageIndex]["message-from"], numNewMessages, obj)
                        if(decision == 2):
                            return
                        else:
                            decideSaveOrDeleteMessage(currentUser, obj["all-messages"][messageIndex]["message-from"], numNewMessages)
                            decideToRespond(currentUser, obj["all-messages"][messageIndex]["message-from"], numNewMessages)
                    
    return

def decideToRespond(user, messageFrom, numNewMessages):
    print("\nWould you like to respond the message(s)?:")
    print("\nPlease select an option:")
    print("[1] Yes, respond the message(s)")
    print("[2] No, exit")
    selection = input("Selection: ")
    
    if selection == "1":
        message = input("Enter the message: ")
        sendMessage(user, messageFrom, message)
        return
    elif selection == "2":
        return
    else:
        print("Incorrect input. Please try again.")
        decideToRespond(user, messageFrom, numNewMessages)
        return

def decideSaveOrDeleteMessage(user, messageFrom, numNewMessages):
    print("\nWould you like to save or delete the message(s)?:")
    print("\nPlease select an option:")
    print("[1] Save the message(s)")
    print("[2] Delete the message(s)")
    selection = input("Selection: ")
    
    if selection == "1":
        saveMessage(user, messageFrom, numNewMessages)
        return
    elif selection == "2":
        deleteMessage(user, messageFrom, numNewMessages)
        return
    else:
        print("Incorrect input. Please try again.")
        decideSaveOrDeleteMessage(user, messageFrom, numNewMessages)
        return

def decideReadMessage(user, messageFrom, numNewMessages, obj):
    print("\nWould you like to read to the message(s)?:")
    print("\nPlease select an option:")
    print("[1] Yes, read the message(s)")
    print("[2] No, exit")
    selection = input("Selection: ")
    
    if selection == "1":
        readNewMessage(user, messageFrom, numNewMessages, obj)
        return
    elif selection == "2":
        return 2
    else:
        print("Incorrect input. Please try again.")
        decideReadMessage(user, messageFrom, numNewMessages, obj)
        return

def readNewMessage(user, messageFrom, numNewMessages, obj):
    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == user and obj["all-messages"][messageIndex]["message-from"] == messageFrom):
                    messageLength = len(obj["all-messages"][messageIndex]["message-list"])
                    print("\nUnread Messages: ")
                    for message in range(messageLength-numNewMessages, messageLength):
                        latestMessage = obj["all-messages"][messageIndex]["message-list"][message]["message"]
                        print(messageFrom + ": " + latestMessage)
    return

def saveMessage(user, messageFrom, numNewMessages):
    obj = json.load(open("messagesList.json"))
    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == user) and obj["all-messages"][messageIndex]["message-from"] == messageFrom:
                    messageLength = len(obj["all-messages"][messageIndex]["message-list"])
                    for message in range(messageLength-numNewMessages, messageLength):
                        obj["all-messages"][messageIndex]["original-count"] += 1
                        open("messagesList.json", "w").write(
                            json.dumps(obj, indent=4)
                        )
                    print("Message(s) has been saved")
                    return
            
    return

def deleteMessage(user, messageFrom, numNewMessages):
    obj = json.load(open("messagesList.json"))

    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == user and obj["all-messages"][messageIndex]["message-from"] == messageFrom):
                    messageLength = len(obj["all-messages"][messageIndex]["message-list"])
                    for message in range(messageLength-numNewMessages, messageLength):
                        obj["all-messages"][messageIndex]["original-count"] += 1
                        obj["all-messages"][messageIndex]["message-list"].pop(messageLength-numNewMessages)
                        open("messagesList.json", "w").write(
                            json.dumps(obj, indent=4)
                        )
                    print("Message successfully deleted")
                    return
    return

def send_message_prompt(usersName):
    existsMessages()
    existsFriendList()
    existsMembershipList()
    membershipStatus = get_membership_status(usersName)
    decide_message_type(usersName, membershipStatus)

def decide_message_type(usersName, membershipStatus):
    if membershipStatus == "Standard":
        print("\nList of friends you can message: ")
        friends = displayFriends(usersName)
        if(friends == "None"):
            return
    elif membershipStatus == "Plus":
        print("\nList of people you can message: ")
        displayAllUsers(usersName)
    else:
        print("membership status not found. Aborting")
        return
    recipient = input("\nEnter the full name of the person you want to send a message to: ")
    if(recipient == usersName):
        print("You cannot message yourself. Please try again.")
        decide_message_type(usersName, membershipStatus)
        return
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
                    print("Message has been sent.")
                    return
    return


def sendMessageType(usersName, membershipStatus, existsRecipient, friendStatus, recipient):
    if membershipStatus == "Standard":
        if friendStatus == True:
            setupMessage(usersName, recipient)
        else:
            print("I'm sorry, you are not friends with that person")
            return "I'm sorry, you are not friends with that person"
    elif membershipStatus == "Plus":
        if existsRecipient == True:
            setupMessage(usersName, recipient)
            return True
        else:
            print("User not found")
    else:
        print("membership status not found. Aborting")
        return

def searchMessage(sender, receiver, messageList):
    countSenderRecevier = 0
    countRecevierSender = 0
    if(os.stat("messagesList.json").st_size == 0):
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
            print("Sending message...")
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
        return False
    else:
        return True

    
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
                    print("You have no friends to message.")
                    return "None"
    return

def displayAllUsers(usersName):
    with open("friendList.txt", "r") as file:
        for line in file:
            friendsList = ast.literal_eval(line)
            if(friendsList["Username"] != usersName):
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
                            print("Friend not found")
                else:
                    #print("You have no friends")
                    return
    return isFriend

def existsFriendList():
    fileExist = exists("friendList.txt")
    if fileExist == 0:
        file = open("friendList.txt", "a")
        file.close()
        return False
    else:
        return True

def existsMembershipList():
    fileExist = exists("membership.txt")
    if fileExist == 0:
        file = open("membership.txt", "a")
        file.close()
        return False
    else:
        return True