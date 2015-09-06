# coding: utf-8

from settings import *

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

    def judge(self):
        for y in range(0, 15):
            count = 1
            prev = self.board[y * 15]
            for x in range(1, 15):
                if self.board[y * 15 + x] == prev:
                    count += 1
                    if count == 5 and prev != BLANK_BLOCK: return prev
                else:
                    count = 1
                    prev = self.board[y * 15 + x]

        for x in range(0, 15):
            count = 1
            prev = self.board[x]
            for y in range(1, 15):
                if self.board[y * 15 + x] == prev:
                    count += 1
                    if count == 5 and prev != BLANK_BLOCK: return prev
                else:
                    count = 1
                    prev = self.board[y * 15 + x]
                print count

        for x in range(0, 15):
            count = 1
            prev = self.board[x]
            for i in range(1, 15 - x):
                if self.board[i * 15 + (x + i)] == prev:
                    count += 1
                    if count == 5 and prev != BLANK_BLOCK: return prev
                else:
                    count = 1
                    prev = self.board[i * 15 + (x + i)]

        for y in range(0, 15):
            count = 1
            prev = self.board[y * 15]
            for i in range(1, y + 1):
                if self.board[(y - i) * 15 + i] == prev:
                    count += 1
                    if count == 5 and prev != BLANK_BLOCK: return prev
                else:
                    count = 1
                    prev = self.board[(y - i) * 15 + i]

        return BLANK_BLOCK


    # 임시로 평가 테이블만
    def get_score(self, player, x, y):
        if x < 0 or y < 0 or x > 14 or y > 14: return 0

        max_match = 0
        # 양옆
        match = 1
        for i in reversed(range(0, x)):
            if self.board[y * 15 + i] == player: match += 1
            else: break
        for i in range(x + 1, 15):
            if self.board[y * 15 + i] == player: match += 1
            else: break
        max_match = match

        # 위아래
        match = 1
        for i in reversed(range(0, y)):
            if self.board[i * 15 + x] == player: match += 1
            else: break
        for i in range(y + 1, 15):
            if self.board[i * 15 + x] == player: match += 1
            else: break
        if match > max_match: max_match = match

        top = (x + 1) if (x + 1) < (y + 1) else (y + 1)
        bottom = (15 - x) if (15 - x) < (15 - y) else (15 - y)
        # 오른쪽아래로
        match = 1
        for i in range(1, top):
            if self.board[(y - i) * 15 + (x - i)] == player: match += 1
            else: break
        for i in range(1, bottom):
            if self.board[(y + i) * 15 + (x + i)] == player: match += 1
            else: break
        if match > max_match: max_match = match

        top = (15 - x) if (15 - x) < (y + 1) else (y + 1)
        bottom = (x + 1) if (x + 1) < (15 - y) else (15 - y)
        # 오른쪽위로
        match = 1
        for i in range(1, top):
            if self.board[(y - i) * 15 + (x + i)] == player: match += 1
            else: break
        for i in range(1, bottom):
            if self.board[(y + i) * 15 + (x - i)] == player: match += 1
            else: break
        if match > max_match: max_match = match

        return max_match

    def ai_turn(self):
        candidates = {}
        for i in range(0, 225):
            if self.board[i] != BLANK_BLOCK:
                x_pos = i % 15
                y_pos = i / 15
                for y_plus in range(-1, 2):
                    for x_plus in range(-1, 2):
                        x = x_pos + x_plus
                        y = y_pos + y_plus
                        pos = y * 15 + x
                        if self.board[pos] != BLANK_BLOCK: continue

                        black = self.get_score(BLACK_BLOCK, x, y) * 2 - 1
                        white = self.get_score(WHITE_BLOCK, x, y) * 2
                        candidates[pos] = black if black > white else white

        pos = max(candidates, key=candidates.get)
        self.board = self.board[:pos] + WHITE_BLOCK + self.board[pos + 1:]
