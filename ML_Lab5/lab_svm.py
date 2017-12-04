import matplotlib.pyplot as plt
import numpy as np

class data_unit:
    
    def __init__(self, str):
        
        infos = str.split()
        self.feature_num = len(infos) - 1
        self.cl = infos[0]
        self.features = [inf.split(':')[-1] for inf in infos[1:]]

def read_data(path):
    
    with open(path, 'r') as f:

        lines = f.readlines()
        num = len(lines)
        clss = np.zeros(num)

        tmp = lines[0].split()
        feature_num = len(tmp) - 1
        f_lables = [la.split(':')[0] for la in tmp[1:]]
        features = dict.fromkeys(f_lables, [])

        k = 0
        for line in lines:
            infos = line.split()
            clss[k] = infos[0]
            for info in infos[1:]:
                fn_and_f = info.split(':')
                features[fn_and_f[0]].append( fn_and_f[1] )

            k += 1

    return clss, features

if __name__ == '__main__':

    clss, features = read_data('data')
    for i in range(4):
        print(clss[i], ' ', features['1'][i], features['2'][i])