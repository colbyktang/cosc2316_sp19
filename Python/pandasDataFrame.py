import pandas as pd

lst = ['John', 'Sam', 'Jack', 'are', 'always', 'good', 'friends']
data = {
        'Age':[20,21,19,18],
        'Name': ['Tom', 'nick', 'krish', 'Jack'],
        'City': ['Austin', 'San Antonio', 'Houston', 'Dallas'],
        'Qualification': ['Ready','Good','Excellent','Amazing']
        }

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col="Name")

first = data["Age"]

print (first)


#df = pd.DataFrame(lst)
#df = pd.DataFrame(data)
#print(df[['Name','Qualification']])
