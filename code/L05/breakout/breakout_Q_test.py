import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
from breakout_MDP import num_states, num_actions
from breakout_MDP import MDP1_transition as MDP_transition

#####################################################################
def to_scalar(state):
    if min(state) == 0:
        states_in_scalar = 0 # Terminal state
    else:
        states_in_scalar = state[0]
        for i in range(1, len(state)):
            states_in_scalar = states_in_scalar * 5 + state[i]

    return states_in_scalar

#####################################################################
def test_Q_table():
    Q = np.zeros([num_states, num_actions])
    f = open("Q_table.txt", "r")
    for i in range(num_states):
        for j in range(num_actions):
            Q[i][j] = float(f.readline().strip())

    num_steps = 0
    state = [5, 5, 5, 5, 5]
    while True:
        state_scalar = to_scalar(state)
        # select action according to the learned Q value
        action = Q[state_scalar].argmax()
        
        _, state_next, terminate = MDP_transition(state, action)
                
        state = state_next

        num_steps += 1
        
        if terminate:
            return num_steps

#####################################################################
def run():
    num_steps = test_Q_table()
    print ("# steps with the trained Q table: ", num_steps)
    
run()
            