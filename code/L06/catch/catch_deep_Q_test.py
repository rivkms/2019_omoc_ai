import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
from catch_MDP import MDP_transition, MDP_initial_state
from catch_DQN import DQN_Test
import tkinter as tk
import time as time  # sleep for updating graphics

size_hidden = 100  # size of hiddle layer of DQN

#####################################################################
def test_DQN(canvas):
    dqn = DQN_Test(size_hidden)
    dqn.restore("./model/catch.ckpt")
    
    num_test = 1000
    num_wins = 0
    for ep in range(num_test):
        state = MDP_initial_state()
        canvas.update(state[0], state[1], state[2])
        while True:
            # select action according to the learned Q value
            Q = dqn.get_Q(state)
            action = Q.argmax()

            r, state_next, terminate = MDP_transition(state, action)

            canvas.update(state_next[0], state_next[1], state_next[2])
            
            if terminate:
                if r > 0: num_wins += 1
                break

            state = state_next
        
        print ("Episode %d: %s" %(ep, ("wins" if r > 0 else "lose")))
            
    return float(num_wins)/num_test

#####################################################################
class Canvas:
    def __init__(self):
        self.canvas = tk.Canvas(width=400, height=400, bg='white')
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.fruit_row = 1
        self.fruit_col = 1
        self.basket_col = 2
        self.fruit = self.canvas.create_rectangle(0,0,40,40, fill="red")
        self.basket = self.canvas.create_rectangle(0,360,120,400, fill="blue")

    def update(self, fruit_row, fruit_col, basket_col):
        drow = fruit_row - self.fruit_row
        dcol = fruit_col - self.fruit_col
        self.canvas.move(self.fruit, 40*dcol, 40*drow)
        self.canvas.move(self.basket, 40*(basket_col-self.basket_col), 0)
        self.fruit_row = fruit_row
        self.fruit_col = fruit_col
        self.basket_col = basket_col
        self.canvas.update()
        time.sleep(0.03)
        
    def loop(self): self.canvas.mainloop()
    
#####################################################################
def run():
    canvas = Canvas()
    win_prob = test_DQN(canvas)
    print ("Winning probability with the trained DQN: ", win_prob)
    
run()
