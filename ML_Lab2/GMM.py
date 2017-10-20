import numpy as np


class GMM:

    def __init__(self, dimension):

        self.d = dimension

        # mode arguments
        self._alphas = None
        self._mus = None
        self._varianceMatrix = None

    def modeInit(self):

        self._alphas = np.array([1. / self.d for i in range(self.d)])
        self._mus = np

if __name__ == '__main__':
    pass