import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
from breakout_MDP import MDP1_transition, MDP2_transition, MDP3_transition
from breakout_DQN import DQN_Test

#####################################################################
environment = 1  # select among 1,2,3

MDP_transition = [ MDP1_transition, MDP2_transition, MDP3_transition ][environment-1]

#####################################################################
def test_DQN():
    dqn = DQN_Test()
    dqn.restore("./model/breakout_MDP%d.ckpt" %environment)
    
    num_steps = 0
    state = [5, 5, 5, 5, 5]
    while True:
        # select action according to the learned Q value
        Q = dqn.get_Q(state)
        action = Q.argmax()
        
        _, state_next, terminate = MDP_transition(state, action)

        state = state_next
        
        num_steps += 1
        
        if terminate:
            return num_steps
    
#####################################################################
def run():
    num_steps = test_DQN()
    print ("# steps with the trained Q table: ", num_steps)
    
run()
