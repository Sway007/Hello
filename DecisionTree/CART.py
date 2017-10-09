__author__ = 'Sway007'

import graphviz as graph
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

     def isSecondLevelLeaf(self):

         return self.lessNext.isLeaf() and self.greatNext.isLeaf() and not self.isLeaf()

     def setLeaf(self):

         self.spoint = -1


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


def getParentNode(node, treeRoot):

    parentNode = treeRoot
    if node.spoint < treeRoot.spoint:
        curNode = treeRoot.lessNext
    else:
        curNode = treeRoot.greatNext

    while not curNode.isLeaf():

        if node.spoint == curNode.spoint:
            return parentNode

        parentNode = curNode
        if node.spoint < curNode.spoint:
            curNode = curNode.lessNext
        else:
            curNode = curNode.greatNext

    return None


def getParentSplitPoint(sp, treeRoot):

    parentNode = treeRoot
    if sp < treeRoot.spoint:
        curNode = treeRoot.lessNext
    else:
        curNode = treeRoot.greatNext

    while not curNode.isLeaf():

        if sp == curNode.spoint:
            return parentNode.spoint

        parentNode = curNode
        if sp < curNode.spoint:
            curNode = curNode.lessNext
        else:
            curNode = curNode.greatNext

    return None


def subRecordsMerge(recordsLess, recordsGreat):
    '''
    return None if should not merge, else return merged records
    '''

    varPre = getVariance(recordsLess) + getVariance(recordsGreat)
    mergedRecords = recordsLess[:]
    mergedRecords.extend(recordsGreat)
    varAfter = getVariance(mergedRecords)

    if varAfter < varPre:
        return mergedRecords
    else:
        return None


def getSubRecords(treeRoot, records):
    '''
    return list:
    '''
    splitPoints = []
    stack = deque([treeRoot])

    # traverse tree in mid-order
    curNode = stack[-1].lessNext
    while len(stack) > 0 or not curNode.isLeaf():

        while not curNode.isLeaf():

            stack.append(curNode)
            curNode = curNode.lessNext

        curNode = stack.pop()
        splitPoints.append(curNode.spoint)
        curNode = curNode.greatNext


    subRecords = []
    index = 0
    lsp = -1
    while True:

        curSp = splitPoints[index]

        subRecords.append( ( [oneRecord for oneRecord in records if lsp < oneRecord[0] < splitPoints[index]],
                             curSp ) )
        lsp = splitPoints[index]
        index += 1

        if index == len(splitPoints):
            subRecords.append( ( [oneRecord for oneRecord in records if splitPoints[-1] < oneRecord[0] ],
                             curSp + 1 ) )
            break
        #
        # subRecords.append(([oneRecord for oneRecord in records if lsp < oneRecord[0] < splitPoints[index]],
        #                    curSp))
        # lsp = splitPoints[index]
        # index += 1

    # subRecords.append(([oneRecord for oneRecord in records if oneRecord[0] > splitPoints[-1]],
    #                    splitPoints[-1]))
    return subRecords


def getSubLeafRecords(node, allSubRecords):

    sp = node.spoint
    recordsLess = None
    recordsGreat = None

    spList = [i[1] for i in allSubRecords]
    spLess = max([csp for csp in spList if csp <= sp])
    spGreat = min([csp for csp in spList if csp > sp])

    for subrecords in allSubRecords:
        if spLess - 0.005 < subrecords[1] < spLess + 0.005:
            recordsLess = subrecords[0]
        elif spGreat - 0.005 < subrecords[1] < spGreat + 0.005:
            recordsGreat = subrecords[0]
        elif recordsLess and recordsGreat:
            break

    return (recordsLess, spLess), (recordsGreat, spGreat)


def treePrune(treeRoot, records):
    '''
    TODO
    method 2.
    try to find all second-level leaf, and pack into queue q
    while q is not empty:
        n = q.pop()
        n' = merge n.
        if mergable, q.push(n')
    :return:
    '''

    subRecords = getSubRecords(treeRoot, records)
    queue = deque([treeRoot])

    testList = []

    while len(queue) > 0:

        curNode = queue.pop()
        if curNode.isSecondLevelLeaf():

            curLessAndGreatRecords = getSubLeafRecords(curNode, subRecords)
            mergedRecords = subRecordsMerge(curLessAndGreatRecords[0][0], curLessAndGreatRecords[1][0])
            if mergedRecords is not None:   # should merge

                testList.append(curNode.spoint)

                subRecords.remove(curLessAndGreatRecords[0])
                subRecords.remove(curLessAndGreatRecords[1])
                newsp = curLessAndGreatRecords[1][1]
                subRecords.append((mergedRecords, newsp))

                pNode = getParentNode(curNode, treeRoot)
                queue.appendleft(pNode)
                curNode.setLeaf()

            else:
                continue

        elif not curNode.isLeaf():
            if not curNode.lessNext.isLeaf():
                queue.appendleft(curNode.lessNext)
            if not curNode.greatNext.isLeaf():
                queue.appendleft(curNode.greatNext)


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


count = 0
def nodeToStr(node):

    global count
    if node.isLeaf():
        count += 1
        return 'Leaf {}'.format(count)
    else:
        return str(node.spoint)

def treeView(treeRoot, fileName):

    q = deque([treeRoot])
    edges = []

    while len(q) > 0:

        curNode = q.pop()

        if curNode.isLeaf():
            continue

        edges.extend([[nodeToStr(curNode), nodeToStr(curNode.lessNext)], [nodeToStr(curNode), nodeToStr(curNode.greatNext)]])
        q.extendleft([curNode.lessNext, curNode.greatNext])


    G = graph.Digraph(filename=fileName, format='png')
    G.edges(edges)
    G.view()


if __name__ == '__main__':

   datas = trainingDataPreprocess('train.txt')
   # print(numpy.array(datas))
   # t = regressionSplit(datas, 0)
   # print(t)
   treeRoot = buildTree(datas)

   treeView(treeRoot, 'preTree')

   treePrune(treeRoot, datas)

   treeView(treeRoot, 'afterTree')

   testDatas = getTestRecords('test.txt')
   fileName = 'testOutput.txt'
   with open(fileName, 'w') as output:

       for record in testDatas:

            p = predictValue(treeRoot, record[0])
            record.append(p)
            print(record, file=output)


