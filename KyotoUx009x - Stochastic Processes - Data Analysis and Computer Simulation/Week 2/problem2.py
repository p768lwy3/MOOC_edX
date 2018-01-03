fig, ax = plt.subplots(figsize=(7.5,7.5))
plt.xlim(0, 100)
plt.ylim(-0.001,0.12)
#plt.ylim(0, 100)
def binomial(n,m,p):
    comb = math.factorial(m) / (math.factorial(n) * math.factorial(m-n))
    prob = comb * p ** n * (1 - p) ** (m - n)
    return prob
p = 0.5
M = 100
x = np.arange(M)
y = np.zeros(M)
for i in range(M):
    y[i]=binomial(i,M,p)
plt.plot(x, y, lw=5, color='k')
p = 0.2
M = 100
x = np.arange(M)
y = np.zeros(M)
for i in range(M):
    y[i]=binomial(i,M,p)
plt.plot(x, y, lw=5, color='r')
p = 0.1
M = 500
x = np.arange(M)
y = np.zeros(M)
for i in range(M):
    y[i]=binomial(i,M,p)
plt.plot(x, y, lw=5, color='b')
plt.xlabel(r'$n$', fontsize=28)
plt.ylabel(r'$P(n)$', fontsize=28)
ax.legend([r'$p=0.5,M=100$',r'$p=0.2,M=100$',r'$p=0.1,M=500$'], fontsize=24)
plt.tick_params(labelsize=20)
plt.show()
