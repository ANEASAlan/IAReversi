import Reversi
import myPlayer
import time
from io import StringIO
import sys
import pygame
import tests

## Update the board
def update(b):
    for posX in range(10):
        for posY in range(10):
            if b._board[posX][posY] == b._BLACK:
                screen.blit(cB,(posX*32,posY*32))
            elif b._board[posX][posY] == b._WHITE:
                screen.blit(cW,(posX*32,posY*32))
            else :
                screen.blit(cE,(posX*32,posY*32))
    pygame.display.flip()

## Initialize pygame
pygame.init()

## Set screen
screen = pygame.display.set_mode((320,320))

## Set Refresh
clock = pygame.time.Clock()
FPS = 60
clock.tick(FPS)

## Load image
cW = pygame.image.load("White.png")
cB = pygame.image.load("Black.png")
cE = pygame.image.load("Empty.png")

## Variable to write the end only once
done = True

b = Reversi.Board(10)

players = []
player1 = myPlayer.myPlayer(countingCorners)
player1.newGame(b._BLACK)
players.append(player1)
player2 = myPlayer.myPlayer(countingCorners)
player2.newGame(b._WHITE)
players.append(player2)

totalTime = [0,0] # total real time for each player
nextplayer = 0
nextplayercolor = b._BLACK
nbmoves = 1

outputs = ["",""]
sysstdout= sys.stdout
stringio = StringIO()
## Inifinite loop to keep the window open
while True:
    ## Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            quit()
    
    ## print(b.legal_moves()) Useless
    while not b.is_game_over():
        print("Referee Board:")
        print(b)
        print("Before move", nbmoves)
        print("Legal Moves: ", b.legal_moves())
        nbmoves += 1
        otherplayer = (nextplayer + 1) % 2
        othercolor = b._BLACK if nextplayercolor == b._WHITE else b._WHITE
        
        currentTime = time.time()
        sys.stdout = stringio
        move = players[nextplayer].getPlayerMove()
        sys.stdout = sysstdout
        playeroutput = "\r" + stringio.getvalue()
        stringio.truncate(0)
        print(("[Player "+str(nextplayer) + "] ").join(playeroutput.splitlines(True)))
        outputs[nextplayer] += playeroutput
        totalTime[nextplayer] += time.time() - currentTime
        print("Player ", nextplayercolor, players[nextplayer].getPlayerName(), "plays" + str(move))
        (x,y) = move 
        if not b.is_valid_move(nextplayercolor,x,y):
            print(otherplayer, nextplayer, nextplayercolor)
            print("Problem: illegal move")
            break
        b.push([nextplayercolor, x, y])

        update(b)

        players[otherplayer].playOpponentMove(x,y)

        nextplayer = otherplayer
        nextplayercolor = othercolor
        print(b)

    ## Final result, done only once
    if done:
        done = False
        print("The game is over")
        print(b)
        (nbwhites, nbblacks) = b.get_nb_pieces()
        print("Time:", totalTime)
        print("Winner: ", end="")
        if nbwhites > nbblacks:
            print("WHITE")
        elif nbblacks > nbwhites:
            print("BLACK")
        else:
            print("DEUCE")

