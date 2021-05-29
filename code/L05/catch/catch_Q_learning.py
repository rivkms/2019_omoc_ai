import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
from catch_MDP import MDP_transition, MDP_initial_state, num_actions, num_row, num_col

num_states = (num_row-1) * num_col * (num_col-2)  # 720

#####################################################################
def to_scalar(state):
    fruit_row, fruit_col, basket = state
    i = (fruit_row-1)*num_col + (fruit_col-1)
    j = basket-2
    s = (num_col-2)*i + j
    return s

#####################################################################
def Q_learning():
    alpha = 0.1
    gamma = 0.9
    num_episodes = 3000 
    
    num_wins = 0
    Q = np.zeros([num_states, num_actions])
    for ep in range(num_episodes):
        state = MDP_initial_state()
        epsilon = 1.0 - ep/float(num_episodes-1)
        
        while True:
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
                if r > 0: num_wins += 1
                break
                
            state = state_next
                
        if ep%100 == 0:
            print ("Episode %d:" %ep, (float(num_wins)/(ep+1)*100))
            
    return Q

#####################################################################
def run():
    Q  = Q_learning()

    f = open("Q_table.txt", "w")
    for i in range(num_states):
        for j in range(num_actions):
            f.write(str(Q[i][j]) + "\n")
    f.close()

run()