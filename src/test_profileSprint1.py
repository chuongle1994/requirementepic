import ast
import loginfunctions, profileFunctions

# Test Title, Major, University, About section is stored
def test_profile():
    profileFunctions.createProfile("Hyunjung Lee", "Lee")
    profileFunctions.createProfile("Danh Le", "Le")
    profileFunctions.createProfile("Chuong Le", "Le")
    profileFunctions.createProfile("Tri Le", "Le",)
    profileFunctions.createProfile("Dinh Le", "Le")

    profileFunctions.writeProfileBase("Hyunjung Lee", "Software", "computer science", "usf", "Test1", "None", "None")
    profileFunctions.writeProfileBase("Danh Le", "Hardware", "computer engineering", "university of south florida", "Test2", "None", "None")
    profileFunctions.writeProfileBase("Chuong Le", "Developer", "cs", "ut", "Test3", "None", "None")
    profileFunctions.writeProfileBase("Tri Le", "Tester", "ce", "uf", "Test4", "None", "None")
    profileFunctions.writeProfileBase("Dinh Le", "Data Analysist", "CS", "university", "Test5", "None", "None")

    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Username"] == "Hyunjung Lee":
                assert data["Title"] == "Software"
                assert data["Major"] == "Computer Science"
                assert data["University"] == "Usf"
                assert data["About"] == "Test1"

            elif data["Username"] == "Danh Le":
                assert data["Title"] == "Hardware"
                assert data["Major"] == "Computer Engineering"
                assert data["University"] == "University Of South Florida"
                assert data["About"] == "Test2"

            elif data["Username"] == "Chuong Le":
                assert data["Title"] == "Developer"
                assert data["Major"] == "Cs"
                assert data["University"] == "Ut"
                assert data["About"] == "Test3"

            elif data["Username"] == "Tri Le":
                assert data["Title"] == "Tester"
                assert data["Major"] == "Ce"
                assert data["University"] == "Uf"
                assert data["About"] == "Test4"

            elif data["Username"] == "Dinh Le":
                assert data["Title"] == "Data Analysist"
                assert data["Major"] == "Cs" 
                assert data["University"] == "University"
                assert data["About"] == "Test5"
    
    loginfunctions.clearFile("profile.txt")


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
                if data["Title"] == "Tester1":
                    assert data["Employer"] == "Apple"
                    assert data["Start"] == "2.21.15"
                    assert data["End"] == "8.11.17"
                    assert data["Location"] == "Tampa"
                    assert data["Description"] == "Test Something"
                if data["Title"] == "Developer2":
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
                if data["School"] == "school2":
                    assert data["Degree"] == "Bachelor"
                    assert data["Years"] == "2017"
                if data["School"] == "school3":
                    assert data["Degree"] == "Master"
                    assert data["Years"] == "2022"

    loginfunctions.clearFile("profEducation.txt")