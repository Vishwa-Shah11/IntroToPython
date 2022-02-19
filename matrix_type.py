def diagonal(M):
    mtype = 'diagonal'
    flag1 = True
    
    for i in range(len(M)):
        if (M[i][i] == 0):
            flag1 = False
            mtype = 'non-diagonal'
            break 
    if flag1 == True:
        for i in range(len(M)):
            if flag1 == True:
                for j in range(len(M)):
                    if (i != j):
                        if (M[i][j] != 0):
                            flag1 = False
                            mtype = 'non-diagonal'
                            break
    return mtype
    

def matrix_type(M):
    mtype1 = ''
    def scalar(M):
        mtype = ''
        flag2 = False
        value = M[0][0]
        if (diagonal(M) == 'diagonal'):
            flag2 = True
            for i in range(len(M)):
                if (M[i][i] != value):
                    flag2 = False
                    break
        if flag2 == True:
            mtype = 'scalar'
        else:
            mtype = 'non-diagonal'
        return mtype

    if (scalar(M) == 'scalar' and M[0][0] == 1):
        mtype1 = 'identity'
    else:
        mtype1 = 'non-diagonal'
    return mtype1
  
m = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m1 = [[1, 2, 5], [2, 3, 5], [1, 4, 9]]
print(matrix_type(m1))