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

    if(x != y and y != width - x - 1 and x != width - y - 1):
        subChange(powerSpots, y, x, value, width)

def subAdd(powerSpots, x, y, value, width = 10):
    powerSpots[x][y] += value

    x = width - x - 1
    powerSpots[x][y] += value

    y = width - y - 1
    powerSpots[x][y] += value

    x = width - x - 1
    powerSpots[x][y] += value

def AddPowerSpots(powerSpots, x, y, value, width = 10):
    subAdd(powerSpots, x, y, value, width)

    if(x != y and y != width - x - 1 and x != width - y - 1):
        subAdd(powerSpots, y, x, value, width)

def AddForEntireTable(powerSpots, table):
    l = len(table) # Suposedly a table of size 15 in order to change the entire table
    x = 0
    y = 0
    for i in range(l):
        AddPowerSpots(powerSpots, x, y, table[i])
        if x == y:
            x = 0
            y += 1
        else:
            x += 1

def ChangeForEntireTable(powerSpots, table):
    l = len(table) # Suposedly a table of size 15 in order to change the entire table
    x = 0
    y = 0
    for i in range(l):
        ChangePowerSpots(powerSpots, x, y, table[i])
        if x == y:
            x = 0
            y += 1
        else:
            x += 1
