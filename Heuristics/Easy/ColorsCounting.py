import Reversi

# Cette méthode heuristique calcule la différence entre le nombre de pions noirs
# et le nombre de pions blancs

# PION NOIR = -1
# PION BLANC = 1
# CASE VIDE = 0
def heuristic(board, move):
    # On récupère la taille du plateau
    size = board.get_board_size()

    # On récupère le tableau représentant les coins
    corners = board.corners

    # Sotcke la valeur heuristique finale à renvoyer
    colorsCount = 0

    # On parcourt l'entiereté du plateau
    return board._nbWHITE - board._nbBLACK
