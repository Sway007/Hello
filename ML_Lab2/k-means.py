import numpy as np 
import scipy.spatial.distance as distance
import random
import csv

import matplotlib.pyplot as plt

# iterN = 20

def readCSVDatas(fileName):

    with open(fileName) as csvfile:

        reader = csv.reader(csvfile)

        infos = [row[0].split() for row in reader]
        retDatas = [[float(i) for i in info[1:]] for info in infos[1:-1]]

    return np.array(retDatas)


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

    return clustering(centers, datas, 20)


def clustering_medoids(centers, datas, iterNum):

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

        for cluster in retCluster:

            disMatrix_center = distance.cdist(cluster, cluster)
            sum = np.sum(disMatrix_center, axis=0)
            c = np.max(sum)


        iterNum -= 1

    return centers, retCluster

def k_medoids_2d(datas, centerNum):
    '''
    :param datas: numpy.array
    :return: same as k_means_2d
    '''
    centers = getInitCenters(datas, centerNum)




def drawPoints(points, style, axis, markersize=3.):

    points = np.array(points)
    x = points[:, 0]
    y = points[:, 1]
    axis.plot(x, y, style, markersize=markersize)

def draw(datas, centers):

    fig = plt.figure()
    ax = fig.add_subplot(1 , 1 , 1)

    colors = 'bgrcmykw'
    colori = 0

    for oneCluster in datas:

        drawPoints(oneCluster, colors[colori] + 'o', ax)
        colori += 1

    drawPoints(centers, 'k*', ax, markersize=5.)


if __name__ == '__main__':

    size = 1000
    k = 4

    ndatas = readCSVDatas('data_1024.csv')

    centers, clusters = k_means_2d(ndatas, k)
    draw(clusters, centers)

    plt.show()