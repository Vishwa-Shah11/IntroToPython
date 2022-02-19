def rotate(mat):
    
    row = len(mat)
    col = len(mat[0])
    
    for i in range(col):
        for j in range(row-1,-1,-1):
            if (j != 0):
              print(mat[j][i], end = ',')
            if (j == 0):
              print(mat[j][i], end = '')
        print()
   
rotate([[1,2,3], [4,5,6]])
rotate([[1,2], [3,4], [5,6]])
rotate([[1,2,3], [4,5,6], [7,8,9]])
rotate([[1,2], [3,4], [5,6], [7,8]])
rotate([[1,2,3,4], [5,6,7,8]])
rotate([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
rotate([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]])