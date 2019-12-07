def subChange(powerSpots, x, y, value, width = 10):
    powerSpots[x][y] = value

    x = width - x - 1
    powerSpots[x][y] = value

    y = width - y - 1
    powerSpots[x][y] = value

    x = width - x - 1
    powerSpots[x][y] = value

def ChangePowerSpots(powerSpots, x, y, value, width = 10):

    subChange(powerSpots, x, y, value, width)

    if(x != y):
        subChange(powerSpots, y, x, value, width)
