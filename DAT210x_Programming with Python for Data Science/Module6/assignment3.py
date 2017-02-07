import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.svm import SVC

#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
# Load up the /Module6/Datasets/parkinsons.data data set into a variable X, being sure to drop the name column.
X = pd.read_csv('Datasets/parkinsons.data')
## print(X.head()); print(X.dtypes); print(X.isnull().sum())
X.drop(['name'], axis=1, inplace=True)

# Splice out the status column into a variable y and delete it from X.
y = X.status
X.drop(['status'], axis=1, inplace=True)

# Wait a second. Pull open the dataset's label file from: https://archive.ics.uci.edu/ml/datasets/Parkinsons
# Look at the units on those columns: Hz, %, Abs, dB, etc. What happened to transforming your data? With all of those units interacting with one another, some pre-processing is surely in order.
# Right after you preform the train/test split but before you train your model, inject SciKit-Learn's pre-processing code. Unless you have a good idea which one is going to work best, you're going to have to try the various pre-processors one at a time, checking to see if they improve your predictive accuracy.
# Experiment with Normalizer(), MaxAbsScaler(), MinMaxScaler(), KernelCenterer(), and StandardScaler().
# After trying all of these scalers, what is the new highest accuracy score you're able to achieve?
## T = X ## 0.915254237288
## T = preprocessing.Normalizer().fit_transform(X) ## 0.796610169492
## T = preprocessing.MaxAbsScaler().fit_transform(X) ## 0.881355932203
## T = preprocessing.MinMaxScaler().fit_transform(X) ## 0.881355932203
## T = preprocessing.KernelCenterer().fit_transform(X) ## 0.915254237288
T = preprocessing.StandardScaler().fit_transform(X) ## 0.932203389831

# Perform a train/test split. 30% test group size, with a random_state equal to 7.
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

best_score = 0

# The accuracy score keeps creeping upwards. Let's have one more go at it. Remember how in a previous lab we discovered that SVM's
# are a bit sensitive to outliers and that just throwing all of our unfiltered, dirty or noisy data at it, particularly in
# high-dimensionality space, can actually cause the accuracy score to suffer?
# Well, let's try to get rid of some useless features. Immediately after you do the pre-processing, run PCA on your dataset. The
# original dataset has 22 columns and 1 label column. So try experimenting with PCA n_component values between 4 and 14. Are you able
# to get a better accuracy?
'''
from sklearn.decomposition import PCA
pca = PCA(n_components=9).fit(X_train) ##from 4(0.915254237288) to 14(0.915254237288)
X_train = pca.transform(X_train)
X_test = pca.transform(X_test)
'''
# If you are not, then forget about PCA entirely, unless you want to visualize your data. However if you are able to get a higher score,
# then be *sure* keep that figure in mind, and comment out all the PCA code.
# In the same spot, run Isomap on the data, before sending it to the train / test split. Manually experiment with every inclusive
# combination of n_neighbors between 2 and 5, and n_components between 4 and 6. Are you able to get a better accuracy?
from sklearn.manifold import Isomap
for k in range(2, 6):
  for l in range(4, 7):
    iso = Isomap(n_neighbors=k, n_components=l).fit(X_train)
    X_train = iso.transform(X_train)
    X_test = iso.transform(X_test)

    # Instead, lets get the computer to do what computers do best. Program a naive, best-parameter search by creating nested for-loops. The outer for-loop should iterate a variable C from to , using unit increments. The inner for-loop should increment a variable gamma from to , using unit increments. As you know, Python ranges won't allow for float intervals, so you'll have to do some research on NumPy ARanges, if you don't already know how to use them.

    for i in np.arange(start = 0.05, stop = 2.05, step = 0.05):
      for j in np.arange(start = 0.001, stop = 0.101, step = 0.001):
        # Create a SVC classifier. Don't specify any parameters, just leave everything as default. Fit it against your training data and then score your testing data.
        model = SVC(C=i, gamma=j).fit(X_train, y_train)
        score = model.score(X_test, y_test)
        if(score>best_score):
          best_score = score
          best_C = model.C
          best_gamma = model.gamma
          best_n_neighbors = iso.n_neighbors
          ##best_n_components = pca.n_components
          best_n_components = iso.n_components

print('The highest score obtained: ', best_score)
print('C value: ', best_C)
print('gamma value: ', best_gamma)
print('isomap n_neighbors: ', best_n_neighbors)
##print('pca n_components: ', best_n_components)
print('isomap n_components: ', best_n_components)


## how can i get the real answer = 0.949152542373?
## both my pca and iso is worse than original