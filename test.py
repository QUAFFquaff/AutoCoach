from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np
p = 0.5
temp = np.random.binomial(1,p,size=100)
x = []
for i in range(len(temp)):
    x.append(2 * temp[i] -1)
print(x)
y = [x[0]/2]
for i in range(1,len(x)):
    y.append((x[i]+x[i-1])/2)
z = [x[0]*2/3]
for i in range(1,len(x)):
    z.append( x[i] * 2/3 + x[i-1] / 3 )
print(y)
print('E[x] = ')
print(sum(x)/100)
print('E[y] = ')
print(sum(y)/100)
print('E[z] = ')
print(sum(z)/100)