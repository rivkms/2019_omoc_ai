import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
from catch_MDP import MDP_transition, MDP_initial_state, num_actions, num_row, num_col
import tkinter as tk
import time as time  # sleep for updating graphics

num_states = (num_row-1) * num_col * (num_col-2)  # 720

#####################################################################
def to_scalar(state):
    fruit_row, fruit_col, basket = state
    i = (fruit_row-1)*num_col + (fruit_col-1)
    j = basket-2
    s = (num_col-2)*i + j
    return s

#####################################################################
def test_Q_table(canvas):
    Q = np.zeros([num_states, num_actions])
    f = open("Q_table.txt", "r")
    for i in range(num_states):
        for j in range(num_actions):
            Q[i][j] = float(f.readline().strip())

    num_test = 5000
    num_wins = 0
    for ep in range(num_test):
        state = MDP_initial_state()
        canvas.update(state[0], state[1], state[2])
        while True:
            
            state_scalar = to_scalar(state)
            # select action according to the learned Q value
            action = Q[state_scalar].argmax()

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
    win_prob = test_Q_table(canvas)
    print ("Winning probability with the trained Q table: ", win_prob)
    
run()
            