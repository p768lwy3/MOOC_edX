import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pltparams = {'legend.fontsize': 16, 'axes.labelsize': 20, 'axes.titlesize': 20,
             'xtick.labelsize': 12, 'ytick.labelsize':12, 'figure.figsize': (7.5, 7.5),}
plt.rcParams.update(pltparams)
def problem2(cols,taus):
    from datetime import datetime
    from pandas_datareader import data as pdr
    from pandas_datareader import wb as pwb
    # Logarithmic return of price time series
    def logreturn(Pt,tau=1):
        return np.log(Pt[tau:]) - np.log(Pt[0:-tau]) # Eq.(J2) : G_tau(t) = log(S(t+tau)) - log(S(t)) 
    # Normalize data to have unit variance (<(x - <x>)^2> = 1)
    def normalized(data):
        return (data/np.sqrt(np.var(data)))
    # Add G_tau to data frame object
    def computeReturn(data, name, tau):
        data[name]=pd.Series(normalized(logreturn(data['Adj Close'].values, tau)),index=data.index[:-tau])

    # define time interval
    end_time   = datetime(2016, 12, 31)
    start_time = datetime(1989, 1, 1)
    apple      = pdr.DataReader('AAPL','yahoo',start_time,end_time)
    for col,tau in zip(cols,taus):
        computeReturn(apple, col, tau)
    return apple
def plot2(ax, data, cols, labels):
    # compute normalized probability distribution function
    def pdf(data,bins=50):
        hist, edges = np.histogram(data[~np.isnan(data)], bins=bins, density=True) # remove NaNs and compute histogram (returns bar heights and bar edges)
        edges   = (edges[:-1] + edges[1:])/2.0 # get bar centers
        nonzero = hist > 0.0                   # only keep non-zero points 
        return edges[nonzero], hist[nonzero]

    for col,lbl in zip(cols,labels):
        edges, hist = pdf(np.abs(data[col]), bins=20)
        ax.plot(edges, hist, label=lbl, lw=3)

    #plot gaussian
    x = np.logspace(-1, 1.2)
    ax.plot(x,np.abs(np.exp(-x**2/2)/np.sqrt(2*np.pi)),lw=6,ls='--',color='gray',alpha=0.8,label=r'Gaussian')
        
    ax.set_ylim(1e-4, 2e0)
    ax.set_xlim(1e-1, 2e1)
    ax.semilogx()
    ax.semilogy()
    ax.legend(loc=3)
    ax.set_xlabel(r'Absolute normalized price return $|G_n|$')
    ax.set_ylabel(r'Probability distribution')

cols,taus = ['G30','G90','G180'], [30,90,180]
apple = problem2(cols, taus)

fig, ax = plt.subplots(figsize=(7.5,7.5))
plot2(ax, apple, cols, [r'$G_{30}$', r'$G_{90}$', r'$G_{180}$'])
fig.tight_layout()
plt.show()
