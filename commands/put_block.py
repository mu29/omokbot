# coding: utf-8

import re
from settings import *
from omokbot import OmokBot
from message import Message
from game import Game

def run(bot, msg):
    if not re.match("[A-O][1-9][0-9]?", msg.content):
        bot.client.rtm_send_message(msg.channel, u"잘 좀 입력해 봐")
        return

    if not msg.user in bot.game:
        bot.client.rtm_send_message(msg.channel, u"게임 중인거 맞아?")
        return

    x = ord(msg.content[0]) - 65
    y = int(msg.content[1:]) - 1
    pos = y * 15 + x
    game = bot.game[msg.user]

    if y > 14 :
        bot.client.rtm_send_message(msg.channel, u"잘 좀 입력해 봐")
        return
    if game.board[pos] != "0":
        bot.client.rtm_send_message(msg.channel, u"거긴 놓을 수 없어")
        return

    game.board = game.board[:pos] + BLACK_BLOCK + game.board[pos + 1:]
    bot.client.rtm_send_message(msg.channel, bot.game[msg.user].get_board())

    if game.judge == BLACK_BLOCK:
        bot.client.rtm_send_message(msg.channel, u"니가 이겼어 ㄷㄷ")
        del(bot.game[msg.user])

    game.ai_turn()
    bot.client.rtm_send_message(msg.channel, bot.game[msg.user].get_board())

    if game.judge == WHITE_BLOCK:
        bot.client.rtm_send_message(msg.channel, u"내가 이겼네?")
        del(bot.game[msg.user])
