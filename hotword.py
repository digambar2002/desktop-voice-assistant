# Use pvporcupine to detect hotword

import struct
import time
import pyaudio
import pvporcupine
porcupine=None
paud=None
audio_stream=None


def hotword():

    try:
        access_key="paste your access key here" #to create access key signup to https://console.picovoice.ai/ 
        #new version of pvporcupine has a limitation--> you can use only in upto 3 devices in free version. 
        #you can install older version of pvporcupine --> pip install pvporcupine==1.9.5 , which does not require any access key
        #if you are using older version of pvporcupine, replace the below line with--> porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) #pvporcupine.KEYWORDS for all keywords
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            keyword_index=porcupine.process(keyword)
            if keyword_index>=0:
                print("hotword detected")
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

hotword()