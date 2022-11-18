from os.path import exists
import uuid, os
import createAccountFunctions, linkFunctions, profileFunctions, friendList, notification, loginfunctions

# Input: Student Account API
def inputAccountAPI():
    fileName = "studentAccounts.txt"

    if exists(fileName):
        with open(fileName) as file:
            lines = file.readlines()
            for line in lines:

                if line == "=====\n" or line == "=====":
                    createAccountFunctions.storeData(username, password, firstname, lastname, fullname)
                    createAccountFunctions.promptMembership("0", fullname)
                    linkFunctions.firstControlsSetting(fullname)
                    linkFunctions.firstLanguageSetting(fullname)
                    profileFunctions.createProfile(fullname, lastname)
                    friendList.createFriendList(fullname)
                    notification.addNewStudentList(fullname)
                    notification.storeJobData(fullname)
                elif ' ' in line:
                    accLimit = createAccountFunctions.checkAccNum()
                    # check maximum number of student account
                    if accLimit == 1:
                        print("All permitted accounts have been created, please come back later")
                        break
                    accountInfo = line.split()
                    username = accountInfo[0]
                    # username already exists
                    if createAccountFunctions.checkUser(username) == 1:
                        print("Username already exists, please try again")
                        break
                    firstname = accountInfo[1]
                    lastname = accountInfo[2]
                    fullname = firstname + ' ' + lastname
                elif ' ' not in line:
                    accountInfo = line.split()
                    password = accountInfo[0]

        file.close()

    # else:
    #     print("\nNo Input API File.")

    return 

# Input: Jobs API
def inputJobsAPI():
    fileName = "newJobs.txt"

    if exists(fileName):
        with open(fileName) as file:
            lines = file.read()
            jobPosts = lines.split("=====\n")

            for jobPost in jobPosts:
                if jobPost == "":
                    break
                
                filesize = os.path.getsize("jobPosts.json")
                if filesize != 0:
                    if loginfunctions.getNumberOfJobPosts() >= 10:
                        print("\nThe system can only permit up to 10 jobs to be posted.")
                        break
                
                jobPost = jobPost.split("&&&\n")
                jobInfo1 = jobPost[0].split("\n")
                jobInfo2 = jobPost[1].split("\n")
                title = jobInfo1[0]
                description = jobInfo1[1]
                postername = jobInfo2[0]
                employer = jobInfo2[1]
                location = jobInfo2[2]
                salary = jobInfo2[3]
                jobID = str(uuid.uuid4())[:8]
                applicantsList = []
                loginfunctions.createJobPost(jobID, title, description, employer, location, salary, postername, applicantsList)
                notification.saveNewJob(postername, title)

        file.close()

    # else:
    #     print("\nNo Input API File.")

    return 