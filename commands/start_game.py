# coding: utf-8

from omokbot import OmokBot
from message import Message
from game import Game

def run(bot, msg):
    bot.game[msg.user] = Game()
    bot.client.rtm_send_message(msg.channel, u"게임을 시작하지")
    bot.client.rtm_send_message(msg.channel, bot.game[msg.user].get_board())
