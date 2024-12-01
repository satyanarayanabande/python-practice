import sys

type = sys.argv[1]

if type == "t2.micro":
  print ("it will charge you 2 dollars a day")

elif type == "t2.medium":
  print ("it will charge you 4 dollars a day")

elif type == "t2.xlarge":
  print ("it will charge you 8 dollars a day")

else:
  print ("please provide a valid instance type")

# @satyanarayanabande ➜ /workspaces/python (main) $ python test3.py t2.micro
it will charge you 2 dollars a day
@satyanarayanabande ➜ /workspaces/python (main) $ python test3.py t3.micro
please provide a valid instance type
@satyanarayanabande ➜ /workspaces/python (main) $ python test3.py t3.medium
please provide a valid instance type
@satyanarayanabande ➜ /workspaces/python (main) $ python test3.py t2.medium
it will charge you 4 dollars a day
