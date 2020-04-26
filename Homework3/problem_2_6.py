import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# rank k approx
def low_rank_k(u,s,vh,num):
    u = u[:,:num]
    vh = vh[:num,:]
    s = s[:num]
    s = np.diag(s)
    my_low_rank = np.dot(np.dot(u,s),vh)
    return my_low_rank

simg = Image.open('simple.png').convert('L')
simple = np.array(simg)
print(simple.shape)

dimg = Image.open('less.jpg').convert('L')
complicated = np.array(dimg)
print(complicated.shape)

rand_matrix = np.random.randn(300,300)
print(rand_matrix.shape)


image = rand_matrix


for rank in [10,20,40,60,100,200,250,300]:
    original_norm = np.linalg.norm(image)
    u,s,vh = np.linalg.svd(image)
    rank_approx = low_rank_k(u, s, vh, rank)
    subtraction = image - rank_approx
    new_norm = np.linalg.norm(subtraction)
    print(new_norm/original_norm)


u,s,vh = np.linalg.svd(image)
x = [i for i in range(1,len(s) + 1)]

plt.plot(x,s)
plt.show()