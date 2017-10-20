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
    B = np.exp( -0.5 * np.mat(varX - mu) * np.mat(sigma) *
                np.mat(varX - mu).I )
    return A * B


class GMM:

    def __init__(self, modeNum):

        self.n = modeNum

        # mode arguments
        self._alphas = None
        self._mus = None
        self._varianceMatrix = None

        self.modeInit()

    def modeInit(self):

        self._alphas = np.array([1. / self.n for i in range(self.n)])
        self._mus = np.random.randint(0, 3 * self.n, size=self.n)
        self._varianceMatrix = np.eye(self.n, k=0, dtype=float) * 0.1

    def trainMode(self, trainingDatas):

        '''
        :param trainingDatas: expeted type numpy.array
        '''
        assert (trainingDatas[0].shape == 1, self.n), 'training data dimension \
                                                       not matched'
        gammaPosteriorArray = np.array([])



if __name__ == '__main__':

    pass