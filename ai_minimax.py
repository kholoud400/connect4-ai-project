import math
import random
from board import Board
from ai_eval import score_position, is_terminal_node
from constants import PLAYER, AI

def minimax(board: Board, depth, alpha, beta, maximizingPlayer):
    valid_locations = board.available_moves()
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if board.check_winner(AI):
                return (None, 1000000000)
            elif board.check_winner(PLAYER):
                return (None, -1000000000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, AI))
    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            board.make_move(col, AI)
            new_score = minimax(board, depth-1, alpha, beta, False)[1]
            board.undo_move(col)
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            board.make_move(col, PLAYER)
            new_score = minimax(board, depth-1, alpha, beta, True)[1]
            board.undo_move(col)
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value