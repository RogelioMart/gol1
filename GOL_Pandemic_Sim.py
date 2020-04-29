import time
import random
import pygame, sys
from pygame.locals import *

'''
INSTRUCTIONS 
By pressing select keys the patterns on the grid change
The grid is a 47x47

The game will always begin with a random setup but it can be changed
immediatly after beginning.

These are the only possible keys to use.
    r = random
    d = decalethon
    p = pulsar
    g = gos gun glider
    s = social isolation
    n = no social isolation
    b = begining of a pandemic

for social distancing and not social distancing (s, n)
	when the board is filled it has a 40% change of being unused squares
	(dead), 30% of being healthy squares, 30% of being infected squares.

s = social distancing:
	This is to show how pandemics propogate when social distancing is 
	used. It does not necesarilly mirror Covid19 on a scale this is 
	just meant to show how a pandemic that has about ends sooner or
	does not end in catastrophy when the proper precautions are taken.
	To simulate this I set the infection rate to 80%

n = not social distancing:
	to simulate social distancing I lowered the infection rate to 30%

b = begining of a pandemic:
	This is meant to simulate how a pandemic starts with only 5 or less
	infected people but their infection rate is 100% because in this case
	the existance of the virus is not yet known and like covid19 this one
	simulates a case in which people are carriers of the virus for some
	period of time without showing symptoms. Therefore I set the infection
	rate for the begining one to be 100%
	
Aside from random the rest just display known patterns.

'''

def aroundTheBlock(currR, currC, twoD):

    numOfNeighbors = 0

    maxC = 46
    maxR = 46

    if (currC != maxC): #checks east
        if (twoD[currR][currC + 1] >= 1):
            numOfNeighbors = numOfNeighbors + 1

    if ((currC != maxC) and (currR != maxR)): #checkst south east
        if (twoD[currR + 1][currC + 1] >= 1):
            numOfNeighbors = numOfNeighbors + 1

    if (currR != maxR): # checks south
        if (twoD[currR + 1][currC] >= 1):
            numOfNeighbors = numOfNeighbors + 1

    if ((currR != maxR) and (currC != 0)): #checks south west
        if (twoD[currR + 1][currC - 1] >= 1):
            numOfNeighbors = numOfNeighbors + 1

    if (currC != 0): #checks west
        if (twoD[currR][currC - 1] >= 1):
            numOfNeighbors = numOfNeighbors + 1

    if ((currC != 0) and (currR != 0)): #checks north west
        if (twoD[currR - 1][currC - 1] >= 1):
            numOfNeighbors = numOfNeighbors + 1

    if (currR != 0): #checks north
        if (twoD[currR - 1][currC] >= 1):
            numOfNeighbors = numOfNeighbors + 1

    if ((currR != 0) and (currC != maxC)): # checks north east
        if (twoD[currR - 1][currC + 1] >= 1):
            numOfNeighbors = numOfNeighbors + 1

    return(numOfNeighbors)

#ENDS aroundTheBlock function

def infectTheBlock(currR, currC, twoD):

    maxC = 46
    maxR = 46

    if (currC != maxC): #checks east
        if (twoD[currR][currC + 1] >= 1):
            twoD[currR][currC + 1] = 2

    if ((currC != maxC) and (currR != maxR)): #checkst south east
        if (twoD[currR + 1][currC + 1] >= 1):
            twoD[currR + 1][currC + 1] = 2

    if (currR != maxR): # checks south
        if (twoD[currR + 1][currC] >= 1):
            twoD[currR + 1][currC] = 2

    if ((currR != maxR) and (currC != 0)): #checks south west
        if (twoD[currR + 1][currC - 1] >= 1):
            twoD[currR + 1][currC - 1] = 2

    if (currC != 0): #checks west
        if (twoD[currR][currC - 1] >= 1):
            twoD[currR][currC - 1] = 2

    if ((currC != 0) and (currR != 0)): #checks north west
        if (twoD[currR - 1][currC - 1] >= 1):
            twoD[currR - 1][currC - 1] = 2

    if (currR != 0): #checks north
        if (twoD[currR - 1][currC] >= 1):
            twoD[currR - 1][currC] = 2

    if ((currR != 0) and (currC != maxC)): # checks north east
        if (twoD[currR - 1][currC + 1] >= 1):
            twoD[currR - 1][currC + 1] = 2

    return(twoD)

#ENDS infectTheBlock function

def aroundTheBoard(boardATB):

    rowATB = 0
    colATB = 0
    neighborsATB = 0

    for rowATB in range(0, 47):
        for colATB in range(0, 47):

            neighborsATB = 0
            aroundTheBlock(rowATB, colATB, boardATB, neighborsATB)

            if(neighborsATB < 2): #//Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                boardATB[rowATB][colATB] = 0
            else:
                if((2 <= neighborsATB) and (neighborsATB <= 3)): #Any live cell with two or three live neighbours lives on to the next generation.

                    if((boardATB[rowATB][colATB] == 0) and (neighborsATB == 3)): #Any dead cell with three live neighbors becomes a live cell.
                        boardATB[rowATB][colATB] = 1

                    else:
                        if (neighborsATB >= 4): #Any live cell with more than three live neighbours dies, as if by overpopulation.
                            boardATB[rowATB][colATB] = 0;
                        else:
                            boardATB[rowATB][colATB] = 0;
            #ENDS if statement
        #ENDS inner for loop
    #ENDS outer for loop
    return (boardATB)
