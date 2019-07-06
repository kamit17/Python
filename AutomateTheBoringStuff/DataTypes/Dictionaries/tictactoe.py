
theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': ''}


def printBoard(board):  # Function to print the board on the screen
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
for i in range(9):
    printBoard(theBoard)  # prints out the board at the start of new turn
    print('Turn for ' + turn + '.Move on which space?')

    move = input()  # updating the board

    theBoard[move] = turn  # swpas the active player

    if turn == 'X':  # next turn
        turn = 'o'
    else:
        turn = 'X'

printBoard(theBoard)
