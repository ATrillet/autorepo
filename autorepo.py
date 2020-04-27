import os
import subprocess
from os import path
import platform
import git
from github import Github

if platform.system() == "Darwin":
    save_path = "/Users/drewtrillet/Desktop/CodingPractice/Python/"
else:
    save_path = r"C:/Users/andre/Documents/CodingPractice/Python/"

repo_name = input("Enter file name: ")
save_path = os.path.join(save_path, repo_name)
r = git.Repo.init(save_path)
r.index.commit("initial commit")
test = os.environ['GITUSER']
g = Github(test, os.environ['GITPASSWORD'])
u = g.get_user()
repo = u.create_repo(repo_name)

remote = r.create_remote(
    'origin', url='https://github.com/ATrillet/'+repo_name+'.git')
