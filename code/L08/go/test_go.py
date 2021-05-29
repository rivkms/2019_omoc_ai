import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
from constant import *
from board import Board
from CNN import CNN_Test
from play_for_data import playGames

rand0 = np.zeros(nTest)
rand1 = np.ones(nTest)

#####################################
def test():
    global nGen
    val_net_B = [None]*(nGen+1)
    val_net_W = [None]*(nGen+1)
    for g in range(1,nGen+1):
        val_net_B[g] = CNN_Test("val_net_B_" + str(g))
        val_net_W[g] = CNN_Test("val_net_W_" + str(g))

    Pall = [ [ [None,None]  for g2 in range(nGen+1) ]  for g1 in range(nGen+1) ]

    nGen = len(val_net_B)-1
    for g1 in range(0,nGen+1):
        for g2 in range(0,nGen+1):
            if g1 == 0:
                valB, randB = None, rand1
            else:
                valB, randB = val_net_B[g1], rand0
            if g2 == 0:
                valW, randW = None, rand1
            else:
                valW, randW = val_net_W[g2], rand0
                
            _, _, _, _, P = playGames(nTest, valB, None, randB, valW, None, randW, True)
            print ("[Test/B%d-W%d] win prob." %(g1,g2) , P[0], "/", P[1])

            Pall[g1][g2][B] = P[B]
            Pall[g1][g2][W] = P[W]

    for player in [0,1]:
        print ("================================")
        print ("Winning rate of %s\n  " %["Black","White"][player], end=" ")
        for g2 in range(0,nGen+1): print (" %s%d " %(["W","B"][player], g2), end=" ")
        print()
        for g1 in range(0,nGen+1):
            print ("%s%d" %(["B","W"][player], g1), end=" ")
            sum = 0.0
            for g2 in range(0,nGen+1):
                p = Pall[g1][g2][B] if player == B else Pall[g2][g1][W]
                sum += p
                print ("%.2f" %(p) , end=" ")
            print (" %.3f" %(sum/(nGen+1)))

#####################################
test()
