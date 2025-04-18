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

# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals", ascending=False)

# Print the top few rows
print(homelessness_ind.head())

# Print homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])

print(homeless_reg_fam.head())

# Subsetting ---------------------------------------------------------------------------
#Subsetting columns
#Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

print(state_fam.head())

#Subsetting row values
# Filter for multiple row values
df2 = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

print(df2)







