import Reversi

# Cette méthode heuristique calcule la différence entre le nombre de pions noirs
# et le nombre de pions blancs

# PION NOIR = -1
# PION BLANC = 1
# CASE VIDE = 0
def heuristic(board, move, player):
    return (board._nbBLACK - board._nbWHITE) * board.sameColor(board._BLACK, player._mycolor)
