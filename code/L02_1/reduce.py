import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import tensorflow as tf

C = tf.constant([ [[1,1], [2,2], [3,3]], \
                  [[4,4], [5,5], [6,6]], \
                  [[7,7], [8,8], [9,9]] ])
C0 = tf.reduce_sum(C, 0)
C1 = tf.reduce_sum(C, 1)
C2 = tf.reduce_sum(C, 2)
C3 = tf.argmin(C2, 1)

print (C)   # not evaluated
print (C1)  # not evaluated
print ("=====================")

sess = tf.Session()
print (sess.run(C0))  # [[12,12], [15,15], [18,18]]
print (sess.run(C1))  # [[6,6], [15,15], [24,24]]
print (sess.run(C2))  # [[2,4,6], [8,10,12], [14,16,18]]
print (sess.run(C3))  # [0,0,0]
print ("=====================")

print (C.get_shape())   # (3,3,2)
print (C0.get_shape())  # (3,2)
print (C1.get_shape())  # (3,2)
print (C2.get_shape())  # (3,3)
print (C3.get_shape())  # (3,)
print ("=====================")

C4 = tf.reduce_sum(C)
print (sess.run(C4))  # 90
