import Reversi

# Cette méthode heuristique compte le nombre de coin blanc et de coin noir et
# en fait la somme

# COIN NOIR = -1
# COIN BLANC = 1
# COIN VIDE = 0
def heuristic(board, move):
    # On récupère la taille du plateau
    size = board.get_board_size()

    # On récupère le tableau représentant les coins
    corners = board.corners

    # Sotcke la valeur heuristique finale à renvoyer
    cornerCount = 0

    # Calcul coin supérieur gauche
    cornerCount += corners[0][0] * (board.getCell(0, 0) * 2 - 3)

    # Calcul coin supérieur droit
    cornerCount += corners[0][size - 1] * (board.getCell(0, size - 1) * 2 - 3)

    # Calcul coin inférieur gauche
    cornerCount += corners[size - 1][0] * (board.getCell(size -1, 0) * 2 - 3)

    # Calcul coin inférieur droit
    cornerCount += corners[size - 1][size - 1] * (board.getCell(size - 1, size - 1) * 2 - 3)
    return cornerCount