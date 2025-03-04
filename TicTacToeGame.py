### Project: Tic Tac Toe Game ###

# global variables and arrays
n=0             # board size
board=[]        # create a board
curPlayer=0     # current player (1 or 2)
numOfMoves=0    # keep the number of moves
row,col=0,0     # current move
finish=0        # status of the game
                # {-1:in progress, 0:tie, 1:player 1 won, 2:player 2 won}

def setupGame():
    # *** TO BE FILLED
    global board, finish, curPlayer, numOfMoves, row, col, n
    board=[""]*3
    for row in range(3):
        board[row]=["-","-","-"]
    
    numOfMoves=0
    curPlayer=1
    finish=-1
def drawScreen():
    # *** TO BE FILLED
    global board, finish, curPlayer, numOfMoves, row, col, n
    for row in board:
        print("".join(row))

    print(" ")
def isValid(x,y):
    global board
    if x>2 or x<0 or y>2 or y<0:
        return True
    elif board[x][y]=='-':
        return False
    else:
        return True
def getMove():
    # *** TO BE FILLED
    global board, finish, curPlayer, numOfMoves, row, col, n
    r,c=input("Player "+str(curPlayer)+", please enter your move (row, col):").split()
    print(" ")
    row=int(r)-1
    col=int(c)-1
    while isValid(row,col):
        print("Invalid move!")
        r,c=input("Player "+str(curPlayer)+", please enter your move (row, col):").split()
        row=int(r)-1
        col=int(c)-1
        print(' ')
def makeMove():
    # *** TO BE FILLED
    global board, finish, curPlayer, numOfMoves, row, col, n
    if curPlayer==1:
        board[row][col]="X"
        curPlayer=2
        numOfMoves+=1
    else:
        board[row][col]="O"
        curPlayer=1
        numOfMoves+=1
def checkEndGame():
    # *** TO BE FILLED
    global board, finish, curPlayer, numOfMoves, row, col, n
    output="NO"

    for row in board:
        if row[0]==row[1] and row[0]==row[2]:
            if row[0]!='-':
                output="YES"

    for col in range(3):
        if board[0][col]==board[1][col] and board[0][col]==board[2][col]:
            if board[0][col]!='-':
                output="YES"

    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!='-':
        output="YES"

    if board[0][2]==board[1][1]==board[2][0] and board[1][1]!='-':
        output="YES"
    
    if output=="YES":
        if curPlayer==1:
            return 1
        else:
            return 2
    
    notTied=False
    for row in range(3):
        for col in range(3):
            if board[row][col]=='-':
                notTied=True

    if notTied:
        return -1
    else:
        return 0
setupGame()                     # STEP 1

# main game loop
while True:
    drawScreen()                # STEP 2
    getMove()                   # STEP 3
    makeMove()                  # STEP 4
    finish = checkEndGame()     # STEP 5
    if finish>-1:               # if game is finished, break the loop
        break

# STEP 6: end game information
drawScreen()

if finish==1:
    print("Player "+str(curPlayer+1)+" won the game!")
elif finish==2:
    print("Player "+str(curPlayer-1)+" won the game!")
else:
    print("Tie!")
