# Advanced Artificial Intelligence Lab 3 - Search
#
# <https://sustech-cs-courses.github.io/AAI/lab/3/>

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from lab3 import greedysearch, astarsearch


def visualize(mapsize, blocks, init, goal, path=None, title=''):

    """Plot map, blocks, starting point and destination
    """
    fig = plt.figure(0)
    fig.suptitle(title, fontweight='bold', fontsize=18)
    axes = fig.add_subplot(111)

    # init and goal positions
    axes.plot(init[0], init[1], 'ro')
    axes.plot(goal[0], goal[1], 'go')

    # bloc
    for b in blocks:
        rec = patches.Rectangle(b, 1, 1, fc='silver')
        axes.add_patch(rec)

    if path is not None:
        axes.plot(path[:, 0], path[:, 1], '-', color='orange')

    # map
    axes.set_aspect('equal', adjustable='box')
    axes.set_xlim([0, mapsize[0]])
    axes.set_ylim([0, mapsize[1]])
    # axes.set_xticklabels([])
    # axes.set_yticklabels([])
    axes.set_xticks(np.arange(mapsize[0]))
    axes.set_yticks(np.arange(mapsize[1]))
    # axes.tick_params(length=0)
    axes.grid()

    plt.show()
    ### Uncomment this line if you are using IPython/Jupyter notebook ###
    # plt.pause(1)


def main():
    # Problem settings
    ### Design your own map ###
    mapsize = (20, 12)
    # init = (2, 7)
    # goal = (18, 5)
    # blocks = np.array([(6, i) for i in range(4, 12)] +
    #                   [(13, i) for i in range(0, 8)])

    # init = (9, 7)
    # goal = (17, 2)
    # blocks = np.array([(6, i) for i in range(4, 10)] +
    #                   [(i, 4) for i in range(7, 14)] +
    #                   [(13, i) for i in range(5, 10)])
    init = (2, 7)
    goal = (28, 5)
    mapsize = (30, 20)
    blocks = np.array([(5, i) for i in range(2, 20)] + [(23, i) for i in range(0, 15)] + [(15, i) for i in range(4, 20)] + [(9, i) for i in range(0, 15)] + [(i, 11) for i in range(13, 15)] + [(i, 7) for i in range(13, 15)])

    # visualize(mapsize, blocks, init, goal)

    path = greedysearch(mapsize, blocks, init, goal)
    # print(1)        # TODO

    visualize(mapsize, blocks, init, goal, np.array(path), 'Greedy Search')
    
    path = astarsearch(mapsize, blocks, init, goal)

    visualize(mapsize, blocks, init, goal, np.array(path), 'A* Search')

if __name__ == '__main__':
    main()
