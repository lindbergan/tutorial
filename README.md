# Git & Terminal commands

* [Git](#git)


* [Alias](#terminal)


* [Terminal](#terminal)


* [Vim](#vim)


## Git

### Stages
1. Commited
_Saved in the git repository database_
2. Staged
_Not saved in the database, waiting to be commited_
3. Unstaged
_Files that have been edited or are new but not added to staged state_

#### Git init
`git init`
_Initializes a new git repository in the current folder_
_Creates a hidden `.git/` folder in the repo_

#### Git status
_To check the status of the repository, see what files have been changed_

`git status`
_add an alias for this, you will use it very often. I use 'gs'._

#### Git Add
_Add the following files to staged state_

`git add <file(s)>`

`git add -A`
_Adds all edited files in the repo_

#### Git commit
_Saves the edits as a commit to the database, it is now possible to revert back to this position in time_

`git commit -m 'Commit description goes here'`
_'-m' = message_

`git commit -am 'Message'`
_Adds all files and commits_

`git commit -amend`
_Adds new files to last commit, allows you to change the last commit message_

`git commit --amend -m 'newmessagehere'`

`git commit —-amend —no-edit`
_Adds new changes to last commit without editing the commit message_

#### Git reset
`git reset HEAD <file(s)>`
_Undo files from staged state_


_Different from checkout because it keeps the changes but need to be added again_

#### Remove Commit
`git rebase -i HEAD~`
_Remove last commit from local head_

#### Git branch
`git branch <branchname>`
_Creates a new timeline for your repository. Now you need to go to that timeline with `git checkout`_

#### Git checkout
`git checkout <branchname>`
_Changes to another timeline in the repository_

`git checkout -b <branchname>`
_Creates a new branchname and changes to that branch (timeline)_

`git checkout -- <filename(s)>`
_Resets the all changes to the file(s) to the state of the last commit_

#### Git push
`git push`
_Pushes all local commits to the remote origin_

`git push --set-upstream origin <branchname>`
_Creates the remote for the repository and pushes to it_

`git push -u origin <branchname>`

_`-u` is short for `--set-upstream`_

#### Git diff
`git diff --cached`
_difference of all files_

`git diff --staged`
_difference of all staged files_





@TODO: Everything from this point and below is to be reformatted in the near future

---



#### What happened since last night
```
git whatchanged
```



##### Remove last commit from Github
```
git rebase -i HEAD~ && push -f
```


#### Git Log
Formatera commits själv med "format"
```
git log --pretty=format:"%h - %an, %ar : %s"
```

##### Format Parameters:
| Option | Description |           
| ------------- |-------------|
| %H | Commit hash  |
| %h | Abbreviated commit hash |
| %T | Tree hash |
| %t | Abbreviated tree hash |
| %P | Parent hashes |
| %p | Abbreviated parent hashes |
| %an | Author name |
| %ae | Author e-mail |
| %ad | Author date (format respects the -date= option) |
| %ar | Author date, relative |
| %cn | Committer name |
| %ce | Committer email |
| %cd | Committer date |
| %cr | Committer date, relative |
| %s | Subject |

##### Ascii Graph
```
git log --graph
```

##### Log Parameters:
| Option | Description |           
| ------------- |-------------|
| -p | Show the patch introduced with each commit.|
| --stat| centered      |
| --shortstat | Display only the changed/insertions/deletions line from the --stat command. |
| --name-only | Show the list of files modified after the commit information. |
| --name-status | Show the list of files affected with added/modified/deleted information as well. |
| --abbrev-commit | Show only the first few characters of the SHA-1 checksum instead of all 40. |
| --relative-date | Display the date in a relative format (for example, "2 weeks ago") instead of using the full date format. |
| --graph | Display an ASCII graph of the branch and merge history beside the log output. |
| --pretty | Show commits in an alternate format. Options include oneline, short, full, fuller, and format (where you specify your own format). |
| -(n) | Show only the last n commits |
| --since, --after | Limit the commits to those made after the specified date. |
| --until, --before | Limit the commits to those made before the specified date. |
| --author | Only show commits in which the author entry matches the specified string. |
| --committer | Only show commits in which the committer entry matches the specified string. |

#### Remote
```
git remote add origin [address]
```
```
git push -u origin master
```

#### Fetch
##### Get data from repo without merge
```
git fetch [remote name] [branch name]
```

##### Get data from repo with merge
```
git pull [remote name] [branch name]
```

#### Tag
##### Show repo tags
```
git tag
```

#### Config
Open in vim

```
git config --global --edit
```

Set alias from terminal

```
git config --global alias.aliasnamehere "git command here remove git"
```

Ex: alias hello => git hello => git log --oneline

```
git config --global alias.hello "log --oneline"
```

### Alias
#### linus
```
log --graph --oneline --color --decorate --abbrev-commit --all
```

#### m
```
!sh -c 'git checkout master && git pull'
```

#### fuck
```
!sh -c 'git rebase -i HEAD~ && git pull -f'
```

## Terminal
#### Show hidden files
```
defaults write com.apple.finder AppleShowAllFiles -boolean YES && killall Finder
```

#### Kill dock
```
defaults write com.apple.dashboard mcx-disabled -boolean YES && killall Dock
```

#### Access android emulator
(Ex: Flickpicker project)
```
adb -s emulator-5554 shell
```

```
cd data/data/com.typeof.flickpicker/database
```

```
sqlite3 flickpicker.db
```

## Vim

### Search and replace
#### Search and replace in lineselection
x: word that you want to replace
y: word that you want to replace it with
```
:s/x/y/g
```
