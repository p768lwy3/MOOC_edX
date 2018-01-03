import numpy as np              # import numpy library as np
import matplotlib.pyplot as plt # import pyplot library as plt 
plt.style.use('ggplot')         # use "ggplot" style for graphs

# Runge-Kutta 2nd
dt, tmin, tmax = 0.1, 0.0, 10.0 # set \Delta t, t0, tmax
step=int((tmax-tmin)/dt)
# create array t from tmin to tmax with equal interval dt 
t = np.linspace(tmin,tmax,step)
y = np.zeros(step) # initialize array y as all 0
ya = np.exp(-t) # analytical solution y=exp(-t)
plt.plot(t,ya,lw=5,label='Exact') # plot y vs. t (analytical)
y[0]=1.0 # initial condition
#####
y1 = np.zeros(step) # initialize array y1 as all 0
for i in range(step-1):
    y1[i]=y[i]-0.5*dt*y[i] # Runge-Kutta Eq.(A15)
    y[i+1]=y[i]-dt*y1[i] # Runge-Kutta Eq.(A16)
#####
plt.plot(t,y, lw=3,ls='--',label='Numerical')# plot y vs t (numerical)
plt.plot(t,y/ya,lw=3,label='Ratio') # plot y/ya vs. t
plt.legend() # display legend
plt.show() # display plots

# Runge-Kutta 4th
dt,tmin,tmax =0.1,0.0,10.0 # set \Delta t, t0, tmax
step=int((tmax-tmin)/dt)
# create array t from tmin to tmax with equal interval dt
t = np.linspace(tmin,tmax,step)
y = np.zeros(step) # initialize array y as all 0
ya = np.exp(-t) # analytical solution y=exp(-t)
plt.plot(t,ya,lw=5,label='Exact') # plot y vs. t (analytical)
y[0]=1.0 # initial condition
#####
y1 = np.zeros(step) # initialize array y1 as all 0
y2 = np.zeros(step) # initialize array y2 as all 0
y3 = np.zeros(step) # initialize array y3 as all 0
for i in range(step-1):
    y1[i]=y[i]-0.5*dt*y[i] # Runge-Kutta Eq.(A18)
    y2[i]=y[i]-0.5*dt*y1[i] # Runge-Kutta Eq.(A19)
    y3[i]=y[i]-dt*y2[i] # Runge-Kutta Eq.(A20)
    y[i+1]=y[i]-dt*(y[i]+2.0*y1[i]+2.0*y2[i]+y3[i])/6.0 # Runge-Kutta Eq.(A21)
#####
plt.plot(t,y,lw=3,ls='--',label='Numerical') # plot y vs t (numerical)
plt.plot(t,y/ya,lw=3, label="Ratio") # plot y/ya vs. t
plt.legend() # display legend
plt.show() # display plots
