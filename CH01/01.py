import numpy as np
np.random.seed(0)
rewards=[]
for n in range(1,11):
    rewards.append(np.random.rand())
    Q=sum(rewards)/n
    print(Q)