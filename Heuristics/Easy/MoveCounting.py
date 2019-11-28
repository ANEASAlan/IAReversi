import Reversi

# NOIR = -1
# BLANC = 1
# VIDE = 0

def heuristic(board, move):
    return len(board.legal_moves()) * (2 * board._nextPlayer - 3)
