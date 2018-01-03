import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

ave = 2.0
std = 4.0
N = 1000
np.random.seed(0)
X = ave+std*np.random.randn(N)
plt.hist(X,bins=25,normed=True)
x = np.arange(-15,15,0.01)
y = np.exp(-(x-ave)**2/(2*std**2))/np.sqrt(2*np.pi*std**2)
plt.xlim(-15,15)
plt.plot(x,y,color='b',lw=4)
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$P(x)$',fontsize=20)
plt.legend([r'Gaussian',r'histgram'], fontsize=16)
plt.show()
