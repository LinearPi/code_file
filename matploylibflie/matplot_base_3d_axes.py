from matplotlib import pyplot as plt
import numpy as np 
import matplotlib as mpl 

from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['font.size'] = 10

samplse = 25
x = np.random.normal(5,1,samplse)
y = np.random.normal(3,0.5,samplse)

fig = plt.figure()
ax = fig.add_subplot(211, projection='3d')

# compute 2d histogran
hist, xedges, yedges = np.histogram2d(x, y, bins=10)

# compute location of the x,y bar position
elements = (len(xedges) - 1) * (len(yedges) -1)
xpos, ypos = np.meshgrid(xedges[: -1]+ .25, yedges[: -1]+.025)

xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(elements)

# make every bar the same width in base
dx = 0.1*np.ones_like(zpos)
dy = dx.copy()

dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', alpha=0.4)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# plot the same x,y corrrelation in scatter plot
# for comparison
ax2 = fig.add_subplot(212)
ax2.scatter(x,y)
ax2.set_xlabel('X Axis')
ax2.set_ylabel('Y Axis')

plt.show