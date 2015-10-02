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
    os.system("xdotool key super+l")


def validCommand(source):
    audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio).lower()
        if cmd == "open chrome" : chrome()
        elif cmd == "open downloads" : downloads()
        elif cmd == "open search" : gnomedo()
        elif cmd == "lock screen" : lockscreen()
        elif cmd == "deactivate" :
            os.system('espeak -v mb-us1 -s 170 "goodbye"')
            return True
        else : return False

    except sr.UnknownValueError : return False
    except sr.RequestError : print("+"),; return False

    return True


def activate(source):
    audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio).lower()
        if cmd == "activate" : 
            os.system('espeak -v mb-us1 -s 170 "listening"')
            while validCommand(source) == False : pass

    except sr.UnknownValueError : return
    except sr.RequestError : print("!")


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        while 1:
            activate(source)
