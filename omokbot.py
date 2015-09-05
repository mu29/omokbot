# coding: utf-8

from slackclient import SlackClient
from settings import *

class OmokBot(object):
	def __init__(self):
		self.client = SlackClient(TOKEN)

	def run(self):
		self.client.rtm_connect()
		self.client.rtm_send_message('random', u'슬랙 봇 테스트')
		print("!")


if '__main__' == __name__:
	bot = OmokBot()
	bot.run()
