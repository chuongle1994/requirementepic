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

    # if has NOT applied in 7 days. Last date applied 11/11/2022
    assert notification.NotApplyNotification("danh le", "11/18/2022") == 1

    # update last date applied to 11/10/2022, today is 11/11/2022
    notification.updateDate("danh le", "11/10/2022")

    # if has applied in 7 days
    assert notification.NotApplyNotification("tri le", "11/11/2022") == 0

    os.remove("firstname.txt")
    os.remove("fullname.txt")
    os.remove("lastname.txt")
    os.remove("passwords.txt")
    os.remove("users.txt")
    os.remove("jobNotification.txt")

def test_numAppliedJobs():
    # create accounts
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")

    # create needed files
    loginfunctions.existsJobPostsFile()
    loginfunctions.existsCurrentUserData()

    # logged in as danh le
    loginfunctions.storeUserData("danhle")
    notification.storeJobData("danh le")

    # danh creates 2 job posts
    applicants = []
    loginfunctions.createJobPost("12345", "engineer", "code", "google", "remote", "50k", applicants)
    loginfunctions.createJobPost("54321", "engineer 2", "code 2", "google 2", "remote2", "150k", applicants)
    
    # if applied for no jobs
    assert notification.total_appliedJob("tri le") == 0

    # tri logs in and applies for first job
    loginfunctions.applyForJob(0, "tri le")
    loginfunctions.writeApp("12345", 0, "tri le", "graddate", "workdate", "description")
    os.remove("currentUserData.txt")
    loginfunctions.storeUserData("trile")

    # numappliedjob should be 1
    assert notification.total_appliedJob("tri le") == 1

    # tri applies for second job
    loginfunctions.applyForJob(1, "tri le")
    loginfunctions.writeApp("54321", 0, "tri le", "graddate", "workdate", "description")

    # numappliedjobs should be 2
    assert notification.total_appliedJob("tri le") == 2

    os.remove("firstname.txt")
    os.remove("fullname.txt")
    os.remove("lastname.txt")
    os.remove("passwords.txt")
    os.remove("users.txt")
    os.remove("jobNotification.txt")
    os.remove("applications.txt")
    os.remove("currentUserData.txt")
    os.remove("jobPosts.json")

def test_newJobPosted():
    # create accounts
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")

    # create needed files
    loginfunctions.existsJobPostsFile()
    loginfunctions.existsCurrentUserData()

    # login as danh
    loginfunctions.storeUserData("danhle")

    # create 2 job posts
    applicants = []
    loginfunctions.createJobPost("12345", "engineer", "code", "google", "remote", "50k", applicants)
    loginfunctions.createJobPost("54321", "engineer 2", "code 2", "google 2", "remote2", "150k", applicants)

    # login as tri
    os.remove("currentUserData.txt")
    loginfunctions.storeUserData("trile")

    # create job data for tri
    notification.storeJobData("tri le")

    # new jobs created by danh should notify tri with num of new jobs
    notification.saveNewJob("danh le", "engineer")
    notification.saveNewJob("danh le", "engineer 2")

    # 2 new jobs created should notify 2
    assert notification.newJobNotification("tri le") == 2

    os.remove("firstname.txt")
    os.remove("fullname.txt")
    os.remove("lastname.txt")
    os.remove("passwords.txt")
    os.remove("users.txt")
    os.remove("jobNotification.txt")
    os.remove("currentUserData.txt")
    os.remove("jobPosts.json")
