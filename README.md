# Git & Terminal commands

* [Git](#git)


* [Alias](#terminal)


* [Terminal](#terminal)


* [Vim](#vim)


## Git
---
### Stages
1. Commited
_Saved in the git repository database_
2. Staged
_Not saved in the database, waiting to be commited_
3. Unstaged
_New files or files that have been edited but not staged_

#### Git init
`git init`
_Initializes a new git repository in the current folder_

_Creates a hidden `.git/` folder in the repo_

#### Git status
`git status`
_Used to check the status of the repository, see what files have been changed_

_add an alias for this, you will use it very often. I use '`gs`'._

#### Git Add
`git add <file(s)>`
_Add the following files to be staged_

`git add -A`
_Adds all edited files in the repository_

#### Git commit
`git commit -m 'Commit description goes here'`
_Saves the edits as a commit to the database, it is now possible to revert back to this position in time_

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


`git reset HEAD~`
_Remove last commit but keep changes_


#### Git branch
`git branch <branchname>`
_Creates a new timeline for your repository. To go to that timeline you need to use `git checkout`._

#### Git checkout
`git checkout <branchname>`
_Changes to another branch (timeline) in the repository_

`git checkout -b <branchname>`
_Creates a new branch with branchname and changes to that branch (timeline)_

`git checkout -- <filename(s)>`
_Resets the all changes to the file(s) to the state of the last commit_

#### Remote
`git remote add <remote name> [url]`
_Adds a new remote with name 'remote name' and url 'url'_

_Remotes are used to backup data to a database. You can put (push) and get (pull / fetch) information from that database_

#### Git push
`git push`
_Pushes all local commits to the remote_

`git push --set-upstream origin <branchname>`
_Creates the upstream remote for the repository and pushes to it_

`git push -u origin <branchname>`

_`-u` is short for `--set-upstream`_

#### Pull and Fetch
**Fetch**

`git fetch [remote name] [branch name]`
_Get data from repo without merge_

**Pull**

`git pull [remote name] [branch name]`
_Get data from repo with merge_

#### Git diff
`git diff HEAD^`
_See the difference in the last commit_

`git diff <commit hash>`
_Difference in that commit_

`git diff --cached`
_difference of all files_

`git diff --staged`
_difference of all staged files_

#### Git log
`git log`
_See all the commit history_

---

### Config
Open in vim

`git config --global --edit`

Set alias from terminal

`git config --global alias.aliasnamehere "git command here remove git"`

_Ex: alias hello => git hello => git log --oneline_

`git config --global alias.hello "log --oneline"`


### Alias
---
#### linus
```
log --graph --oneline --color --decorate --abbrev-commit --all
```

#### fuck
```
!sh -c 'git rebase -i HEAD~ && git pull -f'
```

#### Branch aliases
**sprint**

`git sprint = git checkout sprint-xx`

**dev**

`git dev = git checkout feature-xx`

**m**

`git m = git checkout master`

## Terminal
---
**Show hidden files**
```
defaults write com.apple.finder AppleShowAllFiles -boolean YES && killall Finder
```

**Kill dock**
```
defaults write com.apple.dashboard mcx-disabled -boolean YES && killall Dock
```

**Access android emulator**
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
---
**Search and replace**
```
:s/x/y/g
```
_Search and replace in lineselection_

x: word that you want to replace
y: word that you want to replace it with
