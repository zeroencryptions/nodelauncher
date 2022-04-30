import os

def info():
    print("programmed by zentyndur")
    print("v1.3 - debugging and file tree change")
    print("downloaded from - https://github.com/zeroencryptions/thenodesystem")
    
def profLoader():
    profIn = input("NoΔΞ/prof/")
    if profIn == "create":  
        profName = input("enter desired username")
        passW = input("enter password")
        conPass = input("re-enter password")
        if conPass == passW:
            print("user created")
            with open("localDat/prof1/usrdat.txt", "w") as file:
                file.write(profName +'\n')
                file.write(conPass)
        else:
            print ("creation error")
    if profIn == "login":
        with open("localDat/prof1/usrdat.txt", "r") as file:
            filecontent = file.read().splitlines()
        usr = input("username")
        pas = input("password")
        if filecontent[0] == usr and filecontent[1] == pas:
            print(usr, "logged in")
            nLM()
        else:
            print("error finding user, please create a new profile")
            nLM()
        if profIn == "":
            profLoader()
            
def listF():
    with open("localDat/config/fList.txt", "r") as file:
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
    with open("localDat/config/fList.txt", "w") as file:
        file.write(aFileName +'\n')
        file.write("")
    nLM()
    
def brsF():
    import importlib 
    with open("localDat/config/fList.txt", "r") as file:
        filecontent = file.read().splitlines()
        bFileName = input("NoΔΞ/b/")
    for f in filecontent:
        if f == bFileName:
            try:
                print("--- NoΔΞ -",bFileName,"---")
                ext1 = importlib.import_module(bFileName)
                ext1.main() 
            except:
                print("file",bFileName,"not found, error loading")

def debug():
    debugI = input("NoΔΞ/debug/")
    if debugI == "vlocaldat":
        verifyLocDat()
    if debugI == "list":
        listF()
    else:
        debug()
        
def verifyLocDat():
    from os import listdir
    uDatF = [f for f in listdir("localDat/prof1")]
    print(uDatF)
    if uDatF == ['usrdat.txt']:
        print("no profile problems discovered")
    if uDatF == []:
        print("error, no local data was discovered - would you like to create a new profile?")
        datRecO = input("NoΔΞ/debug/recovery/")
        if datRecO == "y":
            profLoader()
        elif datRecO == "n":
            nLM()
    aDatF = [f for f in listdir("localDat/config")]
    print(aDatF)
    if aDatF == ['fList.txt']:
        print("no file loading problems discovered")
    if uDatF == []:
        print("error, no file data was discovered - please re-install the Node Launcher")           

def kill():
    exit
            
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
    if mainIn == "debug":
        debug()
    if mainIn == "end":
        kill()

nLM()


