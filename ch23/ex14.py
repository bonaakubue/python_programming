# DataFrame
import pandas as pd
data = {'name': ['Ann', 'Steve', 'Mary'], 'score':[77, 88, 93]}
df = pd.DataFrame(data)
print(df)

# dataframes using lists
data = [['Ann', 77],['Steve', 88],['Mary', 93]]
df = pd.DataFrame(data, columns=['name', 'score'])
print(df)
