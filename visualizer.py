from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1]-point2[1])**2)

csum = 0
acosum = 0

cbest_path = [[11, 15], [14, 13], [6, 12], [4, 15], [10, 1], [4, 2], [1, 4], [5, 9], [8, 8], [9, 13], 
[11, 15], ]
acobest_path = [[8, 8], [10, 1], [4, 2], [1, 4], [5, 9], [6, 12], [4, 15], [9, 13], [11, 15], [14, 13], 
[8, 8], ]
points = [[8, 8], [14, 13], [4, 15], [6, 12], [4, 2], [10, 1], [5, 9], [1, 4], [11, 15], [9, 13],]
n_points = len(points)

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

axes[0].set_title("Christofides")
axes[1].set_title("Ant Colony Optimization")

for i in range(n_points):
    csum += distance(cbest_path[i], cbest_path[i+1])
    acosum += distance(acobest_path[i], acobest_path[i+1])
    axes[0].plot([cbest_path[i][0], cbest_path[i+1][0]],
            [cbest_path[i][1], cbest_path[i+1][1]],
            c='g', linestyle='-', linewidth=0.5, marker='.', markersize=8)
    axes[1].plot([acobest_path[i][0], acobest_path[i+1][0]],
            [acobest_path[i][1], acobest_path[i+1][1]],
            c='g', linestyle='-', linewidth=0.5, marker='.', markersize=8)
axes[0].annotate("Total weight: " + str(csum), (0,0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top', fontsize=12)
axes[1].annotate("Total weight: " + str(acosum), (0,0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top', fontsize=12)

plt.show()