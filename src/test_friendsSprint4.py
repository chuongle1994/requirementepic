import linkFunctions, createAccountFunctions, loginfunctions, ast, friendList, profileFunctions

# clear all created files
def clear_all_files():
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")
    loginfunctions.clearFile("currentUserData.txt")
    loginfunctions.clearFile("controls.txt")
    loginfunctions.clearFile("profile.txt")
    loginfunctions.clearFile("friendList.txt")

# making sure all friends show up
def test_showFriends():
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults sms to 1 or "on"
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le") # making an account defaults sms to 1 or "on"
    profileFunctions.createProfile("danh le", "le")
    profileFunctions.createProfile("tri le", "le")
    friendList.createFriendList("danh le")
    friendList.createFriendList("tri le")
    friendList.requestFriend("tri le", "danh le")
    friendList.accept("danh le", "tri le")
    loginfunctions.storeUserData("danhle")
    assert friendList.currentFriendList() == 1
    clear_all_files()

# removing friends from friends list
def test_removeFriend():
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults sms to 1 or "on"
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le") # making an account defaults sms to 1 or "on"
    profileFunctions.createProfile("danh le", "le")
    profileFunctions.createProfile("tri le", "le")
    friendList.createFriendList("danh le")
    friendList.createFriendList("tri le")
    friendList.requestFriend("tri le", "danh le")
    friendList.accept("danh le", "tri le")
    loginfunctions.storeUserData("danhle")
    assert friendList.currentFriendList() == 1
    friendList.disconnect("danh le", "tri le")
    assert friendList.currentFriendList() == 0
    clear_all_files()