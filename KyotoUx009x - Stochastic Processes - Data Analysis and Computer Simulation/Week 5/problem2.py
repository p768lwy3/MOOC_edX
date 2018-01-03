fig, ax = plt.subplots(figsize=(7.5,7.5))
plt.xlim(-1, 10)
plt.ylim(-1, 8)
omega = np.arange(0,10,0.01)
dim=3
###
m    = 1.0
zeta = 1.0
kBT  = 1.0
gamma = zeta/m
plt.plot(omega,(6.0*kBT/m)*gamma/(omega**2 + gamma**2),'k',lw=6)
###
m    = 5.0
zeta = 1.0
kBT  = 1.0
gamma = zeta/m
plt.plot(omega,(6.0*kBT/m)*gamma/(omega**2 + gamma**2),'r',lw=6)
###
m    = 1.0
zeta = 2.0
kBT  = 1.0
gamma = zeta/m
plt.plot(omega,(6.0*kBT/m)*gamma/(omega**2 + gamma**2),'b',lw=6)
ax.set_xlabel(r"angular frequency $\omega$", fontsize=24)
ax.set_ylabel(r"spectral density $S_V(\omega)$", fontsize=24)
plt.legend([r'$m=1,\zeta=1,k_B T=1$',r'$m=5,\zeta=1,k_B T=1$',r'$m=1,\zeta=2,k_B T=1$'], fontsize=20)
plt.tick_params(labelsize=20)
plt.show()
