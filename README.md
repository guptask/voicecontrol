# Voice Control
Laptop functionality control using Google's speech recognition toolkit

### Debian/Ubunutu (or any other Debian-based distribution)

Python (2.7 or higher), pyaudio and SpeechRecognition are needed.
Additional packages needed are espeak, xdotool, nautilus, gnome-do, etc.

Commands needed to download and configure the package:

    sudo apt-get install git
    git clone https://github.com/guptask/voicecontrol
    ./voicecontrol/linux/configure

I'm working on a voicecontrol service that can be installed, started and stopped.
The code is present inside the linux directory but I need to fix some bugs in it.


### Windows

I'm not developing this currently. If you are interested, please take a look 
at the windows directory inside the repository.

Softwares/packages needed: python, pyaudio and SpeechRecognition package.

You have to figure out the rest :)

