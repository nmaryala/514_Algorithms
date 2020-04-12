from numpy import genfromtxt
import numpy
import matplotlib.pyplot as plt


#Defining cities in the given order
cities = ['Boston', 'Buffalo', 'Chicago', 'Dallas', 'Denver', 'Houston','LosAngeles','Memphis','Miami','Minneapolis','NewYork','Omaha','Philadelphia','Phoenix','Pittsburgh','SaintLouis','SaltLakeCity','SanFrancisco','Seattle','Washington D.C.']

#Reading distances
distances = genfromtxt('cities.txt', delimiter=' ')

#Squaring distances as we need D matrix as defined in the problem set
distances = numpy.square(distances)

#Used multiple times in the code. So, pre-defined it
totaldist= numpy.sum(distances)


#This is the matrix which will be P.P_Transpose
m = numpy.zeros((20,20))

for i in range(20):
    for j in range(20):
        a = distances[i][j]
        b = sum(distances[i][k] for k in range(20))/20
        c = sum(distances[j][k] for k in range(20))/20
        d = totaldist/400
        #Formula defined in the problem set
        m[i][j] = -(a-b-c+d)/2


#Calclulating eigen vectors for the m matrix
w,v = numpy.linalg.eig(m)
print(w, v[0])



sigma = numpy.zeros((2,2))
#Taking only the top 2 vectors since we need 2D data
sigma[0][0] = w[0]
sigma[1][1] = w[1]
#We need Singular values not the eigen values. So, used square root.
sigma = numpy.sqrt(sigma)

#Taking only two eigen vectors
v_modified = numpy.zeros((20,2))

for i in range(20):
    v_modified[i][0] = v[i][0]
    v_modified[i][1] = v[i][1]

#Calculating the original position vector by dot product of v and sigma
P = numpy.dot(v_modified, sigma)
print(P)

x = P[:,0]
#Inverting y axis to visualize beter
y = -P[:,1]

fig, ax = plt.subplots()
ax.scatter(x, y)

for i, txt in enumerate(cities):
    plt.text(x[i],y[i], cities[i])

plt.show()
