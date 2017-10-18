import numpy as np
import matplotlib.image as mtimg
import matplotlib.pyplot as plt

from k_means import k_means

def imgWithKmeans(imgFile, k):

    rawData = mtimg.imread(imgFile)

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.set_title('origin img')
    ax2 = fig.add_subplot(122)
    ax2.set_title('k = {}'.format(k))

    ax1.imshow(rawData)

    pixelArray = np.concatenate([i for i in rawData], axis=0)
    imgSize = rawData.shape

    pixelClass, _, _, clusterIndexs = k_means(pixelArray, k, False)

    infos = zip(pixelClass, clusterIndexs)
    for info in infos:

        pixel, indexs = info
        pixelArray[indexs] = pixel

    newImg = pixelArray.reshape(imgSize)
    ax2.imshow(newImg)

    plt.show()
    # mtimg.imsave('kmeans.png', newImg, format='png')

def main():

    imgWithKmeans('me.png', 4)

if __name__ == '__main__':

    main()
