import ast
import loginfunctions, profileFunctions, friendList

# Test profile is complete or not
def test_completeProfile():
    profileFunctions.createProfile("Hyunjung Lee", "Lee")
    profileFunctions.createProfile("Danh Le", "Le")
    profileFunctions.createProfile("Chuong Le", "Le")
    profileFunctions.createProfile("Tri Le", "Le",)
    profileFunctions.createProfile("Dinh Le", "Le")

    profileFunctions.writeProfileBase("Hyunjung Lee", "", "computer science", "usf", "Test1", "None", "None")
    profileFunctions.writeProfileBase("Danh Le", "Hardware", "", "university of south florida", "Test2", "None", "None")
    profileFunctions.writeProfileBase("Chuong Le", "Developer", "cs", "", "", "None", "None")
    profileFunctions.writeProfileBase("Tri Le", "Tester", "ce", "uf", "Test4", "None", "None")
    profileFunctions.writeProfileBase("Dinh Le", "Data Analysist", "CS", "university", "", "None", "None")

    assert profileFunctions.checkComplete("Hyunjung Lee") == "You have not finished creating your profile."
    assert profileFunctions.checkComplete("Danh Le") == "You have not finished creating your profile."
    assert profileFunctions.checkComplete("Chuong Le") == "You have not finished creating your profile."
    assert profileFunctions.checkComplete("Tri Le") == "You have not finished creating your profile."
    assert profileFunctions.checkComplete("Dinh Le") == "You have not finished creating your profile."

    loginfunctions.clearFile("profile.txt")


# Test "Title", "Major", "University", "About" section is stored
# Check major and university is stored with first letters is uppercase
def test_storeProfile():
    profileFunctions.createProfile("Hyunjung Lee", "Lee")
    profileFunctions.createProfile("Danh Le", "Le")
    profileFunctions.createProfile("Chuong Le", "Le")
    profileFunctions.createProfile("Tri Le", "Le",)
    profileFunctions.createProfile("Dinh Le", "Le")

    profileFunctions.writeProfileBase("Hyunjung Lee", "Software", "computer science", "usf", "Test1", "None", "None")
    profileFunctions.writeProfileBase("Danh Le", "Hardware", "computer engineering", "university of south florida", "Test2", "None", "None")
    profileFunctions.writeProfileBase("Chuong Le", "Developer", "cs", "ut", "Test3", "None", "None")
    profileFunctions.writeProfileBase("Tri Le", "Tester", "CE", "UF", "Test4", "None", "None")
    profileFunctions.writeProfileBase("Dinh Le", "Data Analysist", "Cs", "university", "Test5", "None", "None")

    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Username"] == "Hyunjung Lee":
                assert data["Title"] == "Software"
                assert data["Major"] != "computer science"
                assert data["Major"] == "Computer Science"
                assert data["University"] != "usf"
                assert data["University"] == "Usf"
                assert data["About"] == "Test1"

            elif data["Username"] == "Danh Le":
                assert data["Title"] == "Hardware"
                assert data["Major"] != "computer engineering"
                assert data["Major"] == "Computer Engineering"
                assert data["University"] != "university of south florida"
                assert data["University"] == "University Of South Florida"
                assert data["About"] == "Test2"

            elif data["Username"] == "Chuong Le":
                assert data["Title"] == "Developer"
                assert data["Major"] != "cs"
                assert data["Major"] == "Cs"
                assert data["University"] != "ut"
                assert data["University"] == "Ut"
                assert data["About"] == "Test3"

            elif data["Username"] == "Tri Le":
                assert data["Title"] == "Tester"
                assert data["Major"] != "CE"
                assert data["Major"] == "Ce"
                assert data["University"] != "UF"
                assert data["University"] == "Uf"
                assert data["About"] == "Test4"

            elif data["Username"] == "Dinh Le":
                assert data["Title"] == "Data Analysist"
                assert data["Major"] == "Cs" 
                assert data["University"] != "university"
                assert data["University"] == "University"
                assert data["About"] == "Test5"
    
    loginfunctions.clearFile("profile.txt")

# Test "experience" section is stored
def test_experience():
    profileFunctions.saveExperience("Hyunjung Lee", "Developer1", "Google", "1.12.12", "3.21.14", "NY", "Develop Something")
    profileFunctions.saveExperience("Hyunjung Lee", "Tester1", "Apple", "2.21.15", "8.11.17", "Tampa", "Test Something")
    profileFunctions.saveExperience("Hyunjung Lee", "Developer2", "Instagram", "1.12.18", "3.21.20", "NY", "Develop Something")
    profileFunctions.saveExperience("Danh Le", "Scrum Master", "Tesla", "8.12.18", "9.10.20", "Austin", "Organize Daily Scrum")

    with open("profExperience.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Name"] == "Hyunjung Lee":
                if data["Title"] == "Developer1":
                    assert data["Employer"] == "Google"
                    assert data["Start"] == "1.12.12"
                    assert data["End"] == "3.21.14"
                    assert data["Location"] == "NY"
                    assert data["Description"] == "Develop Something"
                elif data["Title"] == "Tester1":
                    assert data["Employer"] == "Apple"
                    assert data["Start"] == "2.21.15"
                    assert data["End"] == "8.11.17"
                    assert data["Location"] == "Tampa"
                    assert data["Description"] == "Test Something"
                elif data["Title"] == "Developer2":
                    assert data["Employer"] == "Instagram"
                    assert data["Start"] == "1.12.18"
                    assert data["End"] == "3.21.20"
                    assert data["Location"] == "NY"
                    assert data["Description"] == "Develop Something"

            elif data["Name"] == "Danh Le":
                if data["Title"] == "Scrum Master":
                    assert data["Employer"] == "Tesla"
                    assert data["Start"] == "8.12.18"
                    assert data["End"] == "9.10.20"
                    assert data["Location"] == "Austin"
                    assert data["Description"] == "Organize Daily Scrum"

    loginfunctions.clearFile("profExperience.txt")

