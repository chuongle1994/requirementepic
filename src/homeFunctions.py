import loginfunctions, createAccountFunctions

def playVideo():
    print("\nVideo is now playing")
    return "Video is now playing"

def successStory():
    print("\nWelcome to the InCollege website.")
    print("Here is a successful story of a person who has used InCollege")
    print("This is Jone: He graduated from USF last summer.")
    print("He got a job interview at Google which was posted on InCollege. He has also completed internships that were posted on InCollege. ")

    while(True):
        print("\nWould you like to watch a video about this?")
        print("[1] Yes")
        print("[2] No")
        select = input("Please pick an option: ")
        if select == "1":
          playVideo()
          break
        elif select == "2":
          print("\nNavigating to the homepage...")
          return
        else:
          print("Invalid selection. Try again")
          continue
    return

def signInScreen():
    # Login screen
    print("\nPlease select an option to login (0 to exit program): ")
    print("[1] Log in")
    print("[2] Create an Account")

    select = input("Selection: ")
    # Selection functions
    if select == "1":
        loginfunctions.loginPage()
        loginfunctions.clearFile("currentUserData.txt")

    elif select == "2":
        # Perform account creation process
        createAccountFunctions.createAcc()
        signInOption()

    elif select == "0":
        print("Terminating program")
        exit()

    else:
        print("Invalid option, try again")
        signInScreen()

def signInOption():
    print("\nDo you want to login now?")
    print("[1] Yes")
    print("[2] No")
    select = input("Please pick an option: ")
    if select == "1":
        loginfunctions.loginPage()
    elif select == "2":
        return
    else:
        print("Invalid selection. Try again")
        signInOption()

def goBackToMainOption():
    print("\nWould you like to continue to our main options?")
    print("[1] Yes")
    print("[2] No")
    select = input("Please pick an option: ")
    if select == "1":
        loginfunctions.displayOptions()
    elif select == "2":
        return
    else:
        print("Invalid selection. Try again")
        goBackToMainOption()

def checkMatch(fullname):
    with open('fullname.txt', 'r') as file:
    # read all content from the fullname file using read()
        content = file.read()
    # check if fullname present or not
    if fullname in content:
        print("\nThey are a part of the Incollege system")
        return "\nThey are a part of the Incollege system"
    else:
        print("\nThey are not yet a part of the InCollege system yet")
    return "\nThey are not yet a part of the InCollege system yet"

def connectPeople():
    print("\nPlease enter the name you want to connect.")
    #input firstname
    firstname = input("First name: ")
    # input lastname
    lastname = input("Last name: ")
    fullname = firstname + " " + lastname 
    response = checkMatch(fullname)
    if response == "\nThey are a part of the Incollege system":
        contactFound()
    else:
        goBackToMainOption()

def contactFound():
    print("\nContact was found in InCollege. Please select from the following options: ")
    print("[1] Log in")
    print("[2] Sign up and join your friends.")
    print("[3] Return to previous level.")
    
    select = input("Selection: ")

    #Selection functions
    if select == "1":
        loginfunctions.loginPage()
        loginfunctions.clearFile("currentUserData.txt")
        return
    elif select == "2":
        #Perform account creation process
        createAccountFunctions.createAcc()
        signInOption()
        return
    elif select == "3":
        loginfunctions.displayOptions()
    else:
        print("Invalid selection. Try again")
        contactFound()
        return
