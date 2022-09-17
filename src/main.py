from functions import loginfunctions, createAccountFunctions

def main():
    #Checks if the user file exists, if not create one
    loginfunctions.existsUserPasswordFile();

    #Home screen
    print("Please select an option:")
    print("[1] Log in")
    print("[2] Create an Account")
    select = input("Selection: ")

    #Selection functions
    if select == "1":
        loginfunctions.loginPage()

    elif select == "2":
        createAccountFunctions.accountCreation()
    else:
        print("Invalid option, terminating program")
        exit()

main()