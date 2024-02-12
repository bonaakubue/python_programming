# Reading data from files

import pandas as pd

df = pd.read_csv('employment.csv')

# without header
df = pd.read_csv('employment.csv', header=None)

# head(), tail() and describe
df.head()
df.tail(3)
df.describe()

# Selecting Columns
result = df.Period
print(result)

# using square brackets
result = df[['Period', 'Magnitude']]
print(result)

# Selecting Rows

# Integer-based indexing using .iloc
#selecting the row at index 0
result = df.iloc[0]
print(result)

#selecting the rows with slicing
result = df.iloc[0:3]
print(result)

#selecting selected rows
result = df.iloc[[1,2,5]]
print(result)

#selecting a specific column
result = df.iloc[:, 0]
print(result)

#selecting a range of columns
result = df.iloc[:, 0:3]
print(result)

#selecting selected columns
result = df.iloc[:, [1,3,5]]
print(result)

#selecting rows and columns
result = df.iloc[0:10, 1:4]
print(result)

# Label based selection using .loc
#selecting the row at index label
result = df.loc['Name']
print(result)

#selecting selected rows
result = df.loc[['Name', 'Subject']]
print(result)

#selecting rows and columns
result = df.loc['Name', ['Subject', 'Period']]
print(result)


# Boolean indexing
#boolean indexing
result = df[df['Period'] > 2023]
print(result)

#the same thing as
result = df.loc[df['Period'] > 2023]
print(result)
