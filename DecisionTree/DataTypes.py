__author__ = 'Sway007'
from collections import deque
# import math
import copy

ATTRIBUTE_NUM = 5
ATTR_RESULT_INDEX = 2

ALL_DATA_RECORDS_LIST = []

CLASSIFICATION_SET = set()

VALUESET_LIST = []      # content is data set in every column


class decisionNode:

    def __init__(self, attrIndex):

        global VALUESET_LIST
        self.attrIndex = attrIndex          # should be integer, -1 denote the root
                                            # index of attr inspected in tree

        self.nextNodeDict = dict.fromkeys(VALUESET_LIST[attrIndex])           # the process of building tree is fill each node's next node
                                                                              # init the branches of decision node
        self.result = None                  # classification for leaf node, set in split function


    def isLeaf(self):
        global CLASSIFICATION_SET
        return self.result is not None and self.result not in CLASSIFICATION_SET



def getAttrValProportionDict(recordSet, attrIndex):

    attrValSet = VALUESET_LIST[attrIndex]
    ret = dict.fromkeys(attrValSet, 0)

    for oneRecord in recordSet:
        val = oneRecord[attrIndex]
        ret[val] += 1

    for k, v in ret.items():
        ret[k] = v / len(recordSet)

    return ret


def getEntropy(trainingRecords):

    return getSplitInfo(trainingRecords, ATTR_RESULT_INDEX)

def getAttrEntropySum(trainingRecords, attrIndex):

    ret = 0
    d = splitTrainingData(trainingRecords, attrIndex)
    for k, v in d.items():
        ret += len(v) / len(trainingRecords) * getEntropy(v)

    return ret

def getSplitInfo(trainingRecords, attrIndex):

    ret = 0
    if len(trainingRecords) == 0:
        return ret

    attrValPropDic = getAttrValProportionDict(trainingRecords, attrIndex)
    for v in attrValPropDic.values():
        if v > 0:
            ret += -v * math.log(v, 2)

    return ret


def getBestAttrIndex(trainingRecords, attrIndexSet):

    ret = -1
    entropy = 2
    for i in attrIndexSet:

        curEntropy = getAttrEntropySum(trainingRecords, i)
        if curEntropy < entropy:
            ret = i
            entropy = curEntropy

    return ret


def getBestAttrIndex_C45(trainingRecords, attrIndexSet):

    ret = -1
    recordsEntropy = getEntropy(trainingRecords)
    IRG = -1

    for i in attrIndexSet:
        infoGain = recordsEntropy - getAttrEntropySum(trainingRecords, i)
        H = getSplitInfo(trainingRecords, i)
        if H == 0:
            return i

        tmpIRG = infoGain / H
        if tmpIRG > IRG:
            IRG = tmpIRG
            ret = i

    return ret


def splitTrainingData(recordSet, attrIndex):      # return a dict[attrValue : recordsList]

    attrValSet = VALUESET_LIST[attrIndex]
    # ret = dict.fromkeys(attrValSet, [])         # @ error, cause each key's value-[] is the same one
    ret = {}
    for val in attrValSet:
        ret[val] = []

    for oneRecord in recordSet:
        val = oneRecord[attrIndex]
        ret[val].append(oneRecord)

    for val in attrValSet:
        if len(ret[val]) == 0:
            del ret[val]

    return ret

def isDataSplitable(dataRecords):
    # done if 1. all records classification are the same
    # or 2. no attribute available to split
    resultSet = getAttrValProportionDict(dataRecords, ATTR_RESULT_INDEX)
    for v in resultSet.values():
        if v >= 1.0:
            return False

    return True


def testPrintQueue(q, idx):
    for data in q:
        for i in data[0]:
            print(i)
        print('records num:' + str(len(data[0])))
        print('*' * 20)
        print('attr available number: ' + str(data[2]))
        print('parent attr: ' + str(data[1].attrIndex) + '  len(queue): ' + str(len(q)))
        print('id: ' + str(idx))

        print('=' * 20)


def buildingTree(trainingRecords, algorithmV):
    '''

    :param algorithmV: 1 for id3, else for c4.5
    :return:
    '''

    # 1.find best attribute -- ba
    # 2.split training set through ba into subset
    # 3.judge if each subset can be split
    # 4.if yes: get a decision node, split training set into subset,
    #       then for each subset, goto step 1.
    #   else: get a leaf node
    #
    # @param trainingRecords: list of records
    # @return root: decisionNode
    root = decisionNode(-1)
    tmpSet = {i for i in range(ATTRIBUTE_NUM) if i != ATTR_RESULT_INDEX}
    queue = deque([[trainingRecords, root, tmpSet], ])        # deque elment [records, parentNode, parentAttrIndexList]
                                                              # parentAttrIndexList means the left attributes allowed to split data set with
    testn = 0  # TODO debug
    while len(queue) > 0 :
        #################
        testPrintQueue(queue, testn)
        testn += 1  # TODO debug
        #################
        pair = queue.pop()
        curDataSet = pair[0]
        parentNode = pair[1]
        parentAttrIndex = parentNode.attrIndex
        parentAttrIndexSet = copy.copy( pair[2] )

        attrIndex = -1
        if len(parentAttrIndexSet) > 0:
            if algorithmV == 1:
                attrIndex = getBestAttrIndex(curDataSet, parentAttrIndexSet)
            else:
                attrIndex = getBestAttrIndex_C45(curDataSet, parentAttrIndexSet)
        newDecisionNode = decisionNode(attrIndex)


        if parentAttrIndex >= 0:
             dataAttrValue = curDataSet[0][parentAttrIndex]
             parentNode.nextNodeDict[ dataAttrValue ] = newDecisionNode          # build tree node link
        else:
             parentNode.nextNodeDict[0] = newDecisionNode            # parent node is root


        if isDataSplitable(curDataSet):

            if len(parentAttrIndexSet) > 0:
                subSets = splitTrainingData(curDataSet, attrIndex)
                if attrIndex >= 0:
                    parentAttrIndexSet.remove(attrIndex)
                queue.extendleft([ [x, newDecisionNode, parentAttrIndexSet] for x in subSets.values() ])


            else:               # if not all are in the same class
                portionDict = getAttrValProportionDict(curDataSet, ATTR_RESULT_INDEX)
                p = 0
                for v, k in portionDict.items():
                    if k > p:
                        p = k
                        newDecisionNode.result = v
        else:
            newDecisionNode.result = curDataSet[0][ATTR_RESULT_INDEX]
            # print(1)

    return root


if __name__ == '__main__':
    pass