#ENDS aroundTheBoard function

def makeAll0():
    row0, col0 = (47, 47)
    board0 = [[0 for i in range(col0)] for j in range(row0)]  # initiates board as a 47 x 47

    return(board0)
#ENDS makeAll0 function

def assign1s(board, charS):

    decide = 0
    rowA = 47
    colA = 47

    board = [[0 for i in range(colA)] for j in range(rowA)]  # initiates board as a 47 x 47

    rowA = 0
    colA = 0

    if(charS == 'r'):
        for rowA in range(0, 47): #goes to 47
            for colA in range(0,47):
                decide = random.choice([0,1])

                board[rowA][colA] = decide

                #ends inner for loop
        #ends out for loop
    elif(charS == 'd'):
        # PENTADECALATHON
        board[4][5] = 1
        board[5][5] = 1
        board[6][4] = 1
        board[6][6] = 1
        board[7][5] = 1
        board[8][5] = 1
        board[9][5] = 1
        board[10][5] = 1
        board[11][4] = 1
        board[11][6] = 1
        board[12][5] = 1
        board[13][5] = 1
    elif (charS == 'p'):
        # PULSAR
        board[3][4] = 1;
        board[3][5] = 1;
        board[3][6] = 1;
        board[3][10] = 1;
        board[3][11] = 1;
        board[3][12] = 1;

        board[5][2] = 1;
        board[5][7] = 1;
        board[5][9] = 1;
        board[5][14] = 1;

        board[6][2] = 1;
        board[6][7] = 1;
        board[6][9] = 1;
        board[6][14] = 1;

        board[7][2] = 1;
        board[7][7] = 1;
        board[7][9] = 1;
        board[7][14] = 1;

        board[8][4] = 1;
        board[8][5] = 1;
        board[8][6] = 1;
        board[8][10] = 1;
        board[8][11] = 1;
        board[8][12] = 1;

        board[10][4] = 1;
        board[10][5] = 1;
        board[10][6] = 1;
        board[10][10] = 1;
        board[10][11] = 1;
        board[10][12] = 1;

        board[11][2] = 1;
        board[11][7] = 1;
        board[11][9] = 1;
        board[11][14] = 1;

        board[12][2] = 1;
        board[12][7] = 1;
        board[12][9] = 1;
        board[12][14] = 1;

        board[13][2] = 1;
        board[13][7] = 1;
        board[13][9] = 1;
        board[13][14] = 1;

        board[15][4] = 1;
        board[15][5] = 1;
        board[15][6] = 1;
        board[15][10] = 1;
        board[15][11] = 1;
        board[15][12] = 1;
    elif (charS == 'g'):# Gos gun glider

        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    elif((charS == 's') or (charS == 'n')):
        for rowA in range(0, 47):  # goes to 47
            for colA in range(0, 47):
                decide = random.choice([0,1,2,3,4,5,6,7,8,9])

                if(0 <= decide <= 3):
                    board[rowA][colA] = 0
                elif(4 <= decide <= 6):
                    board[rowA][colA] = 1
                elif(7 <= decide <= 9):
                    board[rowA][colA] = 2
    elif (charS == 'b'):
        for rowA in range(0, 47): #goes to 47
            for colA in range(0,47):
                decide = random.choice([0,1])

                board[rowA][colA] = decide
        for x in range(0,5):
            decideR = random.randint(0,47)
            decideC = random.randint(0,47)
            board[decideR][decideC] = 2


    else:#does random if any other key is pressed
        for rowA in range(0, 47):  # goes to 47
            for colA in range(0, 47):
                decide = random.choice([0, 1])

                board[rowA][colA] = decide

                # ends inner for loop
        # ends out for loop

    return(board)

#ENDS assign1s functions

