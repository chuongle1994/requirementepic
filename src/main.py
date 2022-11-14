import loginfunctions, homeFunctions, linkFunctions


def main():

    # Creating files for database
    loginfunctions.existsUserPasswordFile()
    loginfunctions.existsJobPostsFile()
    loginfunctions.existsFirstLastFullNameFile()
    loginfunctions.existsCurrentUserData()

    # trigger success story
    homeFunctions.successStory()

    # Add navigation links
    linkFunctions.navigationLinks()
    linkFunctions.selectLinks()

    # Add sign-in screen
    homeFunctions.signInScreen()

    loginfunctions.clearFile("currentUserData.txt")
    return


main()