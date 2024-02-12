#pandas

import pandas as pd

# series
data = [1,2,3,4,5]

series = pd.Series(data)
print(series)

# assigning names to series
data = [1,2,3,4,5]
series = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'], name='Numbers')
print(series)

# dictionaries in series

data = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
series = pd.Series(data, name='Numbers')
print(series)
