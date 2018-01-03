import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pltparams = {'legend.fontsize': 16, 'axes.labelsize': 20, 'axes.titlesize': 20,
             'xtick.labelsize': 12, 'ytick.labelsize':12, 'figure.figsize': (7.5, 7.5),}
plt.rcParams.update(pltparams)
def problem4(tau1, tau2):
    # Logarithmic return of price time series
    def logreturn(Pt,tau=1):
        return np.log(Pt[tau:]) - np.log(Pt[0:-tau]) # Eq.(J2) : G_tau(t) = log(S(t+tau)) - log(S(t)) 
    # Normalize data to have unit variance (<(x - <x>)^2> = 1)
    def normalized(data):
        return (data/np.sqrt(np.var(data)))

    dmy, data = np.loadtxt('./data/06/model1.txt', unpack=True)
    return normalized(logreturn(data, tau1)), normalized(logreturn(data,tau2))

def plot4(ax,g1,g16):
    def pdf(data,bins=50):
        hist,edges=np.histogram(data[~np.isnan(data)],bins=bins,density=True) # remove NaNs and compute histogram
        edges   = (edges[:-1] + edges[1:])/2.0 # get bar center
        nonzero = hist > 0.0                   # non-zero points 
        return edges[nonzero], hist[nonzero]

    for data,lbl in zip([g1,g16], [r'$G_1$', r'$G_{16}$']):
        edges, hist = pdf(np.abs(data), bins=20)
        ax.plot(edges, hist, lw=5, label=lbl)

    x = np.linspace(0, 5)
    ax.plot(x,2*np.exp(-x**2/2)/np.sqrt(2*np.pi),lw=6,ls='--',color='gray',alpha=0.6,label=r'Gaussian')
    ax.plot(x, 2*np.exp(-1.5*x),lw=6,color='k',ls='--',alpha=0.8,label=r'Exponential')
    ax.semilogy()
    ax.set_ylim([5e-4,1])
    ax.set_xlim([5e-1,6])
    ax.legend()
    ax.set_xlabel(r'Absolute normalized price return $|G_1|$')
    ax.set_ylabel(r'Probability density')

fig, ax = plt.subplots(figsize=(7.5,7.5))
g1,g2 = problem4(1,16)
plot4(ax, g1, g2)
fig.tight_layout()
plt.show()
