def is_magic(mat):
    """
    determine if a matrix is magic square

    Argument:
        mat: list of lists
    Return:
        string: 'YES' or 'NO'
    """
    rows = len(mat)
    cols = len(mat[0])

    for i in range(rows):
        rowSum = 0
        for j in range(cols):
            rowSum += mat[i][j]


    for i in range(rows):  
        columnSum = 0
        for j in range(cols):  
            columnSum += mat[j][i]


    principalDiagonalSum = 0
    secondaryDiagonalSum = 0

    for i in range(rows):
        for j in range(rows):
            if (i == j):
                principalDiagonalSum += mat[i][j]
            if ((i+j) == (rows-1)):
                secondaryDiagonalSum += mat[i][j]

    if (rowSum == columnSum == principalDiagonalSum == secondaryDiagonalSum):
        return 'YES'
    else:
        return 'NO'

is_magic([[4,9,2],[3,5,7],[8,1,6]])