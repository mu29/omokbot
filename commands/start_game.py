# coding: utf-8

from omokbot import OmokBot
from message import Message
from game import Game

def run(bot, msg):
    if msg.user in bot.game:
        bot.client.rtm_send_message(msg.channel, u"하던 게임부터 마무리해주렴")
    else:
        bot.game[msg.user] = Game()
        bot.client.rtm_send_message(msg.channel, u"[A-O][1-15]를 입력해서 돌을 놓을 수 있어 (ex : F8)")
        bot.client.rtm_send_message(msg.channel, bot.game[msg.user].get_board())
