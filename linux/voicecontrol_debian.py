#!/usr/bin/python

# Ubuntu/Debian script

import pyaudio,os
import speech_recognition as sr

# Use xdotool for mouse and keyboard control

def chrome():
    os.system("google-chrome&")

def downloads():
    os.system("nautilus $HOME/Downloads/ &")

def gnomedo():
    os.system("gnome-do")

def lockscreen():
    os.system("gnome-screensaver-command --lock")

def mainfunction(source):
    audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio).lower()
        print(cmd)
        if cmd == "open chrome" : chrome()
        elif cmd == "open downloads" : downloads()
        elif cmd == "open search" : gnomedo()
        elif cmd == "lock screen" : lockscreen()
        else : return

    except sr.UnknownValueError: return
    except sr.RequestError: print("Offline")

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while 1:
            mainfunction(source)
