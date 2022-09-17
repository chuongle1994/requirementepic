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
        #Count the current number of account created
        numAccounts = 0
        with open("users.txt") as file:
            while (line := file.readline().rstrip()):
                numAccounts += 1
        file.close()

        #Perform account creation process
        createAccountFunctions.createAcc(numAccounts)
    else:
        print("Invalid option, terminating program")
        exit()

main()