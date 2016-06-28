import time
import csv

from config.config import config
from lib.irc import Irc
from lib.game import Game
from lib.misc import pbutton

class Bot:

    def __init__(self):
        self.config = config
        self.irc = Irc(config)
        self.game = Game()
        self.botOn = True
        self.message_buffer = [{'username': '', 'button': ''}] * self.config['misc']['chat_height']

    def set_message_buffer(self, message):
        self.message_buffer.insert(self.config['misc']['chat_height'] - 1, message)
        self.message_buffer.pop(0)

    def run(self):
        throttle_timers = {button:0 for button in config['throttled_buttons'].keys()}

        while True:
            new_messages = self.irc.recv_messages(1024)
            
            if not new_messages:
                continue

            for message in new_messages: 
                button = message['message'].lower()
                username = message['username'].lower()

                #Turns off the bot with one of your commands
                if username == 'squid767':
                    if button == 'TAKE IT OFF!':
                        self.botOn = False

                #Turns on the bot with one of your commands
                if username == 'squid767':
                    if button == 'GET IT ON!':
                        self.botOn = True

                #Helper for writing actionable data to csv
                if button in self.game.keymap.keys():
                    actionable = 1
                else:
                    actionable = 0

                #Helper for writing is Bot Active data to csv
                if self.botOn == True:
                    chatActionsOn = 1
                else:
                    chatActionsOn = 0

                #Creates an array of data to write to csv
                chat_data_array = [username, time.time(), button, actionable , chatActionsOn]
                
                #Writes a message to the csv that tracks chat data
                with open('chat_data.csv', 'a+') as chatData:
                    writer = csv.writer(chatData)
                    writer.writerow(chat_data_array)

                #If the Bot is on, then it outputs the appropriate action.
                #If the Bot is off, continues to gen the input feed but does not execute an action
                if self.botOn == True:
                    if not self.game.is_valid_button(button):
                        continue

                    if button in self.config['throttled_buttons']:
                        if time.time() - throttle_timers[button] < self.config['throttled_buttons'][button]:
                            continue

                        throttle_timers[button] = time.time()
                    

                    self.set_message_buffer({'username': username, 'button': button})
                    pbutton(self.message_buffer) #This is a console output function. It outputs the log of inputs from chat
                    self.game.push_button(button)
                else:
                    print "Bot Enabled Chat is OFF"
                    self.set_message_buffer({'username': username, 'button': button})
                    pbutton(self.message_buffer)
                    