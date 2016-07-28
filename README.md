#Git & Terminal commands

* [Git](#Git)
* [Terminal](#Terminal)

##Git
Forward tips
git branch namn —no-ff

What happened since last night
git whatchanged

Remove last commit from github
git push -f origin HEAD^:friendDAO

Remove last commit from local head
git rebase -i HEAD^

Add change to last commit
git commit —ammend —no-edit

// Bas status
git status

// Diff p� unstaged filer
git diff 

// Diff p� alla filer
git diff --cached

// Diff p� staged filer
git diff --staged

// Basic commit
git commit -m "Commit message"

// Commit with editor
git commit

// Commit with editor and diff included
git commit -v

// Commit without needing to add files
git commit -a -m "Commit message"

// "Add" en fil till staged (Skall g�ras p� b�da tillagda och �ndrade filer)
git add [filnamn]

// "Add" en borttagen fil till staged
git rm [filnamn]

// �ndra en commit
git commit --amend

// Ta ut en fil fr�n staged
git reset HEAD [filnamn]

// Dra tillbaka �ndringar gjorda till en fil
git checkout -- [filnamn]

// Visa tidigar commits
git log

// Visa tidigare commits och diff
git log -p

// Visa X tidigare commits
git log -[antal commits]

// Visa statestik f�r commits
git log --stat

// Formatera commits [oneline|short|full|fuller|format]
git log --pretty=oneline

// Formatera commits sj�lv med "format"
git log --pretty=format:"%h - %an, %ar : %s"

// format parametrar
%H  Commit hash
%h  Abbreviated commit hash
%T  Tree hash
%t  Abbreviated tree hash
%P  Parent hashes
%p  Abbreviated parent hashes
%an Author name
%ae Author e-mail
%ad Author date (format respects the �date= option)
%ar Author date, relative
%cn Committer name
%ce Committer email
%cd Committer date
%cr Committer date, relative
%s  Subject

// L�gg till ASCII graph till comitts listan
git log --graph

// log parametrar
Option  Description
-p  Show the patch introduced with each commit.
--stat  Show statistics for files modified in each commit.
--shortstat Display only the changed/insertions/deletions line from the --stat command.
--name-only Show the list of files modified after the commit information.
--name-status   Show the list of files affected with added/modified/deleted information as well.
--abbrev-commit Show only the first few characters of the SHA-1 checksum instead of all 40.
--relative-date Display the date in a relative format (for example, �2 weeks ago�) instead of using the full date format.
--graph Display an ASCII graph of the branch and merge history beside the log output.
--pretty    Show commits in an alternate format. Options include oneline, short, full, fuller, and format (where you specify your own format).

// Begr�nsa antal commits
-(n)    Show only the last n commits
--since, --after    Limit the commits to those made after the specified date.
--until, --before   Limit the commits to those made before the specified date.
--author    Only show commits in which the author entry matches the specified string.
--committer Only show commits in which the committer entry matches the specified string.

--grep
--all-match Matchar all parametrar(defult s� g�r den p� om n�gon parameter matchar)

// Avancerad s�k med avslutande path
$ git log --pretty="%h - %s" --author=gitster --since="2008-10-01" \ --before="2008-11-01" --no-merges -- t/
5610e3b - Fix testcase failure when extended attribute
acd3b9e - Enhance hold_lock_file_for_{update,append}()
f563754 - demonstrate breakage of detached checkout wi
d1a43f2 - reset --hard/read-tree --reset -u: remove un
51a94af - Fix "checkout --track -b newbranch" on detac
b0ad11e - pull: allow "git pull origin $something:$cur

// Push ett skapat lokalt git repo till ett remote repo address ex: git@github.com:kallewallin/gitproject.git
git remote add origin [address]
git push -u origin master

// Lista remote repository
git remote

// Lista remote repository och address
git remote -v

// H�mta data fr�n repo utan merge
git fetch [remote name] [branch name] 

// H�mta data fr�n repo med merge
git pull [remote name] [branch name] 

// H�mta info om remote
git remote show [remote name] 

// Visa repo taggar
git tag

// S�k p� repo taggar
git tag -l 'v1.4.2.*'

Cherry pick test i 1.0

##Terminal
Show hidden files
defaults write com.apple.finder AppleShowAllFiles -boolean YES && killall Finder

Kill dock
defaults write com.apple.dashboard mcx-disabled -boolean YES && killall Dock

Access android emulator (Ex: Flickpicker project)
adb -s emulator-5554 shell
cd data/data/com.typeof.flickpicker/database
sqlite3 flickpicker.db
