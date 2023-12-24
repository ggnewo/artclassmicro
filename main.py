import pyautogui
import time
import random

screenWidth, screenHeight = pyautogui.size()
startingvar = 5
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
    #Makes a new window that goes to vercel
    pyautogui.hotkey('ctrl', 'n')
    pyautogui.write('vercel.com', interval=0.1)
    pyautogui.press('enter')
    time.sleep(0.5)
    #Copies the repo so we can paste it later
    pyautogui.hotkey('ctrl', 'n')    
    pyautogui.write('https://github.com/art-class/v4', interval=0.1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'w')
    #Navigating vercel
    time.sleep(0.3)
    pyautogui.moveTo(1531, 260)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(1531,310)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(484,881)
    pyautogui.click()
    time.sleep(1)
    #Pastes the repo link
    pyautogui.hotkey('ctrl','v')
    #More navigating
    pyautogui.moveTo(1201,742)
    pyautogui.click()
    pyautogui.sleep(1)
    pyautogui.moveTo(809,590)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1300,620)
    pyautogui.click()
    #The random-generated website name, which is just random numbers bc that's easy
    pyautogui.write(str(finnumber), interval=0.1) 
    pyautogui.moveTo(1487,671)
    pyautogui.click()
    print("The link is now made!")
    print("Deployment can take anywhere from 30 seconds to a couple minutes, so be patient!")
    print("Type s to run it back, or h to go back home.")
    print("You can also type x to terminate the program :nerd:")
    itdoneyipee = input("")
    if itdoneyipee == "s":
        micro()
    elif itdoneyipee == "h":
        home()
    elif itdoneyipee == "x":
        exit(1)
def starting_thing():
    global startingvar
    for i in range(5):
        print(startingvar)
        startingvar = startingvar - 1
        time.sleep(1)
def home():
    print("Welcome to the Art Class Micro!")
    print("If you need help using the program, enter h")
    print("Press s to get started!")
    print(" ")
    start = input("")
    if start == "s":
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
    else:
        print("You messed up lmao")
        time.sleep(1)
        home()
home()
