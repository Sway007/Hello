import matplotlib.pyplot as plt
import numpy as np


def read_data(path):
    
    with open(path, 'r') as f:

        lines = f.readlines()
        num = len(lines)
        clss = np.zeros(num)

        tmp = lines[0].split()
        f_lables = [la.split(':')[0] for la in tmp[1:]]
        features = dict([(i, np.zeros(num)) for i in f_lables])

        k = 0
        for line in lines:
            infos = line.split()
            clss[k] = int(infos[0])
            for info in infos[1:]:
                fn_and_f = info.split(':')
                features[fn_and_f[0]][k] = ( float(fn_and_f[1]) )

            k += 1

    return clss, features

if __name__ == '__main__':

    clss, features = read_data('data')
    for i in range(4):
        print(clss[i], ' ', features['1'][i], features['2'][i])
    
    figure = plt.figure()
    ax = figure.add_subplot(111)

    ind_cl1 = (np.where(clss == -1))[0]
    ax.plot(features['1'][ind_cl1], features['2'][ind_cl1], 'ro')

    ind_cl2 = np.where(clss == 1)[0]
    ax.plot(features['1'][ind_cl2], features['2'][ind_cl2], 'b*')

    plt.show()