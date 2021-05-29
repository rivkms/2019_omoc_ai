import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
from maze_MDP import random_maze, MDP_transition, num_states, num_actions
from maze_draw import draw

def Q_learning(maze):
    alpha = 0.1
    gamma = 0.9
    epsilon = 0.1  # epsilon-greedy policy improvement
    num_episodes = 10000
    max_steps = 1000  # max steps of each episode. to avoid infinite loop
    
    Q = np.zeros([num_states,num_actions])
    for ep in range(num_episodes):
        state = 0  # start state
        
        for step in range(max_steps):
            if np.random.random() < epsilon:  # exploration
                action = np.random.randint(0,num_actions)
            else:  # exploitation
                # select action according to the learned Q value
                action = Q[state].argmax()
                
            r, state_next, terminate = MDP_transition(state, action, maze)

            maxQ_next = np.max(Q[state_next])
            Q[state][action] += alpha*(r + gamma * maxQ_next - Q[state][action])

            if terminate: break
            
            state = state_next
            
    return Q

##########################################################################
def run():
    maze = random_maze()
    Q = Q_learning(maze)
    draw(maze, Q)

run()