
About twitch-IRC
===

This project's inspirational codebase can be found at https://github.com/aidanrt/twitch-plays
The project has been heavily modified, though the config.py and irc.py files are untouched and work as they do in the original project.

This project's functionality includes:  

* The ability to turn the bot's functionality on and off with a user-specific command
* Chat Data Recording into a CSV for later analysis
* IRC communication with Arduinos through Serial Ports


####Steps to Run the Program:####
___

Rename `config/config_basic.py` to `config/config.py`. Replace the username/password there with your Twitch username and [OAuth token](http://www.twitchapps.com/tmi/). Modifying the start throttle is done here.

Rename `lib/bot_basic.py` tp `lib/bot.py`. Replace the `YOUR USERNAME GOES HERE` field with your username. Replace the `INPUT SHUTOFF` and `INPUT TURNON` with your desired messages.

Begin the program by navigating to the root directory in the command promt. Run it with `python serve.py`. If your username/password is wrong you will be notified.
