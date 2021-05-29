import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
from NN_comp_graph import NN_comp_graph

##########################################################    
def shuffle(x, y):
    data_index = np.arange(len(x))
    np.random.shuffle(data_index)
    return x[data_index], y[data_index]
    
##########################################################    
def get_batch(x, y, batch_size, iteration_no):
    fr = (iteration_no * batch_size) % len(x)
    return x[fr:fr+batch_size], y[fr:fr+batch_size]
    
##########################################################    
def train(x_train_all, y_train_all):
    x_train = tf.placeholder(tf.float32, [None, 784])
    y_train = tf.placeholder(tf.float32, [None,10])
    accuracy, train = NN_comp_graph(x_train, y_train)

    x_train_all, y_train_all = shuffle(x_train_all, y_train_all)
    
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    batch_size = 100
    num_steps = 1000 # 10000
    for i in range(num_steps):
        batch_x, batch_y = get_batch(x_train_all, y_train_all, batch_size, i)
        sess.run(train, feed_dict = {x_train:batch_x, y_train:batch_y})
        print ("Accuracy at step %d: " %i, \
            sess.run(accuracy, feed_dict = {x_train:batch_x, y_train:batch_y}))

    return sess

##############################################
def run():
    mnist = tf.keras.datasets.mnist.load_data()  # ~/.keras/datasets/mnist.npz
    (x_train, y_train), (_, _) = mnist
    x_train = x_train.reshape(-1, 28*28) / 255.0
    y_train = tf.keras.utils.to_categorical(y_train)
    sess = train(x_train, y_train)
    tf.train.Saver().save(sess, "./model/mnist_NN_model.ckpt")  # save variables
    
run()