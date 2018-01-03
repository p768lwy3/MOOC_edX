import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot') # use "ggplot" style for graphs

fig, ax = plt.subplots(figsize=(7.5,7.5))
plt.xlim(-5, 5)
plt.ylim(-0.05,0.85)
x = np.arange(-5, 5, 0.01)
###
std = 1.0
ave = 0.0
y = np.exp(-(x-ave)**2/2/std**2)/np.sqrt(2*np.pi*std**2)
plt.plot(x, y, lw=5, color='k')
###
std = 0.5
ave = 2.0
y = np.exp(-(x-ave)**2/2/std**2)/np.sqrt(2*np.pi*std**2)
plt.plot(x, y, lw=5, color='r')
plt.xlabel(r'$x$', fontsize=28)
plt.ylabel(r'$P(x)$', fontsize=28)
plt.legend([r'$\langle X \rangle=0$, $\sigma=1$',r'$\langle X \rangle=2$, $\sigma=0.5$'], fontsize=24)
#plt.legend([r'$\langle X \rangle=0$, $\sigma=1$'], fontsize=24)
plt.tick_params(labelsize=20)
plt.show()
