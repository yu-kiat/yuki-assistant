#comments
#idk why but i do '' instead of "" when doing os.system()
#i refresh the screen instead of doing a while loop because im lazy and why not? :)

#importing libraries
import os
import time
from datetime import datetime #idk why but this is broken when you just put "import datetime"

#global varriables


#loading screen
def loadingscreen():
    loadingwait = 0
    print("=======================")
    print("  Welcome to yuki AI!  ")
    print("=======================")
    time.sleep(1)
    print("Loading, please wait...")
    print("=======================")
    time.sleep(2)
    for count in range(6):
        print(str(loadingwait) + "%...")
        loadingwait += 20
        time.sleep(1)
    print("All done!")
    time.sleep(2)


#main menu
def mainmenu():
    menuuserchoice = 0
    print("Select an option:")
    time.sleep(1)
    print("1. Basic Tasks.")
    time.sleep(1)
    print("2. Advanced Things.")
    time.sleep(1)
    print("3. Credits and More Stuff!")
    time.sleep(1)
    print("4. Exit.")
    time.sleep(1)
    menuuserchoice = int(input("> "))
    if menuuserchoice == 1:
        os.system('clear')
        basictasks()
    elif menuuserchoice == 2:
        os.system('clear')
        advanced()
    elif menuuserchoice == 3:
        os.system('clear')
        credit()
    elif menuuserchoice == 4:
        os.system('clear')
        endprogram()
    else:
        print("That's not a valid choice!")
        time.sleep(1)
        print("Now you're going to be stuck on this screen.")


#basic tasks
def basictasks():
    basechoice = 0
    print("================================")
    print(" Basic Tasks: Choose an option: ")
    print("================================")
    time.sleep(1)
    print("      1. Your local time.       ")
    print("================================")
    time.sleep(1)
    print("         2. Unix time.          ")
    print("================================")
    time.sleep(1)
    print("        3. System stats.        ")
    print("================================")
    time.sleep(1)
    print("4. Return back to the main menu.")
    print("================================")
    time.sleep(1)
    basicchoice = int(input("> "))
    if basicchoice == 1:
        os.system('clear')
        localtime()
    elif basicchoice == 2:
        os.system('clear')
        unixtime()
    elif basechoice == 3:
        os.system('clear')
        sysstats()
    elif basechoice == 4:
        os.system('clear')
        mainmenu()
    else:
        print("That's not a valid option!")
        time.sleep(1)
        print("Now you're going to be stuck on this screen.")

def localtime():
    current_dateTime = "test"
    localtimechoice = "placeholder"
    print("Your local time is:")
    current_dateTime = str(datetime.now())
    time.sleep(1)
    print(current_dateTime)
    time.sleep(2)
    print("Do you want to return to that basic tasks menu? (Y/N)")
    localtimechoice = input("> ")
    if localtimechoice == "Y":
        os.system('clear')
        basictasks()
    elif localtimechoice == "N":
        print("Okay then, refreshing screen....")
        time.sleep(1)
        os.system('clear')
        localtime()
    else:
        print("That's not a valid option!")
        time.sleep(1)
        print("Now you're going to be stuck on this screen.")

def unixtime():
    unix_dateTime = "test"
    unixtimechoice = "placeholder"
    print("The current Unix time is:")
    unix_dateTime = int(time.time())
    time.sleep(1)
    print(unix_dateTime)
    time.sleep(2)
    print("Do you want to return to that basic tasks menu? (Y/N)")
    unixtimechoice = input("> ")
    if unixtimechoice == "Y":
        os.system('clear')
        basictasks()
    elif unixtimechoice == "N":
        print("Okay then, refreshing screen....")
        time.sleep(1)
        os.system('clear')
        unixtime()
    else:
        print("That's not a valid option!")
        time.sleep(1)
        print("Now you're going to be stuck on this screen.")


#advanced things
def advanced():
    print("placeholder for choice 2")


#credits
def credit():
    menu3userchoice = "placeholder"
    time.sleep(1)
    print("yuki assistant v0.1")
    time.sleep(1)
    print("Made by yuki! >u<")
    time.sleep(1)
    print("Licensed under the GNU GPL V3.")
    time.sleep(1)
    print("This program was made with VS Codium, a FOSS version of VS Code.")
    time.sleep(5)
    menu3userchoice = (input("Do you want to go back the the main menu? (Y/N) "))
    if menu3userchoice == "Y":
        os.system('clear')
        mainmenu()
    elif menu3userchoice == "N":
        print("Okay, refreshing screen...")
        time.sleep(1)
        credit()
    else:
        print("That's not a valid option!")
        print("Now you're going to be stuck on this screen forever!!! >:)")


#exiting
def endprogram():
    print("Exiting....")
    time.sleep(2)
    exit()


#main code
def main():
    loadingscreen()
    os.system('clear')
    mainmenu()

main() #delete this if you don't want to run the code