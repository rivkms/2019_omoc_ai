import numpy as np

num_row = 10
num_col = 10
num_actions = 3  # left/stay/right

########################################################################
def MDP_transition(state, action):  # models environment for catch game
    fruit_row, fruit_col, basket = state
    move = action-1  # left:-1 / stay:0 / right:+1
    basket = min(max(2, basket+move), num_col-1)
    fruit_row += 1  # falling by 1
    state_next = [fruit_row, fruit_col, basket]
    
    if fruit_row == num_row-1:  # reach the bottom
        if abs(fruit_col-basket) <= 1:  # basket catches the fruit
            reward = 1
        else:   # basket misses the fruit
            reward = -1
    else:
        reward = 0

    terminate = (fruit_row == num_row-1)

    return reward, state_next, terminate
    
########################################################################
def MDP_initial_state():  # randomly generate initial state
    fruit_row = 1
    fruit_col = np.random.randint(1,num_row+1)
    basket = np.random.randint(2,num_row)
    return [fruit_row, fruit_col, basket]
    