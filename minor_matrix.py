def minor_matrix(M, i, j):
    """
    Compute the "minor matrix"

    Arguments:
        M: list of lists
        i: integer
        j: integer
    Return:
        M_ij: list of lists
    """
    #return [row[:j] + row[j+1:] for row in (M[:i]+M[i+1:])]
    M.pop(i)
    for k in M:
        k.pop(j)
    return M

m = [[1,2,3],[4,5,6],[7,8,9]]
print(minor_matrix(m,0,1))