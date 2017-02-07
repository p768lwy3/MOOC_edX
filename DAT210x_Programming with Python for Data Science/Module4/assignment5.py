import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import random, math

import glob
from sklearn.manifold import Isomap

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')

#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
for image_path in glob.glob("Datasets/ALOI/32/*.png"):
	image = misc.imread(image_path)
	## print(image.shape) ## result = (144, 192)
	image = image[:,:]
	X = (image).reshape(-1)
	## X = (image/255).reshape(-1)
	samples.append(X)
## print('The samples length is ',len(samples),'.') ## result = 72
## print(samples)
## exit()

#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
for image_path in glob.glob("Datasets/ALOI/32i/*.png"):
	image = misc.imread(image_path)
	## print(image.shape) ## result = (144, 192)
	image = image[:,:]
	X = (image).reshape(-1)
	## X = (image/255).reshape(-1)
	samples.append(X)
colors = ['b', 'r']

#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 
df = pd.DataFrame(samples)
## print(df.shape)
## print(df.head(5))
## print(df.tail(5))
## exit()

#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 
iso = Isomap(n_neighbors=6, n_components=3, eigen_solver='auto')
iso.fit(df)
Y = iso.transform(df)
## print(type(Y))
## print(Y.shape)
## print(Y)

#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 
fig = plt.figure()
plt.scatter(Y[:73,0],Y[:73,1],c='b',marker='o')
plt.scatter(Y[73:84,0],Y[73:84,1],c='r',marker='o')
fig.suptitle('2D-Isomap-Plot')
plt.xlabel('component 0')
plt.ylabel('component 1')

## fig = plt.figure()
## plt.scatter(Y[:,1],Y[:,2],c='blue',marker='o')
## fig.suptitle('2D-Isomap-Plot')
## plt.xlabel('component 1')
## plt.ylabel('component 2')

## fig = plt.figure()
## plt.scatter(Y[:,0],Y[:,2],c='green',marker='o')
## fig.suptitle('2D-Isomap-Plot')
## plt.xlabel('component 0')
## plt.ylabel('component 2')


#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',title='3D-Scatter-plot')
ax.set_xlabel('component 0')
ax.set_ylabel('component 1')
ax.set_zlabel('component 2')
ax.scatter(Y[:73,0],Y[:73,0],Y[:73,0],c='b',marker='o')
ax.scatter(Y[73:84,0],Y[73:84,1],Y[73:84,2],c='r',marker='o')

plt.show()

