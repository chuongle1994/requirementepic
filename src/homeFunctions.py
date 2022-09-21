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

def connectPeople():
    isSuccessfulFinding = False    
    #input firstname
    print("\nFind someone that you know to help you: ")
    while(isSuccessfulFinding == False): 
        # validate finding 
        firstname = input("First name: ")
         # input lastname
        lastname = input("Last name: ")
        fullname = firstname + " " + lastname 
        print("opening file")
        with open('fullname.txt', 'r') as file:
        # read all content from the fullname file using read()
          content = file.read()
        # check if fullname present or not
          if fullname in content:
            contactFound()
            isSuccessfulFinding == True
            break
          else:
            print("They are not yet a part of the InCollege system yet")
            return

def contactFound():
    print("\nContact was found in InCollege. Please select from the following options: ")
    print("[1] Log in")
    print("[2] Sign up and join your friends.")
    print("[3] Return to previous level.")
    
    while(True):
      select = input("Selection: ")

      #Selection functions
      if select == "1":
          loginfunctions.loginPage()
          break

      elif select == "2":
          #Perform account creation process
          createAccountFunctions.createAcc()
          break

      elif select == "3":
          #Perform account creation process
          # return to previous level
          # main.main()
          break

      else:
          print("Invalid option, please try again.")
          continue

    return