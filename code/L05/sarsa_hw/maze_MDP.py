import numpy as np

num_rows = 5
num_columns = 5
num_states = num_rows * num_columns
num_actions = 4  # up, down, left, right

U,D,L,R = 0,1,2,3
WALL = 1

def generate_maze():  
    maze = np.zeros([40])
    maze[4] = maze[7] = maze[8] = maze[11] = maze[12] = maze[15] = WALL
    maze[36] = maze[37] = maze[38] = WALL
    return maze
    
############################################
def MDP_transition(state, action, maze):
    # given state/action, determine reward, next state
    # action: 0/U, 1/D, 2/L, 3/R
    row = int(state/5)
    col = state - 5*row
    state_next = state

    if not ( row==0 and action==D  or row==4 and action==U  or \
             col==0 and action==L  or col==4 and action==R ) :  
        if action == U:
            if maze[state+20] != WALL:
                state_next = state + 5
        elif action == D:
            if maze[state+20-5] != WALL:
                state_next = state - 5
        elif action == L:
            if maze[4*row+col-1] != WALL:
                state_next = state - 1
        elif action == R:
            if maze[4*row+col] != WALL:
                state_next = state + 1
            
    if state_next == 4:
        reward = 100
        terminate = True
    else:
        if state_next in [6,7,8]:
            reward = -100
        else:
            reward = 0
        terminate = False
        
    return reward, state_next, terminate
