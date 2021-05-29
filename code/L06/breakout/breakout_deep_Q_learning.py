import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
from breakout_MDP import MDP1_transition, MDP2_transition, MDP3_transition
from breakout_MDP import num_states, num_actions
from breakout_DQN import DQN_Train, Replay_Memory, Batch_Memory
import time

#####################################################################
hyperparameters = [
    [MDP1_transition, 0.9, 0.25, 1, False, 10, 1],       # for MDP1
    [MDP2_transition, 0.9, 0.0025, 1, True, 6000, 1],    # for MDP2
    [MDP3_transition, 0.9, 0.00025, 32, True, 20000, 20] # for MDP3
]

environment = 1  # select among 1,2,3

MDP_transition, gamma, alpha, size_batch, use_replay, \
num_episodes, period_target_Q_update = hyperparameters[environment-1]

#####################################################################
def deep_Q_learning():
    max_steps = 1000  # max steps of each episode

    dqn = DQN_Train(gamma, alpha)  # build computation graph for DQN

    if use_replay:
        replay_memory = Replay_Memory(size_batch)
    else:
        batch_memory = Batch_Memory(size_batch)
    
    num_trials = np.zeros([num_episodes])
    time_start = time.time()
    for ep in range(num_episodes):
        counter_target_Q_update = 0
        terminate = False
        
        state = [5, 5, 5, 5, 5]
        epsilon = 1.0 - ep/float(num_episodes-1)
        
        for step in range(max_steps):
            # choose action based on epsilon-greedy strategy
            if np.random.random() < epsilon:  # exploration
                action = np.random.randint(0,num_actions)
            else:  # exploitation
                # select action according to the learned Q value
                Q = dqn.get_Q(state)
                action = Q.argmax()

            reward, state_next, terminate = MDP_transition(state, action)

            if use_replay: # store to replay memory & train with random from replay
                replay_memory.store(state, action, reward, state_next, terminate)
                batch = replay_memory.get_batch()
                dqn.train_online_Q(batch)
            else:
                batch_memory.store(state, action, reward, state_next, terminate)
                if batch_memory.is_full():
                    batch = batch_memory.get_batch()
                    dqn.train_online_Q(batch)
                    
            if terminate:
                num_trials[ep] = step+1
                break

            state = state_next

            if counter_target_Q_update < period_target_Q_update:
                counter_target_Q_update += 1
            else:
                counter_target_Q_update = 0
                dqn.update_target_Q()
        if ep % 100 == 0:
            print ("Episode:", ep, num_trials[ep])
                
    print ("Time elapse:", (time.time() - time_start), "sec")
        
    return dqn, num_episodes, num_trials
    
#####################################################################
def run():
    dqn, num_episodes, num_trials = deep_Q_learning()
    
    dqn.save("./model/breakout_MDP%d.ckpt" %environment)

run()
