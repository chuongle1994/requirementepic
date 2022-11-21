import os
import linkFunctions, createAccountFunctions, loginfunctions, ast
 
# get control number: 1 is "on" and 0 is "off"
def get_control_value(control):
    usersName = loginfunctions.getUsersName()
    with open("controls.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)
    # Modify data
    if data["Username"] == usersName and data[control] == 1:
        return 1
    elif data["Username"] == usersName and data[control] == 0:
        return 0

def get_current_language(language):
    usersName = loginfunctions.getUsersName()
    with open("language.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)
    # Modify data
    if data["Username"] == usersName and data[language] == "English":
        return "English"
    elif data["Username"] == usersName and data[language] == "Spanish":
        return "Spanish"
    

# clear all created files
def clear_all_files():
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")
    loginfunctions.clearFile("currentUserData.txt")
    loginfunctions.clearFile("controls.txt")

    os.remove("firstname.txt")
    os.remove("controls.txt")
    os.remove("currentUserData.txt")
    os.remove("fullname.txt")
    os.remove("users.txt")
    os.remove("passwords.txt")
    os.remove("lastname.txt")
    
# test email change
def test_changeEmail():
    loginfunctions.existsCurrentUserData()
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults email to 1 or "on"
    loginfunctions.storeUserData("trile")           # store user data
    linkFunctions.firstControlsSetting("tri le")    # set default controls for user
    assert get_control_value("Email") == 1          # make sure email is defaulted to 1
    linkFunctions.email()                           # change email to 0
    assert get_control_value("Email") == 0          # make sure email is 0
    clear_all_files()

# test sms change
def test_changeSMS():
    loginfunctions.existsCurrentUserData()
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults sms to 1 or "on"
    loginfunctions.storeUserData("trile")           # store user data   
    linkFunctions.firstControlsSetting("tri le")    # set default controls for user
    assert get_control_value("SMS") == 1            # make sure sms is defaulted to 1
    linkFunctions.sms()                             # change sms to 0
    assert get_control_value("SMS") == 0            # make sure email is 0
    clear_all_files()

# test advertising change
def test_changeAdvertising():
    loginfunctions.existsCurrentUserData()
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults advertising to 1 or "on"
    loginfunctions.storeUserData("trile")           # store user data
    linkFunctions.firstControlsSetting("tri le")    # set default controls for user
    assert get_control_value("Advertising") == 1    # make sure advertising is defaulted to 1
    linkFunctions.advertising()                     # change advertising to 0
    assert get_control_value("Advertising") == 0    # make sure advertising is 0
    clear_all_files()

# test language default
def test_language():
    loginfunctions.existsCurrentUserData()
    loginfunctions.existsLanguageFile()
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults language to English
    loginfunctions.storeUserData("trile")                   # store user data
    linkFunctions.firstLanguageSetting("tri le")            # set default controls for user
    assert get_current_language("Language") == "English"    # make sure language is english
    linkFunctions.changeLanguage()                          # change language
    assert get_current_language("Language") == "Spanish"    # make sure language is spanish
    loginfunctions.clearFile("language.txt")
    clear_all_files()
    os.remove("language.txt")