
#**************************************************************************************************************************************
#REQUIRES NIRCMD in path -- http://www.nirsoft.net/utils/nircmd.html
#Virtual Key Codes: https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396
# must install pyPushBullet (pip)
#**************************************************************************************************************************************

import json, time,webbrowser,os

from pushbullet import Pushbullet


MAX_LIST = 25 # pushes before deletion
DELAY = 10 # second refresh
KEY= 'QQKY8npXhlXtREilYK2QK7Ifb66Y6TIX'

def commandURL(url):
    webbrowser.open(url)
    
def command(parsedBody):
    if(parsedBody == "Mute"):
        os.system("nircmd.exe mutesysvolume 1")
        print("Muted")
    elif(parsedBody == "Unmute"):
        os.system("nircmd.exe mutesysvolume 0")
        print("Unmute")
    elif(parsedBody == "Vol Up"):
        os.system("nircmd.exe changesysvolume 8000")
        print("Volume Up!")
    elif(parsedBody == "Vol Down"):
        os.system("nircmd.exe changesysvolume -8000")
        print("Volume Down!")
    elif(parsedBody == "Last Track"):
        os.system("nircmd.exe sendkey 0xB1 press")
        print("Back!")
    elif(parsedBody == "Next Track"):
        os.system("nircmd.exe sendkey 0xB0 press")
        print("Next track!")
    elif(parsedBody == "Play" or parsedBody == "Pause"):
        os.system("nircmd.exe sendkey 0xB3 press")
        print("Play/Pause!")
    elif(parsedBody == "Shutdown"):
        print("Power!")
    elif(parsedBody== "Open Pandora"):
        print("Opening Pandora")
        os.system("start chrome pandora.com")
    elif(parsedBody == "Open Spotify"):
        print("Opening Spotify")
        os.startfile(r'C:\Users\adam\AppData\Roaming\Spotify\Spotify.exe')
    elif(parsedBody == "Open Netflix"):
        print("Opening Netflix")
        os.system('start chrome netflix.com')
    elif(parsedBody == "Shutdown"):
        print("Shutting Down...")
        os.system("shutdown /s /t 0")
    elif(parsedBody.find("Speak")!=-1):
        print("I'll Tell You!")
        os.system('nircmd.exe speak text "'+parsedBody[5:])
    elif(parsedBody == "Screen Off"):
        print("Turning Screen Off")
        os.system('nircmd.exe monitor off')
    elif(parsedBody =="Screen On"):
        print("Turning Screen On")
        os.system('nircmd.exe monitor on')
    elif(parsedBody =="Open tray"):
        print("Opening cd tray")
        os.system('nircmd.exe cdrom open')
pb = Pushbullet(KEY)

pb.delete_pushes()#start with fresh server, no existing commands
pb.refresh()

oldCreated= ""
pushType= ""

while(True):
    
    pushes = pb.get_pushes()

    if(len(pushes)>0):  
        latest= str(pushes[0])
        latestSep= latest.split(",")
        
        print(pushes[0])
        print('\n')

        for x in range(0, len(latestSep)-1):
            if(latestSep[x].find("'url'")!=-1):
                link= latestSep[x]
                parsedLink= link[(link.find(':')+3):len(link)-1]
                print(parsedLink)
                pushType="link"
                
            if(latestSep[x].find("'body'")!=-1):
                body= latestSep[x]
                parsedBody=body[(body.find(':')+3):len(body)-1]
                print(parsedBody)
                pushType= "text"
                
            if(latestSep[x].find("'created'")!=-1):
                created= latestSep[x]
                parsedCreated= created[(created.find(':')+3):len(created)-1]
                print(parsedCreated)
                
        if(oldCreated != parsedCreated):
            if(pushType == "link"):
                commandURL(parsedLink)
            if(pushType== "text"):
                command(parsedBody)
                
            oldCreated= parsedCreated #command has been accessed

        if(len(pushes)>=MAX_LIST):
            pb.delete_pushes()
            pb.refresh()

        time.sleep(DELAY)
        


