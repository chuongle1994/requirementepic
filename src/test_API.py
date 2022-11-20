from os import path
import createAccountFunctions, apiFunctions, loginfunctions

outputJobFile = "MyCollege_jobs.txt"
outputAppliedJobsFile = "MyCollege_appliedJobs.txt"
outputProfileFile = "MyCollege_profiles.txt"
outputUserFile = "MyCollege_users.txt"
outputSavedJobsFile = "MyCollege_savedJobs.txt"

# class TestAllAPIOutputFiles:
#     def test_OutputJobFile(self):
#         assert path.exists(outputJobFile)
#     def test_OutputAppliedJobsFile(self):
#         assert path.exists(outputAppliedJobsFile)
#     def test_OutputProfileFile(self):
#         assert path.exists(outputProfileFile)
#     def test_OutputUserFile(self):
#         assert path.exists(outputUserFile)
#     def test_OutputSavedJobsFile(self):
#         assert path.exists(outputSavedJobsFile)

# Test for input student account API
def test_userAccount():
    loginfunctions.existsUserPasswordFile()
    loginfunctions.existsFirstLastFullNameFile()
    apiFunctions.inputAccountAPI()
    numAccounts = createAccountFunctions.checkAccNum()
    assert numAccounts == 5



