from scipy.io import loadmat
from numpy import dot
from numpy.linalg import norm
import random 
import pyhash
import numpy as np
from PIL import Image

data = loadmat('mnist.mat')
train = data['trainX']


def sim(x):
    cos_sim = dot(x, base)/(norm(x)*norm(base))
    return cos_sim


avgCollisions = []

r = 35
t = 1

hashesOfImages = [[] for i in range(len(train))]

for i_hash in range(r):
    base = [(random.random()-0.5)/2 for i in range(train.shape[1])]
    for i_image,t in enumerate(train):
        if sim(t) < 0:
            hashesOfImages[i_image].append(-1)
        else:
            hashesOfImages[i_image].append(1)

hashOfHashes = [hash(tuple(hashesOfImages[i])) for i in range(len(train))]

mainImage = 0
matches = []
for i in range(len(train)):
    for j in range(len(train)):
        if i == j:
            continue

        if hashOfHashes[i] == hashOfHashes[j]:
            matches.append((i,j))

print(matches[:10])

for match in matches[:10]:
    ex1 = train[match[0]]
    mat = np.reshape(ex1, (28,28))
    img = Image.fromarray(mat, 'L')
    img.show()
    ex1 = train[match[1]]
    mat = np.reshape(ex1, (28,28))
    img = Image.fromarray(mat, 'L')
    img.show()
