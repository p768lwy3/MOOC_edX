import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2',header=1)
## Remark: This is a list of pandas, not a dataframe
df = df[0]
## So, convert list to dataframe

# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
# .. your code here ..
## print(df)
# drop column begin with player which is the header of html table
df = df[df.PLAYER != 'PLAYER']

# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
# .. your code here ..
## print(df.isnull().sum(axis=1))
df = df.dropna(axis=0,thresh=4)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
## print(df)

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop('RK',1)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
## print(pd.isnull(df.columns.values))


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..
## print(df.dtypes) ## not numeric...
df = df.apply(pd.to_numeric,errors='ignore')



# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..
print('The shape of dataframe is ',df.shape)
print('There is ',len(df.PCT.unique()),' unique PCT values exist in the table')
print('The value is ',df.GP[14]+df.GP[15])
