"Additional Formatting Options for matplotlib"

import matplotlib.pyplot as plt
import numpy as np

###################
# coordinates for example
xcoor = np.array([0, 2, 6, 12, 30])
ycoor = np.array([0, 4, 3, 10, 5])

# linewidth
plt.plot(xcoor, ycoor, linewidth = '10')
plt.show()


# multiple lines
ycoor1 = np.array([0, 2, 6, 12, 30])
ycoor2 = np.array([0, 4, 3, 10, 5])

plt.plot(ycoor1)
plt.plot(ycoor2)
plt.show()


# achsis labels, plot title + position, fonts, grid lines
plt.plot(xcoor, ycoor)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.xlabel("x-achsis-label", fontdict = font2)
plt.ylabel("y-achsis-label", fontdict = font2)

plt.title("Plot Title", fontdict = font1, loc = "left")

# axis = empty --> both grid lines
# linestyles and colors --> checkout markers_lines_colors.py
plt.grid(axis = "x", linestyle = ":", color = "blue")

plt.show()
