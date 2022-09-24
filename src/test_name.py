import createAccountFunctions, loginfunctions

users = [["trile", "Abcdwd1!", "tri", "le", "TriLe"],
    ["chuongle", "Abcdwd1!", "chuong", "le", "ChuongLe"],
    ["danhle", "Abcdwd1!", "danh", "le", "DanhLe"],
    ["dinhle", "Abcdwd1!", "dinh", "le", "DinhLe"],
    ["hyunjunglee", "Abcdwd1!", "hyunjung", "lee", "HyunjungLee"]]


createAccountFunctions.storeData(users[0][0],users[0][1],users[0][2],users[0][3],users[0][4])
createAccountFunctions.storeData(users[1][0],users[1][1],users[1][2],users[1][3],users[1][4])
createAccountFunctions.storeData(users[2][0],users[2][1],users[2][2],users[2][3],users[2][4])
createAccountFunctions.storeData(users[3][0],users[3][1],users[3][2],users[3][3],users[3][4])
createAccountFunctions.storeData(users[4][0],users[4][1],users[4][2],users[4][3],users[4][4])


# test first name creation
def test_FirstName():
    
    
    passed = 0

    with open("firstname.txt") as file:                 
        while (line := file.readline().rstrip()):
            if line == users[passed][2]:
                passed += 1
            else:
                break

    assert passed == 5

# test last name creation
def test_LastName():
    
    
    passed = 0

    with open("lastname.txt") as file:                 
        while (line := file.readline().rstrip()):
            if line == users[passed][3]:
                passed += 1
            else:
                break

    assert passed == 5

# test full name creation
def test_FullName():
    
    
    passed = 0

    with open("fullname.txt") as file:                 
        while (line := file.readline().rstrip()):
            if line == users[passed][4]:
                passed += 1
            else:
                break

    assert passed == 5

    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")


