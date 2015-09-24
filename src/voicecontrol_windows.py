#!/usr/bin/python

# Windows script

import pyaudio,os
import speech_recognition as sr

def chrome():
    os.system("start chrome.exe")

def mainfunction(source):
    audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio).lower()
        print(cmd)
        if cmd == "open chrome" : chrome()
        else : return

    except sr.UnknownValueError: return
    except sr.RequestError: print("Offline")

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while 1:
            mainfunction(source)
