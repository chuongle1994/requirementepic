import createAccountFunctions, loginfunctions
import ast

def clear_all_files():
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")
    loginfunctions.clearFile("currentUserData.txt")
    loginfunctions.clearFile("jobPosts.json")
    loginfunctions.clearFile("savedListings.txt")

# Testing for the number of job posting
def test_numberOfJobPosts():
    createAccountFunctions.storeData("hyunjungl", "!Hello123", "Hyunjung", "Lee", "Hyunjung Lee")
    loginfunctions.storeUserData("hyunjungl")

    loginfunctions.existsJobPostsFile()
    loginfunctions.createJobPost("1", "title1", "description1", "employer1", "location1", "10000", "")
    loginfunctions.createJobPost("2", "title2", "description2", "employer2", "location2", "20000", "")
    loginfunctions.createJobPost("3", "title3", "description3", "employer3", "location3", "30000", "")
    loginfunctions.createJobPost("4", "title4", "description4", "employer4", "location4", "40000", "")
    assert loginfunctions.getNumberOfJobPosts() == 4
    loginfunctions.createJobPost("5", "title5", "description5", "employer5", "location5", "50000", "")
    loginfunctions.createJobPost("6", "title6", "description6", "employer6", "location6", "60000", "")
    loginfunctions.createJobPost("7", "title7", "description7", "employer7", "location7", "70000", "")
    loginfunctions.createJobPost("8", "title8", "description8", "employer8", "location8", "80000", "")
    assert loginfunctions.getNumberOfJobPosts() == 8
    loginfunctions.createJobPost("9", "title9", "description9", "employer9", "location9", "90000", "")
    loginfunctions.createJobPost("10", "title10", "description10", "employer10", "location10", "100000", "")
    loginfunctions.createJobPost("11", "title11", "description11", "employer11", "location11", "110000", "")  
    assert loginfunctions.inputJobInfo() ==  "\nThe system can only permit up to 10 jobs to be posted."

    clear_all_files()

# Test for deleting the job posts
def test_deleteJobPosts():
    createAccountFunctions.storeData("hyunjungl", "!Hello123", "Hyunjung", "Lee", "Hyunjung Lee")
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    loginfunctions.storeUserData("hyunjungl") # current user

    loginfunctions.existsJobPostsFile()
    loginfunctions.createJobPost("1", "title1", "description1", "employer1", "location1", "10000", "")
    loginfunctions.createJobPost("2", "title2", "description2", "employer2", "location2", "20000", "")
    loginfunctions.createJobPost("3", "title3", "description3", "employer3", "location3", "30000", "")
    loginfunctions.createJobPost("4", "title4", "description4", "employer4", "location4", "40000", "")
    # Check for existing job post
    assert loginfunctions.displayAllJobTitles() == True
    assert loginfunctions.getNumberOfJobPosts() == 4

    # Checking for the person who has posted a job can delete a job
    loginfunctions.deleteJobByIndex(0)
    assert loginfunctions.getNumberOfJobPosts() == 3

    # Change current user
    loginfunctions.clearFile("currentUserData.txt")
    loginfunctions.storeUserData("trile")

    # Checking for the person who has not posted a job cannot delete a job
    loginfunctions.deleteJobByIndex(0)
    assert loginfunctions.getNumberOfJobPosts() == 3

    clear_all_files()

def checkSaved(index, name):
    found = 0
    with open("savedListings.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Index"] == index and data["Name"] == name:
                found = 1
    return found

# Test for saving and unsaving jobs
def test_saveJobPost():
    createAccountFunctions.storeData("hyunjungl", "!Hello123", "Hyunjung", "Lee", "Hyunjung Lee")
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    createAccountFunctions.storeData("dinhle", "Abcdef1!", "dinh", "le", "dinh le")
    loginfunctions.storeUserData("hyunjungl") # current user
    # create 4 job posts
    loginfunctions.existsJobPostsFile()
    loginfunctions.createJobPost("1", "title1", "description1", "employer1", "location1", "10000", "")
    loginfunctions.createJobPost("2", "title2", "description2", "employer2", "location2", "20000", "")
    loginfunctions.createJobPost("3", "title3", "description3", "employer3", "location3", "30000", "")
    loginfunctions.createJobPost("4", "title4", "description4", "employer4", "location4", "40000", "")

    # Save a job post
    loginfunctions.saveJob(0, "tri le")
    loginfunctions.saveJob(0, "dinh le")
    loginfunctions.saveJob(1, "tri le")
    loginfunctions.saveJob(2, "dinh le")

    # Testing for saving a job
    assert checkSaved(0, "tri le") == 1
    assert checkSaved(0, "dinh le") == 1
    assert checkSaved(1, "tri le") == 1
    assert checkSaved(1, "dinh le") == 0
    assert checkSaved(2, "dinh le") == 1
    assert checkSaved(2, "tri le") == 0
    assert checkSaved(3, "dinh le") == 0

    # Change current user
    loginfunctions.clearFile("currentUserData.txt")
    loginfunctions.storeUserData("trile")

    # Testing for unsaving a job
    loginfunctions.unsaveJob(0)
    assert checkSaved(0, "tri le") == 0
    assert checkSaved(0, "dinh le") == 1
    assert checkSaved(1, "tri le") == 1
    assert checkSaved(2, "dinh le") == 1

    loginfunctions.unsaveJob(1)
    assert checkSaved(1, "tri le") == 0
    assert checkSaved(0, "dinh le") == 1
    assert checkSaved(2, "dinh le") == 1

    clear_all_files()