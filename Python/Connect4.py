# Declare the Array (game board) and columns
array2d = []
columns = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

#DEBUG Array to confirm that all success checks work
#array2d = [['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],
#           ['-','-','-','-','-','-','-','-','-','-'],['X','-','-','-','-','-','X','-','-','-'],
#           ['-','X','-','-','-','X','-','-','-','-'],['-','-','X','-','X','-','-','-','-','-'],
#           ['X','X','X','-','X','X','X','-','-','-'],['-','-','X','X','X','-','-','-','-','-'],
#           ['-','X','-','X','-','X','-','-','-','-'],['X','-','-','X','-','-','X','-','-','-']]

#Initialise null values
def init (array):
    for i in range (10):
        array.append([])
        for j in range (10):
            array[i].append('-')

#Run the function before anything else happens
init(array2d)

#Display the board
def display (array):
    for i in range (10):
        x = ''
        for j in range (10):
            x = x+array[i][j]+' '
        #print(x+str(i))
        print('| '+x+'|')
    print('=======================\n| A B C D E F G H I J |')

#Display the board to the player(s)
display(array2d)

#Adds a piece to the board
#Is run on every turn
def addpiece (col, token, turn):
    x = columns[col]
    blankSpace = 9 #Start at bottom row (gravity!)
    cont = True
    endGame = False
    while(cont):
        #If the space looking at is empty
        if(array2d[blankSpace][x] == '-'):
            #DEBUG print('=-')
            array2d[blankSpace][x] = token #Add the token
            display(array2d) #Redisplay the updated board
            cont = False #Do not continue trying to add the token
            message = '\nAdded '+token+' at column '+col+'\n'
            if (checkHwin(token, blankSpace, x) or
                checkVwin(token, blankSpace, x) or
                checkD1win(token, blankSpace, x) or
                checkD2win(token, blankSpace, x)):
                print('\n\nPlayer '+token+', you have won!\n\nGame has ended.')
                endGame = True
            else:
                turn *= -1
        elif(blankSpace == 0):
            #DEBUG print('=0')
            cont = False
            message = 'Column is full!'
        else:
            blankSpace = blankSpace - 1
    #DEBUG print(str(blankSpace)+' and '+str(x))
    print(message)
    if (endGame == False):
        humanTurn(turn)

#Check a horizontal success
def checkHwin(token, row, col):
    hasWon = False
    #DEBUG print(token, row, col)
    # X [] [] []
    if(col <  7):
        if((array2d[row][col+1] == token) and (array2d[row][col+2] == token) and (array2d[row][col+3] == token)):
            #DEBUG print('Yes H1')
            hasWon = True
    # [] X [] []
    if((col > 0) and (col <  8)):
        if((array2d[row][col-1] == token) and (array2d[row][col+1] == token) and (array2d[row][col+2] == token)):
            #DEBUG print('Yes H2')
            hasWon = True
    # [] [] X []    
    if((col > 1) and (col <  9)):
        if((array2d[row][col-2] == token) and (array2d[row][col-1] == token) and (array2d[row][col+1] == token)):
            #DEBUG print('Yes H3')
            hasWon = True
    # [] [] [] X
    if(col > 2):
        if((array2d[row][col-3] == token) and (array2d[row][col-2] == token) and (array2d[row][col-1] == token)):
            #DEBUG print('Yes H4')
            hasWon = True
    #DEBUG print('Checked Horizontal')
    return hasWon;
#Check a vertical success
def checkVwin(token, row, col):
    hasWon = False
    # X
    # []
    # []
    # []
    if(row <  7):
        if((array2d[row+1][col] == token) and (array2d[row+2][col] == token) and (array2d[row+3][col] == token)):
            #DEBUG print('Yes V')
            hasWon = True
    #DEBUG print('Checked Vertical')
    return hasWon

#Check an inclining diagonal success
def checkD1win(token, row, col):
    hasWon = False
    #      X
    #    []
    #  []
    #[]
    if((col > 2) and (row < 7)):
        if((array2d[row+1][col-1] == token) and (array2d[row+2][col-2] == token) and (array2d[row+3][col-3] == token)):
            #DEBUG print('Yes D11')
            hasWon = True
    #      []
    #    X
    #  []
    #[]
    if((col > 1) and (col < 9) and (row < 8) and (row > 0)):
        if((array2d[row-1][col+1] == token) and (array2d[row+1][col-1] == token) and (array2d[row+2][col-2] == token)):
            #DEBUG print('Yes D12')
            hasWon = True
    #      []
    #    []
    #  X
    #[]
    if((col > 0) and (col < 8) and (row < 9) and (row > 1)):
        if((array2d[row-2][col+2] == token) and (array2d[row-1][col+1] == token) and (array2d[row+1][col-1] == token)):
            #DEBUG print('Yes D13')
            hasWon = True
    #      []
    #    []
    #  []
    #X
    if((col < 7) and (row > 2)):
        if((array2d[row-3][col+3] == token) and (array2d[row-2][col+2] == token) and (array2d[row-1][col+1] == token)):
            #DEBUG print('Yes D14')
            hasWon = True
    #DEBUG print('Checked Bottom Left, Top Right Diagonal')
    return hasWon

#Check a declining diagonal success
def checkD2win(token, row, col):
    hasWon = False
    #X
    #  []
    #    []
    #      []
    if((col < 7) and (row < 7)):
        if((array2d[row+1][col+1] == token) and (array2d[row+2][col+2] == token) and (array2d[row+3][col+3] == token)):
            #DEBUG print('Yes D21')
            hasWon = True
    #[]
    #  X
    #    []
    #      []
    if((col > 0) and (col < 8) and (row < 8) and (row > 0)):
        if((array2d[row-1][col-1] == token) and (array2d[row+1][col+1] == token) and (array2d[row+2][col+2] == token)):
            #DEBUG print('Yes D22')
            hasWon = True
    #[]
    #  []
    #    X
    #      []
    if((col > 1) and (col < 9) and (row < 9) and (row > 1)):
        if((array2d[row-2][col-2] == token) and (array2d[row-1][col-1] == token) and (array2d[row+1][col+1] == token)):
            #DEBUG print('Yes D23')
            hasWon = True
    #[]
    #  []
    #    []
    #      X
    if((col > 2) and (row > 2)):
        if((array2d[row-3][col-3] == token) and (array2d[row-2][col-2] == token) and (array2d[row-1][col-1] == token)):
            #DEBUG print('Yes D24')
            hasWon = True
    #DEBUG print('Checked Top Left, Bottom Right Diagonal')
    return hasWon

def humanTurn(turn):
    player = ''
    if(turn == 1):
        player = 'X'
    else:
        player = 'O'
    column=input('\nPlayer '+player+', please enter a column letter to place your token: ')
    print('\n')
    if column in columns:
        #DEBUG print('turn is: '+ str(turn))
        if turn == 1:
            addpiece(column, 'X', turn)
        else:
            addpiece(column, 'O', turn)
    else:
        print('That is an invalid column!')
        humanTurn(turn)
    
humanTurn(1)
