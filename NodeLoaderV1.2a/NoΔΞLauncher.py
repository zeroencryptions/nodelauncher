import os

def info():
    print("The NoΔΞ Laucher is a system coded in python for easy editing,")
    print("creation and loading of scripts designed for ease of access")
    print("version 1.2a - programmed by zencrypto")
    print("https://github.com/zeroencryptions/thenodesystem")
    
def profLoader():
    profIn = input("NoΔΞ/prof/")
    if profIn == "create":  
        profName = input("enter desired username")
        passW = input("enter password")
        conPass = input("re-enter password")
        if conPass == passW:
            print("user created")
            with open("profiles/localProf1.txt", "w") as file:
                file.write(profName +'\n')
                file.write(conPass)
        else:
            print ("creation error")
    if profIn == "login":
        with open("profiles/localProf1.txt", "r") as file:
            filecontent = file.read().splitlines()
        usr = input("username")
        pas = input("password")
        if filecontent[0] == usr and filecontent[1] == pas:
            print(usr, "logged in")
            nLM()
        else:
            print("error finding user")
            nLM()
        if profIn == "":
            profLoader()
            
def listF():
    with open("config/fList.txt", "r") as file:
        filecontent = file.read().splitlines()
        print(filecontent)
        nLM()
            
def commands():
    print("a - add a script to load")
    print("b - browse a script to load")
    print("api - open the application interface for creating scripts")
    print("h - shows the list of avalible commands")
    print("i - provides info")
    print("l - shows files added to load")
    
def api():
    apiO = input("NoΔΞ/api/")
    if apiO == "open":
        os.startfile(r'APIexample.py')
        print("remember, all scripts need to be listed using the ""a"" command")
    if apiO =="help":
        print("keep the main() function and don't run it anywhere else in the template file")
        print("add whatever you like, but name the file accordingly and add a description using the guidelines")
    if apiO == "":
        api()

def addF():
    aFileName = input("enter file name:")
    with open("config/fList.txt", "w") as file:
        file.write(aFileName +'\n')
        file.write("")
    nLM()
    
def brsF():
    import importlib 
    with open("config/fList.txt", "r") as file:
        filecontent = file.read().splitlines()
        bFileName = input("NoΔΞ/b/")
    for f in filecontent:
        if f == bFileName:
            try:
                print("-----------------------------------")
                ext1 = importlib.import_module(bFileName)
                print(f,"sucessfully loaded")
                ext1.main() 
            except:
                print("file",bFileName,"not found, error loading")
        else:
            print("file load error - doesn't exist")

def nLM():
    mainIn = input("NoΔΞ/")
    if mainIn == "a":
        addF()
    if mainIn == "b":
        brsF()
    if mainIn == "api":
        api()
    if mainIn == "h":
        commands()
    if mainIn == "prof":
        profLoader()
    if mainIn == "i":
        info()
    if mainIn == "":
        nLM()
    if mainIn == "l":
        listF()

nLM()
