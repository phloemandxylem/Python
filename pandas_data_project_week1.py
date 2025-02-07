## reading a csv into a dataframe PANDAS
df = pd.read_csv('foodhub_order.csv')
# returns the first 5 rows
df.head()

## checking the number of rows and columns 
df.shape

## check the datatype of the csv
df.info()

## check the missing values
missing_values=df.isnull().sum()
print(missing_values)

## checking statistical values in pandas
min = df['food_preparation_time'].min()
mean = df['food_preparation_time'].mean()
max = df['food_preparation_time'].max()

print('Minimum time: ', min)
print('Average time: ', mean)
print('Maximum time: ', max)

## how many orders are not rated?
df['rating'].value_counts()

## create a histogram plot for univariate analysis
sns.histplot(df, x = 'cost_of_the_order', hue=df['day_of_the_week'], kde=True)

## What percentage of the orders cost more than 20 dollars? 
## 1. Count the elements within a column that > 20 dollars.
## 2. Find the total columns
## 3. Find the percentage for dividing #1 / #2 





