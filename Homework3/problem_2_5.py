import numpy as np
import matplotlib.pyplot as plt

#Number of dimensions
dimensions = 100
#Number of clusters
c = 10
#Number of points in each cluster
p = 100

seeds = []
#10 seeds which will form the center of the clusters
for i in range(c):
    seed = []
    for i in range(dimensions):
        seed.append((np.random.randint(0,100) * np.random.randint(1,40)))
    seeds.append(seed)

print(len(seeds))

points = []
for i in range(c):
    for j in range(p):
        points.append(np.random.randn(dimensions) + seeds[i])

print(len(points))

#SVD of the data
u,s,vh = np.linalg.svd(points)
print(u.shape, s.shape)
print(s)

x = [i for i in range(1,len(s) + 1)]

plt.plot(x,s)
plt.show()