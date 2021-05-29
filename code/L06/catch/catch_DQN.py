import tensorflow as tf
import numpy as np
import math
from catch_MDP import num_row, num_col, num_actions

size_state = num_row * num_col

def state_to_vector(state):
    fruit_row, fruit_col, basket = state
    L = [0] * size_state
    i = (fruit_row-1)*num_col + (fruit_col-1)
    j = (num_row-1)*num_col + (basket-1)
    L[i], L[j-1], L[j], L[j+1] = 1,1,1,1
    return L
    
action_matrix = np.identity(3)
def action_to_vector(action): return action_matrix[action]
    
#####################################################################
class DQN_Train(object):  # DQN for training
    @staticmethod
    def NN_state_to_action(state, size_hidden):  # state: placeholder
        # NN with 1 hidden layer (fully connected, not CNN)
        W1 = tf.Variable(tf.truncated_normal([size_state, size_hidden],
                                    stddev=1.0/math.sqrt(float(size_state))))
        b1 = tf.Variable(tf.truncated_normal([size_hidden], stddev=0.01))
        y1 = tf.nn.relu(tf.matmul(state, W1) + b1)  # shape: [None,100]
        
        W2 = tf.Variable(tf.truncated_normal([size_hidden, size_hidden],
                                    stddev=1.0/math.sqrt(float(size_hidden))))
        b2 = tf.Variable(tf.truncated_normal([size_hidden], stddev=0.01))
        y2 = tf.nn.relu(tf.matmul(y1, W2) + b2)     # shape: [None,100]
        
        W3 = tf.Variable(tf.truncated_normal([size_hidden, num_actions],
                                    stddev=1.0/math.sqrt(float(size_hidden))))
        b3 = tf.Variable(tf.truncated_normal([num_actions], stddev=0.01))
        return tf.matmul(y2, W3) + b3  # shape: [None,3]
        
    def __init__(self, size_hidden, gamma):
        # placeholders
        self.state_in = tf.placeholder(tf.float32, shape=[None, size_state])
        self.action_in = tf.placeholder(tf.float32, shape=[None, num_actions])

        with tf.variable_scope("Q"):
            self.Q = DQN_Train.NN_state_to_action(self.state_in, size_hidden)
            
        # cost function & optimizer
        loss = tf.reduce_mean(tf.square(tf.subtract(self.Q, self.action_in)))
        self.optimizer = tf.train.GradientDescentOptimizer(0.2).minimize(loss)
        
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

    def train_Q(self, batch_train):
        state, action = batch_train
        self.sess.run(self.optimizer,
                      feed_dict={self.state_in:state, self.action_in:action})
        
    def get_Q(self, state):
        Q = self.sess.run(self.Q,
                          feed_dict={self.state_in:[state_to_vector(state)]})
        return Q[0]
        
    def save(self, file_path):
        tf.train.Saver().save(self.sess, file_path)

#####################################################################
class DQN_Test(object):  # DQN for testing a trained DQN
    def __init__(self, size_hidden):
        self.state_in = tf.placeholder(tf.float32, shape=[None, size_state])
        with tf.variable_scope("Q"):
            self.Q = DQN_Train.NN_state_to_action(self.state_in, size_hidden)
        self.sess = tf.Session()

    def get_Q(self, state):
        Q = self.sess.run(self.Q,
                          feed_dict={self.state_in:[state_to_vector(state)]})
        return Q[0]
        
    def restore(self, file_path):
        tf.train.Saver().restore(self.sess, file_path)

#####################################################################
class Replay_Memory(object):
    def __init__(self, dqn_train, size_memory, size_batch, gamma):  # fixed size
        self.dqn_train = dqn_train
        self.state = [None] * size_memory
        self.action = [None] * size_memory
        self.reward = [None] * size_memory
        self.state_next = [None] * size_memory
        self.terminate = [None] * size_memory
        self.size_memory = size_memory
        self.size_batch = size_batch
        self.cur_index = 0
        self.count = 0
        self.gamma = gamma
        
    def store(self, state, action, reward, state_next, terminate):
        self.state[self.cur_index] = state
        self.action[self.cur_index] = action
        self.reward[self.cur_index] = reward
        self.state_next[self.cur_index] = state_next
        self.terminate[self.cur_index] = terminate
        self.count = max(self.count, self.cur_index+1)
        self.cur_index = (self.cur_index+1) % self.size_memory # circular

    def get_batch(self):
        num_sample = min(self.count, self.size_batch)
        sample_indices = np.random.randint(0, self.count, num_sample)
        batch_state = []
        batch_action = []
        for i in range(num_sample):
            j = sample_indices[i]
            Q1 = self.dqn_train.get_Q(self.state[j]) 
            Q2 = self.dqn_train.get_Q(self.state_next[j])
            if self.terminate[j]:
                Q1[self.action[j]] = self.reward[j]
            else:
                Q1[self.action[j]] = self.reward[j] + self.gamma * np.max(Q2)
            batch_state.append(state_to_vector(self.state[j]))
            batch_action.append(Q1)
        return [ batch_state, batch_action ]
