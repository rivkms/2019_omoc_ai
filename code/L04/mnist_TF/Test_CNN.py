import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
from CNN_comp_graph import CNN_comp_graph

##########################################################    
def get_batch(x, y, batch_size, iteration_no):
    fr = (iteration_no * batch_size) % len(x)
    return x[fr:fr+batch_size], y[fr:fr+batch_size]

########################################################################3
def test(x_test_all, y_test_all):
    x_test = tf.placeholder(tf.float32, shape=[None, 784])
    y_test = tf.placeholder(tf.float32, shape=[None, 10])
    keep_prob = 1.0
    accuracy, _ = CNN_comp_graph(x_test, y_test, keep_prob)
    
    sess = tf.Session()
    tf.train.Saver().restore(sess, "./model/mnist_CNN_model.ckpt")  # restore CNN

    batch_size = 100
    num_steps = len(x_test_all) // batch_size
    acc = 0
    for i in range(num_steps):
        batch_x, batch_y = get_batch(x_test_all, y_test_all, batch_size, i)
        acc += sess.run(accuracy, feed_dict={x_test:batch_x, y_test:batch_y})
    print ("Accurary of trained model against test data:", acc/num_steps)
    
##############################################
def run():
    mnist = tf.keras.datasets.mnist.load_data()  # ~/.keras/datasets/mnist.npz
    (_, _), (x_test, y_test) = mnist
    x_test = x_test.reshape(-1, 28*28) / 255.0
    y_test = tf.keras.utils.to_categorical(y_test)
    test(x_test, y_test)
    
run()

