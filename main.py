import loginfunctions, createAccountFunctions, homeFunctions

def main():
    #Checks if the user file exists, if not create one
    print("Welcome to the Incollege website")
    print("Here is a successfull story of a person who using Incollege")
    print("This is Jone: He graduated from USF last summer")
    print("He got a job interview at Google which was post on Incollege. He also has taken many internships that were posted on Incollege. ")
    print("Do you want to watch a video of him?")
    print("Yes or No")
    select = input("Please pick an option: ")
    if select =="Yes":
       print("Video is now playing")
    elif select =="No":
       print("I know you already love that story ")
       exit()
    else:
       print("Invalid selection")
       exit()
    loginfunctions.existsUserPasswordFile()
    
    homeFunctions.connectPeople()
  
    #Home screen
    print("Please select an option to create an account:")
    print("[1] Log in")
    print("[2] Create an Account")
    select = input("Selection: ")
    #Selection functions
    if select == "1":
        loginfunctions.loginPage()
    elif select == "2":
        #Perform account creation process
        createAccountFunctions.createAcc()
    else:
        print("Invalid option, terminating program")
        exit()

main()
