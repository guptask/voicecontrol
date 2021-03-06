#!/usr/bin/python

# Ubuntu/Debian script

import pyaudio,os
import speech_recognition as sr
import subprocess

def announce(message):
    espeak_cmd = 'espeak -v mb-us1 -s 170 "' + message + '"'
    subprocess.call(espeak_cmd, shell=True)

def betty(command):
    betty_cmd = '~/.betty/main.rb ' + command
    output = subprocess.check_output(betty_cmd, shell=True)
    return output

def search(cmd):
    announce('Searching')
    betty('turn web on')
    output = betty(cmd)
    zenity_cmd = 'zenity --info --text="' + output + '"'
    execute(zenity_cmd)
    betty('turn web off')

def execute(command):
    os.system(command)

def validCommand(source):
    audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio).lower()
        print(cmd)
        if   cmd == "open chrome"    : execute('google-chrome&')
        elif cmd == "open downloads" : execute('nautilus $HOME/Downloads/ &')
        elif cmd == "local search"   : execute('gnome-do&')
        elif cmd == "lock screen"    : execute('xdotool key super+l')
        else :
            if cmd.startswith("search ") : search(cmd[7:])
            else                         : return False

    except sr.UnknownValueError : return False
    except sr.RequestError      : return False

    announce('Goodbye for now')
    return True

def activate(source):
    audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio).lower()
        if cmd == "activate" : 
            announce('Hello. Listening')
            while validCommand(source) == False : pass

    except sr.UnknownValueError : return
    except sr.RequestError      : return


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        while 1:
            activate(source)
