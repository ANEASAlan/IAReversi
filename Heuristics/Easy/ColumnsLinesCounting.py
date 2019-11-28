import Reversi

# Cette méthode heuristique compte le nombre de colonnes et de lignes et
# en fait la somme

# COIN NOIR = -1
# COIN BLANC = 1
# COIN VIDE = 0

def countingLineCol(board, x, y, tmp, streak):
    if isWhite(board, x, y) and tmp >= 0:
        tmp += 1

    elif isWhite(board, x, y) and tmp < 0:
        tmp = 1
        if abs(tmp) > abs(streak):
            streak = tmp

    if isBlack(board, x, y) and tmp <= 0:
        tmp -= 1

    elif isBlack(board, x, y) and tmp > 0:
        tmp = -1
        if abs(tmp) > abs(streak):
            streak = tmp

    return (tmp, streak)


    

def countingColumnsAndLines(board):
    # To parse the board you want to do a double for loop
    # Best case would be to do it all in a unique loop but that's
    # difficult

    # The board is a square
    size = board.get_board_size()

    # The board to use, to avoid multiple dots
    board = board._board

    count = 0

    for x in range(size):
        streak = [0, 0]
        tmp = [0, 0]
        for y in range(size):
            (tmp[0], streak[0]) = countingLineCol(board, x, y, tmp[0], streak[0])
            (tmp[1], streak[1]) = countingLineCol(board, y, x, tmp[1], streak[1])

    return streak[0] + streak[1]
