#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int aroundTheBlock(int currR, int currC, int **twoD, int maxR, int maxC)
{
    int numOfNeighbors = 0;
    
    if(currC != maxC)//checks east
    {
        if(twoD[currR][currC + 1] == 1)
            numOfNeighbors = numOfNeighbors + 1;
    }
    if((currC != maxC) && (currR != maxR)) // checks south east
    {
        if(twoD[currR + 1][currC + 1] == 1)
            numOfNeighbors = numOfNeighbors + 1;
    }
    if(currR != maxR) // checks south
    {
        if(twoD[currR + 1][currC] == 1)
            numOfNeighbors = numOfNeighbors + 1;
    }
    if((currR != maxR) && (currC != 0)) // checks south west
    {
        if(twoD[currR + 1][currC - 1] == 1)
            numOfNeighbors = numOfNeighbors + 1;
    }
    if(currC != 0) // checks west
    {
        if(twoD[currR][currC - 1] == 1)
            numOfNeighbors = numOfNeighbors + 1;
    }
    if((currC != 0) && (currR != 0)) // checks north west
    {
        if(twoD[currR - 1][currC - 1] == 1)
            numOfNeighbors = numOfNeighbors + 1;
    }
    if(currR != 0) // checks north
    {
        if(twoD[currR - 1][currC] == 1)
            numOfNeighbors = numOfNeighbors + 1;
    }
    if( (currR != 0) && (currC != maxC))// checks north east
    {
        if(twoD[currR - 1][currC + 1] == 1)
            numOfNeighbors = numOfNeighbors + 1;
    }
    
	//printf("on r: %d c: %d neighbors = %d\n\n", currR, currC, numOfNeighbors);//DEBUGGING
	
    return(numOfNeighbors);
}

int **aroundTheBoard(int **board, int maxR, int maxC)
{
    int r = 0;
    int c = 0;
    int neighbors = 0;
    
    for(r = 0; r <= maxR; r++)
    {
     
        for(c = 0; c <= maxC; c++)
        {
            neighbors = 0;
            
            neighbors = aroundTheBlock(r, c, board, maxR, maxC);
            
            //RULE SET
            if(neighbors < 2) //Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            {
                board[r][c] = 0;
            }
            else
            {
                if((2 <= neighbors) && (neighbors <= 3)) // Any live cell with two or three live neighbours lives on to the next generation.
                {
                   if((board[r][c] == 0) && (neighbors == 3)) //Any dead cell with three live neighbors becomes a live cell.
				   {
					   board[r][c] = 1;
				   }
                }
				else
				{
					if(neighbors >= 4)//Any live cell with more than three live neighbours dies, as if by overpopulation.
					{
					   board[r][c] = 0;
					}
					else
					{
						board[r][c] = 0;
					}
				}
            }//ends if statement rule set
            
        }//end for loop of column
        
    }//ends for loop of row
	
	return(board);
	
}

int printBoard(int ** board, int maxR, int maxC)
{
	
	int r = 0;
    int c = 0;
    
    for(r = 0; r <= maxR; r++)
    {
     
        for(c = 0; c <= maxC; c++)
        {
			
			if(board[r][c] == 0)
			{
				printf("%c", 176);
			}
			else
			{
				printf("%c", 178);
			}
			
        }//end for loop of column
        
		printf("\n");
		
    }//ends for loop of row
	
	printf("\n\n");
	
	return(0);
}

int **initArray(int **board, int maxR, int maxC)
{
	int i = 0;
	int j = 0;
	        //[row] [column]// 2,4 2,5 3,4
	board = (int**)malloc(maxR * sizeof(int*));
	for(i = 0; i < maxR; i++)
	{
		board[i] = (int*)malloc (maxC* sizeof(int));
	}

	for(i = 0; i < maxR; i++)
	{
		for(j = 0; j < maxC; j++)
		{
			board[i][j] = 0;
		}
	}

	return(board);
}

int ** makeAll0(/*int **board,*/ int maxR, int maxC)
{
	
	int i = 0;
	int j = 0;
	
	int **board;
	
	board = (int**)malloc(maxR * sizeof(int*));
	
	for(i = 0; i < maxR; i++)
	{
		board[i] = (int*)malloc (maxC* sizeof(int));
	}
	
	for(i = 0; i < maxR; i++)
	{
		for(j = 0; j < maxC; j++)
		{
			board[i][j] = 0;
		}
	}

	return(board);
	
}

int **assign1s(int **board, int maxR, int maxC)
{
	
	time_t t;
	srand(time(&t));
	
	int decide;
	
	int r = 0;
	int c = 0;
	
	for(r = 0; r <= maxR; r++)
	{
		for(c = 0; c <= maxC; c++)
		{
			
			//decide = (rand() % (max - min + 1) ) + min;
			decide = (rand() % (100 - 0 + 1) ) + 0;
			
			if( decide % 10 == 0  )
			{
				board[r][c] = 1;
			}
			
		}//loop for column
		
	}//loop for row
	
	return(board);
	
}

