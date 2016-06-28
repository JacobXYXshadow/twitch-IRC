import os
import time
import serial
from serial_start import serialFeed1
#from subprocess import Popen
    #Use Popen if you want to start a subprocess with an input


class Game:
    keymap = {
           'wave': ["1"],
           'smile': ["2"],
           'frown': ["3"],
           'eyeRoll': ["4"],
           'twitch': ["5"],
           'fly': ["6"],
           'cat': ["7"]
        }

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    #This function is what executes when the bot is on and receives an actionable message
    def push_button(self, button):
            serialFeed1.write(str(self.button_to_key(button)))
