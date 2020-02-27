from entry_point.run import run
import multiprocessing

import numpy as np


# custom kernel of RBF kernel
def my_kernel_normal(X, Y):
    m, n = np.shape(X)
    o, p = np.shape(Y)

    gamma = 1
    K = np.mat(np.zeros((m, o)))
    for i in range(o):
        M = np.mat(np.zeros((m, 1)))
        for j in range(m):
            deltaRow = X[j, :] - Y[i, :]
            M[j] = np.dot(deltaRow, deltaRow.T)
        K[:, i] = np.exp(-gamma * M)
    return K




# main = run()
if __name__ == '__main__':

    run()