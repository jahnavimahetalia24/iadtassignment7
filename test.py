import git
import shutil
import os

# clone repo
git.Git("/Users/jahnavimahetalia/assignment7iadt").clone("https://github.com/jahnavimahetalia24/iadtassignment7.git")
repo = git.Repo("iadtassignment7")

# path to source directory
src_dir = "/Users/jahnavimahetalia/index/index.html"

# path to dest directory
dest_dir = "/Users/jahnavimahetalia/assignment7iadt/iadtassignment7/index.html"

# getting all the files in the source directory
shutil.move(src_dir, dest_dir)

# to add specific working file(s).
repo.git.add("/Users/jahnavimahetalia/assignment7iadt/iadtassignment7/index.html") 

# commit file to repo
repo.git.commit("-m", "commit message from python script")

# push the commited file
origin = repo.remote(name='origin')
origin.push()