import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import sys
from constant import *
from board import *
from CNN import *
from strategy import selectMove

# humanPlayer, computerPlayer = B, W
humanPlayer, computerPlayer = W, B

#####################################
def playHuman():
    if len(sys.argv) == 2 and sys.argv[1] in [str(x) for x in range(1,nGen+1)]:
        val_net = CNN_Test("val_net_B_" + sys.argv[1])
    else:
        print ("Usage: python3 play_human.py generation_no")
        return
        
    canvas = Canvas()
    board = Board(canvas=canvas)
    maxStep = N*N*2
    player = B
    nStep = 0
    nNoMove = 0
    while nStep < maxStep:  # similar to play_for_data.py
        moves = board.validMoves(player)
        if len(moves) == 0:
            nNoMove += 1
            if nNoMove == 2: break
        else:
            nNoMove = 0
            if player == computerPlayer:
                move = selectMove(board, moves, player, val_net, None, True)
            else:
                # i = raw_input("Enter row (1-%d): " %N)
                # j = raw_input("Enter column (1-%d): " %N)
                # i = int(i) if i in digit else 0
                # j = int(j) if j in digit else 0
                # move = (i-1,j-1)
                move = canvas.waitInput()
                if move not in moves:
                    print ("Invalid move")
                    continue
            board.setMove(player, move)
            nStep += 1

        player = opponent(player)

    winner = board.winner()
    canvas.setMessage("The winner is " + ["B","W"][winner])
    
###################################################    
playHuman()