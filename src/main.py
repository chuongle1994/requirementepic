import loginfunctions, createAccountFunctions, homeFunctions

def main():

    # Creating files for database
    loginfunctions.existsUserPasswordFile()
    loginfunctions.existsJobPostsFile()
    loginfunctions.existsFirstLastFullNameFile()
    loginfunctions.existsCurrentUserData()

    # trigger success story
    homeFunctions.successStory()

    #Home screen
    print("\nPlease select an option to create an account:")
    print("[1] Log in")
    print("[2] Create an Account")
    print("[3] Connect with others")
    select = input("Selection: ")
    #Selection functions
    if select == "1":
        loginfunctions.loginPage()
        main()

    elif select == "2":
        #Perform account creation process
        createAccountFunctions.createAcc()
        
    elif select == "3":
        homeFunctions.connectPeople()
        main()
        
    else:
        print("Invalid option, terminating program")
        exit()

    loginfunctions.clearFile("currentUserData.txt")
    return

main()