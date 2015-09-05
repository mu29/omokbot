# coding: utf-8

class Message(object):
    def __init__(self):
        self.user = None
        self.channel = None
        self.command = None
        self.content = None

    def set(self, user, channel, command, content):
        self.user = user
        self.channel = channel
        self.command = command
        self.content = content
