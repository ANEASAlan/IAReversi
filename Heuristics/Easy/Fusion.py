import Reversi
import sys

# NOIR = -1
# BLANC = 1
# VIDE = 0

CustomValues = True
CustomWeights = [1.5,10,0.10,20,2.0,4,2.2,5], [99,-8,-24,8,-4,7,6,-3,4,0,3,-3,2,0,0]
## tester CustomWeights = [1.5,-10,0.10,20,2.0,4,2.2,5], [64,-5,-16,5,-3,5,4,-2,3,0,2,-2,1,0,0]

def heuristic(board, myMove, player):

    #if mycolor == 0:

    if board._BLACK != player._mycolor and board._nbBLACK == 0:
        return 100000

    if board._WHITE != player._mycolor and board._nbWHITE == 0:
        return 100000

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
            if board._BLACK == player._mycolor :
                point += player.myPowerSpots[x][y] * board.sameColor(board.getCell(x, y), player._mycolor)
            else:
                point += player.ennemyPowerSpots[x][y] * board.sameColor(board.getCell(x, y), player._mycolor)
            # ici MonteCarlo, à changer par un tableau de Power spots custom donné par les tests en réseaux de neurones

    move += len(board.legal_moves())
    board.pop()
    move -= len(board.legal_moves())
    board.push(myMove)

    # Calcul coin supérieur gauche
    corner += corners[0][0] * board.sameColor(board.getCell(0, 0), player._mycolor)

    # Calcul coin supérieur droit
    corner += corners[0][size - 1] * board.sameColor(board.getCell(0, size - 1), player._mycolor)

    # Calcul coin inférieur gauche
    corner += corners[size - 1][0] * board.sameColor(board.getCell(size - 1, 0), player._mycolor)

    # Calcul coin inférieur droit
    corner += corners[size - 1][size - 1] * board.sameColor(board.getCell(size - 1, size - 1), player._mycolor)

    totalNbPieces = board._nbBLACK + board._nbWHITE
    color = (board._nbBLACK - board._nbWHITE) * board.sameColor(board._BLACK, player._mycolor)

    if(CustomValues):
        moveCountWeight = move * (CustomWeights[0][0] - totalNbPieces / 100.0) ** CustomWeights[0][1]
        colorsWeight = color * (CustomWeights[0][2] + totalNbPieces / 100.0) ** CustomWeights[0][3]
        pointWeight = point * (CustomWeights[0][4] - totalNbPieces / 100.0) ** CustomWeights[0][5]
        cornerWeight = corner * (CustomWeights[0][6] - totalNbPieces / 100.0) ** CustomWeights[0][7]
    else:
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
