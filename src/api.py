from os.path import exists
import os
import json
import ast
# create jobAPI
def createJobApi():
    if exists("MyCollege_jobs.txt") == 0:
        file = open("MyCollege_jobs.txt", "w")
        file.close()

def updateJobApi():
    if(os.stat("jobPosts.json").st_size == 0):
        print("No jobs found")
        return
    
    jobs = []
    obj = json.load(open("jobPosts.json"))
    if(len(obj["job-posts"]) != 0):
        for i in range(len(obj["job-posts"])):
            jobs.append(obj["job-posts"][i])

    with open("MyCollege_jobs.txt", 'w') as file:
        pass

    with open("MyCollege_jobs.txt", 'a') as file:
        for i in jobs:
            file.write(f'{i["title"]}\n{i["description"]}\n{i["employer"]}\n{i["location"]}\n{i["salary"]}\n"====="\n')

def createProfileApi():
    if exists("MyCollege_profiles.txt") == 0:
        file = open("MyCollege_profiles.txt", "w")
        file.close()

def updateProfileApi():
    
    profiles = []
    with open("profile.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            profiles.append(data)
    
    educarions = []
    with open("profEducation.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            educarions.append(data)

    experiences = []
    with open("profExperience.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
            experiences.append(data)


    with open("MyCollege_profiles.txt", 'w') as file:
        pass

    with open("MyCollege_profiles.txt", 'a') as file:
        for i in profiles:
            file.write(f'{i["Title"]}\n{i["Major"]}\n{i["University"]}\n{i["About"]}\n{i["Experience"]}\n')
            for exp in experiences:
                file.write(f'{exp["Title"]}\n{exp["Employer"]}\n{exp["Start"]}\n{exp["End"]}\n{exp["Location"]}\n{exp["Description"]}\n')
            file.write(f'{i["Education"]}\n')
            for edu in educarions:
                file.write(f'{edu["School"]}\n {edu["Degree"]}\n {edu["Years"]}\n=====\n')