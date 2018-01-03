import numpy as np # import numpy library as np
import matplotlib.pyplot as plt # import pyplot library as plt 
plt.style.use('ggplot') # use "ggplot" style for graphs 

N = 1000 # size of R
np.random.seed(0) # initialization of the random number generator
R = np.random.rand(N) # generate random sequence and store it as R
# plot normalized histgram of R using 100 bins
plt.hist(R,bins=100,normed=True)
plt.show() # show plot
