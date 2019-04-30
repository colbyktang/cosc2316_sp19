import pandas as pd
s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])

print (s['a'])
print (s[['a','c','d']])
print (s[-3:])