def makeNextGen(board1, board2, rules):

    rowN = 0
    colN = 0
    neighborsN = 0
    decideM = 0


    for rowN in range(0, 47):
        for colN in range(0, 47):
            neighborsN = aroundTheBlock(rowN, colN, board1)

            # RULES SET
            if ((board1[rowN][colN] == 1) and (neighborsN < 2)):  # Any live cell with fewer than two live neighbours dies
                board2[rowN][colN] = 0

            elif ((board1[rowN][colN] >= 1) and (2 <= neighborsN) and (neighborsN <= 3)):  # Any live cell with two or three live neighbours lives
                if((board1[rowN][colN] == 1)):
                    board2[rowN][colN] = 1 #if the person was not already infected
                else:
                    board2[rowN][colN] = 2 #if the person was already infected

            elif ((board1[rowN][colN] == 1) and (neighborsN > 3)):  # Any live cell with more than three live neighbours dies
                board2[rowN][colN] = 0

            elif ((board1[rowN][colN] == 0) and (neighborsN == 3)):  # Any dead cell with exactly three live neighbours becomes a live cell
                board2[rowN][colN] = 1
            # ENDS if statements

    #ends Original rules
    if(rules == 1):

        for rowN in range(0, 47):
            for colN in range(0, 47):
                if (board2[rowN][colN] == 2):
                    decideM = random.choice([0,1,2,3,4,5,6,7,8,9])

                    if(0 <= decideM <= 7): #turn the neighbors into infected 80% of the time
                        board2 = infectTheBlock(rowN, colN, board2)

        #ends outer for loop
    elif(rules == 2):
        for rowN in range(0, 47):
            for colN in range(0, 47):
                if (board2[rowN][colN] == 2):
                    decideM = random.choice([0,1,2,3,4,5,6,7,8,9])

                    if(7 <= decideM <= 9): #turn the neighbors into infected 30% of the time
                        board2 = infectTheBlock(rowN, colN, board2)

    elif (rules == 3):
        for rowN in range(0, 47):
            for colN in range(0, 47):
                if (board2[rowN][colN] == 2):
                    decideM = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

                    if (0 <= decideM <= 9):  # turn the neighbors into infected 100% of the time
                        board2 = infectTheBlock(rowN, colN, board2)
    # ends infected rules

    return(board2)
#ENDS makeNextGen function

def wait4User():
    retVal = 'r'
    vari = True
    while vari:
        for event in pygame.event.get():
            #key = pygame.key.get_pressed()
            if ((event.type == KEYDOWN) and ((event.key == K_d) or (event.key == K_p) or (event.key == K_g) or (event.key == K_r) or (event.key == K_s) or (event.key == K_n))):
                if((event.key == K_d)):
                    retVal = 'd'
                    return (retVal)
                if(event.key == K_p):
                    retVal = 'p'
                    return (retVal)
                if (event.key == K_g):
                    retVal = 'g'
                    return (retVal)
                if (event.key == K_r):
                    retVal = 'r'
                    return (retVal)
                if (event.key == K_s):
                    retVal = 's'
                    return (retVal)
                if (event.key == K_n):
                    retVal = 'n'
                    return (retVal)

#Ends the wait for user function



def main():
    sqrsize = 15

    row, col = (47, 47)
    board = [[0 for i in range(col)] for j in range(row)]  # initiates board as a 47 x 47
    board2 = [[0 for i in range(col)] for j in range(row)]  # initiates board as a 47 x 47

    OGgameRules = 0

    pygame.init()

    board = assign1s(board, 'r')

    #Local Variables
    canvas=pygame.display.set_mode((700,700),0,32)

    WHITE=(255,255,255)
    DEAD = (204,102,0)
    ALIVE = (0,0,204)
    INFECTED = (255,0,0)

    canvas.fill(WHITE)

    while True:

        #This cluster of code updates the colors on the table
        rowP = -1
        colP = -1
        for y in range(0, 700, sqrsize):
            colP = colP + 1
            rowP = -1
            for x in range(0, 700, sqrsize):
                rowP = rowP + 1
                if (board[colP][rowP] == 1):
                    pygame.draw.rect(canvas, ALIVE, (x, y, sqrsize, sqrsize))
                elif(board[colP][rowP] == 0):
                    pygame.draw.rect(canvas, DEAD, (x, y, sqrsize, sqrsize))
                else:
                    pygame.draw.rect(canvas, INFECTED, (x, y, sqrsize, sqrsize))

        #This cluster of code draws the borders
        rowP = -1
        colP = -1
        for y in range(0, 700, sqrsize):
            for x in range(0, 700, sqrsize):
                    pygame.draw.rect(canvas, (0,0,0), (x, y, sqrsize, sqrsize), 1)


        time.sleep(0.20)

        board = makeNextGen(board, board2, OGgameRules)

        board2 = makeAll0()



        for event in pygame.event.get():
            if (event.type==QUIT):
                pygame.quit()
                sys.exit()

        keyb = pygame.key.get_pressed()
        if(keyb[K_p]):
            board = assign1s(board, 'p')
            OGgameRules = 0
        elif(keyb[K_r]):
            board = assign1s(board, 'r')
            OGgameRules = 0
        elif (keyb[K_d]):
            board = assign1s(board, 'd')
            OGgameRules = 0
        elif (keyb[K_g]):
            board = assign1s(board, 'g')
            OGgameRules = 0
        elif (keyb[K_s]):
            board = assign1s(board, 's')
            OGgameRules = 2
        elif (keyb[K_n]):
            board = assign1s(board, 'n')
            OGgameRules = 1
        elif (keyb[K_b]):
            board = assign1s(board, 'b')
            OGgameRules = 3

        pygame.display.update()

main()
