import loginfunctions
import ast

def navigationLinks():
    # Useful Links Lists
    print("\nUseful Links")
    usefulLinks = ["[a] General", "[b] Browse InCollege", "[c] Business Solutions", "[d] Directories"]
    print('\n'.join(map(str,usefulLinks)))
    # InCollege Important Links Lists
    print("\nInCollege Important Links")
    importantLinks = ["[A] A Copyright Notice", "[B] About", "[C] Accessibility", "[D] User Agreement", "[E] Privacy Policy", "[F] Cookie Policy", "[G] Copyright Policy", "[H] Brand Policy", "[I] Guest Controls", "[J] Languages"]
    print('\n'.join(map(str, importantLinks)))


def selectLinks():
    select = input("Please select an option (0 to exit): ")
    if select == "a":
        general()
    elif select == "b":
        browseInCollege()
    elif select == "c":
        businessSolutions()
    elif select == "d":
        directories()
    elif select == "A":
        copyrightNotice()
    elif select == "B":
        aboutImportant()
    elif select == "C":
        accessibility()
    elif select == "D":
        userAgreement()
    elif select == "E":
        privacyPolicy()
    elif select == "F":
        cookiePolicy()
    elif select == "G":
        copyrightPolicy()
    elif select == "H":
        brandPolicy()
    elif select == "I":
        guestControls()
    elif select == "J":
        languages()
    elif select == "0":
        return
    else:
        print("Invalid input. Try selecting an option again.")
        navigationLinks()
        selectLinks()

# Useful Links: 1. General
def general():
    print("\nGeneral")
    generalLinks = ["[1] Sign Up", "[2] Help Center", "[3] About", "[4] Press", "[5] Blog", "[6] Careers", "[7] Developers", "[8] Return to previous level"]
    print('\n'.join(map(str, generalLinks)))

    select = input("Please select an option (0 to exit): ")
    if select == "1":
        signUp()
        previousToGeneral()
    elif select == "2":
        helpCenter()
        previousToGeneral()
    elif select == "3":
        aboutUseful()
        previousToGeneral()
    elif select == "4":
        press()
        previousToGeneral()
    elif select == "5":
        blog()
        previousToGeneral()
    elif select == "6":
        careers()
        previousToGeneral()
    elif select == "7":
        developers()
        previousToGeneral()
    elif select == "8":
        navigationLinks()
        selectLinks()
    elif select == "0":
        return
    else:
        print("Invalid input. Try selecting an option again.")
        general()

def previousToGeneral():
    print("\nWould you like to return to previous level?")
    print("[1] Yes")
    print("[2] No")
    
    select = input("Please pick an option: ")
    if select == "1":
        general()
    elif select == "2":
        return
    else:
        print("Invalid selection. Try again")
        previousToGeneral
        
        
# Useful Links: 2. Browse InCollege
def browseInCollege():
    print("\nUnder construction")
    previousToNavi()
    
# Useful Links: 3. Business Solutions
def businessSolutions():
    print("\nUnder construction")
    previousToNavi()

# Useful Links: 4. Directories
def directories():
    print("\nUnder construction")
    previousToNavi()

def previousToNavi():
    print("\nWould you like to return to previous level?")
    print("[1] Yes")
    print("[2] No")
    
    select = input("Please pick an option: ")
    if select == "1":
        navigationLinks()
        selectLinks()
    elif select == "2":
        return
    else:
        print("Invalid selection. Try again")
        previousToNavi()
    
# Useful Links: General: 1. Sign Up
def signUp():
    loginfunctions.loginPage()

# Useful Links: General: 2. Help Center
def helpCenter():
    print("\nWe're here to help")

# Useful Links: General: 3. About
def aboutUseful():
    print("\nIn College: Welcome to InCollege, the world's largest college student network with many users in many countries and territories worldwide")

# Useful Links: General: 4. Press
def press():
    print("\nIn College Pressroom: Stay on top of the latest news, updates,and reports")

# Useful Links: General: 5. Blog
def blog():
    print("\nUnder construction")

# Useful Links: General: 6. Careers
def careers():
    print("\nUnder construction")

# Useful Links: General: 7. Developers
def developers():
    print("\nUnder construction")


# Important Links: 1. Copyright Notice
def copyrightNotice():
    print("\n© InCollege Corporation 2022. All Rights Reserved.")
    previousToNavi()

# Important Links: 2. About
def aboutImportant():
    print("\nAbout InCollege\nWelcome to InCollege website, the world's largest professional network for all college students!\n")
    previousToNavi()

# Important Links: 3. Accessibility
def accessibility():
    print("\nInCollege is a place where every student can find their opportunity. Whatever your goals, ideas, and abilities are, we're here to help you succeed.")
    previousToNavi()

# Important Links: 4. User Agreement
def userAgreement():
    print("\nWhen you use our services you agree to all of these terms. Your use of our services is also subject to our cookie policy and our privacy policy, which covers how we collect, use, share, and store your personal information. Please see the detail. ")
    previousToNavi()

# Important Links: 5. Privacy Policy
def privacyPolicy():
    print("\nThe InCollege Corporation cares about your privacy and the security of your information. We want to be familiar with how we collet, use and disclose information, including personal information.")
    
    # add additional option "Guest Control"
    print("\nFor your privacy, we provide guest control setting. Do you want to change your setting?")
    print("[1] Yes")
    print("[2] No")
    select = input("Please pick an option: ")
    if select == "1":
        guestControls()
    else:
        previousToNavi()

