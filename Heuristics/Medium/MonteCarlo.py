import Reversi

# Cette fonction calcule si les pions sont plutot influent ou non
# Si les blancs sont très influents alors le résultat est plus grand
# Si les noirs sont très influents alorsl e résultats est plus petit
def heuristic(board, move, player):
    # On récupère la taille du plateau
    size = board.get_board_size()

    # La valeur a renvoyé à la fin
    points = 0

    # On parcourt le plateau
    for x in range(size):
        for y in range(size):
            points += player.powerPoints[x][y] * board.sameColor(board.getCell(x, y), player.color)
    return points
