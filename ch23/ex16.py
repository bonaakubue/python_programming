# Assigning values in a DataFrame

import pandas as pd

df = pd.read_csv('employment.csv')

# # Assigning a value to entire 'Subject' column
# df['Subject'] = "Languages"

# # Assigning a row using iloc
# df.iloc[2] = "Nothing to show"

# # Assigning values based on conditions
# df.loc[df['Scores'] > 69, 'Student'] = "A"

# # Performing arithmetic assignment
# df['Score'] = df['Score'] + 10

# Sorting Data
result = df.sort_values('Period')
print(result)

# descending order
result = df.sort_values('Period', ascending=False)
print(result)

# Data Cleaning Functions

cleaned_df = df.dropna()
print(cleaned_df)

result = df.fillna('Nothing to show')
print(result)

# remove duplicates
result = df.drop_duplicates()
print(result)
