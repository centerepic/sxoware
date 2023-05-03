import os
import git

local_folder_path = "C:/Users/Sasha/Downloads/sxoware"
github_repo_url = "https://github.com/centerepic/sxoware.git"

# Initialize a new git repository or open an existing one
if not os.path.exists(os.path.join(local_folder_path, ".git")):
    repo = git.Repo.init(local_folder_path)
else:
    repo = git.Repo(local_folder_path)

# Add the files to the repository
repo.index.add("*")

# Commit the changes
repo.index.commit("Automatically committed by Commiter.py")

# Add the remote repository
origin = None
for remote in repo.remotes:
    if remote.name == 'origin':
        origin = remote
        break
if not origin:
    origin = repo.create_remote('origin', github_repo_url)

# Push the changes to the remote repository
try:
    origin.push(refspec="refs/heads/master:refs/heads/master", set_upstream=True, force = True)
    print("Changes pushed to remote repository")
except git.exc.GitCommandError as e:
    print("Error:", e)