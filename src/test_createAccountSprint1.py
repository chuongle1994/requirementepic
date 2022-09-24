
from fileinput import close
import createAccountFunctions, loginfunctions


# test if number of account is greater than 5
def test_accNumTest():
    # Check if it correctly evaluates a full file.
    createAccountFunctions.storeData("trile", "Abcdef1!", "Tri", "Le", "Tri Le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "Danh", "Le", "Danh Le:")
    createAccountFunctions.storeData("dinhle", "Abcdef1!", "Dinh", "Le", "Dinh Le")
    createAccountFunctions.storeData("chuongle", "Abcdef1!", "Chuong", "Le", "Chuong Le")
    createAccountFunctions.storeData("hyunjung", "Abcdef1!", "Hyunjung", "Lee", "Hyunjung Lee")
    assert createAccountFunctions.checkAccNum() == 1
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")

    # Check if it correctly evaluates a file with one more spot.
    createAccountFunctions.storeData("trile", "Abcdef1!", "Tri", "Le", "Tri Le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "Danh", "Le", "Danh Le:")
    createAccountFunctions.storeData("dinhle", "Abcdef1!", "Dinh", "Le", "Dinh Le")
    createAccountFunctions.storeData("chuongle", "Abcdef1!", "Chuong", "Le", "Chuong Le")
    assert createAccountFunctions.checkAccNum() == 0
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")

# check if there is duplicated account
def test_checkDup():
    createAccountFunctions.storeData("trile", "Abcdef1!", "Tri", "Le", "Tri Le")
    assert createAccountFunctions.checkUser("trile") == 1 # Check for a duplicate.
    assert createAccountFunctions.checkUser("triiile") == 0 # Check for no duplicate.
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")

# check if passwords are eligible
def test_checkPass():
    assert createAccountFunctions.checkPass("abc") == 1
    assert createAccountFunctions.checkPass("aaaaaaaaaaa") == 1
    assert createAccountFunctions.checkPass("AAAAAAAAAAA") == 1
    assert createAccountFunctions.checkPass("AAAAA!!!!!!") == 1
    assert createAccountFunctions.checkPass("AAAAA11111") == 1
    assert createAccountFunctions.checkPass("AAAAAA1111!") == 0