import numpy as np


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
        self._mus = np.array([trainingDatas[6, :], trainingDatas[22, :], trainingDatas[27, :]])
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

            # assert trainingDatas[0].shape == (1, self.n), 'training data dimension \
            #                                                not matched'
            # get probability matrix such as:
            #     x1, x2, ..., xn
            #     -----------------
            # M1 | p11 p22 ...  p1n
            # M2 | p21 p22 ...  p2n
            # ...| ...
            # Mk | pk1 pk2 ...  pkn
            i = 0
            l = []
            for i in range(self.n):
                l.append(self._alphas[i] * np.apply_along_axis(getGaussianDisPro, 1, trainingDatas,
                                                                self._mus[i], self._varianceMatrix[i]))
                # l.append( [ self._alphas[i] * np.apply_along_axis(getGaussianDisPro, 1, x,
                #                                 self._mus[0], self._varianceMatrix[0])
                #             for x in trainingDatas ] )
            probMatrix = np.mat(np.vstack(l))

            # get posterior probability that var j is generate by mode i
            def getPosterior(varInd, modeInd):

                return probMatrix[modeInd, varInd] / np.sum(probMatrix[:, varInd])

            # make new mode arguments
            self._alphas =  np.array([np.sum([getPosterior(j, i)
                                                for j in range(len(trainingDatas))])
                                                for i in range(self.n)])
            self._alphas *= 1./len(trainingDatas)
            assert 0.999 < np.sum(self._alphas) < 1.001, 'Error!'

            self._mus = np.array([ np.sum([getPosterior(j, i) * trainingDatas[j] for j in range(len(trainingDatas))]) / \
                          np.sum([getPosterior(j, i) for j in range(len(trainingDatas))])
                                 for i in range(self.n)]
                                 )

            def vectorSqure(vec):

                t = np.mat(vec).T * np.mat(vec)
                return np.mat(vec).T * np.mat(vec)

            def multiMatixAdd(matrixArray):

                ret = matrixArray[0]
                for m in matrixArray[1:]:

                    ret += m
                return ret

            self._varianceMatrix = np.array([ multiMatixAdd([vectorSqure(trainingDatas[j] - self._mus[i]) * getPosterior(j, i) for j in range(len(trainingDatas))]) / \
                                     np.sum([getPosterior(j, i) for j in range(len(trainingDatas))])
                                     for i in range(self.n)
                                   ])

    def getClusters(self):

        pass


def getTrainingData(file):

    with open(file, 'r') as f:

        infos = [line.split() for line in f]
        datas = [[float(d) for d in row] for row in infos]

    return np.array(datas)

if __name__ == '__main__':

    trainingData = getTrainingData('table4_0')
    gmm = GMM(3, iterNum=50)
    gmm.trainMode(trainingData)
    clusters = gmm.getClusters()