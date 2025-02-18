# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def solveSudo(SudoGrid):
    ''' hmm'''
    return 
def sumRow(SudoGrid, rowNum):
    rowNum = rowNum - 1
    row = SudoGrid[rowNum]
    print('row: ', row)
    return sum(row)

def sumCol(SudoGrid, colNum):
    colNum = colNum - 1
    col = [row[colNum] for row in SudoGrid]
    print('col: ', col)
    return sum(col)

def sumBox(SudoGrid, boxNum):
    if boxNum == 
    box = 

SudoGrid = [
    [0,8,3,0,0,2,4,1,0],
    [2,0,4,0,0,5,0,0,0], 
    [0,1,0,0,7,4,0,2,8],
    [3,0,0,4,9,0,1,5,0],
    [0,0,7,0,1,0,0,0,6],
    [9,0,0,7,5,3,0,8,0],
    [8,4,0,0,0,0,6,0,0],
    [5,0,0,0,4,0,0,3,1],
    [1,3,6,0,2,0,5,0,0]
    ]

print(SudoGrid)

print(sumRow(SudoGrid, 1))
print(sumCol(SudoGrid, 1))

SolvedSudoku = solveSudo(SudoGrid)
print('Solved Sudoku:', SolvedSudoku)
