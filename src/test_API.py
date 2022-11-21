from os import path
import os
import createAccountFunctions, apiFunctions, loginfunctions, profileFunctions

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

# Test for output users API
def test_outputUsersAPI():
   apiFunctions.inputAccountAPI()
   with open(outputUserFile, 'r') as f:
      assert f.readline().strip() == 'hyunjungl Standard'
      assert f.readline().strip() == 'trile Standard'
      assert f.readline().strip() == 'danhle Standard'
      assert f.readline().strip() == 'dinhle Standard'
      assert f.readline().strip() == 'chuongle Standard'
   f.close()
   clear_all_files()

# test ouput job API
def test_outputJobAPI():
   loginfunctions.existsJobPostsFile()
   apiFunctions.inputJobsAPI()
   apiFunctions.outputJobApi()
   with open('MyCollege_jobs.txt', 'r') as f:
      assert f.readline().strip() == 'job1'
      assert f.readline().strip() == 'This is description for job1'
      assert f.readline().strip() == 'USF'
      assert f.readline().strip() == 'Tampa'
      assert f.readline().strip() == '100000'
      assert f.readline().strip() == '====='
      assert f.readline().strip() == 'job2'
      assert f.readline().strip() == 'This is description for job2'
      assert f.readline().strip() == 'USF'
      assert f.readline().strip() == 'Miami'
      assert f.readline().strip() == '200000'
      assert f.readline().strip() == '====='
   f.close()
   clear_all_files()

#test the output appliedJobAPI
def test_OuputAppliedJobsAPI():
   loginfunctions.createJobPost("1", "title1", "description1", "employer1", "location1", "salary1", "Hyunjung Lee", "")
   loginfunctions.createJobPost("2", "title2", "description2", "employer2", "location2", "salary2", "Hyunjung Lee", "")
   loginfunctions.createJobPost("3", "title3", "description3", "employer3", "location3", "salary3", "Chuong Le", "")
   loginfunctions.writeApp("3", "2", "Hyunjung Lee", "2022", "2022", "Description1")
   loginfunctions.writeApp("2", "1", "Chuong Le", "2023", "2023", "Description2")
   loginfunctions.writeApp("2", "1", "Tri Le", "2023", "2023", "Description3")
   apiFunctions.outputAppliedJobsAPI()
   with open(outputAppliedJobsFile, 'r') as f:
      # Strips the newline character
      assert f.readline().strip() == 'title1'
      assert f.readline().strip() == '=====' 
      assert f.readline().strip() == 'title2'
      assert f.readline().strip() == 'Chuong Le: Description2'
      assert f.readline().strip() == 'Tri Le: Description3'
      assert f.readline().strip() == '====='
      assert f.readline().strip() == 'title3'
      assert f.readline().strip() == "Hyunjung Lee: Description1"
   f.close()
   clear_all_files()

# Test the output saved job API
def test_outputSavedJobsAPI():
   apiFunctions.inputJobsAPI()
   loginfunctions.saveJob(1, "Hyunjung Lee")
   loginfunctions.saveJob(2, "Hyunjung Lee")
   loginfunctions.saveJob(0, "Danh Le")
   loginfunctions.saveJob(4, "Danh Le")
   loginfunctions.saveJob(5, "Danh Le")
   loginfunctions.saveJob(3, "Tri Le")
   loginfunctions.saveJob(5, "Dinh Le")
   apiFunctions.outputSavedJobsAPI()
   with open(outputSavedJobsFile, 'r') as f:
      # Strips the newline character
      assert f.readline().strip() == 'Hyunjung Lee: job2 job3'
      assert f.readline().strip() == '=====' 
      assert f.readline().strip() == 'Danh Le: job1 job5 job6'
      assert f.readline().strip() == '====='
      assert f.readline().strip() == 'Tri Le: job4'
      assert f.readline().strip() == '====='
      assert f.readline().strip() == 'Dinh Le: job6'
      assert f.readline().strip() == '====='
   f.close()
   clear_all_files()

# Test the output profiles API
def test_outputProfilesAPI():
   profileFunctions.createProfile("Hyunjung Lee", "Lee")
   profileFunctions.writeProfileBase("Hyunjung Lee", "title1", "Cs", "Usf", "Info1", "-", "-")
   profileFunctions.saveExperience("Hyunjung Lee", "software engineer", "apple", "2020", "2022", "tampa", "Great")
   profileFunctions.saveEducation("Hyunjung Lee", "college1", "degree1", "2018")
   profileFunctions.saveEducation("Hyunjung Lee", "college2", "degree2", "2020")
   apiFunctions.outputProfileApi()
   with open(outputProfileFile, 'r') as f:
      # Strips the newline character
      assert f.readline().strip() == 'title1'
      assert f.readline().strip() == 'Cs' 
      assert f.readline().strip() == 'Usf'
      assert f.readline().strip() == 'Info1'
      assert f.readline().strip() == '-'
      assert f.readline().strip() == 'software engineer'
      assert f.readline().strip() == 'apple'
      assert f.readline().strip() == '2020'
      assert f.readline().strip() == '2022'
      assert f.readline().strip() == 'tampa'
      assert f.readline().strip() == 'Great'
      assert f.readline().strip() == '-'
      assert f.readline().strip() == 'college1'
      assert f.readline().strip() == 'degree1'
      assert f.readline().strip() == '2018'
      assert f.readline().strip() == 'college2'
      assert f.readline().strip() == 'degree2'
      assert f.readline().strip() == '2020'
      assert f.readline().strip() == '====='
   f.close()
   clear_all_files()
   os.remove("applications.txt")
   os.remove("controls.txt")
   os.remove("firstname.txt")
   os.remove("friendList.txt")
   os.remove("fullname.txt")
   os.remove("jobNotification.txt")
   os.remove("jobPosts.json")
   os.remove("language.txt")
   os.remove("lastname.txt")
   os.remove("membership.txt")
   os.remove("MyCollege_appliedJobs.txt")
   os.remove("MyCollege_jobs.txt")
   os.remove("MyCollege_profiles.txt")
   os.remove("MyCollege_savedJobs.txt")
   os.remove("MyCollege_users.txt")
   os.remove("passwords.txt")
   os.remove("profEducation.txt")
   os.remove("profExperience.txt")
   os.remove("profile.txt")
   os.remove("savedListings.txt")
   os.remove("users.txt")


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
   loginfunctions.clearFile("applications.txt")
   loginfunctions.clearFile("savedListings.txt")
   loginfunctions.clearFile("profEducation.txt")
   loginfunctions.clearFile("profExperience.txt")
   loginfunctions.clearFile(outputProfileFile)
   loginfunctions.clearFile(outputUserFile)
   loginfunctions.clearFile(outputJobFile)
   loginfunctions.clearFile(outputAppliedJobsFile)
   loginfunctions.clearFile(outputSavedJobsFile)
