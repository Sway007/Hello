__author__ = 'Sway007'

import DataTypes
from DataTypes import *
from collections import deque

def trainingDataPreprocess(dataFile):

    DataTypes.VALUESET_LIST = [set() for i in range(DataTypes.ATTRIBUTE_NUM)]

    with open(dataFile, 'r+', encoding='utf-8') as f:
        for line in f:
            s = line.split(maxsplit=4)
            for i in range(len(s)):
                s[i] = s[i].strip()
            DataTypes.ALL_DATA_RECORDS_LIST.append(s)

            for i in range(len(s)):
                DataTypes.VALUESET_LIST[i].add(s[i])

    DataTypes.CLASSIFICATION_SET = DataTypes.VALUESET_LIST[DataTypes.ATTR_RESULT_INDEX]




def id3():
    # TODO
    pass


########## test function ###############
def printDict(d):
    for k, v in d.items():
        print(k, ' :')
        if isinstance(v, list):
            for item in v:
                print(item)
        else:
            print(v, '\n')

def printDecisionTree(root, file):
    f = open(file, 'w')
    print('[root ;attr index: {}]'.format(root.nextNodeDict[0].attrIndex), file=f)
    queue = deque([])
    idx = 0
    queue.append([-1, root.nextNodeDict[0], -1, idx, -1])
    curRow = 0
    while queue:

        info = queue.pop()
        curNode = info[1]
        parentRow = info[2]
        nodeRow = parentRow + 1
        parentId = info[3]

        for k, v in curNode.nextNodeDict.items():

            if v is None:
                continue

            if curRow < nodeRow:
                print('\n' + '*' * 30, file=f)
                curRow += 1
            idx += 1

            if v.result is not None:
                print('**{} --> {} | pid: {}**\t'.format(k, v.result, parentId), end='  ', file=f)
            else:
                queue.appendleft([k, v, nodeRow, idx, parentId])
                print('[id: {}, parent value: {} | attr index: {}, pid: {}]  '.format(idx, k, v.attrIndex, parentId), end=' ', file=f)

    f.close()

########################################

if __name__ == '__main__' :
    trainingDataPreprocess('lenses.txt')
    # print(getEntropy(ALL_DATA_RECORDS_LIST[:5]))
    # printDict(splitTrainingData(ALL_DATA_RECORDS_LIST[:], 4))
    # print(getAttrEntropySum(ALL_DATA_RECORDS_LIST, 4))
    # print(getBestAttrIndex(ALL_DATA_RECORDS_LIST, [i for i in range(5) if i != ATTR_RESULT_INDEX]))
    tree = buildingTree(ALL_DATA_RECORDS_LIST, 1)
    printDecisionTree(tree, 'debug_log_id3.txt')

    treeC45 = buildingTree(ALL_DATA_RECORDS_LIST, 2)
    printDecisionTree(treeC45, 'debug_log_c45.txt')