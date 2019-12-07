# y being the abscissa, and x being the ordinate, even though it's unusual, in order to have the user write the abscissa before and the ordinate after
def PositivePowerSpots(powerSpots, y, x, length = 10):

    if (y != 0 and y != length - 1) or (x != 0 and x != length - 1):
        return

    
    if x == 0 :
        powerSpots[1][y] = abs(powerSpots[1][y])
        
    elif x == length - 1 :
        powerSpots[x-1][y] = abs(powerSpots[x-1][y])

    if y == 0 :
        print("d")
        powerSpots[x][1] = abs(powerSpots[x][1])

    elif y == length - 1 :
        powerSpots[x][y-1] = abs(powerSpots[x][y-1])

    if x == 0 and y == 0 :
        powerSpots[1][1] = abs(powerSpots[1][1])

    elif x == 0 and y == length - 1 :
        powerSpots[1][y-1] = abs(powerSpots[1][y-1])

    elif y == 0 and x == length - 1 :
        powerSpots[x-1][1] = abs(powerSpots[x-1][1])

    elif x == length-1 and y == length - 1 :
        powerSpots[x-1][y-1] = abs(powerSpots[x-1][y-1])

