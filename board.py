# board.py
#connect with constants.py
from constants import PLAYER, AI, EMPTY, ROWS, COLS

class Board:
    def _init_(self):
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

    def make_move(self, col, piece):
        for r in range(ROWS-1, -1, -1):
            if self.board[r][col] == EMPTY:
                self.board[r][col] = piece
                return True
        return False

    def undo_move(self, col):
        for r in range(ROWS):
            if self.board[r][col] != EMPTY:
                self.board[r][col] = EMPTY
                return True
        return False

    def available_moves(self):
        return [c for c in range(COLS) if self.board[0][c] == EMPTY]

    def is_full(self):
        return all(self.board[0][c] != EMPTY for c in range(COLS))

    def check_winner(self, piece):
        # Horizontal
        for r in range(ROWS):
            for c in range(COLS-3):
                if all(self.board[r][c+i] == piece for i in range(4)):
                    return True
        # Vertical
        for c in range(COLS):
            for r in range(ROWS-3):
                if all(self.board[r+i][c] == piece for i in range(4)):
                    return True
        # Positive Diagonal
        for r in range(ROWS-3):
            for c in range(COLS-3):
                if all(self.board[r+i][c+i] == piece for i in range(4)):
                    return True
        # Negative Diagonal
        for r in range(3, ROWS):
            for c in range(COLS-3):
                if all(self.board[r-i][c+i] == piece for i in range(4)):
                    return True
        return False