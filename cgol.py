# 
# *Conways Game of Life*

# %%
# import libraries
import numpy as np
import matplotlib.pyplot as plt
import random
import time
from matplotlib.animation import FuncAnimation
from itertools import count

# %%
# setup hyperparameters
n=20   # grid size

# %%
def Neighbour(Grid, i, j):
    D = 0
    try:
        D += Grid[i-1,j]
    except IndexError:
        pass
    try:
        D += Grid[i+1,j]
    except IndexError:
        pass
    try:
        D += Grid[i,j-1]
    except IndexError:
        pass
    try:
        D += Grid[i,j+1]
    except IndexError:
        pass
    try:
        D += Grid[i+1,j+1]
    except IndexError:
        pass
    try:
        D += Grid[i-1,j+1]
    except IndexError:
        pass
    try:
        D += Grid[i+1,j-1]
    except IndexError:
        pass
    try:
        D += Grid[i-1,j-1]
    except IndexError:
        pass
    return int(D)

# %%
def Grow(Grid):
    ResGrid = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            D = Neighbour(Grid, i, j)
            if Grid[i, j]==0 :
                if D==3: ResGrid[i, j] = 1
            else :
                if D==2 or D==3: ResGrid[i, j] = 1
    return ResGrid

# %%
# setup initial conditions
Grid = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        Grid[i,j] = random.choice([0, 0, 0, 1])

time = count()

# %%
def animate(i):
    global Grid
    plt.cla()
    plt.imshow(Grid, cmap='gray')
    Grid = Grow(Grid)
    plt.title('Generation: ' + str(next(time)))

# %%
# updation process
anime = FuncAnimation(plt.gcf(), animate, frames=100, interval=1000)
plt.show()

# %%



