Git tutorial
====
This repo handles mainly Git but it also contains some good2know commands and the use of the terminal. Feel free to check it out and leave comments if you want to change something.

Content:
----
* [Git](#git)
* [Alias](#terminal)
* [Terminal](#terminal)
* [Vim](#vim)


### Git
Stages:
1. Commited: </br>
_Saved in the git repository database_

2. Staged: </br>
_Not saved in the database, waiting to be commited_

3. Unstaged: </br>
_New files or files that have been edited but not staged_


Starting: </br>
To start with Git you must first start a repository. This is done with the `git init` command in the folder you want to create a repository in.
</br> _Note: some things might look different because I use a theme in my terminal but the content should be the same._

```
➜ ~ mkdir testfolder

➜ ~ cd testfolder

➜ testfolder git init
Initialized empty Git repository in /Users/lindberg/testfolder/.git/

➜ testfolder git:(master)

```

Now you have a git repository to work with. To check that everything works correctly you could use the `git status` command.

```
➜ testfolder git:(master) git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)

➜ testfolder git:(master)
```

As you can see there are no commits yet. This means that there are no saved points in the repository. To create a commit (saved point) there must be something to commit, a change. I start by adding a file to my empty repository.

```
testfolder git:(master) touch newfile.txt

➜ testfolder git:(master?) git status
On branch master

No commits yet

Untracked files:
 (use "git add <file>..." to include in what will be committed)

 newfile.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Now I have something to commit, first we must select what we want to commit and we do that with the `git add` command.

```
➜ testfolder git:(master?) git add newfile.txt

➜ testfolder git:(master+) git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   newfile.txt


➜ testfolder git:(master+)
```
Now you have _staged_ a file, this means it is ready to commit. To unstage (to unselect the file) you can use the command above `git rm --cached <filename>`

We want to commit so we use the `git commit` command.

This will open your terminal editor most likely _vim_ or _nano_ which are two terminal editors. This is what it looks like in Vim.

```
1
2 # Please enter the commit message for your changes. Lines starting
3 # with '#' will be ignored, and an empty message aborts the commit.
4 #
5 # On branch master
6 #
7 # Initial commit
8 #
9 # Changes to be committed:
10 #       new file:   newfile.txt
11 #
```

To start editing type `i` and to stop editing type `esc`. To quit vim type `:wq` to write and quit or just quit `:!q`. We will go over vim later but these are the navigation commands most people know and use.

Now you have commited (created a save point).

```
➜ testfolder git:(master+) git commit
[master (root-commit) c8b452a] Test commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 newfile.txt
```

To check previous commits you can check the log with the `git log` command.

```
commit c8b452acee6e408a0adc80356e7ac0fe3983230e (HEAD -> master)
Author: Adrian Lindberg <adrlin@student.chalmers.se>
Date:   Thu Jan 18 09:33:29 2018 +0100

    Test commit
(END)
```

To exit `git log` type `q`.

These are the most basic commands that you will use in your life. Here is a summary of the commands:

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

#### Git log
`git log`
_See all the commit history_


When you become more experienced you might want to start to look at the `git branch` command and the `git checkout` command. These two create a powerful tool that helps you organise commits and to go back if something went wrong.

Here is the summary of the two commands:

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

Why would I want to use this? You want to use this because when for example multiple people are working on the same files at the same time. These two commands helps you merge the combined changes that all people create.

Start by creating a new branch by `git branch <nameofbranch>`.

```
➜ testfolder git:(master) git branch name

➜ testfolder git:(master) git branch
* master
  name
```

The first command `git branch <nameofbranch> (the branch I created is called name)` creates a new branch (timeline) and the second command lists all current branches (timelines). The current branch `master` is shown by a `*`.

To go to the other branch you use the `git checkout <branchname>` command.

```
➜ testfolder git:(master) git checkout name
Switched to branch 'name'

➜ testfolder git:(name)
```

You are now on your branch. As you can see on the last line it is shown that I am currently on the branch called name in `git:(name)`.


#### Git reset
`git reset HEAD <file(s)>`
_Undo files from staged state_


_Different from checkout because it keeps the changes but need to be added again_

#### Remove Commit
`git rebase -i HEAD~`
_Remove last commit from local head_


`git reset HEAD~`
_Remove last commit but keep changes_




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
