
Installation
============

This version is linux ready. If you do not have xdotool installed on linux, use `apt-get install xdotool`. If the above does not work prefix that same command with `sudo`.

If on windows you are going to need [pywin32](http://sourceforge.net/projects/pywin32/). If you run into errors try running this with Python [2.7.x](http://www.python.org/download/releases/2.7/).

Rename `config/config_basic.py` to `config/config.py`, and replace the username/password there with your Twitch username and [OAuth token](http://www.twitchapps.com/tmi/). Feel free to modify the start throttle here aswell.

___


After you've set that up, open up your terminal and type `python serve.py`. If your username/password is wrong you will be notified.

Whilst the script is running make sure you have your emulator in focus as your primary window. If you click onto another window, the script won't work. If you're not able to stay focused on one window as you need to do other things with your computer, you could try running all of this from within a virtual machine.

--

You'll need to have VBA in focus for this to work, so your best bet would be to run all of this
from within a VM.
