# coding: utf-8

import time
from slackclient import SlackClient
from message import *
from settings import *

class OmokBot(object):
	def __init__(self):
		self.client = SlackClient(TOKEN)

	def dispatch_message(self, events):
		messages = []
		for e in events:
			channel = e.get('channel', '')
			text = e.get('text', '')
			command = text.split(' ')[0]
			content = text.replace(command + ' ', '')

			msg = Message()
			msg.set(text, command, content)
			messages.append(msg)

			print(channel + "," + command + "," + content);

		return messages

	def run(self):
		self.client.rtm_connect()
		#self.client.rtm_send_message('random', u'슬랙 봇 테스트')
		while True:
			events = self.client.rtm_read()
			if events:
				messages = self.dispatch_message(events)
			time.sleep(1)



if '__main__' == __name__:
	bot = OmokBot()
	bot.run()
