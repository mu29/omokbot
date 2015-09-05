# coding: utf-8

import time
from slackclient import SlackClient
from importlib import import_module
from message import *
from settings import *

class OmokBot(object):
	def __init__(self):
		self.client = SlackClient(TOKEN)
		self.commands = {}

	def load(self):
		for i in range(0, len(COMMANDS) / 2):
			name = COMMANDS[i * 2]
			func = COMMANDS[i * 2 + 1]
			self.commands[name] = import_module('commands.' + func)

	def dispatch(self, events):
		messages = []
		for e in events:
			channel = e.get('channel', '')
			text = e.get('text', '')
			command = text.split(' ')[0]
			content = text.replace(command + ' ', '')

			msg = Message()
			msg.set(channel, command, content)
			messages.append(msg)

		return messages

	def handle(self, message):
		if (message.command in self.commands):
			print("!")
			self.commands[message.command].run(self, message)

	def run(self):
		self.client.rtm_connect()
		#self.client.rtm_send_message('random', u'슬랙 봇 테스트')
		while True:
			events = self.client.rtm_read()
			if events:
				messages = self.dispatch(events)
				for msg in messages:
					self.handle(msg)
			time.sleep(1)


if '__main__' == __name__:
	bot = OmokBot()
	bot.load()
	bot.run()