# Test "education" section is stored
def test_education():
    profileFunctions.saveEducation("Hyunjung Lee", "school1", "AA", "2012")
    profileFunctions.saveEducation("Hyunjung Lee", "school2", "Bachelor", "2017")
    profileFunctions.saveEducation("Hyunjung Lee", "school3", "Master", "2022")

    with open("profEducation.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Name"] == "Hyunjung Lee":
                if data["School"] == "school1":
                    assert data["Degree"] == "AA"
                    assert data["Years"] == "2012"
                elif data["School"] == "school2":
                    assert data["Degree"] == "Bachelor"
                    assert data["Years"] == "2017"
                elif data["School"] == "school3":
                    assert data["Degree"] == "Master"
                    assert data["Years"] == "2022"

    loginfunctions.clearFile("profEducation.txt")

# Test edit "title", "major", "university", "information" section
def test_editProfile():
    # create profile
    profileFunctions.createProfile("Hyunjung Lee", "Lee")
    profileFunctions.createProfile("Danh Le", "Le")
    profileFunctions.createProfile("Chuong Le", "Le")
    profileFunctions.createProfile("Tri Le", "Le",)
    # complete profile
    profileFunctions.writeProfileBase("Hyunjung Lee", "Software", "computer science", "usf", "Test1", "-", "-")
    profileFunctions.writeProfileBase("Danh Le", "Hardware", "computer engineering", "university of south florida", "Test2", "-", "-")
    profileFunctions.writeProfileBase("Chuong Le", "Developer", "cs", "ut", "Test3", "-", "-")
    profileFunctions.writeProfileBase("Tri Le", "Tester", "ce", "uf", "Test4", "-", "-")
    
    # edit profile - "title"
    profileFunctions.writeProfileBase("Hyunjung Lee", "Software Engineer", "computer science", "usf", "Test1", "-", "-")
    # edit profile - "major"
    profileFunctions.writeProfileBase("Danh Le", "Hardware", "Computer Science", "university of south florida", "Test2", "-", "-")
    # edit profile - "university"
    profileFunctions.writeProfileBase("Chuong Le", "Developer", "cs", "USF", "Test3", "-", "-")
    # edit profile - "information"
    profileFunctions.writeProfileBase("Tri Le", "Tester", "ce", "uf", "Information", "-", "-")

    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Username"] == "Hyunjung Lee":
                assert data["Title"] != "Software"
                assert data["Title"] == "Software Engineer"
            elif data["Username"] == "Danh Le":
                assert data["Major"] != "Computer Engineering"
                assert data["Major"] == "Computer Science"
            elif data["Username"] == "Chuong Le":
                assert data["University"] != "Ut"
                assert data["University"] == "Usf"
            elif data["Username"] == "Tri Le":
                assert data["About"] != "Test4"
                assert data["About"] == "Information"
    
    loginfunctions.clearFile("profile.txt")

# Test edit "Experience" section
def test_editExperiene():
    # create experience 
    profileFunctions.saveExperience("Hyunjung Lee", "Developer1", "Google", "1.12.12", "3.21.14", "NY", "Develop Something")
    profileFunctions.saveExperience("Hyunjung Lee", "Tester1", "Apple", "2.21.15", "8.11.17", "Tampa", "Test Something")
    profileFunctions.saveExperience("Hyunjung Lee", "Developer2", "Instagram", "1.12.18", "3.21.20", "NY", "Develop Something")
    # edit experience
    profileFunctions.writeExperience("Hyunjung Lee", "Developer1", "USF", "11.11.11", "22.22.22", "Tampa", "Bull", "Test1")
    profileFunctions.writeExperience("Hyunjung Lee", "Tester1", "Facebook", "33.33.33", "44.44.44", "Miami", "my face", "Test2")
    profileFunctions.writeExperience("Hyunjung Lee", "Developer2", "Chase", "55.55.55", "66.66.66", "Sarasota", "get money", "Test3")
    
    with open("profExperience.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Name"] == "Hyunjung Lee":
                if data["Title"] == "Test1":
                    assert data["Employer"] == "USF"
                    assert data["Start"] == "11.11.11"
                    assert data["End"] == "22.22.22"
                    assert data["Location"] == "Tampa"
                    assert data["Description"] == "Bull"
                elif data["Title"] == "Test2":
                    assert data["Employer"] == "Facebook"
                    assert data["Start"] == "33.33.33"
                    assert data["End"] == "44.44.44"
                    assert data["Location"] == "Miami"
                    assert data["Description"] == "my face"
                elif data["Title"] == "Test3":
                    assert data["Employer"] == "Chase"
                    assert data["Start"] == "55.55.55"
                    assert data["End"] == "66.66.66"
                    assert data["Location"] == "Sarasota"
                    assert data["Description"] == "get money"

    loginfunctions.clearFile("profExperience.txt")

