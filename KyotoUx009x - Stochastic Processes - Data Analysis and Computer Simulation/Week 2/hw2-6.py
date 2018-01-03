import numpy as np
N = 10**5
np.random.seed(0)
X = np.random.randn(N)
Nout = 0
for i in range(N):
    if X[i]>5:
        Nout = Nout+1
print(Nout/N)
