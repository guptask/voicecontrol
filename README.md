# Voice Control

This package contains code for voice activated laptop functionality control. Some 
free+/open source packages have been used to build it, notably Google's sppech 
recognition toolkit and Betty (a natural language processor for Linux).

The goal of this Voice Control package is to create a laptop assistant like those 
present on modern smartphones.

I am still in the process of building it. So expect changes in the package over 
the coming weeks.


## Debian/Ubunutu (or any other Debian-based distribution)

#### Configure:

Python (2.7 or higher), pyaudio and SpeechRecognition are needed.
Additional packages needed are espeak, xdotool, betty, nautilus, gnome-do, etc.

Commands needed to download and configure the package:

    sudo apt-get install git
    git clone https://github.com/guptask/voicecontrol
    ./voicecontrol/linux/configure

I'm working on a voicecontrol service that can be installed, started and stopped.
The code is present inside the linux directory but I need to fix some bugs in it.

#### Use:

    voicecontrol

Type this command from any path on the terminal. You have to say 'activate' every 
time  in order to activate the control. Then you can say 'open chrome', 'open search', 
'lock screen', 'deactivate', etc.

#### Future:

I'm looking for a gesture control package that will allow me to replicate touchpad's 
functionalities using the laptop's webcam.


## Windows

I'm not developing this currently. If you are interested, please take a look 
at the windows directory inside the repository.

Softwares/packages needed: python, pyaudio and SpeechRecognition package.

You have to figure out the rest :)