# Test edit "Education" section
def test_editEducation():
    # create education section
    profileFunctions.saveEducation("Hyunjung Lee", "school1", "AA", "2012")
    profileFunctions.saveEducation("Hyunjung Lee", "school2", "Bachelor", "2017")
    profileFunctions.saveEducation("Hyunjung Lee", "school3", "Master", "2022")
    # edit education sectoin
    profileFunctions.writeEducation("Hyunjung Lee", "school1", "CC", "2014", "UCF")
    profileFunctions.writeEducation("Hyunjung Lee", "school2", "BB", "2015", "USF")
    profileFunctions.writeEducation("Hyunjung Lee", "school3", "AA", "2016", "UF")

    with open("profEducation.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Name"] == "Hyunjung Lee":
                if data["School"] == "UCF":
                    assert data["Degree"] == "CC"
                    assert data["Years"] == "2014"
                elif data["School"] == "USF":
                    assert data["Degree"] == "BB"
                    assert data["Years"] == "2015"
                elif data["School"] == "UF":
                    assert data["Degree"] == "AA"
                    assert data["Years"] == "2016"

    loginfunctions.clearFile("profEducation.txt")

# Test for displaying profiles for User and Friends
def test_friendProfile():
    profileFunctions.createProfile("Hyunjung Lee", "Lee")
    profileFunctions.createProfile("Danh Le", "Le")
    profileFunctions.createProfile("Tri Le", "Le")
    profileFunctions.writeProfileBase("Hyunjung Lee", "Software", "computer science", "usf", "Test1", "-", "-")
    profileFunctions.writeProfileBase("Danh Le", "Hardware", "computer engineering", "university of south florida", "Test2", "-", "-")
    profileFunctions.writeProfileBase("Tri Le", "Database", "cs", "ut", "Test3", "-", "-")
    profileFunctions.saveExperience("Hyunjung Lee", "Developer2", "Instagram", "1.12.18", "3.21.20", "NY", "Develop Something")
    profileFunctions.saveExperience("Danh Le", "Scrum Master", "Tesla", "8.12.18", "9.10.20", "Austin", "Organize Daily Scrum")
    profileFunctions.saveExperience("Tri Le", "Tester", "Tesla", "8.12.18", "9.10.20", "Austin", "Test something")
    profileFunctions.saveEducation("Hyunjung Lee", "school2", "Bachelor", "2017")
    profileFunctions.saveEducation("Danh Le", "school3", "Master", "2022")
    profileFunctions.saveEducation("Tri Lee", "school2", "Bachelor", "2000")

    # Test for printing the current user profile
    assert profileFunctions.currentProfile("Hyunjung Lee") == {"Username": "Hyunjung Lee", "Lastname": "Lee", "Title": "Software", "University": "Usf", "Major":"Computer Science", "About":"Test1", "Experience":"-", "Education":"-"}
    assert profileFunctions.currentProfile("Danh Le") == {"Username": "Danh Le", "Lastname": "Le", "Title": "Hardware", "University": "University Of South Florida", "Major":"Computer Engineering", "About":"Test2", "Experience":"-", "Education":"-"}
    assert profileFunctions.currentEdu("Hyunjung Lee") == [{"Name": "Hyunjung Lee", "School": "school2", "Degree": "Bachelor", "Years": "2017"}]
    assert profileFunctions.currentExp("Hyunjung Lee") == [{"Name": "Hyunjung Lee", "Title": "Developer2", "Employer": "Instagram", "Start": "1.12.18", "End": "3.21.20", "Location": "NY", "Description": "Develop Something"}]

    friendList.createFriendList("Hyunjung Lee")
    friendList.createFriendList("Danh Le")
    friendList.createFriendList("Tri Le")
    friendList.requestFriend("Hyunjung Lee", "Danh Le")
    friendList.accept("Danh Le", "Hyunjung Lee")
    friendList.requestFriend("Hyunjung Lee", "Tri Le")
    friendList.accept("Tri Le", "Hyunjung Lee")

    # Test for displaying the friend List to view the profile
    assert profileFunctions.displayFriendProfileOption("Hyunjung Lee") == 2
    assert profileFunctions.displayFriendProfileOption("Danh Le") == 1
    assert profileFunctions.displayFriendProfileOption("Danh Le") == 1

    loginfunctions.clearFile("profile.txt")
    loginfunctions.clearFile("profExperience.txt")
    loginfunctions.clearFile("profEducation.txt")
    loginfunctions.clearFile("friendList.txt")
