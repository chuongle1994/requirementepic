from os.path import exists
import uuid, os, ast, json
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
                    createAccountFunctions.promptMembership("0", fullname, username)
                    linkFunctions.firstControlsSetting(fullname)
                    linkFunctions.firstLanguageSetting(fullname)
                    profileFunctions.createProfile(fullname, lastname)
                    friendList.createFriendList(fullname)
                    notification.addNewStudentList(fullname)
                    notification.storeJobData(fullname)
                    outputUsersAPI()
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

# Output: Users
def outputUsersAPI():
    fileName = "MyCollege_users.txt"
    userList = []

    if exists(fileName) == 0:
        file = open(fileName, "a")
        file.close()

    else:
        fileExist = exists("membership.txt")

        # Checks if the file exists
        if fileExist == 0:
            file = open("membership.txt", "a")
            file.close()

        with open("membership.txt", "r") as file:
            for line in file:
                data = ast.literal_eval(line)
                username = data["username"]
                membership = data["Membership_Type"]
                info = username + ' ' + membership
                userList.append(info)
        file.close()

        for index in range(len(userList)):
            userList[index] = str(userList[index]) + "\n"

        with open(fileName, "w") as fw:
            fw.writelines(userList)
        fw.close()

    return

# Output: Applied Jobs
def outputAppliedJobsAPI():
    fileName = "MyCollege_appliedJobs.txt"
    jobList = []
    applicationList = []

    if exists(fileName) == 0:
        file = open(fileName, "a")
        file.close()

    else:
        filesize = os.path.getsize("jobPosts.json")
        if filesize != 0:
            obj = json.load(open("jobPosts.json"))
            if(len(obj) != 0):
                if(len(obj["job-posts"]) != 0):
                    for index in range(len(obj["job-posts"])):
                        jobID = obj["job-posts"][index]["jobID"]
                        title = obj["job-posts"][index]["title"]
                        jobs = {"jobID": jobID, "title": title}
                        jobList.append(jobs)
        
        if exists("applications.txt") == 0:
            file = open("applications.txt", "a")
            file.close()
        
        with open("applications.txt", "r") as file:
            for line in file:
                data = ast.literal_eval(line)
                applicationList.append(data)
        file.close()

        with open(fileName, "w") as fw:
            for job in jobList:
                fw.write(f'{job["title"]}\n')
                for user in applicationList:
                    if job["jobID"] == user["jobID"]:
                        fw.write(f'{user["Name"]}\n{user["Desc"]}\n')
                        break
                fw.write("=====" + "\n")
        fw.close()