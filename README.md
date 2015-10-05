# Voice Control

This package contains code for voice activated laptop functionality control. Some 
free+/open source packages have been used to build it, notably Google's speech 
recognition toolkit and Betty (a natural language processor for Linux).

The goal of this Voice Control package is to create a laptop assistant like those 
present on modern smartphones.

I'm still in the process of building it. So expect changes in the package over 
the coming weeks.


## Debian/Ubunutu (or any other Debian-based distribution)

#### Configure:

Python (2.7 or higher), pyaudio and SpeechRecognition are needed. Some of the notable 
packages used in here are espeak, xdotool, betty, nautilus, gnome-do and zenity.

Commands needed to download and configure the package:

    sudo apt-get install git
    git clone https://github.com/guptask/voicecontrol
    ./voicecontrol/linux/configure

I  eventually plan to package it as a service that can be installed, started and 
stopped. The code for this is present inside the linux directory but I haven't been 
able to get it to work properly so far.

#### Use:

    voicecontrol

Type this command from any path on the terminal. You have to say 'activate' every 
time  in order to activate the control. Then you can say any of the following:

    open chrome       - opens a new Google Chrome window
    open downloads    - opens the ~/Downloads directory using nautilus
    local search      - activates gnome-do, which is a desktop search 
                        assistant for gnome.
                        Note: I plan to make this search process voice 
                        controlled as well.
    lock screen       - locks the screen

    search <search query in natural language> 
                      - activates Betty's web search mode which will 
                        allow you to ask questions in natural language
                        e.g.
                             search what is the weather in cincinnati 
                                     OR
                             search what is the date
                        
#### Future:

I'm looking for a gesture control package that will allow me to replicate touchpad's 
functionalities using the laptop's webcam.


## Windows

I'm not developing this currently. If you are interested, please take a look 
at the windows directory inside the repository.

Softwares/packages needed: python, pyaudio and SpeechRecognition package.

You have to figure out the rest :)

