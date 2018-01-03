import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pltparams = {'legend.fontsize': 16, 'axes.labelsize': 20, 'axes.titlesize': 20,
             'xtick.labelsize': 12, 'ytick.labelsize':12, 'figure.figsize': (7.5, 7.5),}
plt.rcParams.update(pltparams)
def problem7(tau):
    # Logarithmic return of price time series
    def logreturn(Pt,tau=1):
        return np.log(Pt[tau:]) - np.log(Pt[0:-tau]) # Eq.(J2) : G_tau(t) = log(S(t+tau)) - log(S(t)) 
    # Normalize data to have unit variance (<(x - <x>)^2> = 1)
    def normalized(data):
        return (data/np.sqrt(np.var(data)))

    price = pd.read_csv('./data/06/model2_M10_5d.txt', header=0, delim_whitespace=True,index_col=False)
    dprice= pd.DataFrame() #create empty frame
    for col in ['d+2','d+1','d0','d-1','d-2']: #populate frames with returns
        dprice[col] = normalized(logreturn(price[col].values,tau))
    return dprice

def plot7(ax,dprice):
    def pdf(data,bins=50):
        hist,edges=np.histogram(data[~np.isnan(data)],bins=bins,density=True) # remove NaNs and compute histogram
        edges   = (edges[:-1] + edges[1:])/2.0 # get bar center
        nonzero = hist > 0.0                   # non-zero points 
        return edges[nonzero], hist[nonzero]

    edges,hist = pdf(np.abs(dprice),bins=20)
    ax.plot(edges,hist,label=r'$d=-2$', lw=3)
    x = np.linspace(0.1, 10)
    ax.plot(x, 2*np.exp(-1.5*x),lw=4,color='gray',ls='--',alpha=0.5,label=r'Exponential')
    ax.plot(x,2*np.exp(-x**2/2)/np.sqrt(2*np.pi),lw=6,ls=':',color='gray',alpha=0.6,label=r'Gaussian')
    ax.plot(x, 0.3*x**(-3), lw=6, color='k', ls='--', alpha=0.5, label=r'Power Law $\propto x^{-3}$')
    ax.semilogy()
    ax.semilogx()
    ax.set_xlim([5e-1,2e1])
    ax.set_ylim([5e-4,1])
    ax.legend()
    ax.set_xlabel(r'Absolute normalized price return $|G_1|$')
    ax.set_ylabel(r'Probability density')
    
fig, ax = plt.subplots(figsize=(7.5,7.5))
dprice = problem7(1)
plot7(ax, dprice['d-2'])
fig.tight_layout()
plt.show()
