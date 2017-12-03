import numpy as np
import NeuralNetwork as nn


def train(images, one_hot_labels):
    
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

    net = nn.nnetwork([3072, 120, 10])

    net.train(training_data, 10, 40, 3.0, test_data=test_data)


# def predict(images):
#     # Return a Numpy ndarray with the length of len(images).
#     # e.g. np.zeros((len(images),), dtype=int) means all predictions are 'airplane's
#     raise NotImplementedError
