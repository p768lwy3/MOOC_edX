import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

p = 0.5
M = 100
N = 100000
ave = M*(2*p-1)
std = np.sqrt(4*M*p*(1-p))
print('p =',p,'M =',M)
L = np.zeros(N)
np.random.seed(0)
for i in range(N):
    step=np.random.choice([-1,1],M)
    L[i]=np.sum(step)
nmin=np.int(ave-std*5)
nmax=np.int(ave+std*5)
nbin=np.int((nmax-nmin)/4)
plt.hist(L,range=[nmin,nmax],bins=nbin,normed=True)
x = np.arange(nmin,nmax,0.01/std)
y = np.exp(-(x-ave)**2/(2*std**2))/np.sqrt(2*np.pi*std**2)
plt.plot(x,y,lw=4,color='b')
plt.xlabel(r'$l$',fontsize=20)
plt.ylabel(r'$P(l,m)$',fontsize=20)
plt.legend([r'Gauss',r'histogram'], fontsize=16)
plt.xlim(ave-250,ave+250)
plt.show()
