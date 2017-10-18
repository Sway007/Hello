import numpy as np
import matplotlib.image as mtimg

from k_means import k_means

def imgWithKmeans(imgFile, k):

    rawData = mtimg.imread(imgFile)
    pixelArray = np.concatenate([i for i in rawData], axis=0)
    imgSize = rawData.shape[0:2]

    pixelClass, clusters, _ = k_means(pixelArray, k, False)

    print(pixelArray)

def main():

    imgWithKmeans('me.png', 2)

if __name__ == '__main__':

    main()
