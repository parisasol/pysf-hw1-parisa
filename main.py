from colorama import Fore, Back, Style

def roof():
    for n in range(10):
        print (Back.BLUE + "*"*(40 - n) + Back.RED + " " * n*2 + Back.BLUE + "*"* (40 - n) + Style.RESET_ALL)

def body():
    for n in range(2):
        print (Back.BLUE + "*"*31  + Back.BLACK + " " * 18 + Back.BLUE + "*"* 31  + Style.RESET_ALL )

def window():
    for n in range(2):
        print (Back.BLUE + "*"*31  + Back.BLACK + " " * 8 + Back.YELLOW + " " * 6 + Back.BLACK + " " * 4 + Back.BLUE + "*"* 31  + Style.RESET_ALL )

def door():
    for n in range(4):
        print (Back.BLUE + "*"*31  + Back.BLACK + " " * 7 + Back.LIGHTBLACK_EX + " " * 4 + Back.BLACK + " " * 7 + Back.BLUE + "*"* 31  + Style.RESET_ALL)

def grass():
    for n in range(2):
        print (Back.GREEN + " "*80  + Style.RESET_ALL)


roof()
body()
window()
body()
door()
grass()
