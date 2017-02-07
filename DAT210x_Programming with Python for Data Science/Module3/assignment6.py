import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_table('Datasets/wheat.data',sep=',')

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 
# .. your code here ..
df = df.drop('id',1)
## df = df.drop('wheat_type',1)
#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
matr = df.corr()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.imshow(matr, cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks=[i for i in range(len(df.columns))]
plt.xticks(tick_marks,df.columns)
plt.yticks(tick_marks,df.columns)

plt.show()


