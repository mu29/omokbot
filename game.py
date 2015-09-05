# coding: utf-8

class Game(object):
    def __init__(self):
        self.board = "0" * 225

    def get_board(self):
        board = ""
        for y in range(0, 15):
            for x in range(0, 15):
                block = self.board[y * 15 + x]
                board += ("⬜️" if block == "0" else ("⚫️" if block == "1" else "⚪️"))
            board += "\n"

        return board
