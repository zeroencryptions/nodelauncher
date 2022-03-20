import os

def profLoader():
    profIn = input("do you have an profile?")
    if profIn == "n":
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
    if profIn == "y":
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
        
    
def commands():
    print("a - add a script to load")
    print("b - browse a script to load")
    print("api - open the application interface for creating scripts")
    print("help - shows the list of avalible commands or help")
    
def api():
    apiO = input("NoΔΞ/api/")
    if apiO == "open":
        os.startfile(r'APIexample.py')
        print("remember, all scripts need to be listed using the ""a"" command")
    elif apiO =="help":
        print("keep the main() function and don't run it anywhere else in the template file")
        print("add whatever you like, but name the file accordingly and add a description using the guidelines")       

def addF():
    aFileName = input("enter file name:")
    with open("config/fList.txt", "w") as file:
        file.write(aFileName +'\n')
    
def brsF():
    import importlib #imports the file a variable to be loaded later
    with open("config/fList.txt", "r") as file:
        filecontent = file.read().splitlines()
        bFileName = input("NoΔΞ/b/")
    for f in filecontent:
        if f == bFileName:
            try:
                print("-----------------------------------")
                ext1 = importlib.import_module(bFileName)
                print(f,"sucessfully loaded")
                ext1.main() #loading code from file as a function
            except:
                print("file",bFileName,"not found, error loading")
        else:
            print("file load error - doesn't exist")

def nLM():
    print("NoΔΞ Launcher - programmed by zencrypto")
    mainIn = input("NoΔΞ/")
    if mainIn == "a":
        addF()
    if mainIn == "b":
        brsF()
    if mainIn == "api":
      api()
    if mainIn == "help":
        commands()
    if mainIn == "profile":
        profLoader()
    
nLM()
