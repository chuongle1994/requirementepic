
from fileinput import close
import createAccountFunctions


# test if number of account is greater than 5
def test_accNumTest():
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    createAccountFunctions.storeData("dinhle", "Abcdef1!", "dinh", "le", "dinh le")
    createAccountFunctions.storeData("chuongle", "Abcdef1!", "chuong", "le", "chuong le")
    createAccountFunctions.storeData("hyunjung", "Abcdef1!", "hyunjung", "lee", "hyungjung lee")
    assert createAccountFunctions.checkAccNum() == 1
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

    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le")
    createAccountFunctions.storeData("dinhle", "Abcdef1!", "dinh", "le", "dinh le")
    createAccountFunctions.storeData("chuongle", "Abcdef1!", "chuong", "le", "chuong le")
    assert createAccountFunctions.checkAccNum() == 0
    user = open("users.txt", "w")
    user.close()
    passw = open("passwords.txt", "w")
    passw.close()

# check if there is duplicated account
def test_checkDup():
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le")
    assert createAccountFunctions.checkUser("trile") == 1
    assert createAccountFunctions.checkUser("triiile") == 0
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

# check if passwords are eligible
def test_checkPass():
    assert createAccountFunctions.checkPass("abc") == 1
    assert createAccountFunctions.checkPass("aaaaaaaaaaa") == 1
    assert createAccountFunctions.checkPass("AAAAAAAAAAA") == 1
    assert createAccountFunctions.checkPass("AAAAA!!!!!!") == 1
    assert createAccountFunctions.checkPass("AAAAA11111") == 1
    assert createAccountFunctions.checkPass("AAAAAA1111!") == 0