import time
from os import system
import bot as cleanBot

def pp(message, mtype='INFO'):
    mtype = mtype.upper()
    print '[%s] [%s] %s' % (time.strftime('%H:%M:%S', time.gmtime()), mtype, message)

def ppi(channel, message, username):
    print '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, username.lower(), message)

def pbot(message, channel=''):
    if channel: 
        msg = '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, 'BOT', message)
    else: 
        msg = '[%s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), 'BOT', message)

    print msg

def pbutton(message_buffer):
    #system('clear')
    if cleanBot.Bot().botOn == True:
        print '\n\n'
        print '\n'.join([' {0:<12s} {1:>6s}'.format(message['username'][:12].title(), message['button'].lower()) for message in message_buffer])
    else:
        print '\n\n'
        print '\n'.join('CHAT ENABLED ACTIONS ARE OFF')
        print '\n'.join([' {0:<12s} {1:>6s}'.format(message['username'][:12].title(), message['button'].lower()) for message in message_buffer])
