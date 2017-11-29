import numpy as np
import random



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

    def train(self, training_data, iter_num, mini_batch_size, eta
    , test_data=None
    ):
        '''
        train by using stochastic gradient descent
        '''
        train_set_size = len(training_data)
        for i in xrange(iter_num):
            
            random.shuffle(training_data)
            mini_batchs = [ training_data[k: k + mini_batch_size]
                for k in xrange(0, train_set_size, mini_batch_size) ]
            for mini_batch in mini_batchs:
                self.learning(mini_batch, eta)

            if test_data:
                print("Epoch {0}: {1} / {2}".format(
                    i, self.evaluate(test_data), train_set_size)
                )
            else:
                print("Epoch {0} complete".format(i))

    def learning(self, batch, eta):
        '''
        update network parameters using gradient descent

        @param
            eta: learning rate
        '''
        # TODO
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        
        rate = eta / len(batch)
        self.weights = [w - rate * nw 
            for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - rate * nb 
            for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        '''
        _Backpropagation_ algoritm, to obtain the partial derivative of params
        '''
        ret_nabla_b = [np.zeros(b.shape) for b in self.biases]
        ret_nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x]
        zs = []

        for b, w in zip(self.biases, self.weights):
            z = w * activation + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        
        # backward
        delta = self.cost_derivative(activations[-1], y) * sigmod_derivative(zs[-1])
        ret_nabla_b[-1] = delta
        ret_nabla_w[-1] = delta * activations[-2]

        for l in xrange(2, self.get_layer_num()):
            z = zs[-l]
            delta = self.weights[-l+1] * delta * sigmod_derivative(z)
            ret_nabla_b[-l] = delta
            ret_nabla_w[-l] = delta * activations[-l-1]

        return ret_nabla_b, ret_nabla_w

    def cost_derivative(self, output_activations, y):
        return output_activations - y

    def output(self, input):
        '''
        get network output
        '''
        ret = input
        for b, w in zip(self.biases, self.weights):
            z = np.mat(w) * np.mat(ret).transpose() + np.mat(b).transpose()
            ret = sigmoid(z)
        return ret
    
    def evaluate(self, test_data):
        
        test_results = [ (np.argmax(self.output(x)), y) 
                        for x, y in test_data ]
        return sum(int(x==y) for x, y in test_results)
        

if __name__=='__main__':
    
    import mnist_loader
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

    net = nnetwork([784,30,10])
    net.train(training_data, 30, 10, 3.0, test_data=test_data)
