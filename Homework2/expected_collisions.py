from scipy.io import loadmat
from numpy import dot
from numpy.linalg import norm
import random 
import pyhash
import math


data = loadmat('mnist.mat')
test = data['testX']

rs = [i for i in range(1,31)]
ts = [2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 25, 28, 31, 35, 39, 44, 49, 55, 61, 68, 76, 84, 94]

def sim(x):
    cos_sim = dot(x, base)/(norm(x)*norm(base))
    return cos_sim

def sim(x, y):
    cos_sim = dot(x, y)/(norm(x)*norm(y))
    return cos_sim

print('Computing cosines')
cosines =[[] for i in range(len(test))]
for i_image,t_i in enumerate(test):
    if i_image % 1000 == 0:
        print('calculating conines with i=', i_image)
    for j_image,t_j in enumerate(test):
        cosines[i_image].append(sim(t_i, t_j))

print('Completed cosines')


avgCollisions = []

total_trials = 30
for trial in range(total_trials):
    r = rs[trial]
    t = ts[trial]
    print('trial number = ', trial, ', signature size = ', r, 'repititions = ', t)

    collisions = []

    print('Computing collisions')
    for i in range(len(cosines)):
        if i % 1000 == 0:
            print('calculating collisions with i=', i)
        collision = 0
        for j in range(len(cosines)):
            collision += (t*((1-math.acos(cosines[i][j])/math.pi)**r))
        collisions.append(collision)

    print('Completed collisions')
    print(collisions[:10])
    avg = sum(collisions)/len(collisions)
    print('trial average = ', avg)
    avgCollisions.append(avg)


print(avgCollisions)