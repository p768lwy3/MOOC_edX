import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
df = pd.read_table('Datasets\servo.data',sep=',',names=['motor','screw','pgain','vgain','class'])

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
#print(df['vgain']==5) 
print(df.loc[df['vgain']==5]); print('There is ',df.loc[df['vgain']==5].shape[0],' rows.')

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
print(df.loc[(df['motor']=='E')&(df['screw']=='E')])
print('There is ',df.loc[(df['motor']=='E')&(df['screw']=='E')].shape[0],' rows.')
## The or and and python statements require truth-values. 
## For pandas these are considered ambiguous, so using "bitwise" | (or) or & (and) operations instead.
## and & has higher precedence than ==

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
df_pgain = df.loc[df['pgain']==4]; print('The mean is ',df_pgain['vgain'].mean(),'.')


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print(df_pgain.dtypes)


