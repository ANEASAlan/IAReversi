import Reversi

# NOIR = -1
# BLANC = 1
# VIDE = 0

def countingMoves(board):
    if player == board._WHITE:
        moveCount += len(board.legal_moves())
    else:
        moveCount -= len(board.legal_moves())
