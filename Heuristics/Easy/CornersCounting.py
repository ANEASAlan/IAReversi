import Reversi

# Cette méthode heuristique compte le nombre de coin blanc et de coin noir et
# en fait la somme

# COIN NOIR = -1
# COIN BLANC = 1
# COIN VIDE = 0
def heuristic(board, move, player):
    # On récupère la taille du plateau
    size = board.get_board_size()

    # On récupère le tableau représentant les coins
    corners = board.corners

    # Sotcke la valeur heuristique finale à renvoyer
    cornerCount = 0

    # Calcul coin supérieur gauche
    cornerCount += corners[0][0] * board.sameColor(board.getCell(0, 0), player._mycolor)

    # Calcul coin supérieur droit
    cornerCount += corners[0][size - 1] * board.sameColor(board.getCell(0, size - 1), player._mycolor)

    # Calcul coin inférieur gauche
    cornerCount += corners[size - 1][0] * board.sameColor(board.getCell(size - 1, 0), player._mycolor)

    # Calcul coin inférieur droit
    cornerCount += corners[size - 1][size - 1] * board.sameColor(board.getCell(size - 1, size - 1), player._mycolor)

    return cornerCount
