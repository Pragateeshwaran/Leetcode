import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['X', 'Y', 'Z']})
df2 = pd.DataFrame({'A': [2, 3, 4], 'B': ['W', 'X', 'Y']})

# Merge them on column 'A' using an inner join
merged_df = df1.merge(df2, how='outer', on='B')

print(merged_df)
