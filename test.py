
import numpy as np
score = [20, 21, 22, 19, 45, 50, 49, 89, 91, 90]
# mu = np.mean(data[0:2])
# # sigma = np.var(data)
# print(mu)
for i in range(len(score)):
    mu = np.mean(data[start:i+1])
    sigma = np.var(data[start:i+1])/(i-start)