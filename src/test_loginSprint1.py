import os
import loginfunctions, createAccountFunctions, homeFunctions


# Selecting any of these skills result in “under construction”
def test_frontendDevelopment():
    assert loginfunctions.frontendDevelopment() == "\nunder construction"

def test_backendDevelopment():
    assert loginfunctions.backendDevelopment() == "\nunder construction"

def test_databaseDesign():
    assert loginfunctions.databaseDesign() == "\nunder construction"

def test_agileMethodologies():
    assert loginfunctions.agileMethodologies() == "\nunder construction"

def test_gitVersionControl():
    assert loginfunctions.gitVersionControl() == "\nunder construction"

# search for job / internship and find someone you know result in "under construction"

#def test_searchForJob():
#    assert loginfunctions.searchForAJob() == "\nunder construction"

def test_findSomeone():
    #assert loginfunctions.findSomeone() == "\nunder construction"
    createAccountFunctions.storeData("test1", "Password123!", "Danh", "Le", "Danh Le")

    assert homeFunctions.checkMatch("Danh Le") == "\nThey are a part of the Incollege system"
    assert homeFunctions.checkMatch("Mike Le") == "\nThey are not yet a part of the InCollege system yet"



def test_validateLogin():
    createAccountFunctions.storeData("test1", "Password123!", "Danh", "Le", "Danh Le")
    createAccountFunctions.storeData("test2", "Hitest123!", "Danh", "Le", "Danh Le")
    assert loginfunctions.validateLogin("test1", "Password123!") == True
    assert loginfunctions.validateLogin("test2", "Hitest123!") == True
    user = open("users.txt", "w")
    user.close()
    passw = open("passwords.txt", "w")
    passw.close()
    first = open("firstname.txt", "w")
    first.close()
    last = open("lastname.txt", "w")
    last.close()
    full = open("fullname.txt", "w")
    full.close()

    os.remove("firstname.txt")
    os.remove("fullname.txt")
    os.remove("lastname.txt")
    os.remove("passwords.txt")
    os.remove("users.txt")