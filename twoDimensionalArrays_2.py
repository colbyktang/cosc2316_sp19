from numpy import *
xList = [[4,8],[3,7]]
yList = [[1,0],[5,2]]
resultList = [[0,0],[0,0]]

for x in range(len(xList)):
    for y in range(len(yList)):
        resultList[x][y] = xList[x][y] + yList[x][y]
print (resultList)
