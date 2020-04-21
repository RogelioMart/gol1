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
				printf("_");
			}
			else
			{
				printf("%d", board[r][c]);
			}
			
        }//end for loop of column
        
		printf("\n");
		
    }//ends for loop of row
	
	printf("\n\n\n");
	
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

int main()
{

	

	int **checker;	
											//row, columns
	checker = initArray(checker, 30, 30);
	
	checker = assign1s(checker, 29, 29);
	
	printf("Gen 0\n");
	printBoard(checker, 29, 29); //board must always be 1 smaller for rows and columns
	
	int loopy = 1;
    do
	{
		
		printf("Gen %d\n", loopy);
		
		//aroundTheBoard(int **board, int maxR, int maxC)
		checker = aroundTheBoard(checker, 29, 29);
		
		printBoard(checker, 29, 29);
		
		//loopy = loopy + 1;
		
		sleep(1);
		
	}while(loopy < 11);

	
    return 0;
}