# Important Links: 6. Cookie Policy
def cookiePolicy():
    print("\nAt InCollege, cookie can be used to recognized you when you visit InCollege, remember your preferences, and give you a personalized experience that's in line with your setting. Cookies make your interations with InCollege faster and more secure.")
    previousToNavi()

# Important Links: 7. Copyright Policy
def copyrightPolicy():
    print("\nYou may not share, distribute, or reproduce in any way any copyrighted material, trademarks, or other proprietary information belonging to others without obtaining the prior written consent of the owner of such proprietary rights.")
    previousToNavi()
    
# Important Links: 8. Brand Policy
def brandPolicy():
    print("\nOur trademarks and other brand features are protected by law.  You’ll need our permission in order to use them.")
    previousToNavi()
    
# Important Links: 9. Guest Controls
def firstControlsSetting(username):
    controls = {"Email": 1, "SMS": 1, "Advertising": 1}
    # add username to dictionary
    controls["Username"] = username
    # add dictionay to "controls.txt"
    controlsFile = open("controls.txt", "a")
    controlsFile.write("{}\n".format(controls))
    controlsFile.close()


def currentSetting():
    usersName = loginfunctions.getUsersName()
    if usersName == "":
        print("\nPlease login to change setting!")
        print("Do you want to login for now?")
        print("[1] Yes")
        print("[2] No")
        select = input("Please pick an option: ")

        if select == "1":
            loginfunctions.loginPage()
        else:
            navigationLinks()
            selectLinks()
        
    else: 
        print("\nHere is your current setting: ")
        with open("controls.txt", "r") as file:
            for line in file:
                data = ast.literal_eval(line)
                if data["Username"] == usersName:
                    print(data)
                    break
                
def guestControls():
    currentSetting()
    print("\nWould you like to change the setting?")
    print("[1] Email")
    print("[2] SMS")
    print("[3] Targeted Advertising features")

    onOff = input("Please pick an option to change (0 to exit): ")   
    if onOff == "1":
        email()
        guestControls()
    elif onOff == "2":
        sms()
        guestControls()
    elif onOff == "3":
        advertising()
        guestControls()
    elif onOff == "0":
        return
    else:
        print("Invalid input. Try selecting an option again.")
        guestControls()

def email():
    usersName = loginfunctions.getUsersName()
    with open("controls.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)

    # Modify data
    if data["Username"] == usersName and data["Email"] == 1:
        data["Email"] = 0
    elif data["Username"] == usersName and data["Email"] == 0:
        data["Email"] = 1

    with open("controls.txt", "w") as fw:
        fw.write(repr(data))
            
def sms():
    usersName = loginfunctions.getUsersName()
    with open("controls.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)

    # Modify data
    if data["Username"] == usersName and data["SMS"] == 1:
        data["SMS"] = 0
    elif data["Username"] == usersName and data["SMS"] == 0:
        data["SMS"] = 1

    with open("controls.txt", "w") as fw:
        fw.write(repr(data))

def advertising():
    usersName = loginfunctions.getUsersName()
    with open("controls.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)

    # Modify data
    if data["Username"] == usersName and data["Advertising"] == 1:
        data["Advertising"] = 0
    elif data["Username"] == usersName and data["Advertising"] == 0:
        data["Advertising"] = 1

    with open("controls.txt", "w") as fw:
        fw.write(repr(data))
    

# Important Links: 10. Languages
def firstLanguageSetting(username):
    setting = {"Language": "English"}
    setting["Username"] = username
    # add dictionay to "controls.txt"
    settingFile = open("languege.txt", "a")
    settingFile.write("{}\n".format(setting))
    settingFile.close()

def currentLanguage():
    print("\nHere is your current Language: ")
    usersName = loginfunctions.getUsersName()
    if usersName == "":
        print("Please login to change setting!")
        loginfunctions.loginPage()
    
    with open("languege.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            if data["Username"] == usersName:
                print(data)
                break

def changeLanguage():
    usersName = loginfunctions.getUsersName()
    with open("languege.txt", "r") as f:
        for line in f:
            data = ast.literal_eval(line)

    # Modify data
    if data["Username"] == usersName and data["Language"] == "English":
        data["Language"] = "Spanish"
    elif data["Username"] == usersName and data["Language"] == "Spanish":
        data["Language"] = "English"

    with open("languege.txt", "w") as fw:
        fw.write(repr(data))
    
def languages():
    usersName = loginfunctions.getUsersName()
    default = {"Language": "English"}
    
    if usersName == "":
        print("\nHere is your current Language: ")
        print(default)
        print("\nSelect the language you want:")
        print("[1] English")
        print("[2] Spanish")
        select = input("Please pick an option: ")
        if select == "1":
            default["Language"] = "English"
        elif select == "2":
            default["Language"] = "Spanish"
        else:
            print("Invalid input. Try selecting an option again.")
            languages()
        previousToNavi()
        
    else:
        currentLanguage()
        print("\nSelect the language you want:")
        print("[1] English")
        print("[2] Spanish")
        
        select = input("Please pick an option: ")
        if select == "1":
            changeLanguage()
        elif select == "2":
            changeLanguage()
        else:
            print("Invalid input. Try selecting an option again.")
            languages()