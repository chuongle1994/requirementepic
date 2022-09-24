import loginfunctions

#Checks if the code returns the correct message when the job post reaches it's maximum limit.
def test_postLimit():
    #Create file
    loginfunctions.existsJobPostsFile()
    #Create 5 random data
    loginfunctions.writeJobPost({
        'jobs' : [
            {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }
        ]
    }, {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }, "jobPosts.json")
    loginfunctions.writeJobPost({
        'jobs' : [
            {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }
        ]
    }, {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }, "jobPosts.json")
    loginfunctions.writeJobPost({
        'jobs' : [
            {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }
        ]
    }, {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }, "jobPosts.json")
    loginfunctions.writeJobPost({
        'jobs' : [
            {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }
        ]
    }, {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }, "jobPosts.json")
    loginfunctions.writeJobPost({
        'jobs' : [
            {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }
        ]
    }, {
                "title": "SWE",
                "description": "Intern",
                "employer": "Tri Le",
                "location": "Tampa",
                "salary": "50000",
                "poster-name": "Tri Le"
            }, "jobPosts.json")
    #Performs the check to see if the job posts exceeds 5.
    assert loginfunctions.inputJobInfo() == "\nThe system can only permit up to 5 jobs to be posted."

    #Clear file
    loginfunctions. clearFile("jobPosts.json")