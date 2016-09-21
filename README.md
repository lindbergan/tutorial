#Git & Terminal commands

* [Git](#git)
    * [Forward Tips](#forward-tips)
    * [What happened](#what-happened-since-last-night)
    * [Remove Commit](#remove-commit)
    * [Diff](#diff)
    * [Change Commit](#change-commit)
    * [Log](#git-log)
    * [Remote](#remote)
    * [Fetch](#fetch)
    * [Tag](#tag)
    * [Config](#config)
        
* [Alias](#terminal)
    * [Linus](#linus)
    * [M](#m)
    * [Fuck](#fuck)
    
* [Terminal](#terminal)
    * [Show hidden files](#show-hidden-files)
    * [Kill dock](#kill-dock)
    * [Access android emulator](#access-android-emulator)

* [Vim](#vim)
	* [Search and replace](#search-and-replace)


## Git
#### Forward tips
```
git branch namn —no-ff
```

#### What happened since last night
```
git whatchanged
```

#### Remove Commit
##### Remove last commit from local head
```
git rebase -i HEAD~
```

##### Remove last commit from Github
```
git rebase -i HEAD~ && push -f
```

##### Add change to last commit (local)
```
git commit —ammend —no-edit
```

#### Diff
##### Diff on all files
```
git diff --cached
```

##### Diff on staged files
```
git diff --staged
```

#### Change Commit
```
git commit --amend -m 'newmessagehere'
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
