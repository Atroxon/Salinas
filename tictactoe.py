"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # 'X' always starts
    XCount = 0
    OCount = 0
    for row in board:
        for piece in row:
            if piece == X:
                XCount += 1
            elif piece == O:
                OCount += 1
            else:
                pass

    if XCount == OCount:
        plyr = X
    elif XCount > OCount:
        plyr = O
    else:
        raise NameError('Error in piece count')

    # print(plyr)
    return plyr


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    availableActions = set()
    i = 0
    for row in board:
        j = 0
        for piece in row:
            if piece == None:
                # available slot, create tuple
                availableActions.add((i,j))
            else:
                # unavailable slot
                pass
            j += 1
        i += 1

    #print('Available actions: ' + str(availableActions))
    return availableActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultingBoard = copy.deepcopy(board)
    action = list(action)
    # check if valid move
    if resultingBoard[action[0]][action[1]] == None:
        # valid empty slot
        nextPiece = player(board)
        resultingBoard[action[0]][action[1]] = nextPiece
        pass
    else:
        raise NameError('Invalid Move')
    
    #print('Resulting board: ' + str(resultingBoard))
    return resultingBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    utlt = utility(board)
    if utlt == 1:
        winner = X
    elif utlt == -1:
        winner = O
    else:
        winner = None

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    rowWin = bool
    colWin = bool
    mDiagWin = bool
    iDiagWin = bool
    #gameOver = bool
    
    pieceCount = 0
    for row in board:
        for piece in row:
            if piece != EMPTY:
                pieceCount += 1

    if pieceCount == 9:
        return True

    #control check rows
    r = 0
    c = 0
    for row in board:
        c = 0
        for piece in row:
            tempPiece = piece
            if tempPiece != None:
                masterPiece = tempPiece     # where should i reset this?
                break
            else:
                c += 1     # to exit the loop and continue to next row
                break
            c += 1

        if c > 0:
            rowWin = False
            #r += 1  # iterator
            continue   # win by row not possible (skip row)
        else:
            c = 0
            for piece in row:
                tempPiece = piece
                if tempPiece == masterPiece and c == 2: # cause 0,1,2...
                    rowWin = True
                    break
                elif tempPiece != masterPiece:
                    rowWin = False
                    break
                else:
                    pass
                c += 1

        if rowWin:
            break
        
        #r += 1  #iterator

    #control check columns
    r = 0
    c = 0
    #validColumns = [0,1,2]
    annulatedColumns = []
    for row in board:
        
        if r == 0:
            masterRow = row
            r += 1
            continue

        for col in range(len(board)):
            piece = row[col]
            if col in annulatedColumns:
                continue
            elif piece == None:
                annulatedColumns.append(col)
                continue
            else:
                pass
                
            if piece == masterRow[col]:
                pass
            else:
                annulatedColumns.append(col)

    if len(annulatedColumns) == len(board):
        colWin = False
    else:
        colWin = True

    # control check diagonal
    rng = len(board) # considering it must be a square matrix

    # main diagonal
    i = 0
    j = 0
    for cell in range(rng):
        if board[i][j] == None: # impossible to build a diagonal
            mDiagWin = False
            break

        if i == 0:
            mDiagPiece = board[i][j] # sample piece since all should be equal
            i += 1
            j += 1
            continue
        
        if mDiagPiece != board[i][j]: # first discrepancy cancels loop
            mDiagWin = False
            break
        elif mDiagPiece == board[i][j] and j == (rng-1):
            mDiagWin = True
        else:
            pass

        i += 1
        j += 1

    # inverse diagonal
    j = 0
    for cell in range(rng):
        i = rng-cell-1
        if board[i][j] == None: # impossible to build a diagonal
            iDiagWin = False
            break 
        
        if j == 0:
            iDiagPiece = board[i][j] # sample piece since all should be equal
            j += 1
            continue
        
        if iDiagPiece != board[i][j]: # first discrepancy cancels loop
            iDiagWin = False
            break
        elif iDiagPiece == board[i][j] and j == (rng-1):
            iDiagWin = True
        else:
            pass

        j += 1

    return rowWin or colWin or mDiagWin or iDiagWin


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # only called if terminal(board) == true
    rowWin = bool
    colWin = bool
    # mDiagWin = bool
    iDiagWin = bool
    xCoordsI = []
    xCoordsJ = []
    oCoordsI = []
    oCoordsJ = []
    utlt = 0

    i = 0
    for row in board:
        j = 0
        for piece in row:
            if piece == X:
                xCoordsI.append(i)
                xCoordsJ.append(j)
            elif piece == O:
                oCoordsI.append(i)
                oCoordsJ.append(j) 
            else:
                # empty slot
                pass
            j += 1
        i += 1

    for i in range(3):  # check win by x rows
        count = xCoordsI.count(i)
        if count == 3:  # winner row would be i
            rowWin == True
            utlt = 1
            break   # maybe retur??
        else:
            rowWin == False

    for j in range(3):  # check win by x columns
        count = xCoordsJ.count(j)
        if count == 3:  # winner column would be j
            colWin == True
            utlt = 1
            break
        else:
            colWin == False  

    for i in range(3):  # check win by o rows
        count = oCoordsI.count(i)
        if count == 3:  # winner row would be i
            rowWin == True
            utlt = -1
            break   # maybe retur??
        else:
            rowWin == False

    for j in range(3): # check win by j columns
        count = oCoordsJ.count(j)
        if count == 3:  # winner column would be j
            colWin == True
            utlt = -1
            break
        else:
            colWin == False   

    # control check main diagonal
    rng = len(board) # considering it must be a square matrix
    i = 0
    j = 0
    for cell in range(rng):
        if board[i][j] == None: # impossible to build a diagonal
            mDiagWin = False
            break
        if i == 0:
            mDiagPiece = board[i][j] # sample piece since all should be equal
            i += 1
            j += 1
            continue
        if mDiagPiece != board[i][j]: # first discrepancy cancels loop
            mDiagWin = False
            break
        elif mDiagPiece == board[i][j] and j == (rng-1):
            mDiagWin = True
            if mDiagPiece == X:
                utlt = 1
            else:
                utlt = -1
        else:
            pass

        i += 1
        j += 1

    # inverse diagonal
    j = 0
    for cell in range(rng):
        i = rng-cell-1
        if board[i][j] == None: # impossible to build a diagonal
            iDiagWin = False
            break 
        if j == 0:
            iDiagPiece = board[i][j] # sample piece since all should be equal
            j += 1
            continue
        if iDiagPiece != board[i][j]: # first discrepancy cancels loop
            iDiagWin = False
            break
        elif iDiagPiece == board[i][j] and j == (rng-1):
            iDiagWin = True
            if iDiagPiece == X:
                utlt = 1
            else:
                utlt = -1
        else:
            pass
        j += 1

    return utlt


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board) == True:
        return None 

    # method planned to implement - BFS (queue)
    frontier = []
    nodes = {}
    analizedNodes = []
    terminalStatus = bool
    terminalNodes = []
    availableActions = list(actions(board)) # returns set of all possibles actions

    nodes[0] = {'parent': None, 'action': None, 'result': board, 'terminal': False, 'utility': None, 'children':[]}
    print(nodes[0])

    nodeKey = 1
    for action in availableActions:
        #print(action)
        nodeResult = result(board, action)      # prints result as well
        terminalStatus = terminal(nodeResult)
        if terminalStatus == True:
            boardUtility = utility(nodeResult)  # utility(nodeResult)
            terminalNodes.append(nodeKey)
        else:
            boardUtility = 0
        nodes[nodeKey] = {'parent': 0, 'action': action, 'result': nodeResult, 'terminal': terminalStatus, 'utility': boardUtility, 'children':[]}
        # append children ID
        populatedNodeParentID = nodes[nodeKey]['parent']                # get populated node's parent ID
        populatedNodeParent = nodes[populatedNodeParentID]              # get parent node
        #childrenList = populatedNodeParent['children']                  # query parent's children list
        populatedNodeParent['children'].append(nodeKey)                 # append child and save in dictionary
        frontier.append(nodeKey)                                        # populate frontier with original available actions
        nodeKey += 1

    analizedNodes.append(0) # node 0 equivalent to main board... analized above

    getChildren = nodes[0]['children']
    if len(getChildren) == 9:
        corners = [(0,0), (0,2), (2,0), (2,2)] 
        move = random.choice(corners)
        return move

    print(nodes)
    print(frontier)

    while len(frontier) > 0:
        nodeNum = frontier.pop(0) # takes out number and deletes it from frontier
        analizedNodes.append(nodeNum)
        drawnNode = nodes[nodeNum] # gets corresponding node from nodes dictionary
        nodeBoard = drawnNode['result'] # node result is curentBoard
        
        newActions = list(actions(nodeBoard)) # what happens if no new actions available??
        nodeKey = len(nodes)   # for new referencing
        if drawnNode['terminal'] == True:
            # should not consider children anymore
            #print('Node ' + str(nodeNum) + ' has terminal parent ' + str(drawnNode['parent']))
            for newAction in newActions:
                nodeKey += 1 # in reality this is not even affecting
            continue
        else:
            #print('Node ' + str(nodeNum) + ' can proceed from parent ' + str(drawnNode['parent']))
            for newAction in newActions:
                nodeResult = result(nodeBoard, newAction) # prints result as well
                terminalStatus = terminal(nodeResult)
                if terminalStatus== True:
                    boardUtility = utility(nodeResult)
                    terminalNodes.append(nodeKey)
                else:
                    boardUtility = 0
                nodes[nodeKey] = {'parent': nodeNum, 'action': newAction, 'result': nodeResult, 'terminal': terminalStatus, 'utility': boardUtility, 'children':[]}
                # append children ID
                populatedNodeParentID = nodes[nodeKey]['parent']                # get populated node's parent ID which is equal to nodeNum in this case
                populatedNodeParent = nodes[populatedNodeParentID]              # get parent node
                # childrenList = populatedNodeParent['children']                  # query parent's children list
                populatedNodeParent['children'].append(nodeKey)                 # append child and save in dictionary
                frontier.append(nodeKey)                                        # populate frontier with original available actions
                nodeKey += 1
    
    """
    traceback utilities
    """
    totalNodes = len(nodes)
    nodeCheck = len(nodes) - 1
    for n in range(totalNodes):
        # get relevant node's data
        node = nodes[nodeCheck]
        nodeUtility = node['utility']
        nodeChildren = node['children']
        #print('Node check: ' + str(nodeCheck) + ' Utility: ' + str(nodeUtility))
        if (len(nodeChildren) == 0): # or (len(nodeChildren) == 0): # avoid unnecessary proccesses
            nodeCheck -= 1
            #print('Skipped node... No children')
            continue
        nodeBoard = node['result']
        nextPlayer = player(nodeBoard)

        # split cases X and O
        if nextPlayer == X:
            setPoint = -math.inf
            for child in nodeChildren:
                childNodeUtility = nodes[child]['utility']
                #print('Child utility: ' + str(childNodeUtility))
                if childNodeUtility > setPoint:
                    setPoint = childNodeUtility
                    #print('New utility: ' + str(childNodeUtility))
                    node['utility'] = childNodeUtility
                else:
                    pass

        elif nextPlayer == O:
            setPoint = math.inf
            for child in nodeChildren:
                childNodeUtility = nodes[child]['utility']
                #print('Child utility: ' + str(childNodeUtility))
                if childNodeUtility < setPoint:
                    setPoint = childNodeUtility
                    #print('New utility: ' + str(childNodeUtility))
                    node['utility'] = childNodeUtility
                else:
                    pass
        else:
            raise NameError('No player found') 
        
        nodeCheck -= 1

    #print(nodes)
    print('Node count: ' + str(len(nodes)))
    print('Frontier status: ' + str(len(frontier)))
    print('Analized nodes: ' + str(len(analizedNodes))) 
    #print('Terminal nodes: ' + str(terminalNodes)) 

    lastIndex = nodes[len(nodes)-1]
    print('Last parent called: ' + str(lastIndex['parent']))

    nextPlayer = player(board)
    bestPlay = None
    mainChildren = nodes[0]['children']
    print('Main children: ' + str(mainChildren))
    bestChildCount = math.inf
    if nextPlayer == X:
        setPoint = -math.inf
        for child in mainChildren:
            node = nodes[child]
            utlt = node['utility']
            nodeChildCount = len(node['children'])
            if (utlt >= setPoint) and (nodeChildCount <= bestChildCount):
                setPoint = utlt
                bestPlay = child
            else:
                pass
    else:
        setPoint = math.inf
        for child in mainChildren:
            node = nodes[child]
            utlt = node['utility']
            nodeChildCount = len(node['children'])
            if (utlt <= setPoint) and (nodeChildCount <= bestChildCount):
                setPoint = utlt
                bestPlay = child
            else:
                pass
    
    #print(nodes)
    print('Best play is node: ' + str(bestPlay) + ' with action ' + str(nodes[bestPlay]['action']))
    print('with a utility of: ' + str(setPoint))


    return nodes[bestPlay]['action']
