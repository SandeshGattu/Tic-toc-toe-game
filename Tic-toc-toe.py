import random

def printBoard(a):
    print(a[1],"  |  ",a[2],"  |  ",a[3])
    print("----------------------------")
    print(a[4],"  |  ",a[5],"  |  ",a[6])
    print("----------------------------")
    print(a[7],"  |  ",a[8],"  |  ",a[9])
    
def isboardfull(board):
    #print(not(board.count(" ")==1))
    return board.count(" ")==1

def isfree(board,pos):
    return board[pos]==" "

def insertletter(board,l,move):
        board[move]=l
        
def playerMove(board,let):
    
    flag=True
    while flag:
        move=input("enter player move from 1-9")
        try:
            move=int(move)
            
            if move>0 and move<10:
                if isfree(board,move):
                    flag = False
                    insertletter(board,let,move)
                else:
                    print("No vacant space")
            else:
                print("enter valid input in range of 1-9")
        except:
            print("enter valid input")
            
            
def iswinner(board,le):
    return (board[1]==le and board[2]==le and board[3]==le)or(board[4]==le and board[5]==le and board[6]==le)or(board[7]==le and board[8]==le and board[9]==le)or(board[1]==le and board[4]==le and board[7]==le)or(board[2]==le and board[5]==le and board[8]==le)or(board[9]==le and board[6]==le and board[3]==le)or(board[7]==le and board[5]==le and board[3]==le)or(board[9]==le and board[5]==le and board[1]==le)
   
    
def selectrandom(a):
    r=random.randrange(0,len(a))
    return a[r]

def compMove(board):
    possmoves=[i for i,j in enumerate(board) if j==" " and i>0]
    move=0
    
    for let in ['X','O']:
        for i in possmoves:
            a=board[:]
            a[i]=let
            if iswinner(a,let):
                move=i
                return move
    opencorners=[]
    for i in possmoves:
        if i in [1,3,7,9]:
            opencorners.append(i)
    if len(opencorners)>0:
        move=selectrandom(opencorners)
        return move
    if 5 in possmoves:
        return 5
    if len(possmoves)>0:        
        move=selectrandom(possmoves)
    return move

board=[" " for x in range(10)]
    
def main():
    board=[" " for x in range(10)]
    print("tic toc toe game")
    print(" 1 player vs player")
    print("2 player vs computer")
    print("3 computer vs computer")
    p=0
    l=["player vs player mode","player vs computer mode","computer vs computer mode"]
    flag=True
    while flag:
        p=input("enter the mode")
        try:
            p=int(p)
            if p in [1,2,3]:
                flag=False
                print("you have selected : ",l[p-1])
            else:
                print("please select correct option in range of [1,2,3]")
                
        except:
            print("enter valid number")
                
            
    printBoard(board)
    #print(not(isboardfull))
    while not(isboardfull(board)):
        if not iswinner(board,'O'):
            
            if p!=3:
                print("player turn")
                playerMove(board,'O')
            else:
                move=compMove(board)
                if move==0:
                    print("tie game")
                else:
                    print("computer placed at ",move," position")
                    insertletter(board,'O',move)
                #printBoard(board)
            printBoard(board)
            
            if iswinner(board,'O'):
                print("O\'s won the game '")
                break
            
            
            
        else:
            print("O\'s won the game")
            break
        if not iswinner(board,'X'):
            if p!=1:
                move=compMove(board)
                if move==0:
                    print("tie game")
                else:
                    print("computer placed at ",move," position")
                    insertletter(board,'X',move)
                    
            else:
                print("player turn")
                playerMove(board,'X')
            if iswinner(board,'O'):
                print("X\'s won the game '")
                break
            printBoard(board)
        else:
            print("X\'s won the game'")
            break
                
            
    if isboardfull(board):
        print("tie game")
    


main()