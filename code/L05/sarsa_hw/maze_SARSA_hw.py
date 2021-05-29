import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
from maze_MDP import generate_maze, MDP_transition, num_states, num_actions
from maze_draw import draw

def SARSA(maze):
    alpha = 0.1
    gamma = 0.9
    epsilon = 0.1  # epsilon-greedy policy improvement
    num_episodes = 10000 
    max_steps = 10000  # max steps of each episode. to avoid infinite loop
    
    Q = np.zeros([num_states,num_actions])
    for ep in range(num_episodes):
        
        # IMPLEMENT HERE


        
        if ep % 100 == 0:
            print ("Episode", ep)
            
    return Q

##########################################################################
def run():
    maze = generate_maze()
    Q = SARSA(maze)
    draw(maze, Q)

run()