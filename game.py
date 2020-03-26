def printBoard(board):
    for i in range(0, 3):
        print(board[i])
    print('\n')


def ending(player, board):
    print('*************************************************')
    if player is not None:
        print(player + " won!")
    else:
        print("Draw")
    print('*************************************************')
    printBoard(board)
    print('*************************************************\n')
    return True


def checkForWin(board):
    if checkDiagonal(board) or checkCols(board) or checkRows(board):
        return True
    else:
        return False


def checkDiagonal(board):
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[2][0] == board[1][1] == board[0][2]:
        return True
    return False


def checkCols(board):
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i]:
            return True
    return False


def checkRows(board):
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
    return False


def resetBoard(board):
    for i in range(0, 3):
        for j in range(0, 3):
            board[i][j] = str(i) + str(j)
    return board


def checkPosition(position, board):
    if not position.isdigit():
        print("Position is not a number! Pick again.  ")
        return False
    if int(position[0]) > 2 or int(position[1]) > 2 or int(position[0]) < 0 or int(position[1]) < 0:
        print("Position is out of bounds! Pick again.  ")
        return False
    if board[int(position[0])][int(position[1])] == 'X' or board[int(position[0])][int(position[1])] == 'O':
        print("Position is occupied! Pick again.  ")
        return False
    return True


def mainGame():
    gameOn = 'y'
    while gameOn is not 'q':                                    #Loop for new gameplay
        board = [[0 for i in range(3)] for i in range(3)]
        player = 'X'
        end = False
        boardCount = 0
        board = resetBoard(board)
        while not end:                                          #Loop for ongoing gameplay
            printBoard(board)
            print('Move of player: ' + player)
            print('Where to put your mark?  ')
            position = input()                                  #Get position from person
            while not checkPosition(position, board):
                position = input()                              #Invalid input: get new position
            else:                                               #If input was valid
                boardCount += 1
                board[int(position[0])][int(position[1])] = player
                if checkForWin(board):
                    end = ending(player, board)
                elif boardCount == 9:
                    end = ending(None, board)
                else:
                    end = False
                    if player == 'X':
                        player = 'O'
                    else:
                        player = 'X'
        gameOn = input('Restart? y - yes || q - quit  ')


mainGame()
