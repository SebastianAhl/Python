"Examples for different plot styles"

import matplotlib.pyplot as plt
import numpy as np

###################
# coordinates for example
coor1 = np.array([0, 2, 6, 12, 30])
coor2 = np.array([0, 4, 3, 10, 5])
colors = np.array([0, 25, 50, 75, 100])
sizes = np.array([10, 60, 110, 160, 210])

# Scatterplot
# how to color each dot: https://www.w3schools.com/python/matplotlib_scatter.asp
# transparency with alpha

plt.scatter(coor1, coor2, c = colors, s = sizes, alpha = 0.5)

plt.scatter(coor2, coor1, color = "red")

# colorbar at the side
plt.colorbar()

plt.show()


# Bars
