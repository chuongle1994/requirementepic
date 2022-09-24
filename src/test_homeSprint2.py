import homeFunctions, createAccountFunctions, loginfunctions

def test_video():
    assert homeFunctions.playVideo() == "Video is now playing"

def test_checkNames():
    createAccountFunctions.storeData("trile", "Password123!", "Tri", "Le", "Tri Le")
    assert homeFunctions.checkMatch("Tri Le") == "\nThey are a part of the Incollege system"
    assert homeFunctions.checkMatch("Danh Le") == "\nThey are not yet a part of the InCollege system yet"
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")
    