import numpy as np 
import scipy.spatial.distance as distance
import random

import matplotlib.pyplot as plt


def getInitCenters(datas, k):
    '''

    '''
    cs = set()
    while len(cs) < k:
        n = random.randint(0, len(datas) - 1)
        cs.add(n)

    return datas[list(cs)]


def clustering(centers, datas, iterNum):
    '''
    centers: numpy.array
    datas: numpy.array
    return clusters:tuple(centers[], [[c1points], [c2points], ...])
    '''
    while iterNum > 0:

        retCluster = [[] for i in centers]
        
        disMatrix = distance.cdist(datas, centers, metric='euclidean')
        maxInfo = np.argmin(disMatrix, axis=1)
        
        for i in range(datas.shape[0]):
            
            cIndex = maxInfo[i]
            retCluster[cIndex].append( datas[i] )

        centers = np.array([np.mean(i, axis=0) for i in retCluster])

        iterNum -= 1

    return centers, retCluster


def k_means_2d(datas, centerNum):
    '''
    datas: numpy.array
    return clusters:dict{center index: [points]}
    '''
    centers = getInitCenters(datas, centerNum)

    return clustering(centers, datas, 10)


def draw(datas, centers):

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    print(datas)

    tmp = np.concatenate(datas[:], axis=0)
    x = tmp[:,0]
    y = tmp[:,1]

    ax.plot(x, y, 'bo')
    ax.set_xlim(0,30)
    ax.set_ylim(0,30)
    plt.show()


if __name__=='__main__':
    datas = np.array([
        [0,0], [5,5], [3,3], [2,2],
        [20,20], [25,25], [23, 23], [22, 22]
    ])
    centers, clusters = k_means_2d(datas, 2)

    draw(clusters, centers)