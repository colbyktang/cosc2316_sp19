import numpy as np

def multiplyMatrix (X, Y):
    
    result = [0] * 2 
    for index in range(2):
        result[index] = [0] * 2

    for i in range(2):
        for j in range(2):
            for k in range(3):
                result[i][j] += X[i][k] * Y[k][j]
    print ("\n" + "Code Result: " +  str(result))

# test case
m1 = [[1,2,3],[4,5,6]]
m2 = [[7,8],[9,10],[11,12]]

cx = np.matrix(m1)
cy = np.matrix(m2)

print ("\nCorrect Solution: \n" + str(cx * cy))
multiplyMatrix (m1, m2)
