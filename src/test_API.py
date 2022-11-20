from os import path
outputJobFile = "MyCollege_jobs.txt"
outputAppliedJobsFile = "MyCollege_appliedJobs.txt"
outputProfileFile = "MyCollege_profiles.txt"
outputUserFile = "MyCollege_users.txt"
outputSavedJobsFile = "MyCollege_savedJobs.txt"
class TestAllAPIOutputFiles:
    def test_OutputJobFile(self):
        assert path.exists(outputJobFile)
    def test_OutputAppliedJobsFile(self):
        assert path.exists(outputAppliedJobsFile)
    def test_OutputProfileFile(self):
        assert path.exists(outputProfileFile)
    def test_OutputUserFile(self):
        assert path.exists(outputUserFile)
    def test_OutputSavedJobsFile(self):
        assert path.exists(outputSavedJobsFile)
def test_userAccount():
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    file = open('studentAccounts.txt', 'a')    
    file.write("danhle danh le\n")
    file.write("Abcdef1!\n")
    file.write("=====\n")
    file.close
    #Check the file exists
    x = apiFunctions.inputAccountAPI()
    assert x == 1
    assert createAccountFunctions.checkUser('danhle') == 1

