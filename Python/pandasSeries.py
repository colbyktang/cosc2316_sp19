import pandas as pd
import numpy as np

# Program to create series with scalar values
Data = [1,3,4, 5, 6, 2, 9] #Numeric Data

# Creating series with default index values
a = pd.Series(Data)
print (a)

# predefined index values
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Creating series with predefined index values
ai = pd.Series(Data, Index)
print (ai)

dictionary = {'a': 0., 'b': 1., 'c' : 2.}
s = pd.Series(dictionary)
print(s)

data1 = {'a' : 0., 'b' : 1., 'c' : 2.}
sm = pd.Series(data1, index=['b','c','d','a'])

# Program to create ndarray series
Data2 = [[2, 3, 4], [5, 6, 7]] # Defining 2darray

# Creating series of 2darray
snd = pd.Series(Data2)
print (snd)
