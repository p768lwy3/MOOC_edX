import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pltparams = {'legend.fontsize': 16, 'axes.labelsize': 20, 'axes.titlesize': 20,
             'xtick.labelsize': 12, 'ytick.labelsize':12, 'figure.figsize': (7.5, 7.5),}
plt.rcParams.update(pltparams)
def problem1(cols,taus):
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
def plot1(ax, data, cols, labels):
    for col,lbl in zip(cols,labels):
        data[col].hist(ax=ax,alpha=0.6, normed=True, bins=40, lw=0, label=lbl)
    ax.set_xlim([-5,5])
    ax.set_ylim([0,0.6])
    ax.legend()
    ax.set_xlabel('Normalized price return $G_n(t)$')
    ax.set_ylabel('Probability Distribution')
    
cols,taus = ['G30','G90','G180'], [30,90,180]
apple = problem1(cols, taus)

fig, axes = plt.subplots(figsize=(15.0,7.5))
plot1(axes, apple, cols, [r'$G_{30}$', r'$G_{90}$', r'$G_{180}$'])
fig.tight_layout()
plt.show()
