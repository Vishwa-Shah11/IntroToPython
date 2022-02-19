#import numpy

def transpose(mat):
    row = len(mat)
    col = len(mat[0])
    t_mat = [[0]*row]*col

    for i in range(row):
        #print(i)
        for j in range(col):
            #print(j)
            #t_mat.append(mat[i][j])
            t_mat[j][i] = mat[i][j]
    #print(t_mat)
    return t_mat
    #return numpy.transpose(mat)

print(transpose([[1,2],[3,4],[5,6]]))
print(transpose([(1,2,3),(4,5,6),(7,8,9),(10,11,12)]))