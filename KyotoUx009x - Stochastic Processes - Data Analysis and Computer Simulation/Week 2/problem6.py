import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

M = 4
N = 100000
ave = M/2
std = np.sqrt(M/12)
print('M =',M)
np.random.seed(0)
X = np.zeros(N)
for i in range(N):
    X[i] += np.sum(np.random.rand(M))
nmin=np.int(ave-std*5)
nmax=np.int(ave+std*5)
plt.hist(X,range=[nmin,nmax],bins=50,normed=True)
x = np.arange(nmin,nmax,0.01/std)
y = np.exp(-(x-ave)**2/(2*std**2))/np.sqrt(2*np.pi*std**2)
plt.plot(x,y,color='b',lw=4)
plt.xlabel(r'$x$',fontsize=20)
plt.ylabel(r'$P(x)$',fontsize=20)
plt.legend([r'Gauss',r'histogram'], fontsize=16)
plt.show()
