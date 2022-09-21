import loginfunctions, createAccountFunctions

def connectPeople():
    isSuccessfulFinding = False    
    #input firstname
    print("Find someone that you know to help you: ")
    while(isSuccessfulFinding == False): 
         #validate finding 
        firstname = input("First name: ")
         #input lastname
        lastname = input("Last name: ")
        fullname = firstname + " " + lastname 
        print("opening file")
        with open('fullname.txt', 'r') as file:
        # read all content from the fullname file using read()
          content = file.read()
        # check if fullname present or not
          if fullname in content:
            print("\nThey are a part of the Incollege system")
            contactFound()
            isSuccessfulFinding == True
          else:
            print("They are not yet a part of the Incollege system yet, please try again\n")

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
        # return to previous level
        # main.main()
        print("test")

    else:
        print("Invalid option, terminating program")
        exit()