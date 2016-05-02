from Tree import *
from Node import *
from numpy import random
from random import randint
from math import log
import numpy as np


c = Counter()
count = []
logn = []
for k in range(1,50):
  n = int(5*((1.2)**k))
  j = randint(1,n)
  N = Tree(c)
  logn.append(log(n))
  for i in range(1,n+1):
    j = randint(1,n)
    N.insert(j)
  #N.delete(N.root)
  avg = N.c.query()/n
  N.c.reset()
  count.append(avg)
  #inorder(N.root)
  #print(count)


import matplotlib.pyplot as plt

logn = np.array(logn)
count = np.array(count)

plt.subplot(1,1,1)

plt.scatter(logn, count)
plt.title('')
plt.xlabel('logn')
plt.ylabel('avg no. of ops')
plt.show()

