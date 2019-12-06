import Reversi

# NOIR = -1
# BLANC = 1
# VIDE = 0

def heuristic(board, myMove, mycolor):

    #if mycolor == 0:

    if board._BLACK != mycolor and board._nbBLACK == 0:
        return 10000

    if board._WHITE != mycolor and board._nbWHITE == 0:
        return 10000

    # On récupère la taille du plateau
    size = board.get_board_size()
    # On récupère le tableau représentant les coins
    corners = board.corners

    # La valeur à renvoyer à la fin
    point = 0
    move = 0
    corner = 0
    color = 0
    totalNbPieces = 0

    # On parcourt le plateau
    for x in range(size):
        for y in range(size):
            point += board.powerPoints[x][y] * board.sameColor(board.getCell(x, y), mycolor) # ici MonteCarlo, à changer par un tableau de Power spots custom donné par les tests en réseaux de neurones

    move += len(board.legal_moves())
    board.pop()
    move -= len(board.legal_moves())
    board.push(myMove)

    # Calcul coin supérieur gauche
    corner += corners[0][0] * board.sameColor(board.getCell(0, 0), mycolor)

    # Calcul coin supérieur droit
    corner += corners[0][size - 1] * board.sameColor(board.getCell(0, size - 1), mycolor)

    # Calcul coin inférieur gauche
    corner += corners[size - 1][0] * board.sameColor(board.getCell(size - 1, 0), mycolor)

    # Calcul coin inférieur droit
    corner += corners[size - 1][size - 1] * board.sameColor(board.getCell(size - 1, size - 1), mycolor)

    totalNbPieces = board._nbBLACK + board._nbWHITE
    color = (board._nbBLACK - board._nbWHITE) * board.sameColor(board._BLACK, mycolor)

    moveCountWeight = move * (1.5 - totalNbPieces / 100.0) ** 10
    colorsWeight = color * (0.10 + totalNbPieces / 100.0) ** 20
    pointWeight = point * (2.0 - totalNbPieces / 100.0) ** 4
    cornerWeight = corner * (2.2 - totalNbPieces / 100.0) ** 5

    # print(color)
    # print("---------------------")
    # print(moveCountWeight)
    # print(colorsWeight)
    # print(pointWeight)
    # print(cornerWeight)
    # print("")
    # print(corner)
    # print(corners[0][0])
    # print(board.sameColor(board.getCell(0, 0), color))
    # print(color)
    # print(board.getCell(0, 0))
    # print("\n")

    return moveCountWeight + colorsWeight + pointWeight + cornerWeight
