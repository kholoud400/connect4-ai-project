# ai_eval.py
from constants import PLAYER, AI, EMPTY, ROWS, COLS, WINDOW_LENGTH
# This module contains functions to evaluate the game state for AI decision-making.
from board import Board

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER if piece == AI else AI
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2
    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4
    return score

def score_position(board: Board, piece):
    score = 0
    # center column preference
    center_col = [board.board[r][COLS//2] for r in range(ROWS)]
    score += center_col.count(piece) * 3
    # horizontal
    for r in range(ROWS):
        row_array = [board.board[r][c] for c in range(COLS)]
        for c in range(COLS-WINDOW_LENGTH+1):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)
    # vertical
    for c in range(COLS):
        col_array = [board.board[r][c] for r in range(ROWS)]
        for r in range(ROWS-WINDOW_LENGTH+1):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, piece)
    # positive diagonal
    for r in range(ROWS-WINDOW_LENGTH+1):
        for c in range(COLS-WINDOW_LENGTH+1):
            window = [board.board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)
    # negative diagonal
    for r in range(WINDOW_LENGTH-1, ROWS):
        for c in range(COLS-WINDOW_LENGTH+1):
            window = [board.board[r-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)
    return score

def is_terminal_node(board: Board):
    return board.check_winner(PLAYER) or board.check_winner(AI) or board.is_full()