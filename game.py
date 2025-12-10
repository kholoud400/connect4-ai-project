import math
from board import Board
from ai_minimax import minimax
from constants import PLAYER, AI

class ConnectFourGame:
    def __init__(self):
        self.board = Board()
        self.game_over = False
        self.winner = None

    def player_move(self, col):
        if not self.game_over and self.board.make_move(col, PLAYER):
            if self.board.check_winner(PLAYER):
                self.game_over = True
                self.winner = PLAYER
            elif self.board.is_full():
                self.game_over = True
                self.winner = None
            return True
        return False

    def ai_move(self):
        if not self.game_over:
            col, _ = minimax(self.board, depth=4, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)
            if col is not None:
                self.board.make_move(col, AI)
                if self.board.check_winner(AI):
                    self.game_over = True
                    self.winner = AI
                elif self.board.is_full():
                    self.game_over = True
                    self.winner = None

    def restart(self):
        self.board = Board()
        self.game_over = False
        self.winner = None
