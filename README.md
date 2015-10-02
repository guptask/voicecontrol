# Voice Control
Laptop functionality control using Google's speech recognition toolkit

### Debian/Ubunutu (or any other Debian-based distribution)

#### Configure:

Python (2.7 or higher), pyaudio and SpeechRecognition are needed.
Additional packages needed are espeak, xdotool, nautilus, gnome-do, etc.

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

I want to use a natural language interpretor to create a generic framework for 
command interpretation.


### Windows

I'm not developing this currently. If you are interested, please take a look 
at the windows directory inside the repository.

Softwares/packages needed: python, pyaudio and SpeechRecognition package.

You have to figure out the rest :)

