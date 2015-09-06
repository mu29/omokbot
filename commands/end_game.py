# coding: utf-8

from omokbot import OmokBot
from message import Message
from game import Game

def run(bot, msg):
    if msg.user in bot.game:
        del(bot.game[msg.user])
        bot.client.rtm_send_message(msg.channel, u"뭐야 쫄았어?")
