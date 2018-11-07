'''
We are using random.uniform() to allow for random numbers between -1.0 and 1.0, allowing all the points to be plotted, and not just 1/4 of it (not the most elegant code, but it is spelled-out to learn the basics of the Monte Carlo Simulation):
'''

import matplotlib.pyplot as plt
import random

inside = 0
n = 10**3

x_inside = []
y_inside = []
x_outside = []
y_outside = []

for _ in range(n):
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)
    if x**2+y**2 <= 1:
        inside += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)
        
'''
To estimate pi, the points in the circle correspond to the area of the circle enclosing it (pi*radius^2) and the total points correspond to the area of the square enclosing it (2*radius)^2. So this translates into:

(points in the circle)/(total points) = (pi*radius^2)/(2*radius)^2

Solving for pi, the equation becomes:

pi=4*(points in the circle)/(total points)
'''
        
pi = 4*inside/n
print(pi)

#Plot the points inside and outside the circle:
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.scatter(x_inside, y_inside, color='g', marker='s')
ax.scatter(x_outside, y_outside, color='r', marker='s')
fig.show()
