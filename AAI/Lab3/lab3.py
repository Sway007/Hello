from math import sqrt

def getDisBtween(p1, p2):

    tmpV = [abs(p1[0] - p2[0]), abs(p1[1] - p2[1])]
    l = min(tmpV[0], tmpV[1])
    ret = sqrt(2) * l
    g = max(tmpV[0], tmpV[1])
    ret += g - l

    return ret

def getAdmissibleDis(curPointEdge, goal):

    # tmp = [abs(curPointEdge[1][0] - goal[0]), abs(curPointEdge[1][1] - goal[1])]
    # ret = sum(tmp)

    ret = getDisBtween(curPointEdge[1], goal)

    # tmp = [i - j for i, j in zip(curPointEdge[-1], goal)]
    # ret = 0
    # for i in tmp:
    #     ret += i * i
    # ret = sqrt(ret)

    return ret

def getDisFromStart(curPos, start):

    return getDisBtween(curPos, start)

def getFrontiers(tilePos, mapSize):
    '''

    :param tilePos:
    :param mapSize:
    :return: tuple(directFrontiers, inclinedFrontiers)
    '''

    tmpFrontiers = [[tilePos[0] - 1, tilePos[1]],
                    [tilePos[0] + 1, tilePos[1]],
                    [tilePos[0], tilePos[1] - 1],
                    [tilePos[0], tilePos[1] + 1],

                    [tilePos[0] - 1, tilePos[1] - 1],
                    [tilePos[0] + 1, tilePos[1] - 1],
                    [tilePos[0] - 1, tilePos[1] + 1],
                    [tilePos[0] + 1, tilePos[1] + 1]
                    ]

    return [i[:] for i in tmpFrontiers if mapSize[0] > i[0] >= 0 and mapSize[1] > i[1] >= 0]

def getPathFromEdges(edges, init):
    '''
    :param edges:
        got from findPath
    :return:
        a list with length n (the number of steps) and each element of the list is a position in the format (xi, yi).
    '''

    if len(edges) == 0:
        return None

    path = list(edges[-1])
    curP = edges[-1][0]
    edges.remove(edges[-1])
    edges.reverse()

    while curP != list(init):

        for edge in edges:
            if curP != edge[-1]:
                continue

            path.insert(0, edge[0])
            curP = edge[0]
            edges.remove(edge)
            break

    return path

def getRealBlocks(preBlocks):

    retBlocks = []
    for blockTile in preBlocks.tolist():

        checkedTile = blockTile
        if checkedTile not in retBlocks:
            retBlocks.append(checkedTile)
        checkedTile = [blockTile[0] + 1, blockTile[1]]
        if checkedTile not in retBlocks:
            retBlocks.append(checkedTile)
        checkedTile = [blockTile[0], blockTile[1] + 1]
        if checkedTile not in retBlocks:
            retBlocks.append(checkedTile)
        checkedTile = [blockTile[0] + 1, blockTile[1] + 1]
        if checkedTile not in retBlocks:
            retBlocks.append(checkedTile)

    return retBlocks

def isSuccess(edgesVisited, goal):

    if len(edgesVisited) == 0:
        return False
    if list(goal) == edgesVisited[-1][-1]:
        return True
    return False

def findPath(mapsize, blocks, init, goal, algrotithmV):
    '''

    :return:
        a list whose elements are the lines(format: [[x1, y1], [x2, y2]]) visited in the path
    '''

    pathEdgesVisited = []
    realBlocks = getRealBlocks(blocks)
    frontiers = [[list(init), p] for p in getFrontiers(init, mapsize) if p not in realBlocks]
    visted = []

    while len(frontiers) > 0 and not isSuccess(pathEdgesVisited, goal):

        minDis = 9999
        expandedEdge = None
        for itr in frontiers:
            if algrotithmV == 0:
                tmpDis = getAdmissibleDis(itr, goal)
            else:
                tmpDis = getAdmissibleDis(itr, goal) + getDisBtween(itr[1], init)

            if minDis > tmpDis:
                expandedEdge = itr
                minDis = tmpDis

        # visited current optimal point
        visted.extend(expandedEdge)
        frontiers.remove(expandedEdge)
        pathEdgesVisited.append(expandedEdge)

        # add new frontiers
        potentialFrontiers = getFrontiers(expandedEdge[1], mapsize)

        detectedFrontiers = [i[1] for i in frontiers]
        # new frontier shuold not in detected frontiers for avoiding
        frontiers.extend( [[expandedEdge[1], i] for i in potentialFrontiers if i not in visted and i not in realBlocks and i not in detectedFrontiers] )

    return getPathFromEdges(pathEdgesVisited, init)


def greedysearch(mapsize, blocks, init, goal):
    """Returns:
    - path: a list with length n (the number of steps) and each
    element of the list is a position in the format (xi, yi).
    Or a nx2 matrix.
    """
    return findPath(mapsize, blocks, init, goal, 0)


def astarsearch(mapsize, blocks, init, goal):
    """Returns:
    - path: a list with length n (the number of steps) and each
    element of the list is a position in the format (xi, yi).
    Or a nx2 matrix.
    """
    ### Put your path finding code here ###
    return findPath(mapsize, blocks, init, goal, 1)

# if __name__ == '__main__':
#     print(getPathFromEdges([[1,2], [2,3], [3,4]], 1))