import time #starts the program and import modules 
import os

loginState = "" #storing variables before loaded later
bInt = ""
yourName = ""


def tools(): #games cato
    tCh = input("node/b/tools:")
    if tCh == ("list"):
        print("calculator", "-calc")
    if tCh == ("calc"):
        calc()
    if tCh == ("ste"):
        sTextEdit()

def sTextEdit():
    with open("secretText.txt", "r") as file:
        filecontent = file.read().splitlines()
        print(filecontent[0])
        print(filecontent[1])
        oL1 = input("node/b/t/ste/line1") #overide line 1
        oL2 = input("node/b/t/ste/line2") #overide ine 2
        with open("secretText.txt", "w") as file:
            file.write(oL1+'\n')
            file.write(oL2)
    print("file overide complete")

def calc():
    userOperation = input("what operation would you like?")
    userNo1 = int(input("what is your first number?"))
    userNo2 = int(input("and your second?"))
    if userOperation == "+":
        answer = userNo1 + userNo2
        print ("answer is", answer)
    elif userOperation == "-":
        answer = userNo1 - userNo2
        print ("answer is", answer)
    elif userOperation == "*":
        answer = userNo1 * userNo2
        print ("answer is", answer)
    elif userOperation == "/":
        answer = userNo1 / userNo2
        print("answer is", answer)
    else:
        print("syntax error.")
#end of tools
        
def account(): #account cato for browsing
    print(login)
    print(signup)
    accIn = input("node/b/acc:")
    if accIn == "login":
        login()
    if accIn == "signup":
        signup()

#acc things
def login():
     with open("info.txt", "r") as file:
         filecontent = file.read().splitlines()
     usr = input("username")
     pas = input("password")
     if filecontent[0] == usr and filecontent[1] == pas:
         print(usr, "logged in")
         main()
     else:
         print("error finding user")
         browse()


def signup():
    time.sleep(1)
    yourName = input("enter desired username")
    password = input("enter password")
    conPass = input("re-enter password")
    if conPass == password:
        print("user created")
        with open("info.txt", "w") as file:
            file.write(yourName +'\n')
            file.write(password)
    else:
        print ("creation error")
    browse()    
    time.sleep(2) #end of acc things


def browse(): #browsing the code
    bInt = input("node/b/")
    if bInt == "acc":
        account()
    elif bInt == "tools":
        tools()
    elif bInt == "tools":
        tools()
    elif bInt == "m":
        main()
    else:
        browse()

def info(): #provides info on the node
    print("-------------------------------------------------------")
    print("nodesys.py - programmed by Zencrypto")
    print("github.com/zeroencryptions/thenodesystem")
    print("version 1.0 - 2022")
    print("like python, this program is completely open source")
    print("-------------------------------------------------------")
    time.sleep(2)
    main()

def main(): #main selection menu
    mInt = input("node/")
    if mInt == "brws":
        browse()
    if mInt == "b":
        browse()
    if mInt == "browse":
        browse()
    if mInt == "info":
        info()
    if mInt == "shortcuts": #provides the user with a list of shortcuts for system functions
        print("(node/b/tools")
        print(" node/browse") #intentional formatting
        print(" node/info)")
        print("these cannot be entered fully, only in part though navigation")
        main()
    if mInt == "exit":
        exit()
    
#system start, all defs before are stored in memory 
print("NoΔΞ - Non-linear Operation based Data Explorer")
print("github.com/zeroencryptions/thenodesystem")
print("System built by zencrypto")
main()







   
