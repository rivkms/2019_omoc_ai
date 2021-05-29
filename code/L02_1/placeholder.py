import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float32, shape=(2,2))
y = tf.matmul(x, x)

sess = tf.Session()
#print (sess.run(y))  # ERROR: will fail because x was not fed.

rand_array = np.random.rand(2,2)
print (rand_array)
print (sess.run(y, feed_dict={x:rand_array}))
