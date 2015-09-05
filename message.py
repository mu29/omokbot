# coding: utf-8

class Message(object):
    def __init__(self):
        self.channel = None
        self.command = None
        self.content = None

    def set(self, channel, command, content):
        self.channel = channel
        self.command = command
        self.content = content
