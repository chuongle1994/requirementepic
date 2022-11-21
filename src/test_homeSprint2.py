import os
import homeFunctions, createAccountFunctions, loginfunctions

#Test if the function returns the correct statement.
def test_video():
    assert homeFunctions.playVideo() == "Video is now playing"

#Test if the function correctly checks if the name exists in the database.
def test_checkNames():
    #Create data
    createAccountFunctions.storeData("trile", "Password123!", "Tri", "Le", "Tri Le")

    #Check for existent and nonexistent response.
    assert homeFunctions.checkMatch("Tri Le") == "\nThey are a part of the Incollege system"
    assert homeFunctions.checkMatch("Danh Le") == "\nThey are not yet a part of the InCollege system yet"
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")

    os.remove("firstname.txt")
    os.remove("fullname.txt")
    os.remove("lastname.txt")
    os.remove("passwords.txt")
    os.remove("users.txt")
    