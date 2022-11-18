import loginfunctions, homeFunctions, linkFunctions, apiFunctions


def main():
    # Creating files for database
    loginfunctions.existsUserPasswordFile()
    loginfunctions.existsJobPostsFile()
    loginfunctions.existsFirstLastFullNameFile()
    loginfunctions.existsCurrentUserData()

    # Run input APIs
    apiFunctions.inputAccountAPI()
    apiFunctions.inputJobsAPI()

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