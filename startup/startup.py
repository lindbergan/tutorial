import sys
import subprocess

slack_url = "//Applications/Slack.app/Contents/MacOS/Slack"
iterm_url = "//Applications/iTerm.app/Contents/MacOS/iTerm2"
intellij_url = "//Applications/IntelliJ\ IDEA.app/Contents/MacOS/idea"
spotify_url = "//Applications/Spotify.app/Contents/MacOS/Spotify"
chrome_url = "//Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"


def startProgram(url):
    subprocess.Popen(["open -a " + url], shell=True)


def closeProgram():
    sys.exit(0)


def devMode():
    print "Starting Dev mode!"
    startSlack()
    startTerminal()
    startIntelliJ()
    startSpotify()
    startChrome()


def avanzaMode():
    print "Starting Avanza mode!"
    startSpotify()
    startChrome()


def sharespineMode():
    print "Starting Sharespine mode!"
    startSlack()
    startChrome()
    startSpotify()


def startChrome():
    print "Starting Google Chrome"
    if not debug:
        startProgram(chrome_url)


def startSlack():
    print "Starting Slack"
    if not debug:
        startProgram(slack_url)


def startSpotify():
    print "Starting Spotify"
    if not debug:
        startProgram(spotify_url)


def startTerminal():
    print "Starting Terminal"
    if not debug:
        startProgram(iterm_url)


def startIntelliJ():
    print "Starting IntelliJ Idea"
    if not debug:
        startProgram(intellij_url)


print "Hello, what mode do you want do do today?"
print "- Dev (Slack, Terminal, IntelliJ, Spotify, Google Chrome): D/Dev"
print "- Avanza (Avanza (Google Chrome), Spotify): A/Avanza"
print "- Sharespine (Slack, Google Chrome, Spotify): S/Sharespine"
print "- Everything else will return in doing nothing"

debug = False
if debug:
    print "###################### Starting in debug mode ######################"

option = raw_input("Please select an option: ").lower()


if option == "d" or option == "dev":
    devMode()

elif option == "a" or "option" == "avanza":
    avanzaMode()

elif option == "s" or "option" == "sharespine":
    sharespineMode()

else:
    print "Closing."

if debug:
    closeProgram()
