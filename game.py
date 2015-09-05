class Game(object):
    def __init__(self):
        board = "0" * 225

    def get_board(self):
        for y in range(0, 15):
            for x in range(0, 15):
                block = board[y * 15 + x]
                board += block == 0 ? "⬜️" : block == 1 ? "⚫️" : "⚪️"
            board += "\n"

        return board
