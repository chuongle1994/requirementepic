from os.path import exists
import uuid, os, ast, json
import createAccountFunctions, linkFunctions, profileFunctions, friendList, notification, loginfunctions

# Input: Student Account API
def inputAccountAPI():
    fileName = "studentAccounts.txt"

    # Check the file exists
    if exists(fileName):
        with open(fileName) as file:
            lines = file.readlines()
            for line in lines:
                if line == "=====\n" or line == "=====":
                    # username already exists
                    if createAccountFunctions.checkUser(username) == 1:
                        continue
                    # Save the account info into our system
                    createAccountFunctions.storeData(username, password, firstname, lastname, fullname)
                    # Account setting for new user
                    createAccountFunctions.promptMembership("0", fullname, username)
                    linkFunctions.firstControlsSetting(fullname)
                    linkFunctions.firstLanguageSetting(fullname)
                    profileFunctions.createProfile(fullname, lastname)
                    friendList.createFriendList(fullname)
                    notification.addNewStudentList(fullname)
                    notification.storeJobData(fullname)
                    outputUsersAPI()

                # Read line for username, firstname, lastname
                elif ' ' in line:
                    # check maximum number of student account
                    accLimit = createAccountFunctions.checkAccNum()
                    if accLimit >= 10:
                        print("All permitted accounts have been created, please come back later")
                        break
                    accountInfo = line.split()
                    username = accountInfo[0]
                    firstname = accountInfo[1]
                    lastname = accountInfo[2]
                    fullname = firstname + ' ' + lastname
                # Read line for password
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
    jobList = []

    # Store the job title in our system
    filesize = os.path.getsize("jobPosts.json")
    if filesize != 0:
        obj = json.load(open("jobPosts.json"))
        if(len(obj) != 0):
            if(len(obj["job-posts"]) != 0):
                for index in range(len(obj["job-posts"])):
                    title = obj["job-posts"][index]["title"]
                    jobList.append(title)

    # Check the file exists
    if exists(fileName):
        with open(fileName) as file:
            lines = file.read()
            jobPosts = lines.split("=====\n")

            for jobPost in jobPosts:
                if jobPost == "":
                    break
                # check maximum number of job posts
                filesize = os.path.getsize("jobPosts.json")
                if filesize != 0:
                    if loginfunctions.getNumberOfJobPosts() >= 10:
                        print("\nThe system can only permit up to 10 jobs to be posted.")
                        break
                
                jobPost = jobPost.split("&&&\n")
                jobInfo1 = jobPost[0].split("\n")
                jobInfo2 = jobPost[1].split("\n")
                title = jobInfo1[0]
                # check the title has a different name than the post already in the system
                if title in jobList:
                    print("The title of the new job already exists.")
                    continue
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
        # Checks if the membership file exists
        if exists("membership.txt") == 0:
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
                    if user["jobID"] == job["jobID"]:
                        fw.write(f'{user["Name"]}: {user["Desc"]}\n')
                fw.write("=====" + "\n")
        fw.close()

# Output: Saved Jobs
def outputSavedJobsAPI():
    fileName = "MyCollege_savedJobs.txt"
    jobList = []
    savedList = []
    userList = []

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
        
        if exists("savedListings.txt") == 0:
            file = open("savedListings.txt", "a")
            file.close()
        
        with open("savedListings.txt", "r") as file:
            for line in file:
                data = ast.literal_eval(line)
                savedList.append(data)
                username = data["Name"]
                if username not in userList:
                    userList.append(username)
        file.close()

        with open(fileName, "w") as fw:
            for user in userList:
                fw.write(f'{user}: ')
                for list in savedList:
                    if list["Name"] == user:
                        for job in jobList:
                            if list["jobID"] == job["jobID"]:
                                fw.write(f'{job["title"]} ')
                fw.write("\n" + "=====" + "\n")
        fw.close()
    
# create jobAPI
def createJobApi():
    if exists("MyCollege_jobs.txt") == 0:
        file = open("MyCollege_jobs.txt", "w")
        file.close()

def outputJobApi():
    createJobApi()

    if(os.stat("jobPosts.json").st_size == 0):
        # print("No jobs found")
        return
    
    jobs = []
    obj = json.load(open("jobPosts.json"))
    if(len(obj["job-posts"]) != 0):
        for i in range(len(obj["job-posts"])):
            jobs.append(obj["job-posts"][i])

    with open("MyCollege_jobs.txt", 'w') as file:
        pass

    with open("MyCollege_jobs.txt", 'a') as file:
        for i in jobs:
            file.write(f'{i["title"]}\n{i["description"]}\n{i["employer"]}\n{i["location"]}\n{i["salary"]}\n=====\n')

def createProfileApi():
    if exists("MyCollege_profiles.txt") == 0:
        file = open("MyCollege_profiles.txt", "w")
        file.close()

def outputProfileApi():
    createProfileApi()

    # Checks if the profile file exists
    if exists("profile.txt") == 0:
        file = open("profile.txt", "a")
        file.close()

    profiles = []
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            profiles.append(data)
    
    educations = []
    if exists("profEducation.txt"):
        with open("profEducation.txt", "r") as file:
            for line in file:
                data = ast.literal_eval(line)
                educations.append(data)

    experiences = []
    if exists("profExperience.txt"):
        with open("profExperience.txt", "r") as file:
            for line in file:
                data = ast.literal_eval(line)
                experiences.append(data)


    with open("MyCollege_profiles.txt", 'w') as file:
        pass

    with open("MyCollege_profiles.txt", 'a') as file:
        for i in profiles:
            file.write(f'{i["Title"]}\n{i["Major"]}\n{i["University"]}\n{i["About"]}\n{i["Experience"]}\n')
            # write experience of user
            for exp in experiences:
                if exp["Name"] == i["Username"]:
                    file.write(f'{exp["Title"]}\n{exp["Employer"]}\n{exp["Start"]}\n{exp["End"]}\n{exp["Location"]}\n{exp["Description"]}\n')
            file.write(f'{i["Education"]}\n')
            # write education of user
            for edu in educations:
                if edu["Name"] == i["Username"]:
                    file.write(f'{edu["School"]}\n {edu["Degree"]}\n {edu["Years"]}\n')
            
            file.write("=====\n")
