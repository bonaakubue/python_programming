# Data Aggregation

import pandas as pd

df = pd.read_csv('employment.csv')

data = {
    'Student': ['Andrew', 'Jane', 'Eve', 'Andrew', 'Jane', 'Eve'],
    'Subject': ['Maths', 'Maths', 'Maths', 'English', 'English', 
'English'],
    'Score': [85, 78, 92, 64, 91, 76]
}

df = pd.DataFrame(data)

result = df.groupby('Student')['Score']

print(result.sum())
print(result.mean())
print(result.count())
