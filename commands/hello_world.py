# coding: utf-8

from omokbot import OmokBot
from message import Message
import random

def run(bot, message):
    board = "";
    for y in range(0, 15):
        for x in range(0, 15):
            i = random.randint(0, 2)
            if i == 0:
                board += "⚪️"
            elif i == 1:
                board += "⚫️"
            else:
                board += "⬜️"
        board += "\n"
    bot.client.rtm_send_message(message.channel, board)
