### Project: Word Guessing Game ###

# global variables and arrays
secretWord=""                   # secret word
maskedWord=""                  
    # masked word
usedLetters=""                  # used letters
lives=0                        
    # number of remaining lives
finish=0                        # status of the game - {-1:in progress,0:player lost,1:player won}
letter=""                      
    # the letter that the player chose in the current turn

def setupGame():
    # *** TO BE FILLED
    global secretWord   
    global maskedWord
    global lives
    global finish
    secretWord=input()
    length=len(secretWord)
    maskedWord='*'*length
    lives=5
    finish=-1
    
def drawScreen():
    # *** TO BE FILLED
    print(maskedWord)
    print("Remaining lives:",lives)
    print("Used letters:",usedLetters)
    print(' ')
def getMove():
    # *** TO BE FILLED
    global letter
    letter=input("Enter a lower case letter:")
    while True:
        if letter in usedLetters:
            print(' ')
            print('Invalid! This letter is used before.')
            letter=input("Enter a lower case letter:")
        else:
            break
    print(' ')
def makeMove():
    # *** TO BE FILLED
    global secretWord   
    global maskedWord
    global lives
    global finish
    global letter
    global usedLetters
    secretWord=list(secretWord)
    maskedWord=list(maskedWord)
    if letter not in secretWord:
        lives-=1
    else:
        for i in range(len(secretWord)):
            if secretWord[i]==letter:
                maskedWord[i]=letter
    usedLetters+=letter
    maskedWord="".join(maskedWord)
    secretWord="".join(secretWord)
def checkEndGame():
    # *** TO BE FILLED
    global secretWord   
    global maskedWord
    global lives
    global finish
    global letter
    global usedLetters
    if lives==0:
        return 0
    elif '*' not in maskedWord:
        return 1
    else:
        return -1
setupGame()                    
    # step 1

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
if finish==0 and '*' in maskedWord:
    print(maskedWord)
    print("Remaining lives:",lives)
    print("Used letters:",usedLetters)
    print(' ')
    print("You lost! The secret word was:",secretWord)
elif finish==1:
    print(maskedWord)
    print("Remaining lives:",lives)
    print("Used letters:",usedLetters)
    print(' ')
    print("You won!")  
