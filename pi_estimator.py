import random
import matplotlib.pyplot as plt
import numpy

circle_points = 0
square_points = 0
interval = 0
N = 5000

x = 0
y = 0
horz = []
ver = []

for i in range(N):
    x = random.uniform(-1,1)
    horz = numpy.append(horz,x)
    y = random.uniform(-1,1)
    ver = numpy.append(ver,y)

    d = x*x + y*y
    if (d <= 1):
        circle_points += 1

    square_points += 1


pi = (4*circle_points)/square_points
print("Pi estimation:", pi)


norm1 = numpy.linalg.norm(horz)
xArray = horz/norm1

norm2 = numpy.linalg.norm(ver)
yArray = ver/norm2



plt.scatter(xArray,yArray)
circle = plt.Circle((0,0), 0.025, fill=False, linewidth = 2)
square = plt.Rectangle(xy = (.025, -.025), width = -0.05, height = 0.05, fill = False, linewidth=2)
plt.gca().add_patch(circle)
plt.gca().add_patch(square)
plt.text(-0.027,-0.027,pi)
plt.show()
