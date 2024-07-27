import numpy as np
np.random.seed(0)
Q=0
for n in range(1,11):
    Q=(Q*(n-1)+np.random.rand())/n
    print(Q)