"Create and format subplots"

import matplotlib.pyplot as plt
import numpy as np

###################
# coordinates for example
coor1 = np.array([0, 2, 6, 12, 30])
coor2 = np.array([0, 4, 3, 10, 5])

# first subplot
plt.subplot(1, 2, 1)
plt.plot(coor1, coor2, color = "green")

# second plot
plt.subplot(1, 2, 2)
plt.plot(coor2, coor1, color = "red")

plt.show()

# explaining the three numbers in the subplot function
# the first two numbers define how the whole plot will look like
# imagine it is a chart
# first number = number of rows
# second number = number of columns
# third number = index of the position of the subplot

# first subplot
plt.subplot(2, 2, 1)
plt.plot(coor1, coor2, color = "green")
plt.title("first")

# second plot
plt.subplot(1, 2, 2)
plt.plot(coor2, coor1, color = "red")
plt.title("second")

# adding a super title
plt.suptitle("Super Title")

plt.show()
