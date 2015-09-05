# coding: utf-8

import re
from omokbot import OmokBot
from message import Message
from game import Game

def run(bot, msg):
    if not re.match("[A-O][1-9][0-9]?", msg.content): return

    x = ord(msg.content[0]) - 65
    y = int(msg.content[1:]) - 1
    pos = y * 15 + x
    game = bot.game[msg.user]

    if y > 14: return
    if game.board[pos] != "0": return

    game.board = game.board[:pos] + "1" + game.board[pos + 1:]
    bot.client.rtm_send_message(msg.channel, bot.game[msg.user].get_board())
