#include <stdio.h>
#include <stdlib.h>


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
    
    return(numOfNeighbors);
}

int **aroundTheBoard(int **board, int maxR, int maxC)
{
    int r = 0;
    int c = 0;
    int neighbors = 0;
    
    for(r = 0; r < maxR; r++)
    {
     
        for(c = 0; c < maxC; c++)
        {
            neighbors = 0;
            
            neighbors = aroundTheBlock(r, c, board, maxR, maxC);
            
            //RULE SET
            if((neighbors >= 2) && (neighbors < 4)) //(2 <= x < 4)
            {
                board[r][c] = 1;
            }
            else
            {
                if(neighbors >= 4)
                {
                    board[r][c] = 0;
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
			
			printf("%d ", board[r][c]);
			
        }//end for loop of column
        
		printf("\n");
		
    }//ends for loop of row
	
	printf("\n\n\n");
	
	return(0);
}

int main()
{
	int i = 0;
	int j = 0;
	        //[row] [column]// 2,4 2,5 3,4
	int **checker = (int**)malloc(8 * sizeof(int*));
	for(i = 0; i < 8; i++)
	{
		checker[i] = (int*)malloc (8 * sizeof(int));
	}
	
	for(i = 0; i < 8; i++)
	{
		for(j = 0; j < 8; j++)
		{
			checker[i][j] = 0;
		}
	}
	
	checker[2][4] = 1;
	checker[2][5] = 1;
	checker[3][4] = 1;
	
	printf("Gen 0\n");
	printBoard(checker, 7, 7);
	
	int loopy = 1;
    do
	{
		
		printf("Gen %d\n", loopy);
		
		//aroundTheBoard(int **board, int maxR, int maxC)
		checker = aroundTheBoard(checker, 7, 7);
		
		printBoard(checker, 7, 7);
		
		loopy = loopy + 1;
		
	}while(loopy < 1);

	
    return 0;
}
