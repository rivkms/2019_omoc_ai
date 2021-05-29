import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

#y = tf.multiply(a, b)
y = a * b

sess = tf.Session()

print (sess.run(y, feed_dict={a:3, b:4}))
