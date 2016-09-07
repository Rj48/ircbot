#!/usr/bin/python

import urllib2
import json

def ud(bot,msg):
    if msg.msg.startswith('!ud'):
        split = msg.msg.split(' ')
        if len(split) < 2:
            return

        word = split[1]
        definition = None
        idx = 0

        try:
            if len(split) > 2:
                idx = int(split[2]) - 1
            url = 'http://api.urbandictionary.com/v0/define?term=%s' % word
            resp = urllib2.urlopen(url)
            js = json.loads(resp.read())
            definition = js['list'][idx]['definition']
        except Exception as ex:
            pass

        if not definition:
            answer = 'Couldn\'t find "%s" :(' % word
        else:
            answer = '"%s": %s' % (word, definition)
        bot.sendChannelMessage(msg.replyTo, answer)

def init(bot):
    bot.events.register('channelMessage',ud)

def close(bot):
    bot.events.unregister('channelMessage',ud)
