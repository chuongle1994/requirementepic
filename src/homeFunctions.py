import loginfunctions, createAccountFunctions, main

def contactFound():
    print("Contact was found in InCollege. Please select from the following options: ")
    print("[1] Log in")
    print("[2] Sign up and join your friends.")
    print("[3] Return to previous level.")
    select = input("Selection: ")

    #Selection functions
    if select == "1":
        loginfunctions.loginPage()

    elif select == "2":
        #Perform account creation process
        createAccountFunctions.createAcc()

    elif select == "3":
        #Perform account creation process
        main.main()

    else:
        print("Invalid option, terminating program")
        exit()