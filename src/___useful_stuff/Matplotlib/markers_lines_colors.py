"Desrciption about different kind of markers"

# source https://www.w3schools.com/python/matplotlib_markers.asp

# import libs
import matplotlib.pyplot as plt
import numpy as np

# define array with coordinates
ycoor = np.array([2, 4, 8, 5, 3])

######################
# markers formatting

# List with possible markers
# Marker    Description
# 'o'       Circle
# '*'	    Star
# '.'	    Point
# ','	    Pixel
# 'x'	    X
# 'X'	    X (filled)
# '+'	    Plus
# 'P'	    Plus (filled)
# 's'	    Square
# 'D'	    Diamond
# 'd'	    Diamond (thin)
# 'p'	    Pentagon
# 'H'	    Hexagon
# 'h'	    Hexagon
# 'v'	    Triangle Down
# '^'	    Triangle Up
# '<'	    Triangle Left
# '>'	    Triangle Right
# '1'	    Tri Down
# '2'	    Tri Up
# '3'	    Tri Left
# '4'	    Tri Right
# '|'	    Vline
# '_'	    Hline


# markers at the end of the coordinates
plt.plot(ycoor, marker = "<")

plt.show()


######################
# using the fmt format string

# marker|line|color

# creates a dotted line in the color red
plt.plot(ycoor, ":r")
plt.show()


# line formatting

# possible line formatting parameters
# Line Syntax	Description
# '-'           Solid line
# ':'	        Dotted line
# '--'	        Dashed line
# '-.'	        Dashed/dotted line


# color formatting
# the use of hex color codes is ok too
# https://www.w3schools.com/colors/colors_hexadecimal.asp
# or html colors
# https://www.w3schools.com/colors/colors_names.asp

# possible color formatting parameters
# Color Syntax	Description
# 'r'	        Red
# 'g'	        Green
# 'b'	        Blue
# 'c'	        Cyan
# 'm'	        Magenta
# 'y'	        Yellow
# 'k'	        Black
# 'w'	        White


######################
# marker size
# ms

plt.plot(ycoor, marker = "o", ms = 20)
plt.show()

######################
# marker edge color
# mec

plt.plot(ycoor, marker = "o", mec = "r")
plt.show()

######################
# marker face color
# mfc

plt.plot(ycoor, marker = "o", mfc = "r")
plt.show()
