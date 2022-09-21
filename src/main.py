import loginfunctions, createAccountFunctions, homeFunctions

def main():

    # Creating files for database
    loginfunctions.existsUserPasswordFile()
    loginfunctions.existsJobPostsFile()
    loginfunctions.existsFirstLastFullNameFile()

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
        elif select == "2":
            #Perform account creation process
            createAccountFunctions.createAcc()
        elif select == "3":
            homeFunctions.connectPeople()
        else:
            print("Invalid option, terminating program")
            exit()

main()