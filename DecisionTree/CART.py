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
         self.value = value
         self.lessNext = None
         self.greatNext = None


def isSplitable(records, attrIndex):
    s = set([i[attrIndex] for i in records])
    return len(records) > LEASTNUM and len(s) > 1

def regressionSplit(records, attrIndex):

    attrValueSet = list(set([i[attrIndex] for i in records]))
    vll = attrValueSet[0]
    errsum = sys.float_info.max
    retRecordsL = []
    retRecordsG = []
    retValA = 0

    # tmplist = []
    if isSplitable(records, attrIndex):

        for vlg in attrValueSet[1:]:

            vla = float((vll + vlg) / 2)
            recordsL = [a[:] for a in records if a[attrIndex] <= vla]
            recordsG = [a[:] for a in records if a[attrIndex] > vla]
            cL = sum([i[1] for i in recordsL]) / len(recordsL)
            cG = sum([i[1] for i in recordsG]) / len(recordsG)

            tmpErrsum = sum([pow(r[-1] - cL, 2) for r in recordsL])
            tmpErrsum = sum([pow(r[-1] - cG, 2) for r in recordsG], tmpErrsum)
            if errsum > tmpErrsum:
                errsum = tmpErrsum
                retRecordsL = recordsL
                retRecordsG = recordsG
                retValA = vla

            vll = vlg

            # tmplist.append([tmpErrsum, vla])
    else:
        retValA = -1
    # for i in tmplist:
    #     print(i)
    average = sum([i[-1] for i in records]) / len(records)

    return retValA, retRecordsL, retRecordsG, average

def buildTree(trainingRecords):

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


# ------------------------------------------------

def trainingDataPreprocess(dataFile):
    '''
    :param dataFile:
    :return: numpy.array
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

