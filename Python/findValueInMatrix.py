
def searchMatrix(mat, n, x):

    #index = mat[0][len(mat[0]) - 1]
    i = 0
    j = n -1
    while ( i < n and j >= 0 ):
        if (mat[i][j] == x):
            print ("n found at ", i, ",", j)
            return 1

        if (mat[i][j] > x):
            j -=1
        else:
            i+= 1
            print ("Element not found")
            return 0

matrix = [[10,20,30,40],[15,25,35,45],[21,29,37,48],[32,33,39,50]]
searchMatrix (matrix, len(matrix), 29)
