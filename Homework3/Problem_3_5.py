from numpy import genfromtxt
import numpy
import matplotlib.pyplot as plt


#Defining cities in the given order
cities = ['Boston', 'Buffalo', 'Chicago', 'Dallas', 'Denver', 'Houston','LosAngeles','Memphis','Miami','Minneapolis','NewYork','Omaha','Philadelphia','Phoenix','Pittsburgh','SaintLouis','SaltLakeCity','SanFrancisco','Seattle','Washington D.C.']

#Reading distances
distances = genfromtxt('cities.txt', delimiter=' ')
distances = numpy.square(distances)

#Calclulating eigen vectors for the m matrix
w,v = numpy.linalg.eig(distances)
print(w.shape, v.shape)
print(w)

#Calclulating eigen vectors for the m matrix
u,s,vh = numpy.linalg.svd(distances)
print(u.shape, s.shape)
print(s)

x = [i for i in range(1,21)]

plt.plot(x,s)
plt.show()