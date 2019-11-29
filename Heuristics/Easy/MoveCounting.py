import Reversi

# NOIR = -1
# BLANC = 1
# VIDE = 0

def heuristic(board, move, color):
    return len(board.legal_moves())
