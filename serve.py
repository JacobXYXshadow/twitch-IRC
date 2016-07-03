#!/usr/bin/env python

from sys import exit
from config.config import config
import lib.bot as bot
from lib.serial_start import serialFeed1
import pygame

# twitch-IRC
# Inspired by http://twitch.tv/twitchplayspokemon
# Initialized from a build of Twitch Plays by Aidan Thomson
# Original github repository: https://github.com/aidanrt/twitch-plays 
# ---
# Additional Functionality added by Paul Perrone
#
# Ability to turn the bot off and on mid stream
# 	-Uses a specific message in chat by a specific twitch account
# Communication with Arduino through serial ports
# 	-Controller support for the same keymap commands
# Chat data collection into a csv for analysis
#

try:
    bot.Bot().run()
except KeyboardInterrupt:
    exit()
