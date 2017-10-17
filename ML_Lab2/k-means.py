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


def drawPoints(points, style, axis):

    points = np.array(points)
    x = points[:, 0]
    y = points[:, 1]
    axis.plot(x, y, style)

def draw(datas, centers):

    fig = plt.figure()
    ax = fig.add_subplot(1 , 1 , 1)

    colors = 'bgrcmykw'
    colori = 0

    for oneCluster in datas:

        drawPoints(oneCluster, colors[colori] + 'o', ax)
        colori += 1

    # tmp = np.concatenate(datas[:], axis=0)
    # drawPoints(tmp, 'bo', ax)

    drawPoints(centers, 'k*', ax)

    plt.show()


if __name__ == '__main__':

    size = 1000
    k = 6

    xarray = np.random.randint(50000, size=size).reshape(size, 1)
    yarray = np.random.randint(50000, size=size).reshape(size, 1)

    ndatas = np.concatenate((xarray, yarray), axis=1)


    centers, clusters = k_means_2d(ndatas, k)

    draw(clusters, centers)