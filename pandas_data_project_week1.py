## reading a csv into a dataframe PANDAS
df = pd.read_csv('foodhub_order.csv')
# returns the first 5 rows
df.head()

## Checking the number of rows and columns 
df.shape

## Check the datatype of the csv
df.info()
