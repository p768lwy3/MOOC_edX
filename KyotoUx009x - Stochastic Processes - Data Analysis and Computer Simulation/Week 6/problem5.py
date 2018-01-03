import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pltparams = {'legend.fontsize': 16, 'axes.labelsize': 20, 'axes.titlesize': 20,
             'xtick.labelsize': 12, 'ytick.labelsize':12, 'figure.figsize': (7.5, 7.5),}
plt.rcParams.update(pltparams)

def model2RW(params,p0,deltapm):        # simulate Random-Walk for 1 transaction
    price = np.array([p0[0], p0[1]])    # initialize mid-prices for dealers p_1 and p_2
    cdp   = params['c']*params['dp']    # define random step size
    ddt   = params['d']*params['dt']    # define trend drift term
    Dt    = [price[0]-price[1]]         # initialize price difference as empty list
    At    = [np.average(price)]         # initialize avg price as empy list
    while np.abs(price[0]-price[1]) < params['L']:
        price=price+np.random.choice([-cdp,cdp],size=2) # random walk step for mid-prices Eq. (L4)
        price=price+ddt*deltapm         # Model 2 : add trend-following term in Eq. (L4)
        Dt.append(price[0]-price[1])
        At.append(np.average(price))
    return np.array(Dt),np.array(At)-At[0] # return difference array and average centered at zero
def plot5(ax, dvalues, labels):
    params={'L':0.01,'c':0.01,'dp':0.01,'dt':0.01**2, 'd':1.25, 'M':1} # define model parameters
    p0 = [100.25, 100.25]
    deltapm = 0.003
    for dval,lbl in zip(dvalues, labels):
        np.random.seed(123456)
        params['d'] = dval
        Dt,At = model2RW(params, p0, deltapm) 
        ax.plot(At,Dt,alpha=0.8,label=lbl)    #plot RW
        ax.plot(At[-1],Dt[-1],marker='o',color='k') # plot last point
    ax.plot(0, 0, marker='s', color='k', markersize=10) # starting position
    ax.plot([-0.04,0.04],[params['L'],params['L']],color='k') #top absorbing boundary P=L
    ax.plot([-0.04,0.04],[-params['L'],-params['L']],color='k') #bottom absorbing boundary P=-L
    ax.set_ylim([-0.012, 0.012])
    ax.set_xlim([-0.02, 0.02])
    ax.legend(loc=4,framealpha=0.8)
    
fig, ax = plt.subplots(figsize=(7.5,7.5))
plot5(ax, [-2.0,-1.0,0.0,1.0,2.0], [r'$d = -2$',r'$d = -1$',r'$d = 0$',r'$d = +1$',r'$d = +2$'])
ax.set_xlim([-0.020,0.020])
fig.tight_layout()
plt.show()
