"Basic example on how to draw a line with Matplotlib & Numpy"

import matplotlib.pyplot as plt
import numpy as np

# coordinates for the line
# creates a line from 0/0 to 6/250
xcoor = np.array([0, 6])
ycoor = np.array([0, 250])

# creates the diagram
plt.plot(xcoor, ycoor)

# shows the diagram
plt.show()

###################
# drawing without a line, draw with points
plt.plot(xcoor, ycoor, "o")
plt.show()

###################
# line with multiple points
xcoor = np.array([0, 2, 6, 12, 30])
ycoor = np.array([0, 4, 3, 10, 5])

plt.plot(xcoor, ycoor)
plt.show()

###################
# without x-coordinates
# x will be [1,2,3,..]
plt.plot(ycoor)
plt.show()
