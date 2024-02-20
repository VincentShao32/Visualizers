import numpy as np
import matplotlib.pyplot as plt

x = np.array([5, 10, 50, 100, 150, 200, 250, 300])
cy = np.array([1.05, 1.28, 1.37, 1.30, 1.30, 1.37, 1.39, 1.34])
acoy = np.array([1.03, 1.13, 1.18, 1.28, 1.36, 1.41, 1.43, 1.46])


fig, ax = plt.subplots(1, 1, figsize=(8, 8))

ax.set_title("Graph Size vs Approximation Ratio")
for i in range(len(x)):
    ax.plot(x[i], cy[i], marker=".", c="b", markersize=10)
    ax.plot(x[i], acoy[i], marker=".", c="r", markersize=10)


ax.set_xlabel("Graph Size (vertices)")
ax.set_ylabel("Approximation Ratio")
plt.show()