# coding: utf-8

import time
from slackclient import SlackClient
from importlib import import_module
from message import *
from settings import *

class OmokBot(object):
	def __init__(self):
		self.client = SlackClient(TOKEN)
		self.game = {}
		self.commands = {}

	def load(self):
		for i in range(0, len(COMMANDS) / 2):
			name = COMMANDS[i * 2]
			func = COMMANDS[i * 2 + 1]
			self.commands[name] = import_module('commands.' + func)

	def dispatch(self, events):
		messages = []
		for e in events:
			user = e.get('user', '')
			channel = e.get('channel', '')
			text = e.get('text', '')
			command = text.split(' ')[0]
			content = text.replace(command + ' ', '', 1)

			if user and channel and command:
				msg = Message()
				msg.set(user, channel, command, content)
				messages.append(msg)

		return messages

	def handle(self, messages):
		for msg in messages:
			if msg.command in self.commands:
				self.commands[msg.command].run(self, msg)

	def run(self):
		self.client.rtm_connect()
		while True:
			events = self.client.rtm_read()
			if events:
				messages = self.dispatch(events)
				self.handle(messages)
			time.sleep(1)


if '__main__' == __name__:
	bot = OmokBot()
	bot.load()
	bot.run()
