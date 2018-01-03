import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

p = 0.5
M = 1000
N = 100000
ave = M*p
std = np.sqrt(M*p*(1-p))
print('p =',p,'M =',M)
np.random.seed(0)
X = np.random.binomial(M,p,N)
nmin=np.int(ave-std*5)
nmax=np.int(ave+std*5)
nbin=nmax-nmin+1
plt.hist(X,range=[nmin,nmax],bins=nbin,normed=True)
x = np.arange(nmin,nmax,0.01/std)
y = np.exp(-(x-ave)**2/(2*std**2))/np.sqrt(2*np.pi*std**2)
plt.plot(x,y,color='b',lw=4)
plt.xlabel(r'$n$',fontsize=16)
plt.ylabel(r'$P(n)$',fontsize=16)
plt.legend([r'Gauss',r'histogram'], fontsize=16)
plt.show()
