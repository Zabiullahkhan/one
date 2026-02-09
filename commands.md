- `git --version`

- `git status`

- `git config --global user.email "khanzabiullah55@gmail.com"` ###To change use same commands to edit/overwrite
- `git config --global user.name "Zabiullah Khan"`

- `git config --list`

#### Creating a Repository
- step 1: `git status`
- step 2: `git init` ###You can now be able to see the .git folder in your folder using 'ls -la'
- step 3: `git add <file1> <file2>....` or `git add .` To add all the folder
- step 4: `git rm --cached <file>...` to unstage changes
- step 5: `git commit -m "your message"`
- step 6: `git log`
- step 7: add `.gitignore` file for some files to get ignored like `.env`, `.vscode`, `node_modules`etc


#### To change the code editor
- `git config --global core.editor "code --wait"`

#### Git Ignore
- it is a file named `.gitignore` where you can put the names of all those files you want to be ignred during commit or push
- you find out any gitgenerator files online like gitignore file for vscode etc

#### Git Keep
- it is a file named `.gitkeep` if you want to keep your *empty* folders in to your repo, then keep `.gitkeep` file inside the empty folder
- because git do not track the empty folders

#### MAJOR STEPS :- Write --> Add --> Commit

- `git init` --> Working Directory --> `git add` --> Staging area --> `git commit` --> Repository --> `git push` --> GitHub


#### Creating a New Branch
- `git branch`
- `git branch bug-fix`
- `git switch bug-fix`
- `git log`
- `git switch main`
- `git switch -c dark-mode`
- `git checkout orange-mode`
Some points to note:-
- *git branch* - This command lists all the branches in the current repository
- *git branch bug-fix* - This command creates a new branch called `bug-fix`.
- *git switch bug-fix* - This command switches to `bug-fix` branch.
- *git log* - This command shows the commit history for the current branch.
- *git switch main* - This command swithes to `main` branch.
- *git switch -c dark-mode* - This command creates a new branch named `dark-mode`. the `-c` flag is used to create a new branch.
- *git checkout orange-mode* - This command switches to the `orange-mode` branch.    

#### Rename a branch
- `git branch -m <old-branch-name> <new-branch-name>`

#### Delete a branch
- `git branch -d <branch-name>`

#### Checkout a branch
- `git checkout <branch-name>`

#### Merging branches
- In Git we two types of merges:
    - Fast-Forward Merges (if branches have not diverged)
    - 3-Way Merges (if branches have diverged)

- *Fast-Forward Merge diagram*
        main:         o----o------------------------------o (merge)
                            \                            /
                             \                          /
                              \                        /
        bug-fix:               o----------o----------o

- `git checkout main`- This command switches to the `main` branch.
- `git merge bug-fix`- This command merges the `bug-fix` branch in to the `main` branch.




- *3-Way Merge diagram*
        main:         o----o----o----o--------------------o (merge)
                            \                            /
                             \                          /
                              \                        /
        bug-fix:               o----------o----------o          



