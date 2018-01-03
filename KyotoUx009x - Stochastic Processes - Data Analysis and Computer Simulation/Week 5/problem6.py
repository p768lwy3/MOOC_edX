# return power spectrum for positive frequencies of even signal v
from numpy import fft
def psd(v,dt):  
    vw = fft.fft(v)*dt # V(w) with zero-frequency component at vw(0)
    return np.abs(vw[:nums//2])**2/(nums*dt) # S_V for w > 0 (Eq. (G9))
Sw   = np.zeros([nums//2])
for n in range(nump):
    for d in range(dim):
        Sw = Sw + psd(Vs[:,n,d],dt) # power spectrum of d-component of velocity for particle n
Sw = Sw/nump
fig, ax = plt.subplots(figsize=(7.5,7.5))
gamma = zeta/m
omega = fft.fftfreq(nums,d=dt)[:nums//2]*2.0*np.pi
#ax.plot(omega,(6.0*kBT/m)*gamma/(omega**2 + gamma**2),'r',lw=6,label=r'$6k_BT/(\omega^2+\zeta^2)$')                         
ax.plot(omega,Sw,'b',lw=6)
ax.set_xlabel(r"angular frequency $\omega$", fontsize=16)
ax.set_ylabel(r"spectral density $S_V(\omega)$", fontsize=16)
#ax.legend(fontsize=16)
plt.xlim(-1, 10)
plt.ylim(-1, 8)
plt.show()
