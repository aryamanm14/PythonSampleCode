### Project: Alphaman Game ###

# global variables and arrays
n,m=0,0                     # maze size N x M
maze=[]                     # current maze,
rowAM,colAM=0,0             # Alphaman's position in maze
rowExit,colExit=0,0         # Exit position in maze
rowTarget,colTarget=0,0     # The new position after the move

finish=0                    # status of the game - {-1:in progress,0:game finished}
curMove=0                   # player's move

totalGems=0
currentGems=0

eaten=False
def setupGame():
    # *** TO BE FILLED
    global n, m, maze, rowAM, colAM, rowExit, colExit, rowTarget, colTarget, finish, curMove, totalGems, currentGems, eaten
    
    n,m=input().split()
    n=int(n)
    m=int(m)
    
    rowAM=0
    colAM=0
    rowExit=0
    colExit=0
    
    matrix=[0]*n
    for row in range(n):
        matrix[row]=list(input())
    
    for row in range(n):
        for col in range(m):
            if matrix[row][col]=="E":
                rowExit=row
                colExit=col
            elif matrix[row][col]=="A":
                rowAM=row
                colAM=col
            elif matrix[row][col]=="G":
                totalGems+=1
    
    finish=-1
    maze=matrix
def drawScreen():
    # *** TO BE FILLED
    global n, m, maze, rowAM, colAM, rowExit, colExit, rowTarget, colTarget, finish, curMove, totalGems, currentGems, eaten
    
    for row in maze:
        print("".join(row))
    print("Remaining gems: "+str(totalGems-currentGems))
    print(" ")
def isValid(x,y):
    global maze
    if maze[rowTarget][colTarget]=="#":
        return True
    elif totalGems-currentGems!=0 and maze[rowTarget][colTarget]=="E":
        return True
    else:
        return False
def getMove():
    # *** TO BE FILLED
    global n, m, maze, rowAM, colAM, rowExit, colExit, rowTarget, colTarget, finish, curMove, totalGems, currentGems, eaten

    curMove=input("Enter move: ")
    print(" ")

    if curMove=="u":
        rowTarget=rowAM-1
        colTarget=colAM

    elif curMove=="d":
        rowTarget=rowAM+1
        colTarget=colAM
    
    elif curMove=="l":
        rowTarget=rowAM
        colTarget=colAM-1
    
    elif curMove=="r":
        rowTarget=rowAM
        colTarget=colAM+1
    
    while isValid(rowTarget,colTarget):
        print("Invalid move!")
        curMove=input("Enter move: ")
        print(" ")

        if curMove=="u":
            rowTarget=rowAM-1
            colTarget=colAM

        elif curMove=="d":
            rowTarget=rowAM+1
            colTarget=colAM
    
        elif curMove=="l":
            rowTarget=rowAM
            colTarget=colAM-1
    
        elif curMove=="r":
            rowTarget=rowAM
            colTarget=colAM+1
def makeMove():
    # *** TO BE FILLED
    global n, m, maze, rowAM, colAM, rowExit, colExit, rowTarget, colTarget, finish, curMove, totalGems, currentGems, eaten
    if maze[rowTarget][colTarget]=="G":
        currentGems+=1
    if maze[rowTarget][colTarget]=="M":
        eaten=True
    maze[rowAM][colAM]="."
    if eaten==False:
        maze[rowTarget][colTarget]="A"
        rowAM=rowTarget
        colAM=colTarget
def checkEndGame():
    # *** TO BE FILLED
    if rowAM==rowExit and colAM==colExit:
        return 0
    elif eaten==True:
        return 1
    else:
        return -1
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
# *** TO BE FILLED
drawScreen()
if finish==1:
    print("You lost!!!")
else:
    print("Congrats, you finished!!!")
