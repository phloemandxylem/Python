# Exploring dataframes with Pandas-----------------------------------------------------
# Print the head of data to expose the first few rows.
print(homelessness.head())

# Print information about the data showing columns, data types, and number of missing values.
print(homelessness.shape)

# Print a description of the data that calculates a few summary statistics for each column
print(homelessness.describe())

# Import pandas using alias 
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.column)

# Print the row index of homelessness
print(homelessness.index)
