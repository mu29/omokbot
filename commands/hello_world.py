# coding: utf-8

from omokbot import OmokBot
from message import Message

def run(bot, message):
    bot.client.rtm_send_message(message.channel, u'그래 안녕')
