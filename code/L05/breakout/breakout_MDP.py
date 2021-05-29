import numpy as np

num_rows = 5
num_columns = 5
num_states = (num_rows+1)**num_columns
num_actions = 5

#####################################################################    
def MDP1_transition(state, action):  # models environment #1 for breakout game
    # If any one of the columns is cleared, all bricks are cleared
    col = action
    state_next = state[:]
    reward = 0
    if state_next[col] > 0:
        state_next[col] -=  1  # break the bottom brick in col
        reward = 1

    terminate = False
    if 0 in state_next:
        terminate = True
        reward += sum(state_next)  # break all the remaining bricks
        for i in range(5):
            state_next[i] = 0
            
    return reward, state_next, terminate

#####################################################################    
def MDP2_transition(state, action):  # models environment #2 for breakout game
    # If any one of the columns is cleared, all rows except the bottom are cleared
    col = action
    state_next = state[:]
    reward = 0
    if state_next[col] == 0:
        reward = 0
    elif state_next[col] == 1:
        reward = 1
        state_next[col] = 0
        for i in range(5):
            if state_next[i] <= 4:
                reward += state_next[i]
                state_next[i] = 0
            elif state_next[i] == 5:
                reward += 4
                state_next[i] = 6  # 6 means only the bottom brick is present
            elif state_next[i] == 6:    
                state_next[i] = 6  # no change
    elif state_next[col] == 6:
        reward = 1
        state_next[col] = 0
    elif 2 <= state_next[col] <= 5:
        reward = 1
        state_next[col] -= 1

    terminate = (max(state_next) == 0)
    return reward, state_next, terminate

#####################################################################    
def MDP3_transition(state, action):  # models Environment #3 for breakout game
    # If any two consecutive columns are cleared, all bricks are cleared
    col = action
    state_next = state[:]
    reward = 0
    if state_next[col] > 0:
        state_next[col] -= 1
        reward = 1

    terminate = False
    for i in range(4):
        if state_next[i] == state_next[i+1] == 0:
            terminate = True
            break

    if terminate:
        reward += sum(state_next)
        for i in range(5):
            state_next[i] = 0

    return reward, state_next, terminate
