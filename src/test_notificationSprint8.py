import createAccountFunctions, message, friendList, loginfunctions, os, json, notification, profileFunctions
def test_delete():
    # Check for no deleted jobs
    assert notification.delete_job("tri le") == 0

    # Create a deleted job, and test notification
    loginfunctions.writeNotification("deleted", "tri le", "1", "engineer", "din")
    assert notification.delete_job("tri le") == 1
    os.remove("userNotifications.txt")

def test_profile():
    # Check if it notifies a user to create their profile
    profileFunctions.createProfile("tri le", "le")
    assert notification.profileNotification("tri le") == 1

    #Check if the user does not get notified after creating a profile
    profileFunctions.writeProfileBase("tri le", "Tester", "ce", "uf", "Test4", "Y", "Y")
    assert notification.profileNotification("tri le") == 0
    os.remove("profile.txt")

def test_newMsg():
    # Checks new message notification
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    createAccountFunctions.promptMembership("1", "tri le")
    createAccountFunctions.promptMembership("0", "danh le")
    message.existsMessages()
    message.sendMessageType("tri le", "Plus", True, False, "danh le")
    message.sendMessage("tri le", "danh le", "test")
    assert notification.messageNotification("danh le") == 1
    os.remove("firstname.txt")
    os.remove("fullname.txt")
    os.remove("lastname.txt")
    os.remove("membership.txt")
    os.remove("messagesList.json")
    os.remove("passwords.txt")
    os.remove("users.txt")

def test_newMember():
    # Checks new student notification
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    profileFunctions.createProfile("danh le", "le")
    profileFunctions.createProfile("tri le", "le")
    friendList.createFriendList("danh le")
    friendList.createFriendList("tri le")
    notification.addNewStudentList("danh le")
    assert notification.newStudentNotification("tri le") == 1
    os.remove("firstname.txt")
    os.remove("fullname.txt")
    os.remove("lastname.txt")
    os.remove("friendList.txt")
    os.remove("passwords.txt")
    os.remove("users.txt")
    os.remove("profile.txt")

def test_sevenDays():
    # Checks if student hasn't applied in 7 days, reminder appears
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    notification.storeJobData("danh le")

    #if has NOT applied in 7 days. Last date applied 11/11/2022
    assert notification.NotApplyNotification("danh le", "11/18/2022") == 1

    #update last date applied to 11/10/2022, today is 11/11/2022
    notification.updateDate("danh le", "11/10/2022")

    #if HAS applied in 7 days
    assert notification.NotApplyNotification("tri le", "11/11/2022") == 0

    os.remove("firstname.txt")
    os.remove("fullname.txt")
    os.remove("lastname.txt")
    os.remove("passwords.txt")
    os.remove("users.txt")
    os.remove("jobNotification.txt")