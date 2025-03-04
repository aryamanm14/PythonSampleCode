### Project: Toads and Frogs Game ###

# global variables and arrays
n=0                         # board size
board=[]                   
    # current board
dashPos=0                   # the position of the empty spot on the current board
finish=0                   
    # status of the game - {-1:in progress,0:game finished}
curMove=0                   # the move chosen by the player in the current turn
numOfMoves=0               
    # keep the number of moves
def isValid(x):
    output="invalid"

    if x>=1 and x<=len(board):
        if board[x-1]=='F':
            if (x>=2 and board[x-2]=='-') or (x>=3 and board[x-3]=='-'):
                output="valid"
        if board[x-1]=='T':
            if (x<len(board) and board[x]=='-') or (x+1<len(board) and board[x+1]=='-'):
                output="valid"
    if output=="valid":
        return False
    else:
        return True
        
    
def setupGame():
    # *** TO BE FILLED
    global n, board, dashPos, finish, curMove, numOfMoves
    n=int(input())
    board=[""]*n
    for x in range(n):
        if x<n/2-1:
            board[x]='T'
        elif x==n//2:
            board[x]='-'
        elif x>n/2-1:
            board[x]='F'

    dashPos=board.index('-')
    finish=-1
def drawScreen():
    # *** TO BE FILLED
    print(''.join(board))
    print("Number of moves:",numOfMoves)
    print(' ')
def getMove():
    # *** TO BE FILLED
    global n, board, dashPos, finish, curMove, numOfMoves
    curMove=input("Enter move (1.."+str(n)+"):")
    curMove=int(curMove)
    print(' ')
    while isValid(curMove):
        print("Invalid move!")
        curMove=input("Enter move (1.."+str(n)+"):")
        curMove=int(curMove)
        print(' ')
    #print(''.join(board))
def makeMove():
    # *** TO BE FILLED
    global n, board, dashPos, finish, curMove, numOfMoves
    board[curMove-1],board[dashPos]=board[dashPos],board[curMove-1]
    dashPos=curMove-1
    numOfMoves+=1
def checkEndGame():
    # *** TO BE FILLED
    global n, board, dashPos, finish, curMove, numOfMoves
    if board[0:n//2]==['F']*(n//2) and board[n//2+1:]==['T']*(n//2):
        return 0
    else:
        return -1
setupGame()                     # step 1

# main game loop
while True:
    drawScreen()                # step 2
    getMove()                  
    # step 3
    makeMove()                  # step 4
    finish = checkEndGame()     # step 5
   
    if finish>-1:
        break

# step 6: end game information
# *** TO BE FILLED

print(''.join(board))
print("Number of moves:",numOfMoves)
print(' ')
print("You finished!")
