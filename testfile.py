def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    rowWin = bool
    colWin = bool
    mDiagWin = bool
    iDiagWin = bool
    #gameOver = bool
    
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
