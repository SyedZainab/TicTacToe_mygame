import random
def showInstructions():
    print("  Tic-Tac-Toe")
    print("Choose a cell numbered from 1 to 9 as below and play")

    print('   |   |')
    print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
    print('   |   |')
def wincheck(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def ask_player():
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print("Do you want to be X or O?")
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print("Would you like to play again?")
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def declarewinner(bo,le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le)or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le))

def getBoardCopy(board):
    dupeBoard=[]
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board,move):
    return board[move]==' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Choose where to place your mark (1-9)')
        move = input()
    return int(move)

def random_move(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def computermove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if declarewinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if declarewinner(copy, playerLetter):
                return i
    move = random_move(board,[1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board,5):
        return 5

    return random_move(board,[2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')
showInstructions()
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = ask_player()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            wincheck(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if declarewinner(theBoard, playerLetter):
                wincheck(theBoard)
                print("You have won the game! Congratulations")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    wincheck(theBoard)
                    print("Tie!")
                    break
                else:
                    turn = 'computer'

        else:
            move = computermove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if declarewinner(theBoard, computerLetter):
                wincheck(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    wincheck(theBoard)
                    print('Tie!')
                    break

                else:
                    turn = 'player'

    if not playAgain():
        break




