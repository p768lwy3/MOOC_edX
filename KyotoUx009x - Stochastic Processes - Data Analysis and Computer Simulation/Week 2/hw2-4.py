import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def auto_correlate(x):
    cor = np.correlate(x,x,mode="full")
    return cor[N-1:]
def rng(seed, a, b, M, ntotal):
    data = np.zeros(ntotal)
    data[0] = seed
    for i in range(1,ntotal):
        data[i] = np.mod((a*data[i-1]+b), M)
    return data/np.float(M)
seed,a,b,m,N = 123456, 8121, 28411, 134456, 100000
X = rng(seed, a, b, m, N)
c = auto_correlate(X-np.average(X))/N
plt.plot(c/c[0],'r',lw=2)
plt.xlabel(r'$i$')
plt.ylabel(r'$\varphi(i)$')
plt.xlim(-500,8000)
plt.show()
