fig, ax = plt.subplots(figsize=(7.5,7.5))
plt.xlim(0,60)
plt.ylim(0,400)
time = np.arange(0,100,0.01)
dim=3
###
m    = 1.0
zeta = 1.0
kBT  = 1.0
D = kBT/zeta
plt.plot(time,2*dim*D*time,'k',lw=6)
###
m    = 2.0
zeta = 2.0
kBT  = 1.0
D = kBT/zeta
plt.plot(time,2*dim*D*time,'r',lw=6)
###
m    = 1.0
zeta = 1.0
kBT  = 2.0
D = kBT/zeta
plt.plot(time,2*dim*D*time,'b',lw=6)
ax.set_xlabel(r"time $t$", fontsize=24)
ax.set_ylabel(r"MSD", fontsize=24)
plt.legend([r'$m=1,\zeta=1,k_B T=1$',r'$m=2,\zeta=2,k_B T=1$',r'$m=1,\zeta=1,k_B T=2$'], fontsize=20)
plt.tick_params(labelsize=20)
plt.show()
