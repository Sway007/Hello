__author__ = 'Sway007'

import numpy
import sys
from collections import deque

LEASTNUM = 4

# ------------------------------------------------
# ============ for CART ================

class binaryNode:

     def __init__(self, splitPoint, value):

         self.spoint = splitPoint
         self.value = value                     # average value
         self.lessNext = None
         self.greatNext = None

     def isLeaf(self):

         return self.spoint < 0


def isSplitable(records, attrIndex):

    s = set([i[attrIndex] for i in records])
    return len(records) > LEASTNUM and len(s) > 1


def getVariance(records, average=None):

    l = len(records)
    if average is None:
        average = sum([r[-1] for r in records]) / l

    return sum( pow( r[-1] - average, 2) for r in records ) / l


def regressionSplit(records, attrIndex):

    attrValueSet = list(set([i[attrIndex] for i in records]))
    vll = attrValueSet[0]
    variance = sys.float_info.max
    retRecordsL = []
    retRecordsG = []
    retValA = 0

    if isSplitable(records, attrIndex) and variance > 1.0 :

        for vlg in attrValueSet[1:]:

            # get the variance
            vla = float((vll + vlg) / 2)
            recordsL = [a[:] for a in records if a[attrIndex] <= vla]
            recordsG = [a[:] for a in records if a[attrIndex] > vla]

            tmpvariance = getVariance(recordsL) * len(recordsL) + getVariance(recordsG) * len(recordsG)


            if variance > tmpvariance:
                variance = tmpvariance
                retRecordsL = recordsL
                retRecordsG = recordsG
                retValA = vla

            vll = vlg

    else:
        retValA = -1
    # for i in tmplist:
    #     print(i)
    average = sum([i[-1] for i in records]) / len(records)

    return retValA, retRecordsL, retRecordsG, average

def buildTree(trainingRecords):
    '''

    :param trainingRecords:
    :return: a binaryNode with left and right children
    '''

    if not isSplitable(trainingRecords, 0):
        return
    infos = regressionSplit(trainingRecords, 0)     # TODO
    rootNode = binaryNode(infos[0], infos[-1])
    queue = deque([infos[1], infos[2], rootNode])

    while len(queue) > 0:

        parentNode = queue.pop()
        curGRecords = queue.pop()

        # if isSplitable(curGRecords, 0):

        curInfos = regressionSplit(curGRecords, 0)
        newGNode = binaryNode(curInfos[0], curInfos[-1])
        parentNode.greatNext = newGNode
        if newGNode.spoint > 0:
            queue.extendleft([newGNode, curInfos[2], curInfos[1]])


        curLRecords = queue.pop()
        # if isSplitable(curLRecords, 0):

        curInfos = regressionSplit(curLRecords, 0)
        newLNode = binaryNode(curInfos[0], curInfos[-1])
        parentNode.lessNext = newLNode
        if newLNode.spoint > 0:
            queue.extendleft([newLNode, curInfos[2], curInfos[1]])

    return rootNode


def treeMergeWithParentNode(parentNode, records):
    '''

    :param parentNode: root of the try-to-merge subtree
    :param records:
    :return:
    '''



def treePrune(treeRoot, records):
    '''
    method 1.
    1.depth search tree to find current 2 merge-able leaf nodes
    2.perform tree merge if pre-merge variance > after-merge variance

    TODO
    method 2.
    1.split origin records into:
            [[sub-records_1_a, spoint1], [sub-records_1_b, spoints1],
             [sub-records_2_a, spoint2], [sub-records_2_a, spoints2],
             ...
             ...
             [sub-records_i_a, spointi], [sub-records_i_a, spointsi],
             ...
             ...]
    2.try to merge sub-records with the same spoints.
    3.rebuild tree according to the spoints:
            **all the spoints in the list above are the attr _spoint_ of leaf node**
    :param treeRoot:
    :return:
    '''

    # 因为n0 = n2 + 1 所以所有非叶节点就是分裂点

    # split the origin records
    # get all split points
    splitPoints = []
    stack = deque(treeRoot)
    while(len(stack) > 0):

        curParent = stack.pop()
        if curParent.isleaf:
            continue

        elif curParent.lessNext.isleaf and curParent.greatNext.isleaf:           # second-level-leaf-node
            visit curParent

        else:
            stack.extend(curParent.greatNext, curParent.lessNext)



# ------------------------------------------------

def trainingDataPreprocess(dataFile):
    '''
    :param dataFile:
    :return: numpy.array which is sorted
    '''

    l = []
    with open(dataFile, 'r+') as f:
        for line in f:
            s = line.split()
            for i in range((len(s))):
                s[i] = float(s[i])

            l.append(s)
        l.sort(key=lambda itr: itr[0])
    return l

def getTestRecords(dataFile):

    ret = []
    with open(dataFile, 'r+') as f:
        for line in f:
            s = [float(i) for i in line.split()]
            ret.append(s)

    return ret

def predictValue(treeRoot, testData):

    curBinaryNode = treeRoot
    while curBinaryNode.spoint > 0:
        if testData == curBinaryNode.spoint:
            break
        elif testData > curBinaryNode.spoint:
            curBinaryNode = curBinaryNode.greatNext
        else:
            curBinaryNode = curBinaryNode.lessNext

    return curBinaryNode.value

if __name__ == '__main__':

   datas = trainingDataPreprocess('train.txt')
   # print(numpy.array(datas))
   # t = regressionSplit(datas, 0)
   # print(t)
   treeRoot = buildTree(datas)
   testDatas = getTestRecords('test.txt')

   fileName = 'testOutput'
   with open(fileName, 'w') as output:

       for record in testDatas:

            p = predictValue(treeRoot, record[0])
            record.append(p)
            print(record, file=output)