int **makeNextGen(int **board1, int **board2, int maxR, int maxC)
{
	
	int r = 0;
    int c = 0;
    int neighbors = 0;
	
	for(r = 0; r <= maxR; r++)
    {
     
        for(c = 0; c <= maxC; c++)
        {
            neighbors = 0;
            
            neighbors = aroundTheBlock(r, c, board1, maxR, maxC);
            
            //RULE SET
            if((board1[r][c] == 1) && (neighbors < 2)) //Any live cell with fewer than two live neighbours dies
			{
				board2[r][c] = 0;
			}
			else if ((board1[r][c] == 1) && ( 2 <= neighbors) && (neighbors <= 3))//Any live cell with two or three live neighbours lives
			{
				board2[r][c] = 1;
			}
            else if((board1[r][c] == 1) && (neighbors > 3 ))//Any live cell with more than three live neighbours dies
			{
				board2[r][c] = 0;
			}
			else if((board1[r][c] == 0) && (neighbors == 3))//Any dead cell with exactly three live neighbours becomes a live cell
			{
				board2[r][c] = 1;
			}
			
        }//end for loop of column
        
    }//ends for loop of row
	
	return(board2);
	
}

/*
	if you plan to turn this in add 
	more shapes to use 
	add a select funciton for those shapes
	modify your current shapes to have them move in different places
 */

int main()
{
	
	//Initiates all the appropriate variables and arrays.
	int initRow = 18;//45
	int initCol = 18;//90
	int pRow = initRow - 1;
	int pCol = initCol - 1;

	int **checker;
	int **checker2;

	checker = initArray(checker, initRow, initCol);
	checker2 = initArray(checker2, initRow, initCol);
	
	//OPTIONS FOR BOARD PATTERN
	
	//checker = assign1s(checker, pRow, pCol);//DOES RANDOMLY
	
	
	//TO MAKE THE PULSAR 18x18
	{
	checker[3][4] = 1;
	checker[3][5] = 1;
	checker[3][6] = 1;
	checker[3][10] = 1;
	checker[3][11] = 1;
	checker[3][12] = 1;
	
	checker[5][2] = 1;
	checker[5][7] = 1;
	checker[5][9] = 1;
	checker[5][14] = 1;
	
	checker[6][2] = 1;
	checker[6][7] = 1;
	checker[6][9] = 1;
	checker[6][14] = 1;
	
	checker[7][2] = 1;
	checker[7][7] = 1;
	checker[7][9] = 1;
	checker[7][14] = 1;
	
	checker[8][4] = 1;
	checker[8][5] = 1;
	checker[8][6] = 1;
	checker[8][10] = 1;
	checker[8][11] = 1;
	checker[8][12] = 1;
	
	checker[10][4] = 1;
	checker[10][5] = 1;
	checker[10][6] = 1;
	checker[10][10] = 1;
	checker[10][11] = 1;
	checker[10][12] = 1;
	
	checker[11][2] = 1;
	checker[11][7] = 1;
	checker[11][9] = 1;
	checker[11][14] = 1;
	
	checker[12][2] = 1;
	checker[12][7] = 1;
	checker[12][9] = 1;
	checker[12][14] = 1;
	
	checker[13][2] = 1;
	checker[13][7] = 1;
	checker[13][9] = 1;
	checker[13][14] = 1;
	
	checker[15][4] = 1;
	checker[15][5] = 1;
	checker[15][6] = 1;
	checker[15][10] = 1;
	checker[15][11] = 1;
	checker[15][12] = 1;
	}
	
	
	/*//pentadecalathon //best with R=18 & C=11 
	{		  //R  C
		checker[4][5] = 1;
		checker[5][5] = 1;
		checker[6][4] = 1;
		checker[6][6] = 1;
		checker[7][5] = 1;
		checker[8][5] = 1;
		checker[9][5] = 1;
		checker[10][5] = 1;
		checker[11][4] = 1;
		checker[11][6] = 1;
		checker[12][5] = 1;
		checker[13][5] = 1;
	}
	*/
	
	printf("Gen 0\n");
	printBoard(checker, pRow, pCol); //board must always be 1 smaller for rows and columns
	
	//printf("1\n");//DEBUGGING
	system("cls");
	int loopy = 1;
    do
	{
		
		printf("Gen %d\n", loopy);
		
		//aroundTheBoard(int **board, int maxR, int maxC)
		//checker = aroundTheBoard(checker, pRow, pCol);
		
		checker = makeNextGen(checker, checker2, pRow, pCol);
		
		printBoard(checker, pRow, pCol);
		
		checker2 = makeAll0(initRow, initCol);
		
		loopy = loopy + 1;
		
		sleep(0.75);
		
		system("cls");
		
	}while(loopy < 1000);

	
    return 0;
}
