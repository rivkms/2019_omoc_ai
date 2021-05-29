import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np
from NN_comp_graph import NN_comp_graph

##########################################################    
def test(x_test, y_test):
    accuracy, _ = NN_comp_graph(x_test, y_test)

    sess = tf.Session()
    tf.train.Saver().restore(sess, "./model/mnist_NN_model.ckpt")  # restore NN

    print ("Accurary of trained model against test data:", sess.run(accuracy))
        
##############################################
def run():
    mnist = tf.keras.datasets.mnist.load_data()  # ~/.keras/datasets/mnist.npz
    (_, _), (x_test, y_test) = mnist
    x_test = x_test.astype(np.float32).reshape(-1, 28*28) / 255.0
    y_test = tf.keras.utils.to_categorical(y_test)
    test(x_test, y_test)
    
run()