import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def draw(maze, Q): 
    fig, ax = plt.subplots()
    patches = []
    for j in range(5):
        for i in range(5):
            polygon1 = Polygon(
                [[10.0 / 10 * i + 9.0 / 10, 10.0 * j / 10 + 1.0 / 10],
                 [10.0 * i / 10 + 9.0 / 10, 10.0 * j / 10 + 9.0 / 10],
                 [10.0 * i / 10 + 5.0 / 10, 10.0 * j / 10 + 5.0 / 10]], True)
            polygon2 = Polygon(
                [[10.0 * i / 10 + 1.0 / 10, 10.0 * j / 10 + 1.0 / 10],
                 [10.0 * i / 10 + 1.0 / 10, 10.0 * j / 10 + 9.0 / 10],
                 [10.0 * i / 10 + 5.0 / 10, 10.0 * j / 10 + 5.0 / 10]], True)
            polygon3 = Polygon(
                [[10.0 * i / 10 + 1.0 / 10, 10.0 * j / 10 + 1.0 / 10],
                 [10.0 * i / 10 + 9.0 / 10, 10.0 * j / 10 + 1.0 / 10],
                 [10.0 * i / 10 + 5.0 / 10, 10.0 * j / 10 + 5.0 / 10]], True)
            polygon4 = Polygon(
                [[10.0 * i / 10 + 1.0 / 10, 10.0 * j / 10 + 9.0 / 10],
                 [10.0 * i / 10 + 9.0 / 10, 10.0 * j / 10 + 9.0 / 10],
                 [10.0 * i / 10 + 5.0 / 10, 10.0 * j / 10 + 5.0 / 10]], True)
            patches.append(polygon1)
            patches.append(polygon2)
            patches.append(polygon3)
            patches.append(polygon4)
    polygon = Polygon([[0.0, 0.0], [5.0, 0.0], [5.0, 0.1], [0.0, 0.1]], True)
    patches.append(polygon)
    polygon = Polygon([[0.0, 0.0], [0.0, 5.0], [0.1, 5.0], [0.1, 0.0]], True)
    patches.append(polygon)
    polygon = Polygon([[5.0, 5.0], [5.0, 0.0], [4.9, 0.0], [4.9, 5.0]], True)
    patches.append(polygon)
    polygon = Polygon([[5.0, 5.0], [0.0, 5.0], [0.0, 4.9], [5.0, 4.9]], True)
    patches.append(polygon)

    for i in range(5):
        for j in range(4):
            if maze[4*i+j] == 1:
                polygon = Polygon([[10.0 * j / 10 + 0.95, 10.0 * i / 10 + 0.05],
                                   [10.0 * j / 10 + 0.95, 10.0 * i / 10 + 1.05],
                                   [10.0 * j / 10 + 1.05, 10.0 * i / 10 + 1.05],
                                   [10.0 * j / 10 + 1.05, 10.0 * i / 10 + 0.05]],
                                  True)
                patches.append(polygon)
    for i in range(4):
        for j in range(5):
            if maze[20+5*i+j] == 1:
                polygon = Polygon([[10.0 * j / 10 + 0.05, 10.0 * i / 10 + 0.95],
                                   [10.0 * j / 10 + 1.05, 10.0 * i / 10 + 0.95],
                                   [10.0 * j / 10 + 1.05, 10.0 * i / 10 + 1.05],
                                   [10.0 * j / 10 + 0.05, 10.0 * i / 10 + 1.05]],
                                  True)
                patches.append(polygon)
    p = PatchCollection(patches, cmap=matplotlib.cm.gray, alpha=0.4)
    colors = np.ones([104 + int(np.sum(maze))])

    for i in range(25):
        maxval = Q[i].max(0)
        for j in range(4):
            if Q[i][j] == maxval:
                colors[4*i+3-j] = 0.1
    for i in range(4 + int(np.sum(maze))):
        colors[100+i] = 0

    # show Q values
    p.set_array(np.array(colors))
    ax.set_xlim([0, 5])
    ax.set_ylim([0, 5])
    ax.add_collection(p)
    for i in range(5):
        for j in range(5):
            plt.text(1.0 * i + 0.6, 1.0 * j + 0.35,
                     "{0:.2f}".format(Q[5 * j + i, 3]))
            plt.text(1.0 * i + 0.1, 1.0 * j + 0.35,
                     "{0:.2f}".format(Q[5 * j + i, 2]))
            plt.text(1.0 * i + 0.35, 1.0 * j + 0.1,
                     "{0:.2f}".format(Q[5 * j + i, 1]))
            plt.text(1.0 * i + 0.35, 1.0 * j + 0.6,
                     "{0:.2f}".format(Q[5 * j + i, 0]))

    plt.show()
