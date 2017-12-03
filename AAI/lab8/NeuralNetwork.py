import numpy as np
import random



def sigmoid(z):
    
    return 1./(1. + np.exp(-z))

def sigmod_derivative(z):

    return np.array(sigmoid(z)) * np.array((1 - sigmoid(z)))


class nnetwork:
    '''
    a sigmoid neural network
    '''

    def __init__(self, size):
        '''
        @param size: -list, [each layer's neuron number]
        '''

        self.size = size

        self.biases = [np.random.randn(n, 1) for n in size[1:]]
        # weights: w_{ij}^{l} is the weight
        #        (l-1)th layer's jth neuron  ----> (l)th layer's ith neuron
        self.weights = [np.random.randn(m, n) for m, n in zip(size[1:], size[:-1])]
        
    def get_layer_num(self):
        return len(self.size)

    def train(self, training_data, iter_num, mini_batch_size, eta
    , test_data=None
    ):
        '''
        train by using stochastic gradient descent
        '''
        train_set_size = len(training_data)
        for i in range(iter_num):
            
            random.shuffle(training_data)
            mini_batchs = [ training_data[k: k + mini_batch_size]
                for k in range(0, train_set_size, mini_batch_size) ]
            for mini_batch in mini_batchs:
                self.learning(mini_batch, eta)

            if test_data:
                print("Epoch {0}: {1} / {2}".format(
                    i, self.evaluate(test_data), len(test_data))
                )
            else:
                print("Epoch {0} complete".format(i))

    def learning(self, batch, eta):
        '''
        update network parameters using gradient descent

        @param
            eta: learning rate
        '''
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
        pass

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
            z = np.dot(w, activation) + np.mat(b)
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        
        # backward
        delta = np.array(self.cost_derivative(activations[-1], y)) * np.array(sigmod_derivative(zs[-1]))
        ret_nabla_b[-1] = delta
        ret_nabla_w[-1] = delta * activations[-2].transpose()

        for l in range(2, self.get_layer_num()):
            z = zs[-l]
            delta = np.array(np.mat(self.weights[-l+1]).transpose() * np.mat(delta)) * np.array(sigmod_derivative(z))
            ret_nabla_b[-l] = delta
            ret_nabla_w[-l] = np.mat(delta) * np.mat(activations[-l-1]).transpose()

        return ret_nabla_b, ret_nabla_w

    def cost_derivative(self, output_activations, y):
        return output_activations - y

    def output(self, input):
        '''
        get network output
        '''
        ret = input
        for b, w in zip(self.biases, self.weights):
            z = np.mat(w) * np.mat(ret) + np.mat(b)
            ret = sigmoid(z)
        return ret
    
    def evaluate(self, test_data):
        
        test_results = [ (np.argmax(self.output(x)), y) 
                        for x, y in test_data ]
        return sum(int(x==y) for x, y in test_results)
        

if __name__ == '__main__':

    import cifar10
    def data_reshape(data, type_img=True):

        if type_img:
            return data.reshape(-1, 3072,1)
        else:
            return data.reshape(-1, 10, 1)

    images_train, cls_idx_train, labels_train = cifar10.load_training_data()
    images_train = data_reshape(images_train)
    labels_train = data_reshape(labels_train, type_img=False)
    training_data = [(x, y) for x, y in zip(images_train, cls_idx_train)]

    images_test, cls_idx_test, lables_test = cifar10.load_test_data()
    images_test = data_reshape(images_test)
    lables_test = data_reshape(lables_test, type_img=False)
    test_data = [(x, y) for x, y in zip(images_test, cls_idx_test)]

    net = nnetwork([3072, 50, 10])

    net.train(training_data, 10, 40, 3.0, test_data=test_data)
