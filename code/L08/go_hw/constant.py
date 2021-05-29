N = 5
B = 0  # BLACK
W = 1  # WHITE
EMPTY = 2
#DRAW = 2

def withinBoard(i,j): return 0<=i<N and 0<=j<N
def opponent(player): return 1-player

####### graphics related #########
SQ_SIZE = 50
SHOW_GRAPHICS = False  # used by test.py (not by play_human.py)

######## tree-search related ##########
NUM_MC_TRIALS = 100 # 1000
val_net_B_gen = 4 #13  # for Komi = 3.5
val_net_W_gen = 5 #15  # for Komi = 3.5

nTest = 100
