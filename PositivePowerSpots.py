import abs from math

def PositivePowerSpots(powerSpots, x, y, length = 10):

    if x != y || x != 0 || x != length - 1:
        return
    
    if x == 0 :
        powerSpots[1,y] = abs(powerSpots[1,y])

    elif x == length - 1 :
        powerSpots[x-1,y] = abs(powerSpots[x-1,y])

    if y == 0 :
        powerSpots[x,1] = abs(powerSpots[x,1])

    elif y == length - 1 :
        powerSpots[x,y-1] = abs(powerSpots[x,y-1])

    if x == 0 && y == 0 :
        powerSpots[1,1] = abs(powerSpots[1,1])

    elif x == 0 && y == length - 1 :
        powerSpots[1,y-1] = abs(powerSpots[1,y-1])

    elif y == 0 && x == length - 1 :
        powerSpots[x-1,1] = abs(powerSpots[x-1,1])

    elif x == length-1 && y == length - 1 :
        powerSpots[x-1,y-1] = abs(powerSpots[x-1,y-1])
