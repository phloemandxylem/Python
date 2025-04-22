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
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True,False])

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

#Subsetting rows by categorical variables
#Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness
canu = ["California", "Arizona", "Nevada", "Utah"]
mojave_homelessness = homelessness[homelessness[homelessness["state"].isin(canu)]

print(mojave_homelessness)

#Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals] + homelessness["family_members"]
homelessness["p_homeless"] = homelessness["total"] / homelessness["state_pop"]

print(homelessness)

#Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]

#Subset rows for indiv_per_10k greater than 20
high_homelessness_srt = homelessness.sort_values(["indiv_per_10k"] > 20)

#From high_homelessness_art, select the state and indiv_per_10k cols
result = homelessness[["state", "indiv_per_10k"]]

#Print the head of the sales DataFrame
print(sales.head())

#Print the info about the sales DataFrame
print(sales.info())

#Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

#Print the median of weekly_sales
print(sales["weekly_sales"].median())


