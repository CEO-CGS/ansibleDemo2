#!/usr/bin/python
from github import Github
import sys
import os
import datetime
  
Current_Date_Formatted = datetime.datetime.today().strftime ('%d-%m-%Y')

# authenticate to github
g = Github(os.environ['ACCESS_TOKEN'])
# get the authenticated user
user = g.get_user()

# Then play with your Github objects:
for repo in user.get_repos():
    print(repo.name)
    
repo = g.get_repo("CEO-CGS/ansibleDemo2")
contents = repo.get_contents("/errors/README.md")

#adds new content
newContent = contents.decoded_content.decode() + "|" + str(Current_Date_Formatted) + " | " + str(sys.argv) + "|\n" 

print(newContent)

repo.update_file(contents.path, "more tests",str.encode(newContent), contents.sha)

