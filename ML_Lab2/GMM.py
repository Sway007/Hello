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
    A = np.pow(2 * np.pi, n/2.) * np.pow( np.linalg.det(np.mat(mu)), 0.5 )
    A = 1 / A
    B = np.exp( -0.5 * np.mat(varX - mu) * np.mat(sigma) *
                np.mat(varX - mu).I )
    return A * B


class GMM:

    def __init__(self, dimension):

        self.d = dimension

        # mode arguments
        self._alphas = None
        self._mus = None
        self._varianceMatrix = None

        self.modeInit()

    def modeInit(self):

        self._alphas = np.array([1. / self.d for i in range(self.d)])
        self._mus = np.random.randint(0, 3*self.d, size=self.d)
        self._varianceMatrix = np.eye(self.d, k=0, dtype=float) * 0.1

    def trainMode(self, trainingDatas):

        '''
        :param trainingDatas: expeted type numpy.array
        '''
        assert (trainingDatas[0].shape == 1, self.d), 'training data dimension \
                                                       not matched'
        gammaPosteriorArray = np.array([])



if __name__ == '__main__':

    pass