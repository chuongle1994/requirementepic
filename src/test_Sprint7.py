import createAccountFunctions, message, friendList, loginfunctions, os
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
    createAccountFunctions.promptMembership("1", "tri le")
    createAccountFunctions.promptMembership("0", "danh le")

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







