import numpy as np
import math
import random
import linecache
import time
import matplotlib.pyplot as plt

#Example 1
n = 10000000
TRNG = []
pt = 1
image = 1
file = 'TRNG txt data - Image {}.txt'.format(image)

tic = time.perf_counter()
Rand_mod = np.random.rand(n,2)
toc = time.perf_counter()
inside = Rand_mod[np.sqrt(Rand_mod[:,0]**2+Rand_mod[:,1]**2)<1]
estimate = 4*len(inside)/len(Rand_mod)
print ('Estimate of pi: {}'.format(estimate))
print(f"Random module took {toc - tic:0.4f} seconds to generate RNG array.")
plt.figure(figsize=(8,8))
plt.scatter(Rand_mod[:,0],Rand_mod[:,1], s = .5, c='red')
plt.scatter(inside[:,0], inside[:,1], s=.5, c='blue')
plt.show()

tic = time.perf_counter()
for i in range (n*2):
    rand = float(linecache.getline(file,pt))
    TRNG.append(rand)
    pt += 1
    if i == 5999999:
        image = 10
        file = 'TRNG txt data - Image {}.txt'.format(image)
        pt = 1
    if i == 5999999*2:
        image = 53
        file = 'TRNG txt data - Image {}.txt'.format(image)
        pt = 1
    if i == 5999999*3:
        image = 80
        file = 'TRNG txt data - Image {}.txt'.format(image)
        pt = 1
        
TRNG = np.array(TRNG).reshape(n,2)
toc = time.perf_counter()
inside = TRNG[np.sqrt(TRNG[:,0]**2+TRNG[:,1]**2)<1]
estimate = 3.5*len(inside)/len(TRNG)
print ('Estimate of pi: {}'.format(estimate))
print(f"TRNG took {toc - tic:0.4f} seconds to generate RNG array.")
plt.figure(figsize=(8,8))
plt.scatter(TRNG[:,0],TRNG[:,1], s = .5, c='red')
plt.scatter(inside[:,0], inside[:,1], s=.5, c='blue')
plt.show()
