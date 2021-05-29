import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf

C = tf.constant([[3.0,8.0,1.5], [2.0,5.0,4.5]])
D = tf.nn.softmax(C)

sess = tf.Session()
print (sess.run(D))

print (D.get_shape())
