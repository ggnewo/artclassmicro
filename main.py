import pyautogui
import time
import random

screenWidth, screenHeight = pyautogui.size()
startingvar = 5
smyorn = False
nowyoucan = False
numbermade = 0
loopmode = False
proxymode = ""
#Gets a random number
def getrandomnumber():
    global number
    number = random.randint(0,1000000)
#Adds them all together to get the website name
def getname():
    global finnumber
    getrandomnumber()
    n1 = number
    getrandomnumber()
    n2 = number
    getrandomnumber()
    n3 = number
    getrandomnumber()
    n4 = number
    getrandomnumber()
    n5 = number
    finnumber = n1 + n2 + n3 + n4 + n5
getname()
#Dont want the number to be too low so that we don't run into the issue with a website with the same name :)
if finnumber > 1000:
    getname()
print(finnumber)

#The micro :0, start from google/opera gx/tor/whatever
def micro():
    print("Micro Starting!")
    print(str(numbermade) + " proxies generated this session")
    #Generates a new name for the website
    getrandomnumber()
    getname()
    #Resets the countdown value
    startingvar = 5
    #Makes a new window that goes to vercel
    pyautogui.hotkey('ctrl', 'n')
    pyautogui.write('https://vercel.com/new/clone?repository-url=https://github.com/art-class/v4', interval=0.02)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(809,590)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1300,620)
    pyautogui.click()
    #The random-generated website name, which is just random numbers bc that's easy and my producer tag
    pyautogui.write(str(finnumber), interval=0.1) 
    pyautogui.write('.ggnewo', interval= 0.1)
    pyautogui.moveTo(1487,671)
    pyautogui.click()
    if loopmode == True:
        print("Link made!")
    if loopmode == False:
        print("The link is now made!")
        print("Deployment can take anywhere from 30 seconds to a couple minutes, so be patient!")
        print("Type s to run it back, or h to go back home.")
        print("You can also type x to terminate the program :nerd:")
        itdoneyipee = input("")
        if itdoneyipee == "s":
            pyautogui.hotkey('ctrl','w')
            micro()
        elif itdoneyipee == "h":
            pyautogui.hotkey('ctrl','w')
            home()
        elif itdoneyipee == "x":
            pyautogui.hotkey('ctrl','w')
            exit(1)
def starting_thing():
    global startingvar
    for i in range(5):
        print(startingvar)
        startingvar = startingvar - 1
        time.sleep(1)
def home():
    print("Welcome to the Art Class Micro!")
    print("If you need help using the program, enter h\nYou can also enable experemental features, but they might not work as I haven't heavily tested them")
    print("Press s to get started!")
    print(" ")
    start = input("")
    if start == "s":
        proxymode = "github.com/art-class/v4"
        starting_thing()
        micro()
    elif start == "h":
        print("This micro is designed to automate making proxies, but there are a couple requirements")
        print("First, you need to make sure that you have all the packages listed in the readme installed, not sure how you got here without them")
        print("Also, this is deisigned for 1920x1080 screens, but I'll probably make other versions supporting other screensizes if people use this")
        print("Also, not sure if browser matters, but the ctrl+n and ctrl+w commands need to open and close tabs for this to work")
        print("If you have any problems, DM me on discord at: ggnewo")
        print("Made with ♡ by ggnewo")
        backtohome = input("Type h to go back to the home: ")
        if backtohome == "h" or "H":
            home()
    elif start == "e":
        print("Now in experimental mode!")
        print("Keep in mind these features might not work.")
        print("Again, if there's any issues, dm me on discord my username is ggnewo :)")
        print("Current experemental features:\n1:Infinite Loop mode\n2:Controlled loop mode")
        ec = input("Chose the mode you want: ")
        if ec == "1":
            loopmode = True
            while True:
                starting_thing()
                micro()
                numbermade = numbermade + 1
        elif ec == "2":
            loopmode = True
            print("How many proxies do you want to make?")
            proxienum = input()
            print("Ok, making " + proxienum + " proxies")
            numba = int(proxienum)
            starting_thing()
            for i in range(numba):
                micro()
                numbermade = numbermade + 1
        else:
            print("Buddy")
            time.sleep(1)
            home()
    else:
        print("You messed up lmao")
        time.sleep(1)
        home()
home()
