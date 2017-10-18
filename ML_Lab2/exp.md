# exercise k-means and image compression

## numpy

  * numpy matrix indexing

  * numpy.where

  * image processing 

    when access image pixel, better not iterate the numpy array storing the pixels cause its low efficient. e.g.. in the proj the pixel number of the processed pic is almost 1.2 millon. if you pick the way snippt 1, program will likely _**"Stop"**_ there(I did not wait for its termination). contrarily, the snippet 2 cost little time(if you debug you will the big diffirence).

    ```
    #  snippet 1
    # for i in range(datas.shape[0]):
        #
        #     cIndex = maxInfo[i]
        #     retCluster[cIndex].append( datas[i] )

    # snippet 2
    for i in range(len(centers)):

        cindArray = np.where(maxInfo == i)
        retCluster[i] = datas[cindArray]
        retClusterIndexs[i] = cindArray
    ```

## matplot

  * matplot.image, matplot.pyplot.figure.axis.imshow(), etc..