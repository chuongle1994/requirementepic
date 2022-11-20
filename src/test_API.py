from os import path
import createAccountFunctions, apiFunctions, loginfunctions

outputJobFile = "MyCollege_jobs.txt"
outputAppliedJobsFile = "MyCollege_appliedJobs.txt"
outputProfileFile = "MyCollege_profiles.txt"
outputUserFile = "MyCollege_users.txt"
outputSavedJobsFile = "MyCollege_savedJobs.txt"

class TestAllAPIOutputFiles:
   def test_OutputJobFile(self):
      apiFunctions.outputUsersAPI()
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
 #Test for input jobs
def test_jobInput():
    apiFunctions.inputJobsAPI()
    assert loginfunctions.getNumberOfJobPosts() == 6
