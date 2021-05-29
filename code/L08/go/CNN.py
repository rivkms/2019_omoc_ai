import tensorflow as tf
import numpy as np
from board import *
    
#####################################################################
class CNN_Train(object):  # CNN for training
    @staticmethod
    def NN_state_to_win_prob(state):  # state: placeholder (with batch size)
        init_var = tf.random_normal_initializer(stddev = 0.0001)
        
        # 1st convolution (w/o pooling) layer
        W_conv1 = tf.get_variable("W_conv1", [3,3,3,30], initializer=init_var)
        b_conv1 = tf.get_variable("b_conv1", [30], initializer=init_var)
                
        conv1 = tf.nn.conv2d(state, W_conv1, strides = [1,1,1,1], padding='SAME')
        out1 = tf.nn.relu(conv1 + b_conv1)

        # 2nd convolution (w/o pooling) layer
        W_conv2 = tf.get_variable("W_conv2", [3,3,30,50], initializer=init_var)
        b_conv2 = tf.get_variable("b_conv2", [50], initializer=init_var)

        conv2 = tf.nn.conv2d(out1, W_conv2, strides = [1,1,1,1], padding='SAME')
        out2 = tf.nn.relu(conv2 + b_conv2)

        # 3rd convolution (w/o pooling) layer
        W_conv3 = tf.get_variable("W_conv3", [3,3,50,70], initializer=init_var)
        b_conv3 = tf.get_variable("b_conv3", [70], initializer=init_var)

        conv3 = tf.nn.conv2d(out2, W_conv3, strides = [1,1,1,1], padding='SAME')
        out3 = tf.nn.relu(conv3 + b_conv3)
        
        # 1st full-connection layer
        Nr, Nc = N, N
        W_fc1 = tf.get_variable("W_fc1", [Nr*Nc*70,100], initializer=init_var)
        b_fc1 = tf.get_variable("b_fc1", [100], initializer=init_var)

        out3 = tf.reshape(out3, [-1, Nr*Nc*70])
        fc1 = tf.nn.relu(tf.matmul(out3, W_fc1) + b_fc1)
        
        # 2nd full-connection layer
        W_fc2 = tf.get_variable("W_fc2", [100,3], initializer=init_var)
        b_fc2 = tf.get_variable("b_fc2", [3], initializer=init_var)

        # estimation for unnormalized log prob
        Y = tf.matmul(fc1, W_fc2) + b_fc2  
        # estimation for prob
        P = tf.nn.softmax(Y, name="softmax")
        return Y, P
        
    def __init__(self, S, W, var_scope):
        alpha = 0.0025
        Nr, Nc = N, N
        self.S_in = tf.placeholder(tf.float32, shape=[None, Nr,Nc,3])
        self.W_in = tf.placeholder(tf.int32, shape=[None])

        with tf.variable_scope(var_scope):
            Y, self.P = CNN_Train.NN_state_to_win_prob(self.S_in)
            # target in one-hot vector
            Y_target = tf.one_hot(self.W_in, 3, name="Y_target")
            # cost function & optimizer
            self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=Y, labels=Y_target))
            var = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope=var_scope)
            # L2 regularization
            for i in range(len(var)): self.loss += 0.0001 * tf.nn.l2_loss(var[i])
            self.optimizer = tf.train.RMSPropOptimizer(alpha).minimize(self.loss, var_list=var)
        
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())
        self.__train(S, W)
        tf.train.Saver().save(self.sess, "./model/" + var_scope + ".ckpt")
        
    def __train(self, S, W):  # accessible only by the constructor
        epoch = 10
        size_batch = 1024

        data_index = np.arange(len(W))
        np.random.shuffle(data_index)
        
        for i_epoch in range(epoch):
            num_batches = int(np.ceil(len(W) / float(size_batch)))
            loss = 0
            for i_batches in range(num_batches):
                i_start = i_batches * size_batch
                i_end = min((i_batches+1)*size_batch, len(W))
                indices = data_index[np.arange(i_start, i_end)]
                d = {self.S_in: S[indices], self.W_in: W[indices]}
                self.sess.run(self.optimizer, feed_dict=d)
                loss += self.sess.run(self.loss, feed_dict=d)
            print ("[CNN_Train] Epoch:", i_epoch, " | Loss:", loss)
        
    def win_prob(self, state, player):
        W = self.sess.run(self.P, feed_dict={self.S_in:[state]})
        return W[0][player]
        #return W[0][player] + W[0][DRAW]/2.0
        
    def best_state(self, states, player, show_prob=False):
        W = self.sess.run(self.P, feed_dict={self.S_in:states})
        return W[:,player].argmax()
        #return (W[:,player] + W[:,DRAW]/2.0).argmax()
        
#####################################################################
class CNN_Test(object):  # CNN for testing a trained DQN
    def __init__(self, var_scope):
        Nr, Nc = N, N
        self.S_in = tf.placeholder(tf.float32, shape=[None, Nr,Nc,3])

        with tf.variable_scope(var_scope):
            _, self.P = CNN_Train.NN_state_to_win_prob(self.S_in)
        
        self.sess = tf.Session()
        tf.train.Saver().restore(self.sess, "./model/" + var_scope + ".ckpt")
        
    def win_prob(self, state, player):
        W = self.sess.run(self.P, feed_dict={self.S_in:[state]})
        return W[0][player]
        #return W[0][player] + W[0][DRAW]/2.0

    def best_state(self, states, player, show_prob=False):
        W = self.sess.run(self.P, feed_dict={self.S_in:states})
        if show_prob:
            print (W[:,player])
            print (W[:,player].max())
        return W[:,player].argmax()
        #return (W[:,player] + W[:,DRAW]/2.0).argmax()
