import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(7.5,7.5))
plt.xlim(-1,10)
plt.ylim(-0.5,3.5)
time = np.arange(0,10,0.01)
dim=3
###
m    = 1.0
zeta = 1.0
kBT  = 1.0
plt.plot(time,dim*kBT/m*np.exp(-zeta/m*time),'k',lw=6)
###
m    = 0.1
zeta = 1.0
kBT  = 0.1
plt.plot(time,dim*kBT/m*np.exp(-zeta/m*time),'r',lw=6)
###
m    = 1.0
zeta = 0.2
kBT  = 1.0
plt.plot(time,dim*kBT/m*np.exp(-zeta/m*time),'b',lw=6)
ax.set_xlabel(r"time $t$", fontsize=24)
ax.set_ylabel(r"auto correlation $\varphi_V(t)$", fontsize=24)
plt.legend([r'$m=1,\zeta=1,k_B T=1$',r'$m=0.1,\zeta=1,k_B T=0.1$',r'$m=1,\zeta=0.2,k_B T=1$'], fontsize=20)
plt.tick_params(labelsize=20)
plt.show()
