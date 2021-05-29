import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf

C = tf.constant([ [[1,1,1], [2,2,2]], \
                  [[3,3,3], [4,4,4]], \
                  [[5,5,5], [6,6,6]] ])
C1 = tf.slice(C, [1,0,0], [1,1,3]) # [[[3,3,3]]]
C2 = tf.slice(C, [1,0,0], [1,2,3]) # [[[3,3,3], [4,4,4]]]
C3 = tf.slice(C, [1,0,0], [2,1,3]) # [[[3,3,3]], [[5,5,5]]]

print (C)   # not evaluated
print (C1)  # not evaluated
print ("=====================")

sess = tf.Session()
print (sess.run(C1))
print (sess.run(C2))
print (sess.run(C3))