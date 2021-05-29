N = 5
B = 0  # BLACK
W = 1  # WHITE
EMPTY = 2
#DRAW = 2

def withinBoard(i,j): return 0<=i<N and 0<=j<N
def opponent(player): return 1-player

######## MCTS related ############
NUM_MC_TRIALS = 100 # 1000

####### graphics related #########
SQ_SIZE = 50
SHOW_GRAPHICS = False  # play_for_data.py (not play_human.py)

###### training related ########
nGen = 10
nTrain = 250000
nTest = 1000  # only for trained vs. random