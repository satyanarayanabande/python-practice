import os
folders = input ("please provide list of folders names with spaces in between:").split()
for folder in folders:
  files = os.listdir(folder)
  print(files)

output:
@satyanarayanabande ➜ /workspaces/python-practice/Day-08/01-notes (main) $ python test.py
please provide list of folders names with spaces in between:/tmp
['vscode-ipc-69a6fb1d-e735-4873-a9ae-ba7636c0c707.sock', 'codespaces_logs', 'pyright-9387-TjxqHlBF4E99', 'vscode-git-809ed7cea5.sock', 'python-languageserver-cancellation', 'sshd.log', 'dockerd.log', 'pyright-9387-NdX2J1m6p1Vx', 'BuildScriptGenerator', 'vscode-ipc-b7192f44-e041-40a0-bcea-8cd30d49e068.sock', 'storage_version.txt', 'system-commandline-sentinel-files', 'vscode-ipc-ce8dea39-5b6b-4c99-b6b4-42b505feee45.sock', 'pyright-9387-G6tNaOTYYamL']
@satyanarayanabande ➜ /workspaces/python-practice/Day-08/01-notes (main) $ python test.py
please provide list of folders names with spaces in between:/opt
['containerd', 'oryx', 'tmp', 'python', 'dotnet', 'conda']

==============================

import os
folders = input ("please provide list of folders names with spaces in between:").split()
for folder in folders:
  files = os.listdir(folder)
  print ("=== listing files [for the folder-"+folder)
  print(files)

output:
@satyanarayanabande ➜ /workspaces/python-practice/Day-08/01-notes (main) $ python test.py
please provide list of folders names with spaces in between:/opt
=== listing files [for the folder-/opt
['containerd', 'oryx', 'tmp', 'python', 'dotnet', 'conda']

=============================+==
import os
folders = input ("please provide list of folders names with spaces in between:").split()
for folder in folders:
  try:
    files = os.listdir(folder)
  except FileNotFoundError:
    print("please provide a valid folder name")
    continue
  print ("=== listing files [for the folder-"+folder)
  print(files)

output:
@satyanarayanabande ➜ /workspaces/python-practice/Day-08/01-notes (main) $ python test.py
please provide list of folders names with spaces in between:/xyz
please provide a valid folder name
@satyanarayanabande ➜ /workspaces/python-practice/Day-08/01-notes (main) $ 
@satyanarayanabande ➜ /workspaces/python-practice/Day-08/01-notes (main) $ python test.py
please provide list of folders names with spaces in between:/opt
=== listing files [for the folder-/opt
['containerd', 'oryx', 'tmp', 'python', 'dotnet', 'conda']
