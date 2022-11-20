from os import path
import createAccountFunctions, apiFunctions, loginfunctions

outputJobFile = "MyCollege_jobs.txt"
outputAppliedJobsFile = "MyCollege_appliedJobs.txt"
outputProfileFile = "MyCollege_profiles.txt"
outputUserFile = "MyCollege_users.txt"
outputSavedJobsFile = "MyCollege_savedJobs.txt"

# Test for all output API 
class TestAllAPIOutputFiles:
   def test_OutputJobFile(self):
      loginfunctions.existsJobPostsFile()
      apiFunctions.outputJobApi()
      assert path.exists(outputJobFile)
   def test_OutputAppliedJobsFile(self):
      apiFunctions.outputAppliedJobsAPI()
      assert path.exists(outputAppliedJobsFile)
   def test_OutputProfileFile(self):
      apiFunctions.outputProfileApi()
      assert path.exists(outputProfileFile)
   def test_OutputUserFile(self):
      apiFunctions.outputUsersAPI()
      assert path.exists(outputUserFile)
   def test_OutputSavedJobsFile(self):
      apiFunctions.outputSavedJobsAPI()
      assert path.exists(outputSavedJobsFile)

# Test for input student account API
def test_userAccount():
   loginfunctions.existsUserPasswordFile()
   loginfunctions.existsFirstLastFullNameFile()
   apiFunctions.inputAccountAPI()
   numAccounts = createAccountFunctions.checkAccNum()
   assert numAccounts == 5
   clear_all_files()

# Test for input jobs API
def test_jobInput():
   loginfunctions.existsJobPostsFile()
   apiFunctions.inputJobsAPI()
   numJobs = loginfunctions.getNumberOfJobPosts()
   assert numJobs == 6
   clear_all_files()

# clear all created files
def clear_all_files():
   loginfunctions.clearFile("controls.txt")
   loginfunctions.clearFile("firstname.txt")
   loginfunctions.clearFile("friendList.txt")
   loginfunctions.clearFile("fullname.txt")
   loginfunctions.clearFile("jobNotification.txt")
   loginfunctions.clearFile("language.txt")
   loginfunctions.clearFile("lastname.txt")
   loginfunctions.clearFile("membership.txt")
   loginfunctions.clearFile("passwords.txt")
   loginfunctions.clearFile("profile.txt")
   loginfunctions.clearFile("users.txt")
   loginfunctions.clearFile("jobPosts.json")