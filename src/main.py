import loginfunctions, createAccountFunctions, homeFunctions

def main():

    # Creating files for database
    loginfunctions.existsUserPasswordFile()
    loginfunctions.existsJobPostsFile()
    loginfunctions.existsFirstLastFullNameFile()
    loginfunctions.existsCurrentUserData()

    # trigger success story
    homeFunctions.successStory()
    while(True):
        #Home screen
        print("\nPlease select an option to create an account:")
        print("[1] Log in")
        print("[2] Create an Account")
        print("[3] Connect with others")
        select = input("Selection: ")
        #Selection functions
        if select == "1":
            loginfunctions.loginPage()
            break
        elif select == "2":
            #Perform account creation process
            createAccountFunctions.createAcc()
            continue
        elif select == "3":
            homeFunctions.connectPeople()
            continue
        else:
            print("Invalid option, terminating program")
            exit()

    loginfunctions.clearFile("currentUserData.txt")

main()