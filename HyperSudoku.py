
class HyperSudoku:

    @staticmethod
    def solve(grid):
        """
        Input: An 9x9 hyper-sudoku grid with numbers [0-9].
                0 means the spot has no number assigned.
                grid is a 2-Dimensional array. Look at
                Test.py to see how it's initialized.

        Output: A solution to the game (if one exists),
                in the same format. None of the initial
                numbers in the grid can be changed.
                'None' otherwise.
        """
    def solve(grid):
        
        if(HyperSudoku.solveSudoku(grid)):
            return grid
        else: 
            return None     
    
    @staticmethod
    def printGrid(grid):
        """
        Prints out the grid in a nice format. Feel free
        to change this if you need to, it will NOT be 
        used in marking. It is just to help you debug.
    
        Use as:     HyperSudoku.printGrid(grid)
        """
        print("-"*25)
        for i in range(9):
            print("|", end=" ")
            for j in range(9):
                print(grid[i][j], end=" ")
                if (j % 3 == 2):
                    print("|", end=" ")
            print()
            if (i % 3 == 2):
                print("-"*25)
    @staticmethod            
    def usedInRow(grid, row, num):
        for x in range(1,10):
            if(grid[row-1][x-1] == num):
                return True
        return False
    @staticmethod
    def usedInCol(grid, col , num):
        for x in range(1,10):
            if(grid[x-1][col-1] == num):
                return True
        return False
    @staticmethod
    def usedInHyperBox(grid, r, c, num):
        if r == -1:
            return False
        elif c == -1:
            return False
        else:
            if((2<=r<=4) and (2<=c<=4)):
                for x in range(2,5):
                    for y in range(2,5):
                        if(grid[x-1][y-1] == num):
                            return True
            elif((2<=r<=4) and (6<=c<=8)):        
                for x in range(2,5):
                    for y in range(6,9):
                        if(grid[x-1][y-1] == num):
                            return True
            elif((6<=r<=8) and (2<=c<=4)):
                for x in range(6,9):
                    for y in range(2,5):
                        if(grid[x-1][y-1] == num):
                            return True
            elif((6<=r<=8) and (6<=c<=8)):     
                for x in range(6,9):
                    for y in range(6,9):
                        if(grid[x-1][y-1] == num):
                            return True   
            return False
    @staticmethod
    def usedInBox(grid, boxStartRow, boxStartCol, num):
        for x in range(0,3):
            for y in range(0,3):
	
                if(grid[x + boxStartRow-1][y+boxStartCol-1] == num):
                    return True
        return False
    @staticmethod
    def noConflicts(grid, row, col, num):
        if col == 1 or col == 2 or col == 3:
            startcol=1
        elif col == 4 or col == 5 or col == 6:
            startcol=4
        else:
            startcol = 7
        if row == 1 or row == 2 or row == 3:
            startrow=1
        elif row == 4 or row == 5 or row == 6:
            startrow=4
        else:
            startrow = 7
        return ( not HyperSudoku.usedInRow(grid, row, num) and not HyperSudoku.usedInCol(grid, col, num)
                 and not HyperSudoku.usedInBox(grid, startrow, startcol, num) and not HyperSudoku.usedInHyperBox(grid, row, col, num))
    @staticmethod
    def findUnassignedLocation(grid):
        for x in range(1,10):
            for y in range(1,10):
                if(grid[x-1][y-1] == 0):
                    return (x, y, True)
        return(-1, -1, False)
    @staticmethod
    def solveSudoku(grid):
        (row, col, sol) = HyperSudoku.findUnassignedLocation(grid)
        if(sol is False):
            return(grid)
        for i in range(1,10):
            if(HyperSudoku.noConflicts(grid, row, col, i)):
                grid[row-1][col-1] = i
                if(HyperSudoku.solveSudoku(grid)):
                    return(grid)
                else:
                    grid[row-1][col-1] = 0
        return None
