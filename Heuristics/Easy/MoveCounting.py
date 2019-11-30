import Reversi

# NOIR = -1
# BLANC = 1
# VIDE = 0

def heuristic(board, move, color):
    myMove = len(board.legal_moves())
    board.pop()
    theirMove = len(board.legal_moves())
    board.push(move)
    return (myMove - theirMove)
