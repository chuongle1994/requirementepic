import createAccountFunctions, message, friendList, loginfunctions, os, json
# clear all created files
def delete_files():
    os.remove("currentUserData.txt")
    os.remove("firstname.txt")
    os.remove("friendList.txt")
    os.remove("fullname.txt")
    os.remove("lastname.txt")
    os.remove("membership.txt")
    os.remove("messagesList.json")
    os.remove("passwords.txt")
    os.remove("users.txt")

def test_Messages():
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    createAccountFunctions.promptMembership("1", "tri le", "trile")
    createAccountFunctions.promptMembership("0", "danh le", "danhle")

    #Check if the membership has been logged when registered
    assert message.existsMembershipList() == True

    #Check if message does not exist
    assert message.existsMessages() == False

    #Check if an unfriended user can message another user
    assert message.sendMessageType("danh le", "Standard", True, False, "tri le") == "I'm sorry, you are not friends with that person"

    #Check if a plus member can send a message to another user
    assert message.sendMessageType("tri le", "Plus", True, False, "danh le") == True

    #Check if the message shows up when sent
    message.sendMessage("tri le", "danh le", "test")
    assert message.existsMessages() == True

    #Check if an empty friends list generate correct output
    friendList.createFriendList("tri le")
    assert message.displayFriends("tri le") == "None"

    #Check if the friends list generates
    friendList.createFriendList("danh le")
    friendList.requestFriend("tri le", "danh le")
    friendList.accept("danh le", "tri le")
    loginfunctions.storeUserData("danhle")
    friendList.accept("tri le", "danh le")
    assert message.displayFriends("tri le") == True
    delete_files()

# test deleting message
def test_delete(capsys, monkeypatch):
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    createAccountFunctions.promptMembership("0", "tri le", "trile")
    createAccountFunctions.promptMembership("0", "danh le", "danhle")
    friendList.createFriendList("tri le")
    friendList.createFriendList("danh le")
    friendList.requestFriend("tri le", "danh le")
    friendList.accept("danh le", "tri le")
    # create message txt
    message.existsMessages()

    # send the messages
    message.setupMessage("tri le", "danh le")
    message.sendMessage("tri le", "danh le", "hello")
    message.sendMessage("tri le", "danh le", "hi")

    # assign current user
    loginfunctions.storeUserData("danhle")

    # input selections into user interface
    inputs = iter(["1", "2", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # clear previous prints
    captured = capsys.readouterr()
    message.displayInbox()
    captured = capsys.readouterr()

    
    # test if user interface is correct (read the message, delete the message, no respond)
    assert captured.out == "\nYou have 2 new message(s) from: tri le\n\nWould you like to read to the message(s)?:\n\nPlease select an option:\n[1] Yes, read the message(s)\n[2] No, continue\n\nUnread Messages: \ntri le: hello\ntri le: hi\n\nWould you like to save or delete the message(s)?:\n\nPlease select an option:\n[1] Save the message(s)\n[2] Delete the message(s)\nMessage successfully deleted\n\nWould you like to respond the message(s)?:\n\nPlease select an option:\n[1] Yes, respond the message(s)\n[2] No, continue\n"

    # test receiver message got deleted in the messageList.json file
    obj = json.load(open("messagesList.json"))
    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == "danh le") and obj["all-messages"][messageIndex]["message-from"] == "tri le":
                    # test if receiver successfully read new messages file
                    assert obj["all-messages"][messageIndex]["original-count"] == 2
                    assert obj["all-messages"][messageIndex]["new-count"] == 2
                    # test if receiver successfully save the new messages in file
                    assert obj["all-messages"][messageIndex]["message-list"] == []

    delete_files()

# test replying and saving messages
def test_mes1(capsys, monkeypatch):
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    createAccountFunctions.promptMembership("0", "tri le", "trile")
    createAccountFunctions.promptMembership("0", "danh le", "danhle")
    friendList.createFriendList("tri le")
    friendList.createFriendList("danh le")
    friendList.requestFriend("tri le", "danh le")
    friendList.accept("danh le", "tri le")
    # create message txt
    message.existsMessages()

    # send the messages
    message.setupMessage("tri le", "danh le")
    message.sendMessage("tri le", "danh le", "hello")
    message.sendMessage("tri le", "danh le", "hi")

    # assign current user
    loginfunctions.storeUserData("danhle")

    # input selection
    monkeypatch.setattr('builtins.input', lambda _: "1")

    # clear previous prints
    captured = capsys.readouterr()
    message.displayInbox()
    captured = capsys.readouterr()


    # test receiver interface (read new messages, save messages, respond to sender)
    assert captured.out == "\nYou have 2 new message(s) from: tri le\n\nWould you like to read to the message(s)?:\n\nPlease select an option:\n[1] Yes, read the message(s)\n[2] No, continue\n\nUnread Messages: \ntri le: hello\ntri le: hi\n\nWould you like to save or delete the message(s)?:\n\nPlease select an option:\n[1] Save the message(s)\n[2] Delete the message(s)\nMessage(s) has been saved\n\nWould you like to respond the message(s)?:\n\nPlease select an option:\n[1] Yes, respond the message(s)\n[2] No, continue\nMessage has been sent.\n"

    # test reciver's features
    obj = json.load(open("messagesList.json"))
    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == "danh le") and obj["all-messages"][messageIndex]["message-from"] == "tri le":
                    # test if receiver successfully read new messages file
                    assert obj["all-messages"][messageIndex]["original-count"] == 2
                    assert obj["all-messages"][messageIndex]["new-count"] == 2
                    # test if receiver successfully save the new messages in file
                    assert obj["all-messages"][messageIndex]["message-list"] == [
                {
                    "message": "hello"
                },
                {
                    "message": "hi"
                }
            ]

    # test sender's features
    obj = json.load(open("messagesList.json"))
    if(len(obj) != 0):
        if(len(obj["all-messages"]) != 0):
            for messageIndex in range(len(obj["all-messages"])):
                if(obj["all-messages"][messageIndex]["user"] == "tri le") and obj["all-messages"][messageIndex]["message-from"] == "danh le":
                    # test if sender gets new notification file
                    assert obj["all-messages"][messageIndex]["original-count"] == 0
                    assert obj["all-messages"][messageIndex]["new-count"] == 1
                    # test if sender gets the respond in file
                    assert obj["all-messages"][messageIndex]["message-list"] == [
                {
                    "message": "1"
                }
            ]


    delete_files()





