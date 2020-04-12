r = [x for x in range(1,31)]

t = []
import math

for i in r:
    t.append(int((math.log(0.02)/math.log(1-0.899**i)))+1)

print(t)