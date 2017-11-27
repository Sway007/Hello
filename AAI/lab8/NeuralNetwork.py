import numpy as np

def sigmoid(z):
    
    return 1./(1. + np.exp(-z))

def sigmod_derivative(z):
    
    return sigmoid(z) * (1 - sigmoid(z))


class nnetwork:
    '''
    a sigmoid neural network
    '''

    def __init__(self, size):
        '''
        @param size: -list, [each layer's neuron number]
        '''

        self.size = size

        self.biases = [np.zeros(n) for n in size[1:]]
        # weights: w_{ij}^{l} is the weight
        #        (l-1)th layer's jth neuron  ----> (l)th layer's ith neuron
        self.weights = [np.zeros((m, n)) for m, n in zip(size[1:], size[:-1])]
        
    def get_layer_num(self):
        return len(self.size)

    

if __name__=='__main__':
    net = nnetwork([5,6,2])
