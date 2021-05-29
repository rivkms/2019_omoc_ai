import tensorflow as tf
import numpy as np

def state_to_matrix(state):
    # example:
    #     state = [2, 5, 1, 3, 2]
    #     output = [[1, 1, 0, 0, 0],
    #               [1, 1, 1, 1, 1],
    #               [1, 0, 0, 0, 0],
    #               [1, 1, 1, 0, 0],
    #               [1, 1, 0, 0, 0]]]
    matrix = []
    for i in range(5):
        L = [None]*5
        if state[i] <= 5:
            for k in range(0, state[i]): L[k] = 1
            for k in range(state[i], 5): L[k] = 0
        if state[i] == 6:  # only for MDP2
            for k in range(4): L[k] = 0
            L[4] = 1
        matrix.append(L)
    return matrix

action_matrix = np.identity(5)
def action_to_vector(action): return action_matrix[action]
    
#####################################################################
class DQN_Train(object):  # DQN for training
    @staticmethod
    def NN_state_to_action(state):  # state: placeholder
        state = tf.reshape(state, [-1, 5*5])
        # single-layer NN, not CNN
        init_var = tf.random_normal_initializer()
        W = tf.get_variable("weight", [5*5, 5], initializer=init_var)
        b = tf.get_variable("bias", [5], initializer=init_var)
        return tf.matmul(state, W) + b
        
    def __init__(self, gamma, alpha):
        # placeholders
        self.state_in = tf.placeholder(tf.float32, shape=[None, 5,5])
        self.action_in = tf.placeholder(tf.float32, shape=[None, 5])
        self.reward_in = tf.placeholder(tf.float32, shape=[None, 1])
        self.state_next_in = tf.placeholder(tf.float32, shape=[None, 5,5])
        self.terminate_in = tf.placeholder(tf.float32, shape=[None, 1])

        with tf.variable_scope("target_Q"):
            self.target_Q = DQN_Train.NN_state_to_action(self.state_next_in)
        with tf.variable_scope("online_Q"):
            self.online_Q = DQN_Train.NN_state_to_action(self.state_in)
        
        self.target_Q_var = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, \
                                              scope="target_Q")
        self.online_Q_var = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, \
                                              scope="online_Q")
        
        # cost function
        y_target = self.reward_in + gamma * tf.multiply(self.terminate_in,
                                               tf.reduce_max(self.target_Q, 1))
        y_online = tf.reduce_sum(tf.multiply(self.online_Q, self.action_in), 1)
        loss = tf.reduce_mean(tf.square(tf.subtract(y_target, y_online)))
    
        # optimizer
        self.optimizer = tf.train.RMSPropOptimizer(alpha). \
                         minimize(loss, var_list=self.online_Q_var)
        
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())
        self.update_target_Q()

    def train_online_Q(self, batch_train):
        state, action, reward, state_next, terminate = batch_train
        self.sess.run(self.optimizer,
                      feed_dict={
                          self.state_in:state,   # list of states
                          self.action_in:action, # list of actions
                          self.reward_in:reward,
                          self.state_next_in:state_next,
                          self.terminate_in:terminate
                      })
        
    def update_target_Q(self):
        l = len(self.online_Q_var)
        for i in range(l):
            self.sess.run(self.target_Q_var[i].assign(self.online_Q_var[i]))

    def get_Q(self, state):
        Q = self.sess.run(self.online_Q,
                          feed_dict={self.state_in:[state_to_matrix(state)]})
        return Q[0]
        
    def save(self, file_path):
        tf.train.Saver().save(self.sess, file_path)

#####################################################################
class DQN_Test(object):  # DQN for testing a trained DQN
    def __init__(self):
        self.state_in = tf.placeholder(tf.float32, shape=[None, 5,5])
        with tf.variable_scope("online_Q"):
            self.online_Q = DQN_Train.NN_state_to_action(self.state_in)
        self.sess = tf.Session()

    def get_Q(self, state):
        Q = self.sess.run(self.online_Q,
                          feed_dict={self.state_in:[state_to_matrix(state)]})
        return Q[0]
        
    def restore(self, file_path):
        tf.train.Saver().restore(self.sess, file_path)

#####################################################################
class Replay_Memory(object):
    def __init__(self, size_batch):
        self.state = []
        self.action = []
        self.reward = []
        self.state_next = []
        self.terminate = []
        self.size_batch = size_batch

    def store(self, state, action, reward, state_next, terminate):
        self.state.append(state_to_matrix(state))
        self.action.append(action_to_vector(action))
        self.reward.append([reward])
        self.state_next.append(state_to_matrix(state_next))
        self.terminate.append([terminate])

    def get_batch(self):
        size_memory = len(self.state)
        num_sample = min(size_memory, self.size_batch)
        sample_indices = np.random.randint(0, size_memory, num_sample)
        batch = [None]*5
        batch[0] = [self.state[i] for i in sample_indices]
        batch[1] = [self.action[i] for i in sample_indices]
        batch[2] = [self.reward[i] for i in sample_indices]
        batch[3] = [self.state_next[i] for i in sample_indices]
        batch[4] = [self.terminate[i] for i in sample_indices]
        return batch
        
#####################################################################
class Batch_Memory(object):  # used if replay memory is not used
    def __init__(self, size_batch):
        self.state = []
        self.action = []
        self.reward = []
        self.state_next = []
        self.terminate = []
        self.size_batch = size_batch

    def store(self, state, action, reward, state_next, terminate):
        self.state.append(state_to_matrix(state))
        self.action.append(action_to_vector(action))
        self.reward.append([reward])
        self.state_next.append(state_to_matrix(state_next))
        self.terminate.append([terminate])

    def is_full(self):
        return len(self.state) >= self.size_batch
        
    def get_batch(self):
        assert self.is_full()
        batch = [self.state, self.action, self.reward, self.state_next, self.terminate]
        self.state = []
        self.action = []
        self.reward = []
        self.state_next = []
        self.terminate = []
        return batch
