import linkFunctions, createAccountFunctions, loginfunctions, ast, friendList, profileFunctions, os

# clear all created files
def clear_all_files():
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")
    loginfunctions.clearFile("currentUserData.txt")
    loginfunctions.clearFile("controls.txt")
    loginfunctions.clearFile("profile.txt")

    os.remove("firstname.txt")
    os.remove("controls.txt")
    os.remove("currentUserData.txt")
    os.remove("fullname.txt")
    os.remove("users.txt")
    os.remove("passwords.txt")

def test_searchLastName():
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults sms to 1 or "on"
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le") # making an account defaults sms to 1 or "on"
    profileFunctions.createProfile("danh le", "le")
    profileFunctions.createProfile("tri le", "le")
    assert friendList.searchLastName("danh le", "le") == 1
    clear_all_files()
    
def test_searchUniversity():
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults sms to 1 or "on"
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le") # making an account defaults sms to 1 or "on"
    assert friendList.searchUniversity("danh le", "USF") == 0
    clear_all_files()

def test_searchMajor():
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults sms to 1 or "on"
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le") # making an account defaults sms to 1 or "on"
    assert friendList.searchMajor("danh le", "CS") == 0
    clear_all_files()
    os.remove("lastname.txt")
    os.remove("MyCollege_profiles.txt")
    os.remove("profile.txt")

    
