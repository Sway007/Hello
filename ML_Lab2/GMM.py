import numpy as np
import matplotlib.pyplot as plt
from k_means import draw


def getGaussianDisPro(varX, mu, sigma):
    '''
    :param varX: numpy.array
    :param mu: the mean value argument in Gaussian distribution, \
            and mu has the same shape as varX
    :param sigma: the co-variance matrix
    :return: the probability of varX in distribution
    '''
    _, n = np.mat(varX).shape
    A = np.power(2 * np.pi, n / 2.) * np.power( np.linalg.det(np.mat(sigma)), 0.5 )
    A = 1 / A
    B = np.exp( -0.5 * np.mat(varX - mu) * np.mat(sigma).I *
                np.mat(varX - mu).T )

    return np.asscalar(A * B)

# get posterior probability that var j is generate by mode i
def getPosterior(varInd, modeInd, probMatrix):

    tmp = probMatrix[modeInd, varInd] / np.sum(probMatrix[:, varInd])
    return tmp


class GMM:

    def __init__(self, modeNum, iterNum=10):

        self.n = modeNum

        # mode arguments
        self._alphas = None
        self._mus = None
        self._varianceMatrix = None
        self._iterNum = iterNum

    def modeInit(self, trainingDatas):

        d, = trainingDatas[0].shape
        self._alphas = np.array([1. / self.n for i in range(self.n)])
        # self._mus = np.random.randint(0, 3 * len(trainingData), size=self.n)
        # TODO just for test, delete below
        self._mus = np.array([trainingDatas[5, :], trainingDatas[21, :], trainingDatas[26, :]])
        # Done
        self._varianceMatrix = [np.eye(d, k=0, dtype=float) * 0.1 for i in range(self.n)]

    def trainMode(self, trainingDatas):

        '''
        :param trainingDatas: expeted type numpy.array
        '''
        self.modeInit(trainingData)

        count = 0
        while count < self._iterNum:

            count += 1

            # get probability matrix such as:
            #     x1, x2, ..., xn
            #     -----------------
            # M1 | p11 p22 ...  p1n
            # M2 | p21 p22 ...  p2n
            # ...| ...
            # Mk | pk1 pk2 ...  pkn
            l = []
            for i in range(self.n):
                l.append(self._alphas[i] * np.apply_along_axis(getGaussianDisPro, 1, trainingDatas,
                                                                self._mus[i], self._varianceMatrix[i]))
            probMatrix = np.mat(np.vstack(l))

            # make new mode arguments
            self._alphas = np.array([np.sum([getPosterior(j, i, probMatrix)
                                                for j in range(len(trainingDatas))])
                                                for i in range(self.n)])
            self._alphas *= 1. / len(trainingDatas)
            assert 0.999 < np.sum(self._alphas) < 1.001, 'Error!'

            def vectorSqure(vec):

                t = np.mat(vec).T * np.mat(vec)
                return np.mat(vec).T * np.mat(vec)

            def multiMatixAdd(matrixArray):

                ret = matrixArray[0]
                for m in matrixArray[1:]:

                    ret += m
                return ret

            self._mus = np.array([ multiMatixAdd([getPosterior(j, i, probMatrix) * trainingDatas[j] for j in range(len(trainingDatas))]) / \
                                   np.sum([getPosterior(j, i, probMatrix) for j in range(len(trainingDatas))])
                                   for i in range(self.n)]
                                 )

            self._varianceMatrix = np.array([ multiMatixAdd([vectorSqure(trainingDatas[j] - self._mus[i]) * getPosterior(j, i, probMatrix) for j in range(len(trainingDatas))]) / \
                                     np.sum([getPosterior(j, i, probMatrix) for j in range(len(trainingDatas))])
                                     for i in range(self.n)
                                   ])


    def getClusters(self, datas):
        '''
        :param datas: numpy.array
        :return: cluster data index in datas
        '''

        l = []
        for i in range(self.n):
            l.append(self._alphas[i] * np.apply_along_axis(getGaussianDisPro, 1, datas,
                                                            self._mus[i], self._varianceMatrix[i]))
        probMatrix = np.mat(np.vstack(l))
        posteriorMatrix = np.mat([[getPosterior(j, i, probMatrix) for j in range(len(datas))] for i in range(self.n)])

        clusterIndArray = np.argmax(posteriorMatrix, axis=0)
        retClusters = [np.where(clusterIndArray == i)[-1] for i in range(self.n)]

        retCenters = self._mus

        return retClusters, retCenters


def getTrainingData(file):

    with open(file, 'r') as f:

        infos = [line.split() for line in f]
        datas = [[float(d) for d in row] for row in infos]

    return np.array(datas)

if __name__ == '__main__':

    trainingData = getTrainingData('table4_0')
    iterNum = 50
    gmm = GMM(3, iterNum=iterNum)
    gmm.trainMode(trainingData)
    clusters, centers = gmm.getClusters(trainingData)

    # visualize
    fig = plt.figure()
    fig.suptitle('Gaussian Mixture Mode Clustering')
    ax = fig.add_subplot(111)
    ax.set_title('Iteration Number = {}'.format(iterNum))
    ax.set_xlim(0.1, 0.9)
    ax.set_ylim(0, 0.8)

    datas = [trainingData[index] for index in clusters]
    draw(datas, ax, centers)

    plt.show()