import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pltparams = {'legend.fontsize': 16, 'axes.labelsize': 20, 'axes.titlesize': 20,
             'xtick.labelsize': 12, 'ytick.labelsize':12, 'figure.figsize': (7.5, 7.5),}
plt.rcParams.update(pltparams)
def problem8(colM10,tau=1):
    # Logarithmic return of price time series
    def logreturn(Pt,tau=1):
        return np.log(Pt[tau:]) - np.log(Pt[0:-tau]) # Eq.(J2) : G_tau(t) = log(S(t+tau)) - log(S(t)) 
    # Normalize data to have unit variance (<(x - <x>)^2> = 1)
    def normalized(data):
        return (data/np.sqrt(np.var(data)))

    priceM1   = np.loadtxt('./data/06/model2.txt', usecols=[1,])
    priceM10 = pd.read_csv('./data/06/model2_M10_5d.txt', header=0, delim_whitespace=True, index_col=False)
    dprice    = pd.DataFrame()
    dprice['M1'] = normalized(logreturn(priceM1, tau))
    dprice['M10']= normalized(logreturn(priceM10[colM10].values,tau))
    return dprice

def plot8(ax,dprice1,dprice10):
    # compute self-correlation of vector v
    def auto_correlate(v):
        # np.correlate computes C_{v}[k] = sum_n v[n+k] * v[n]
        corr = np.correlate(v,v,mode="full") # correlate returns even array [0:2*nums-1] centered at nums-1
        return corr[len(v)-1:]/len(v) # take positive values and normalize by number of points
    ax.plot(auto_correlate(dprice1), label=r'$M=1$')
    ax.plot(auto_correlate(dprice10), label=r'$M=10$')
    ax.set_xlim(5e-1,1e3)
    ax.set_ylim(-0.2, 1.0)
    ax.legend()
    ax.semilogx()
    ax.set_xlabel(r'Time n (ticks)')
    ax.set_ylabel(r'Time Correlation function $C_{G_{1}}(t)$')

fig, ax = plt.subplots(figsize=(7.5,7.5))
dprice = problem8('d+1')
plot8(ax,dprice['M1'], dprice['M10'])
fig.tight_layout()
plt.show()
