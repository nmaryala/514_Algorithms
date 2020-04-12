from scipy.io import loadmat
from numpy import dot
from numpy.linalg import norm
import random 
import pyhash


data = loadmat('mnist.mat')
test = data['testX']

rs = [i for i in range(1,31)]
ts = [2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 25, 28, 31, 35, 39, 44, 49, 55, 61, 68, 76, 84, 94]

def sim(x):
    cos_sim = dot(x, base)/(norm(x)*norm(base))
    return cos_sim


avgCollisions = []

total_trials = 30
for trial in range(total_trials):
    r = rs[trial]
    t = ts[trial]
    print('trial number = ', trial, ', signature size = ', r, 'repititions = ', t)

    collisions = [0 for i in range(len(test))]
    for reptition in range(t):
        print('reptition number = ', reptition)
        hashesOfImages = [[] for i in range(len(test))]

        for i_hash in range(r):
            base = [(random.random()-0.5)/2 for i in range(test.shape[1])]

            for i_image,t in enumerate(test):
                if sim(t) < 0:
                    hashesOfImages[i_image].append(-1)
                else:
                    hashesOfImages[i_image].append(1)

        hashOfHashes = [hash(tuple(hashesOfImages[i])) for i in range(len(test))]
        for i in range(len(test)):
            for j in range(len(test)):
                if i == j:
                    continue

                if hashOfHashes[i] == hashOfHashes[j]:
                    collisions[i] += 1

    print(collisions[:10])
    avg = sum(collisions)/len(collisions)
    print('trial average = ', avg)
    avgCollisions.append(avg)


print(avgCollisions)