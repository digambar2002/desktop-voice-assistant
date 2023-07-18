# -------- main file to run jarvis


from enum import Flag
import os
from statistics import mode

# eel gui library
import eel

# to run subprocess

import subprocess

# Carry all commands
from engine.command import *

# Contains all features of assistant
from engine.features import *

# Use for face authentication
from authenticate.recoganize import AuthenticateFace

# Default configaration file
from engine.config import *

# init www directory contains GUI
eel.init('www')

# Function to start jarvis: used by run.py file
def start():

    # Play sound when assistant start
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

    @eel.expose
    def StartSound():
        music_dir = "www\\assets\\audio\\start_sound.mp3"
        playsound(music_dir)



    # Start Jarivs by GUI
    @eel.expose
    def Start():
        subprocess.call([r'static\\device.bat'])
        # os.system("static\\devices.bat")
        eel.AssistantName(ASSISTANT_NAME)

        # from engine.features import auth_protocol
        # auth_protocol()
        # flag = AuthenticateFace()
        flag =1 #skip face authenticate
        print(flag)
        if flag == 1:

            eel.hideFaceAuth()
            speak("Face authentication successfull")
            eel.hideFaceAuthSuccess()

            from engine.features import wish
            wish()
            eel.hideStart()
            eel.init()
        else:
            speak("authentication fail")

    # Use MS Edge default browser
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    
    # Run Index file in browser
    eel.start("index.html", mode=None,
              host='localhost',
              block=True)
