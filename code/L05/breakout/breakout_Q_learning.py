import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
from breakout_MDP import num_states, num_actions
from breakout_MDP import MDP1_transition as MDP_transition
import matplotlib.pyplot as plt

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
def Q_learning():
    alpha = 0.1
    gamma = 0.9
    num_episodes = 100000
    max_steps = 10000  # max steps of each episode
    
    num_trials = np.zeros([num_episodes])
    Q = np.zeros([num_states, num_actions])
    for ep in range(num_episodes):
        state = [5, 5, 5, 5, 5]
        epsilon = 1.0 - ep/float(num_episodes-1)
        
        for step in range(max_steps):
            state_scalar = to_scalar(state)
            # choose action based on epsilon-greedy strategy
            if np.random.random() < epsilon:  # exploration
                action = np.random.randint(0,num_actions)
            else:  # exploitation
                # select action according to the learned Q value
                action = Q[state_scalar].argmax()
                
            r, state_next, terminate = MDP_transition(state, action)
            
            maxQ_next = np.max(Q[to_scalar(state_next)])
            Q[state_scalar][action] += \
                alpha * (r + gamma * maxQ_next - Q[state_scalar][action])

            if terminate:
                num_trials[ep] = step+1
                break
                
            state = state_next
                
    return Q, num_episodes, num_trials

#####################################################################
def draw(num_episodes, num_trials):
    print ("# steps at the end of training: ", num_trials[num_episodes-1])
    # Plot the average number of time steps 
    # Each data point is an average over (num_episodes/100) episodes
    Xaxis = np.linspace(1, 100, 100, endpoint=True)
    C = np.mean(np.reshape(num_trials, [100, num_episodes//100]), axis = 1)
    plt.plot(Xaxis, C, '.')
    plt.show()

#####################################################################
def run():
    Q, num_episodes, num_trials = Q_learning()
    draw(num_episodes, num_trials)

    f = open("Q_table.txt", "w")
    for i in range(num_states):
        for j in range(num_actions):
            f.write(str(Q[i][j]) + "\n")
    f.close()

run()