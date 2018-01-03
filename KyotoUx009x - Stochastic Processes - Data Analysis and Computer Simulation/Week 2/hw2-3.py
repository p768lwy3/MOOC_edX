import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def rng(seed, a, b, M, ntotal):
    data = np.zeros(ntotal)
    data[0] = seed
    for i in range(1,ntotal):
        data[i] = np.mod((a*data[i-1]+b), M)
    return data/np.float(M)
seed,a,b,m,N = 123456, 8121, 28411, 134456, 500000
X = rng(seed, a, b, m, N)
plt.hist(X,normed=True)
plt.xlabel(r'$\zeta$')
plt.ylabel(r'$P(\zeta)$')
plt.show()
