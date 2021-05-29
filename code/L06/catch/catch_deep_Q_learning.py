import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
from catch_MDP import MDP_transition, MDP_initial_state, num_actions
from catch_DQN import DQN_Train, Replay_Memory
import time

# hyperparameters
gamma = 0.9  # discount factor
size_hidden = 100  # size of hiddle layer of DQN
size_memory = 500  # size of replay memory
size_batch = 50
num_episodes = 3000

#####################################################################
def deep_Q_learning():
    max_steps = 1000  # max steps of each episode

    dqn = DQN_Train(size_hidden, gamma)
    replay_memory = Replay_Memory(dqn, size_memory, size_batch, gamma)

    epsilon = 1
    num_wins = 0
    time_start = time.time()
    for ep in range(num_episodes):
        counter_target_Q_update = 0
        terminate = False
        
        state = MDP_initial_state()
        # epsilon = 1.0 - ep/float(num_episodes-1)
        
        for step in range(max_steps):
            # choose action based on epsilon-greedy strategy
            if np.random.random() < epsilon:  # exploration
                action = np.random.randint(0,num_actions)
            else:  # exploitation
                # select action according to the learned Q value
                Q = dqn.get_Q(state)
                action = Q.argmax()

            if epsilon > 0.001: epsilon *= 0.999
                
            reward, state_next, terminate = MDP_transition(state, action)

            replay_memory.store(state, action, reward, state_next, terminate)
            batch = replay_memory.get_batch()
            dqn.train_Q(batch)
                    
            if terminate:
                if reward > 0: num_wins += 1
                break

            state = state_next
                
        print ("Episode %d: %s" %(ep, ("wins" if reward > 0 else "lose")), float(num_wins)/(ep+1)*100)
                
    print ("Time elapse:", (time.time() - time_start), "sec")
        
    return dqn
    
#####################################################################
def run():
    dqn = deep_Q_learning()
    dqn.save("./model/catch.ckpt")

run()
