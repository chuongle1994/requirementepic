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

# search for job / internship and find someone you know result in "under construction"

def test_searchForJob():
    assert loginfunctions.searchForJob() == "\nunder construction"

def test_findSomeone():
    assert loginfunctions.findSomeone() == "\nunder construction"

def test_validateLogin():
    createAccountFunctions.storeData("test1", "Password123!")
    createAccountFunctions.storeData("test2", "Hitest123!")
    assert loginfunctions.validateLogin("test1", "Password123!") == True
    assert loginfunctions.validateLogin("test2", "Hitest123!") == True
    user = open("users.txt", "w")
    user.close()
    passw = open("passwords.txt", "w")
    passw.close()