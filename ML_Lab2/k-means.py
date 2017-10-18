import numpy as np 
import scipy.spatial.distance as distance
import random
import csv

import matplotlib.pyplot as plt
import matplotlib.animation as anim

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

    historyDatas = []  #    for the animation

    while iterNum > 0:

        retCluster = [[] for i in centers]
        
        disMatrix = distance.cdist(datas, centers, metric='euclidean')
        maxInfo = np.argmin(disMatrix, axis=1)
        
        for i in range(datas.shape[0]):
            
            cIndex = maxInfo[i]
            retCluster[cIndex].append( datas[i] )

        historyDatas.append([centers, retCluster])

        centers = np.array([np.mean(i, axis=0) for i in retCluster])

        iterNum -= 1

    historyDatas.append([centers, retCluster])

    return (centers, retCluster, historyDatas)


def k_means_2d(datas, centerNum):
    '''
    datas: numpy.array
    return clusters:dict{center index: [points]}
    '''
    centers = getInitCenters(datas, centerNum)

    return clustering(centers, datas, 10)


def clustering_medoids(centers, datas, iterNum):

    '''
    centers: numpy.array
    datas: numpy.array
    return clusters:tuple(centers[], [[c1points], [c2points], ...])
    '''
    while iterNum > 0:

        retCluster = [[] for i in centers]

        disMatrix = distance.cdist(datas, centers, metric='euclidean')
        minInfo = np.argmin(disMatrix, axis=1)

        for i in range(datas.shape[0]):

            cIndex = minInfo[i]
            retCluster[cIndex].append( datas[i] )

        cindx = 0
        for cluster in retCluster:

            disMatrix_center = distance.cdist(cluster, cluster)

            # print(disMatrix_center)

            sm = np.sum(disMatrix_center, axis=0)
            ind = np.argmin(sm, axis=0)

            centers[cindx] = cluster[ind]
            cindx += 1

        iterNum -= 1

    return centers, retCluster

def k_medoids_2d(datas, centerNum):
    '''
    :param datas: numpy.array
    :return: same as k_means_2d
    '''
    centers = getInitCenters(datas, centerNum)

    return clustering_medoids(centers, datas, 20)


def drawPoints(points, style, axis, markersize=3.):

    points = np.array(points)
    x = points[:, 0]
    y = points[:, 1]
    artist,  = axis.plot(x, y, style, markersize=markersize)

    return artist

def draw(datas, centers, ax):

    colors = 'bgrcmykw'
    colori = 0

    pointsArtist = []

    for oneCluster in datas:

        pa = drawPoints(oneCluster, colors[colori] + 'o', ax)

        pointsArtist.append(pa)
        colori += 1

    centerArtist = drawPoints(centers, 'y*', ax, markersize=5.)

    return centerArtist, pointsArtist


def update(newData, centerArtist, clustersArtist):

    centers, clusters = newData

    xdca, ydca = np.array(centers)[:, 0], np.array(centers)[:, 1]
    centerArtist.set_data(xdca, ydca)

    clusterInfos = zip(clustersArtist, clusters)
    for info in clusterInfos:

        ca, cdata = info
        xd = np.array(cdata)[:, 0]
        yd = np.array(cdata)[:, 1]
        ca.set_data(xd, yd)


if __name__ == '__main__':

    size = 1000
    k = 3

    ndatas = readCSVDatas('data_1024.csv')

    # ndatas = np.array([
    #     [1,1], [2,2], [3,3], [4,4],
    #     [22,22], [23,23], [24,24], [25,25]
    # ])

    fig = plt.figure()

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title('K-means')
    centers, clusters, historyDatas = k_means_2d(ndatas, k)
    ca, pas = draw(clusters, centers, ax1)

    ani = anim.FuncAnimation(fig, update, frames=historyDatas,
                       fargs=(ca, pas), interval=800)


    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title('K-medoids')
    centers, clusters = k_medoids_2d(ndatas, k)
    draw(clusters, centers, ax2)

    plt.show()