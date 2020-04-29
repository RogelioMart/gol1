import time
import random
from tkinter import *


rootWin = Tk()

w = Canvas(rootWin, width=700, height=700)
w.pack()

mcolor = "white"
sqrsize = 20

row,col = (35, 35)
board = [[0 for i in range(col)] for j in range(row)] # initiates board as a 47 x 47
board2 = [[0 for i in range(col)] for j in range(row)] # initiates board as a 47 x 47

def aroundTheBlock(currR, currC, twoD):

    numOfNeighbors = 0

    maxC = 34
    maxR = 34

    if (currC != maxC): #checks east
        if (twoD[currR][currC + 1] == 1):
            numOfNeighbors = numOfNeighbors + 1

    if ((currC != maxC) and (currR != maxR)): #checkst south east
        if (twoD[currR + 1][currC + 1] == 1):
            numOfNeighbors = numOfNeighbors + 1

    if (currR != maxR): # checks south
        if (twoD[currR + 1][currC] == 1):
            numOfNeighbors = numOfNeighbors + 1

    if ((currR != maxR) and (currC != 0)): #checks south west
        if (twoD[currR + 1][currC - 1] == 1):
            numOfNeighbors = numOfNeighbors + 1

    if (currC != 0): #checks west
        if (twoD[currR][currC - 1] == 1):
            numOfNeighbors = numOfNeighbors + 1

    if ((currC != 0) and (currR != 0)): #checks north west
        if (twoD[currR - 1][currC - 1] == 1):
            numOfNeighbors = numOfNeighbors + 1

    if (currR != 0): #checks north
        if (twoD[currR - 1][currC] == 1):
            numOfNeighbors = numOfNeighbors + 1

    if ((currR != 0) and (currC != maxC)): # checks north east
        if (twoD[currR - 1][currC + 1] == 1):
            numOfNeighbors = numOfNeighbors + 1

    return(numOfNeighbors)

#ENDS aroundTheBlock function

def aroundTheBoard(boardATB):

    rowATB = 0
    colATB = 0
    neighborsATB = 0

    for rowATB in range(0, 35):
        for colATB in range(0, 35):

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
    row0, col0 = (35, 35)
    board0 = [[0 for i in range(col0)] for j in range(row0)]  # initiates board as a 47 x 47

    return(board0)
#ENDS makeAll0 function

def assign1s(board):

    decide = 0
    rowA = 0
    colA = 0

    for rowA in range(0, 35): #goes to 47
        for colA in range(0,35):
            decide = random.choice([0,1])

            board[rowA][colA] = decide

            #ends inner for loop
    #ends out for loop

    return(board)

#ENDS assign1s functions

def makeNextGen(board1, board2):

    rowN = 0
    colN = 0
    neighborsN = 0

    for rowN in range(0, 35):
        for colN in range(0, 35):
            neighborsN = aroundTheBlock(rowN, colN, board1)

            #RULES SET
            if ((board1[rowN][colN] == 1) and (neighborsN < 2)): #Any live cell with fewer than two live neighbours dies
                board2[rowN][colN] = 0

            elif ((board1[rowN][colN] == 1) and (2 <= neighborsN) and (neighborsN <= 3)): # Any live cell with two or three live neighbours lives
                board2[rowN][colN] = 1

            elif ((board1[rowN][colN] == 1) and (neighborsN > 3)): # Any live cell with more than three live neighbours dies
                board2[rowN][colN] = 0

            elif ((board1[rowN][colN] == 0) and (neighborsN == 3)): #Any dead cell with exactly three live neighbours becomes a live cell
                board2[rowN][colN] = 1
            #ENDS if statements
    return(board2)
#ENDS makeNextGen function

#CONSIDER THIS YOUR MAIN

 #PENTADECALATHON
board[4][5] = 1;
board[5][5] = 1;
board[6][4] = 1;
board[6][6] = 1;
board[7][5] = 1;
board[8][5] = 1;
board[9][5] = 1;
board[10][5] = 1;
board[11][4] = 1;
board[11][6] = 1;
board[12][5] = 1;
board[13][5] = 1;


''' # PULSAR
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
'''


#board = assign1s(board)

''' # Gos gun glider
board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
'''

rowP = 0
colP = 0

while True:

    rowP = -1
    colP = -1

    #you got a 47 x 47 grid here
    for y in range (0, 700, sqrsize):

        colP = colP + 1
        rowP = -1

        for x in range (0, 700, sqrsize):

            rowP = rowP + 1

            if(board[colP][rowP] == 1):
                mcolor = "red"
            else:
                mcolor = "blue"

            w.create_rectangle(x, y, (x + sqrsize), (y + sqrsize), fill = mcolor);



    #time.sleep(0.25)

    board = makeNextGen(board, board2)

    board2 = makeAll0()

    w.update_idletasks()
    w.update()
    #mainloop();



# you want a gosper glider gun
