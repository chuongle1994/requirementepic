import loginfunctions, createAccountFunctions


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

def test_findSomeone():
    assert loginfunctions.findSomeone() == "\nunder construction"

def test_validateLogin():
    createAccountFunctions.storeData("trile", "Abcdef1!", "Tri", "Le", "Tri Le")
    createAccountFunctions.storeData("danhle", "Abcdef1!", "Danh", "Le", "Danh Le:")
    assert loginfunctions.validateLogin("trile", "Abcdef1!") == True
    assert loginfunctions.validateLogin("danhle", "Abcdef1!") == True
    loginfunctions.clearFile("firstname.txt")
    loginfunctions.clearFile("lastname.txt")
    loginfunctions.clearFile("fullname.txt")
    loginfunctions.clearFile("users.txt")
    loginfunctions.clearFile("passwords.txt")