#########################################
# SkbBomber
# A Bangladeshi SMS Bomber Tool
# Author: ToxicNoob Inc.
# GitHub: https://github.com/Toxic-Noob
# Version: 4.0.0
#########################################

import time
import requests
import sys
import os
import shutil
import json

#Get Rows and Columns of Screen
columns = shutil.get_terminal_size().columns

def psb(z, end="\n"):
    for e in z + end:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

# Check Python Version, as Python < 3.11 Does not support 3.11 encryption
def checkPy():
    major = sys.version_info.major
    minor = sys.version_info.minor
    if (major != 3) or (minor < 11):
        print(f"\n[\033[92m*\033[37m] Your Python Version ({major}.{minor}) is not Supported!")
        print("[\033[92m*\033[37m] Update Your Python Using the Command Below:\n\n    pkg reinstall python\n")
        sys.exit()


# Show New Message from Author
def showAuthorMsg(msg):
    print()
    print("\033[94m-"*columns, end="")
    print("\033[92mMessage From Author".center(columns+4))
    print("\033[95m-"*columns, end="")
    psb("\n\033[37m    " + msg + "\n")
    print("\033[94m-"*columns, end="", flush=1)
    print()
    open("./more/.msg", "w").write(msg)
    time.sleep(2)
    input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
    logo()


#Check Update
def update():
    try:
        toolVersion = json.loads(open("./more/.version", "r").read())["version"]
    except:
        toolVersion = "ToxicNoob"
    
    try:
        authorMsg = open("./more/.msg", "r").read().replace("\n", "")
    except:
        authorMsg = "None"
    
    try:
        parsedData = requests.get("https://raw.githubusercontent.com/Toxic-Noob/ToxicBomber/main/more/.version").json()
    except:
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Connect To The Internet!")
        time.sleep(1)
        l = input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
        update()
    
    mainVersion = parsedData["version"]
    newMsg = parsedData["message"]
    
    #If Tool Version Is Same, Then Return/Close Function
    if (toolVersion != mainVersion):
        psb("\n    \033[92m[\033[37m!\033[92m] \033[37mTool Update Found!")
        time.sleep(0.5)
        psb("\033[92m[\033[37m!\033[92m] \033[37mUpdating Tool: ", end="")
        
        os.system("cd .. && rm -rf ToxicBomber && git clone https://github.com/Toxic-Noob/ToxicBomber > /dev/null 2>&1")
        
        print("\033[37mDone")
        psb("    \033[92m[\033[37m*\033[92m] \033[37mStarting Tool...")
        time.sleep(0.8)
        
        os.system("cd .. && cd ToxicBomber && python Tbomb.py")
    
    else:
        if (authorMsg != newMsg):
            showAuthorMsg(newMsg)


#Logo
def logo():
    os.system("clear")
     print("\033[94m                  
  / ____| |  | |     |__   __|                  
 | (___ | | _| |__      | | ___  __ _ _ __ ___  
  \___ \| |/ / '_ \     | |/ _ \/ _` | '_ ` _ \ 
  ____) |   <| |_) |    | |  __/ (_| | | | | | |
 |_____/|_|\_\_.__/     |_|\___|\__,_|_| |_| |_|
    print("\033[94m│                              \033[94m          │".center(columns+9))
    print("\033[94m│ \033[95mAuthor : Skb Bomber Inc.                \033[94m│".center(columns+15))
    print("│ \033[95mTool   : Unlimited SMS Bomber          \033[94m│".center(columns+9))
    print("│ \033[95mGitHub : Atalamin \033[94m│".center(columns+9))
    print("│ \033[95mCoder  : HunterSl4d3              \033[37mV4.0 \033[94m│".center(columns+15))
    print("\033[94m└────────────────────────────────────────┘".center(columns+5))


#Options Banner
def banner():
    amount = str(main.amount)
    if (len(amount) == 1):
        amount = amount + "                    "
    elif (len(amount) == 2):
        amount = amount + "                   "
    elif (len(amount) == 3):
        amount = amount + "                  "
    elif (len(amount) == 4):
        amount = amount + "                 "
    else:
        amount = amount + "                "
    
    print("\033[95m-" * (columns), end = "")
    print(("\033[92mTarget  : \033[37m0" + main.number + "          ").center(columns + 10))
    print(("\033[92mAmount  : \033[37m" + amount).center(columns + 10))
    print("\033[92mProcess : \033[37mStarted               ".center(columns + 10))
    print("\033[92mNote    : \033[37mPress ctrl + z To Stop".center(columns + 10))
    #print(" ", end="")
    print("\033[95m-" * (columns), end = "")
    print("\n")


#Check SMS Sent and Process
def check(sent):
    amount = main.amount
    delay = main.delay
    
    print("\r\033[92m    [\033[94m#\033[92m] Massage Sent : \033[94m[\033[37m" + str(sent) + "\033[94m]\033[37m", end="")
    
    if (sent == amount):
        psb("\n\n\033[92m    [\033[37m*\033[92m] Bombing Finished!")
        psb("\033[92m    [\033[37m*\033[92m] Amount : \033[37m" + str(amount))
        psb("\033[92m    [\033[37m*\033[92m] Target : \033[37m0" + main.number)
        psb("\033[92m    [\033[37m*\033[92m] From   : \033[37mToxicBomber\n")
        time.sleep(0.6)
        print("\033[92m[\033[93m★\033[92m] Thanks For Using Our Tool \033[92m[\033[93m★\033[92m]".center(columns + 30))
        print("\033[37m")
        
        return True
    else:
        time.sleep(delay)
        return False


#Get Target Number
def getNumber():
    number = input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Target Number:> \033[37m")
    if not number.isdigit():
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter a Correct Number!")
        number = getNumber()
    if not (len(number) == 11):
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter 11 Digit Number!")
        number = getNumber()
    
    return number


#Main    
def main():
    number = getNumber()
    number = number[-10:]
    main.number = number
    
    amount = input("    \033[92m[\033[37m*\033[92m] \033[37mEnter Amount (\033[37mDefault: 10\033[37m):> \033[37m")
    try:
        amount = int(amount)
    except:
        amount = 10
    
    main.amount = amount
    
    delay = input("    \033[92m[\033[37m*\033[92m] \033[37mEnter Time(\033[92mSec\033[37m) Delay (\033[92mDefault: 2s\033[37m):> \033[37m")
    try:
        int(delay)
    except:
        delay = 2
    
    main.delay = int(delay)
    
    time.sleep(1)
    logo()
    banner()
    sent = 0
    while True:
        success = api_1(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_2(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_3(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_4(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_5(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_6(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_7(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_8(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_9(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_10(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_11(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_12(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_13(number)
        if (success):
            sent += 1
            if(check(sent)):
                break
        
        success = api_14(number)
        if (success):
            sent += 1
            if(check(sent)):
                break


# Start Ruuning Tool
if (__name__ == "__main__"):
    checkPy()
    from more.data import *
    logo()
    update()
    main()
